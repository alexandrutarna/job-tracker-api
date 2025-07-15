# Job Tracker API

A mock FastAPI project that simulates job submission and tracking — inspired by CERN's LHCb data pipelines using DIRAC. It is fully containerized using Docker Compose and includes PostgreSQL and pgAdmin for easy development and debugging.

---

## 🚀 Features

- ✅ Submit, read, update, and delete simulated jobs  
- 🐘 PostgreSQL-backed database  
- 📦 Fully dockerized (no local setup required)  
- 🧪 Built-in testing with Pytest and HTTPX  
- 📄 Auto-generated Swagger docs with example payloads  
- 👀 pgAdmin UI for database inspection  

---

## 🛠️ Tech Stack

| Layer      | Tech                     |
|------------|--------------------------|
| Backend    | Python 3.11 + FastAPI    |
| Database   | PostgreSQL 15            |
| Admin UI   | pgAdmin 4                |
| Container  | Docker & Docker Compose  |
| Testing    | Pytest, HTTPX            |

---

## 📦 Project Structure

```bash
job-tracker-api/
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas for validation
│   ├── database.py          # DB engine & session
│   ├── routers/
│   │   └── jobs.py          # Modular job routes
│   └── init_db.py           # DB table creator script
├── tests/
│   ├── __init__.py
│   └── test_jobs.py         # API tests using httpx
├── Dockerfile               # API container
├── docker-compose.yml       # Full-stack services
├── requirements.txt         # Python deps
├── .env                     # DB connection vars
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/alexandrutarna/job-tracker-api.git
cd job-tracker-api
```

### 2. Set environment variables

Create a `.env` file in the root folder:

```env
POSTGRES_DB=jobtracker
POSTGRES_USER=jobuser
POSTGRES_PASSWORD=jobpass
DATABASE_URL=postgresql://jobuser:jobpass@db:5432/jobtracker
```

### 3. Build and start the containers

```bash
docker-compose up --build
```

### 4. Initialize the database

In a second terminal:

```bash
docker-compose exec api python app/init_db.py
```

---

## 🧪 API Documentation

FastAPI generates Swagger and ReDoc UIs automatically:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc UI: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📡 API Examples

### 🔁 POST `/jobs` — Create job

```json
{
  "name": "Build CERN data pipeline",
  "status": "queued",
  "result": null
}
```

### 📄 GET `/jobs` — List all jobs

```json
[
  {
    "id": 1,
    "name": "Build CERN data pipeline",
    "status": "queued",
    "result": null,
    "created_at": "2025-07-15T13:54:23.591450"
  }
]
```

### 🔍 GET `/jobs/{id}` — Fetch job by ID

```json
{
  "id": 1,
  "name": "Build CERN data pipeline",
  "status": "queued",
  "result": null,
  "created_at": "2025-07-15T13:54:23.591450"
}
```

### ✏️ PATCH `/jobs/{id}` — Update job

```json
{
  "status": "running",
  "result": "Started execution"
}
```

### ❌ DELETE `/jobs/{id}` — Delete job

```json
{
  "message": "Job deleted successfully"
}
```

---

## 🧰 pgAdmin Access

- URL: [http://localhost:5050](http://localhost:5050)  
- Email: `admin@example.com`  
- Password: `admin`  

To register a server:

- **Host**: `db`  
- **Port**: `5432`  
- **Username**: `jobuser`  
- **Password**: `jobpass`  
- **Database**: `jobtracker`

---

## ✅ API Endpoints Summary

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | `/`              | Health check             |
| POST   | `/jobs`          | Create a job             |
| GET    | `/jobs`          | List all jobs            |
| GET    | `/jobs/{id}`     | Get a specific job       |
| PATCH  | `/jobs/{id}`     | Update job fields        |
| DELETE | `/jobs/{id}`     | Delete a job             |

---

## 🧪 Running Tests

Make sure containers are running, then run:

```bash
make test
```

This will run the Pytest test suite inside the Docker container using `httpx`.

---

## 🧭 Next Steps

- Add authentication and user roles  
- Export job results to CSV or JSON  
- Refactor with Poetry for dependency management  
- Enable CI/CD with GitHub Actions  
- Add test coverage and badges
