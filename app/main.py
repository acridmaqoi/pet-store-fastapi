from fastapi import FastAPI

from . import models
from .database import engine
from .routers import pets, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/hello")
def hello_world():
    return {"message": "Hello, World!"}


app.include_router(pets.router, prefix="/pets", tags=["pets"])
app.include_router(users.router, prefix="/users", tags=["users"])
