from fastapi import APIRouter
from backend.src.auth.repository import *
from backend.src.database.config import get_db, db_dependency
from backend.src.auth.schemas import *

router = APIRouter()


@router.post("/admins", status_code=status.HTTP_201_CREATED)
async def register(request: AdminCreateRequest, db: db_dependency):
    user = create_user(db, request.login, request.password, 1)
    return await create_admin(request, user.id, db)


@router.put("/admins", status_code=status.HTTP_200_OK)
async def update(user_id: int, user: UserUpdate, db: db_dependency):
    response = await update_admin(user_id, user, db)
    return response


@router.delete("/admins", status_code=status.HTTP_200_OK)
async def delete(user_id: int, db: db_dependency):
    response = await delete_admin(user_id, db)
    return response


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: SignInRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.login, request.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(user)
    return SignInResponse(access_token=token)


@router.get("/check_token", status_code=status.HTTP_200_OK)
def get_protected_resource(request: Request):
    token = get_token_from_header(request)
    token = verify_token(token)
    if token == {}:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
        )
    return {"message": "Токен валидный, успешно"}


@router.get("/secure", status_code=status.HTTP_200_OK)
def secure(user=Depends(get_current_user)):
    return {"message": "This is a secure endpoint for " + user["login"]}


@router.post("/role", status_code=status.HTTP_201_CREATED)
async def role_create(role: RoleBase, db: db_dependency):
    response = await create_role(db, role)
    return response
