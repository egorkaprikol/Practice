from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from src.auth.repository import get_current_user, authenticate_user, create_access_token
from src.auth.repository import create_user
from src.database.config import get_db
from src.auth.schemas import SignUpRequest, SignInRequest, SignInResponse

router = APIRouter()


@router.post("/admin", status_code=status.HTTP_201_CREATED)
async def register(request: SignUpRequest, db: Session = Depends(get_db)):
    user = create_user(db, request.login, request.password, "admin")
    return user


@router.post("/login")
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


@router.get("/default/secure")
def secure(user=Depends(get_current_user)):
    return {"message": "This is a secure endpoint for " + user["login"]}

