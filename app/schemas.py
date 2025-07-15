from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class JobBase(BaseModel):
    name: str = Field(..., example="Build CERN data pipeline")
    status: Optional[str] = Field(default="queued", example="queued")
    result: Optional[str] = Field(default=None, example=None)

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
    id: int = Field(..., example=1)
    created_at: datetime = Field(..., example="2025-07-15T13:54:23.591450")

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
    name: Optional[str] = Field(default=None, example="Analyze data batch 42")
    status: Optional[str] = Field(default=None, example="running")
    result: Optional[str] = Field(default=None, example="Success")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "done",
                    "result": "Job completed successfully"
                }
            ]
        }
    }