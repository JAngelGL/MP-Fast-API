"""
CRUD Operations Module

This module contains the data access layer (CRUD operations)
for the Item entity.

Responsibilities:
- Interact directly with the database session
- Execute queries using SQLAlchemy ORM
- Isolate business logic from API routes
"""

from sqlalchemy.orm import Session
from . import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of items with pagination support.

    Parameters:
    - db: Active database session
    - skip: Number of records to skip (offset)
    - limit: Maximum number of records to return

    Returns:
    - List of Item ORM objects
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    """
    Retrieve a single item by its ID.

    Parameters:
    - db: Active database session
    - item_id: Unique identifier of the item

    Returns:
    - Item ORM object if found
    - None if item does not exist
    """
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemCreate):
    """
    Create a new item in the database.

    Parameters:
    - db: Active database session
    - item: Validated ItemCreate schema

    Process:
    - Convert Pydantic schema to dictionary
    - Instantiate ORM model
    - Persist to database
    - Refresh instance to retrieve generated fields (e.g., ID)

    Returns:
    - Newly created Item ORM object
    """
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    """
    Update an existing item.

    Parameters:
    - db: Active database session
    - item_id: ID of the item to update
    - item: Validated ItemUpdate schema

    Returns:
    - Updated Item ORM object
    - None if item does not exist
    """
    db_item = get_item(db, item_id)
    if not db_item:
        return None

    # Dynamically update fields using Pydantic model data
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    """
    Delete an item from the database.

    Parameters:
    - db: Active database session
    - item_id: ID of the item to delete

    Returns:
    - Deleted Item ORM object
    - None if item does not exist
    """
    db_item = get_item(db, item_id)
    if not db_item:
        return None

    db.delete(db_item)
    db.commit()
    return db_item