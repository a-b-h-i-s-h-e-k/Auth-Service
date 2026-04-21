from fastapi import FastAPI
from .database import Base, engine
from .routers import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Auth Service running"}