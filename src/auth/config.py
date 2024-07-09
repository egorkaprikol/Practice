from fastapi import FastAPI
from passlib.context import CryptContext


SECRET_KEY = "675955430gf44gfj34sdfs454dGdg5vhj32wds"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()
