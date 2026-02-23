"""
Database Configuration Module

This module is responsible for:

- Creating the database engine
- Configuring the session factory
- Defining the Base class for ORM models

It supports environment-based configuration and defaults to SQLite
for local development if no DATABASE_URL is provided.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


# Database connection string
# Priority:
# 1. Uses DATABASE_URL from environment variables
# 2. Falls back to SQLite local database for development
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")


# Create SQLAlchemy engine
# If using SQLite, we must disable same-thread check
# because SQLite has thread limitations in development environments.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)


# Session factory
# - autocommit=False ensures explicit transaction control
# - autoflush=False prevents automatic DB flush before queries
# - bind=engine attaches session to the database engine
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for all ORM models
# Every model (e.g., Item) must inherit from this Base
# so SQLAlchemy can map classes to database tables.
Base = declarative_base()