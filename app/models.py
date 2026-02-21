from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base


# SQLAlchemy model that represents the "items" table in the database
class Item(Base):
    # Name of the table in the database
    __tablename__ = "items"

    # Primary key identifier.
    # - Integer type
    # - Automatically indexed for faster lookups
    # - Uniquely identifies each record
    id = Column(Integer, primary_key=True, index=True)

    # Name of the item.
    # - Required field (nullable=False)
    # - Stored as variable-length string
    name = Column(String, nullable=False)

    # Detailed description of the item.
    # - Required field
    # - Stored as variable-length string
    description = Column(String, nullable=False)

    # Monetary value of the item.
    # - Required field
    # - Stored as floating-point number
    price = Column(Float, nullable=False)

    # Availability status of the item.
    # - Boolean field
    # - Defaults to True if not explicitly provided
    available = Column(Boolean, default=True)