from pydantic import BaseModel


class SignUpRequest(BaseModel):
    login: str
    password: str


class SignInRequest(BaseModel):
    login: str
    password: str


class SignInResponse(BaseModel):
    access_token: str


class UserBase(BaseModel):
    id: int
    login: str
    hashed_password: str

    class Config:
        from_attributes = True

