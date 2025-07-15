import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_get_update_delete_job():
    # Create
    response = client.post("/jobs/", json={"name": "Test Job"})
    assert response.status_code == 200
    job = response.json()
    job_id = job["id"]
    assert job["name"] == "Test Job"

    # Get
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json()["id"] == job_id

    # Update
    update_data = {"status": "done", "result": "Completed successfully"}
    response = client.patch(f"/jobs/{job_id}", json=update_data)
    assert response.status_code == 200
    updated = response.json()
    assert updated["status"] == "done"
    assert updated["result"] == "Completed successfully"

    # Delete
    response = client.delete(f"/jobs/{job_id}")
    assert response.status_code == 204

    # Confirm deletion
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 404


@pytest.fixture
def job_data():
    return {
        "name": "Unit Test Job",
        "status": "queued",
        "result": None
    }

@pytest.fixture
def created_job(job_data):
    response = client.post("/jobs/", json=job_data)
    assert response.status_code == 200
    return response.json()

def test_create_job(job_data):
    response = client.post("/jobs/", json=job_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == job_data["name"]
    assert data["status"] == "queued"
    assert data["result"] is None

def test_read_job(created_job):
    job_id = created_job["id"]
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json()["id"] == job_id

def test_update_job(created_job):
    job_id = created_job["id"]
    update_data = {"status": "done", "result": "Success"}
    response = client.patch(f"/jobs/{job_id}", json=update_data)
    assert response.status_code == 200
    updated = response.json()
    assert updated["status"] == "done"
    assert updated["result"] == "Success"

def test_list_jobs(created_job):
    response = client.get("/jobs/")
    assert response.status_code == 200
    jobs = response.json()
    assert any(j["id"] == created_job["id"] for j in jobs)

def test_delete_job(created_job):
    job_id = created_job["id"]
    response = client.delete(f"/jobs/{job_id}")
    assert response.status_code == 204

    # Confirm deletion
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 404