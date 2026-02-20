from fastapi import FastAPI
from .database import engine
from . import models
from .routers import items

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Items API")

app.include_router(items.router)