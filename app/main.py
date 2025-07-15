from fastapi import FastAPI
from app.routers import jobs  # import the router module

app = FastAPI()

# Root route for health check
@app.get("/")
def read_root():
    return {"message": "Job Tracker API is up and running"}

# Register the jobs API router
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])  # include router
