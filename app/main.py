from fastapi import FastAPI
from .database import engine
from . import models
from .routers import items

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app with metadata
app = FastAPI(
    title="Items API",
    description="REST API built with FastAPI",
    version="1.0.0"
)

# Include routers
app.include_router(items.router)


@app.get("/", tags=["Health Check"])
def root():
    """
    Root endpoint to verify that the API is running.
    """
    return {
        "status": "ok",
        "message": "Items API is running 🚀",
        "documentation": "/docs"
    }