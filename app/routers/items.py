"""
Items Router Module

This module defines the HTTP endpoints for the Item resource.

Responsibilities:
- Handle HTTP requests
- Perform dependency injection (database session)
- Call CRUD layer functions
- Handle HTTP exceptions
- Return validated responses using Pydantic schemas
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal


# Router configuration
# - prefix="/items" means all routes start with /items
# - tags=["Items"] groups endpoints in Swagger documentation
router = APIRouter(prefix="/items", tags=["Items"])


def get_db():
    """
    Dependency that provides a database session.

    - Creates a new session for each request
    - Ensures the session is properly closed after request completion
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.ItemResponse])
def read_items(db: Session = Depends(get_db)):
    """
    Retrieve a list of items.

    Returns:
    - HTTP 200
    - List of ItemResponse schemas
    """
    return crud.get_items(db)


@router.get("/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single item by ID.

    Returns:
    - HTTP 200 if found
    - HTTP 404 if item does not exist
    """
    item = crud.get_item(db, item_id)

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    return item


@router.post("/", response_model=schemas.ItemResponse, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.

    Returns:
    - HTTP 201 (Created)
    - Newly created item
    """
    return crud.create_item(db, item)


@router.put("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    """
    Update an existing item by ID.

    Returns:
    - HTTP 200 if successful
    - HTTP 404 if item does not exist
    """
    updated = crud.update_item(db, item_id, item)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    return updated


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by ID.

    Returns:
    - HTTP 204 (No Content) if successful
    - HTTP 404 if item does not exist
    """
    deleted = crud.delete_item(db, item_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    return {"detail": "Item deleted"}