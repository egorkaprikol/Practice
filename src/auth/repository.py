import time
from fastapi import HTTPException, Request, status
from fastapi.params import Depends
from jwt import PyJWTError, decode, encode
from sqlalchemy.orm import Session
from src.auth.config import pwd_context, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from src.auth.models import User, Role
from src.auth.schemas import RoleBase


def get_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(db: Session, login: str, password: str):
    user = db.query(User).filter(User.login == login).first()

    if not user:
        return False

    if not pwd_context.verify(password, user.hashed_password):
        return False

    return user


def create_access_token(user: User) -> str:
    payload = {
        "login": user.login,
        "role_id": user.role_id,
        "expires": time.time() + (ACCESS_TOKEN_EXPIRE_MINUTES * 60),
    }

    token = encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


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


def role_required(required_role: int):
    def role_required_dependency(user: User = Depends(get_current_user)):
        if user["role_id"] != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have enough permissions to access this endpoint"
            )
        return user

    return role_required_dependency


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


def create_user(db: Session, login: str, password: str, role_id: int) -> User:
    hashed_password = get_password_hash(password)
    db_user = User(login=login, hashed_password=hashed_password, role_id=role_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def create_role(db: Session, role: RoleBase):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
