from pydantic import BaseModel


class SignUpRequest(BaseModel):
    login: str
    password: str


class RoleBase(BaseModel):
    name: str


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


class UserUpdate(BaseModel):
    login: str
    password: str


class AdminBase(BaseModel):
    name: str
    surname: str
    patronymic: str = None


class AdminCreateRequest(AdminBase):
    login: str
    password: str

