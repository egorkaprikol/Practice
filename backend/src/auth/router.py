from fastapi import APIRouter
from backend.src.auth.repository import *
from backend.src.database.config import get_db, db_dependency
from backend.src.auth.schemas import *

router = APIRouter()


@router.post("/admins", status_code=status.HTTP_201_CREATED)
async def register(request: AdminCreateRequest, db: db_dependency):
    user = create_user(db, request.phone_number, request.password, 1)
    return await create_admin(request, user.id, db)


@router.patch("/admins", status_code=status.HTTP_200_OK)
async def update(admin_id: int, admin: AdminUpdate, db: db_dependency):
    response = await update_admin(admin_id, admin, db)
    return response


@router.delete("/admins", status_code=status.HTTP_200_OK)
async def delete(admin_id: int, db: db_dependency):
    response = await delete_admin(admin_id, db)
    return response


@router.get("/admins", status_code=status.HTTP_200_OK)
async def get_all_admins(db: db_dependency):
    response = await get_admins_all(db)
    return response


@router.get("/admins/{admin_id}", status_code=status.HTTP_200_OK)
async def get_by_id(admin_id: int, db: db_dependency):
    response = await get_admin_by_id(admin_id, db)
    return response


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: SignInRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.phone_number, request.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone_number or password",
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
    return {"message": "This is a secure endpoint for " + user["phone_number"]}


@router.post("/roles", status_code=status.HTTP_201_CREATED)
async def role_create(role: RoleBase, db: db_dependency):
    response = await create_role(db, role)
    return response


@router.post("/files/upload", status_code=status.HTTP_200_OK)
async def upload_file(image_file: UploadFile = File(None)):
    response = await upload_image(image_file)
    return response
