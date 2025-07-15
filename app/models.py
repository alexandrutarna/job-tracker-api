from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, default="queued")
    result = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
