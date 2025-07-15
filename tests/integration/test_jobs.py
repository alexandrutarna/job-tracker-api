# import pytest
# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

# def test_create_get_update_delete_job():
#     # Create
#     response = client.post("/jobs/", json={"name": "Test Job"})
#     assert response.status_code == 200
#     job = response.json()
#     job_id = job["id"]
#     assert job["name"] == "Test Job"

#     # Get
#     response = client.get(f"/jobs/{job_id}")
#     assert response.status_code == 200
#     assert response.json()["id"] == job_id

#     # Update
#     update_data = {"status": "done", "result": "Completed successfully"}
#     response = client.patch(f"/jobs/{job_id}", json=update_data)
#     assert response.status_code == 200
#     updated = response.json()
#     assert updated["status"] == "done"
#     assert updated["result"] == "Completed successfully"

#     # Delete
#     response = client.delete(f"/jobs/{job_id}")
#     assert response.status_code == 204

#     # Confirm deletion
#     response = client.get(f"/jobs/{job_id}")
#     assert response.status_code == 404


# @pytest.fixture
# def job_data():
#     return {
#         "name": "Unit Test Job",
#         "status": "queued",
#         "result": None
#     }

# @pytest.fixture
# def created_job(job_data):
#     response = client.post("/jobs/", json=job_data)
#     assert response.status_code == 200
#     return response.json()

# def test_create_job(job_data):
#     response = client.post("/jobs/", json=job_data)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == job_data["name"]
#     assert data["status"] == "queued"
#     assert data["result"] is None

# def test_read_job(created_job):
#     job_id = created_job["id"]
#     response = client.get(f"/jobs/{job_id}")
#     assert response.status_code == 200
#     assert response.json()["id"] == job_id

# def test_update_job(created_job):
#     job_id = created_job["id"]
#     update_data = {"status": "done", "result": "Success"}
#     response = client.patch(f"/jobs/{job_id}", json=update_data)
#     assert response.status_code == 200
#     updated = response.json()
#     assert updated["status"] == "done"
#     assert updated["result"] == "Success"

# def test_list_jobs(created_job):
#     response = client.get("/jobs/")
#     assert response.status_code == 200
#     jobs = response.json()
#     assert any(j["id"] == created_job["id"] for j in jobs)

# def test_delete_job(created_job):
#     job_id = created_job["id"]
#     response = client.delete(f"/jobs/{job_id}")
#     assert response.status_code == 204

#     # Confirm deletion
#     response = client.get(f"/jobs/{job_id}")
#     assert response.status_code == 404




import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_job():
    response = client.post("/jobs/", json={
        "name": "Test Job",
        "status": "queued",
        "result": None
    })

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data["id"], int)
    assert data["name"] == "Test Job"
    assert data["status"] == "queued"
    assert data["result"] is None
    assert "created_at" in data


def test_get_job_by_id():
    # First create
    create_resp = client.post("/jobs/", json={"name": "Test", "status": "queued", "result": None})
    job_id = create_resp.json()["id"]

    # Then fetch
    get_resp = client.get(f"/jobs/{job_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == job_id

def test_update_job():
    # Create
    create_resp = client.post("/jobs/", json={"name": "Old", "status": "queued"})
    job_id = create_resp.json()["id"]

    # Update
    update_resp = client.patch(f"/jobs/{job_id}", json={"status": "done", "result": "Success"})
    assert update_resp.status_code == 200
    assert update_resp.json()["status"] == "done"
    assert update_resp.json()["result"] == "Success"

def test_delete_job():
    create_resp = client.post("/jobs/", json={"name": "Delete Me", "status": "queued"})
    job_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/jobs/{job_id}")
    assert delete_resp.status_code == 204
    assert delete_resp.content == b''  # 204 has no content

    # Optionally verify the job is gone
    get_resp = client.get(f"/jobs/{job_id}")
    assert get_resp.status_code == 404
