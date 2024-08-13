from pydantic import BaseModel


class SignUpRequest(BaseModel):
    phone_number: str
    password: str


class RoleBase(BaseModel):
    name: str


class SignInRequest(BaseModel):
    phone_number: str
    password: str


class SignInResponse(BaseModel):
    access_token: str


class UserBase(BaseModel):
    id: int
    phone_number: str
    hashed_password: str

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    phone_number: str
    password: str


class AdminBase(BaseModel):
    name: str
    surname: str
    patronymic: str = None


class AdminCreateRequest(AdminBase):
    phone_number: str
    password: str


class AdminUpdate(BaseModel):
    name: str
    surname: str
    patronymic: str = None
