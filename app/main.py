from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from .internal.database import Base, engine
from .internal.models.record import RecordNotFound, RecordRelationNotFound
from .routers import auth, pets, store, users

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.exception_handler(RecordNotFound)
def not_found_exception_handler(request: Request, exc: RecordNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": exc.detail}
    )


@app.exception_handler(RecordRelationNotFound)
def relation_not_found_exception_handler(request: Request, exc: RecordRelationNotFound):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": exc.detail}
    )


@app.get("/hello")
def hello_world():
    return {"message": "Hello, World!"}


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(pets.router, prefix="/pets", tags=["pets"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(store.router, prefix="/store", tags=["store"])
