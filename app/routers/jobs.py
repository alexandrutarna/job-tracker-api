# app/routers/jobs.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from datetime import datetime

from app.database import get_db
from app import models, schemas
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.JobResponse)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = models.Job(
        name=job.name,
        status=job.status,
        result=job.result,
        created_at=datetime.utcnow()
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


@router.get("/{job_id}", response_model=schemas.JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.get("/", response_model=List[schemas.JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()
    return jobs


@router.patch("/{job_id}", response_model=schemas.JobResponse)
def update_job(job_id: int, updates: schemas.JobUpdate, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)
    return job

@router.delete("/{job_id}", status_code=204)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    db.delete(job)
    db.commit()
    return
