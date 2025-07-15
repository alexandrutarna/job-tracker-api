# tests/conftest.py

import pytest
from app.database import SessionLocal
from app import models

@pytest.fixture(autouse=True)
def clean_db():
    """Clean the DB before each test to ensure test isolation."""
    db = SessionLocal()
    try:
        db.query(models.Job).delete()
        db.commit()
        print("[DB CLEANUP] Truncated jobs table")
    finally:
        db.close()
