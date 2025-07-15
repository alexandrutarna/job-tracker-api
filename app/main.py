from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Job Tracker API is up and running"}
