import time
from pathlib import Path
from typing import Union
from fastapi import HTTPException, Request, status, UploadFile
from fastapi.params import Depends
from jwt import PyJWTError, decode, encode
from sqlalchemy.orm import Session
from backend.src.auth.config import pwd_context, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from backend.src.auth import models as models_auth
from backend.src.auth.schemas import *
from backend.src.database.config import db_dependency


def create_user(db: db_dependency, phone_number: str, password: str, role_id: int) -> models_auth.User:
    hashed_password = get_password_hash(password)
    db_user = models_auth.User(phone_number=phone_number, hashed_password=hashed_password, role_id=role_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def create_admin(admin: AdminBase, user_id, db: db_dependency):
    db_admin = models_auth.Admin(name=admin.name,
                                 surname=admin.surname,
                                 patronymic=admin.patronymic,
                                 user_id=user_id)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    if db_admin:
        return {"message": "Админ успешно создан", "Admin": db_admin}
    user = db.query(models_auth.User).filter(models_auth.User.id == user_id).first()
    db.delete(user)


async def update_admin(admin_id: int, admin: AdminUpdate, db: db_dependency):
    db_admin = (
        db.query(models_auth.Admin)
        .filter(models_auth.Admin.id == admin_id).first()
    )
    if db_admin:

        if admin.name:
            db_admin.name = admin.name
        if admin.surname:
            db_admin.surname = admin.surname
        if admin.patronymic:
            db_admin.patronymic = admin.patronymic

        db.commit()
        db.refresh(db_admin)

        return {"message": "Профиль админа успешно обновлен", "Admin": db_admin}
    else:
        raise HTTPException(status_code=404, detail="Админ не найден")


async def delete_admin(admin_id: int, db: db_dependency):
    db_admin = db.query(models_auth.Admin).filter(models_auth.Admin.id == admin_id).first()

    if db_admin:

        ## Если удалить админа, то вместе с ним удалится юзер в таблице users, в котором лежат логин и пароль админа
        user = db.query(models_auth.User).filter(
            models_auth.User.id == db_admin.user_id).first()
        db.delete(user)

        db.delete(db_admin)
        db.commit()
        return {"message": "Профиль админа успешно удален"}
    else:
        raise HTTPException(status_code=404, detail="Админ не найден")


async def get_admins_all(db: db_dependency):
    admins = (
        db.query(
            models_auth.User.phone_number,
            models_auth.Admin.id,
            models_auth.Admin.name,
            models_auth.Admin.surname,
            models_auth.Admin.patronymic
        )
        .join(models_auth.Admin, models_auth.User.id == models_auth.Admin.user_id)
    )
    return [
        {
            "id": admin.id,
            "name": admin.name,
            "surname": admin.surname,
            "login": admin.patronymic,
            "phone_number": admin.phone_number
        }
        for admin in admins.all()
    ]


async def get_admin_by_id(admin_id: int, db: db_dependency):

    db_admin = (
        db.query(
            models_auth.Admin.id,
            models_auth.Admin.name,
            models_auth.Admin.surname,
            models_auth.Admin.patronymic,
            models_auth.User.phone_number
        )
        .join(models_auth.User, models_auth.User.id == models_auth.Admin.user_id)
    )

    if admin_id:

        db_admin = db_admin.filter(models_auth.Admin.id == admin_id).all()

    if db_admin:
        return [
            {
                "id": admin.id,
                "name": admin.name,
                "surname": admin.surname,
                "patronymic": admin.patronymic,
                "phone_number": admin.phone_number,
            }
            for admin in db_admin
        ]
    else:
        raise HTTPException(status_code=404, detail={"message": "Админ не найден"})


def authenticate_user(db: Session, phone_number: str, password: str):
    user = db.query(models_auth.User).filter(models_auth.User.phone_number == phone_number).first()

    if not user:
        return False

    if not pwd_context.verify(password, user.hashed_password):
        return False

    return user


def get_current_user(request: Request):
    """
    This function is a dependency that will be used in the secure endpoint.
    It will extract the token from the request, verify it, and return the user data.
    """

    token = get_token_from_header(request)
    data = verify_token(token)

    if not data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
        )

    return data


async def create_role(db: Session, role: RoleBase):
    db_role = models_auth.Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def role_required(required_role: int):
    def role_required_dependency(user: models_auth.User = Depends(get_current_user)):
        if user["role_id"] != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have enough permissions to access this endpoint"
            )
        return user

    return role_required_dependency


def create_access_token(user: models_auth.User) -> str:
    payload = {
        "phone_number": user.phone_number,
        "role_id": user.role_id,
        "expires": time.time() + (ACCESS_TOKEN_EXPIRE_MINUTES * 60),
    }

    token = encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_token_from_header(request: Request):
    auth = request.headers.get("Authorization")

    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return auth.split("Bearer ")[1]


def verify_token(token: str):
    try:
        decoded_token = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except PyJWTError:
        return {}


def get_password_hash(password: str):
    return pwd_context.hash(password)


async def upload_image(image_file: Union[UploadFile, None] = None):

    if not image_file:
        return {"message": "No upload image_file sent"}
    else:
        data = await image_file.read()
        save_to = Path("mediafiles/") / image_file.filename
        with open(save_to, "wb") as f:
            f.write(data)
        return {"filename": image_file.filename}

