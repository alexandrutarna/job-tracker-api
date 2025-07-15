from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class JobBase(BaseModel):
    name: str
    status: Optional[str] = "queued"
    result: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Build CERN data pipeline",
                    "status": "queued",
                    "result": None
                }
            ]
        }
    }


class JobCreate(JobBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Run data analysis",
                    "status": "queued",
                    "result": None
                }
            ]
        }
    }


class JobResponse(JobBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Run data analysis",
                    "status": "queued",
                    "result": None,
                    "created_at": "2025-07-15T13:54:23.591450"
                }
            ]
        }
    }


class JobUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    result: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Analyze data batch 42",
                    "status": "done",
                    "result": "Job completed successfully"
                }
            ]
        }
    }
