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
