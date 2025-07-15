# Job Tracker API

A mock FastAPI project that simulates job submission and tracking — inspired by CERN's LHCb data pipelines using DIRAC. It is fully containerized using Docker Compose and includes PostgreSQL and pgAdmin for easy development and debugging.

## 🚀 Features

- ✅ Submit and track simulated jobs  
- 🐘 PostgreSQL-backed database  
- 📦 Fully dockerized (no local setup required)  
- 📄 Auto-generated Swagger docs with example payloads  
- 👀 pgAdmin UI for database inspection  

## 🛠️ Tech Stack

| Layer      | Tech                     |
|------------|--------------------------|
| Backend    | Python 3.11 + FastAPI    |
| Database   | PostgreSQL 15            |
| Admin UI   | pgAdmin 4                |
| Container  | Docker & Docker Compose  |

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
├── Dockerfile               # API container
├── docker-compose.yml       # Full-stack services
├── requirements.txt         # Python deps
├── .env                     # DB connection vars
└── README.md
```

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

## 🧪 API Documentation

FastAPI generates Swagger and ReDoc UIs automatically:

- Swagger: <http://localhost:8000/docs>  
- ReDoc: <http://localhost:8000/redoc>

### 🔁 Example JSON (POST `/jobs`)

```json
{
  "name": "Build CERN data pipeline",
  "status": "queued",
  "result": null
}
```

### 📄 Example Response (GET `/jobs`)

```json
[
  {
    "id": 1,
    "name": "Build CERN data pipeline",
    "status": "queued",
    "result": null
  }
]
```

### 🗂️ Example Response (GET `/jobs/{id}`)

```json
{
  "id": 1,
  "name": "Build CERN data pipeline",
  "status": "queued",
  "result": null
}
```

### 🔄 Example Update (PATCH `/jobs/{id}`)

```json
{
  "status": "running"
}
```

### ❌ Example Delete (DELETE `/jobs/{id}`)

```json
{
  "message": "Job deleted successfully"
}
```

## 🧰 pgAdmin Access

- URL: <http://localhost:5050>  
- Email: `admin@example.com`  
- Password: `admin`  

Add a new server:

- **Host**: `db`  
- **Port**: `5432`  
- **Username**: `jobuser`  
- **Password**: `jobpass`  
- **Database**: `jobtracker`

## ✅ API Status

- `GET /` → Health check  
- `POST /jobs` → Submit a job  
- `GET /jobs` → List all jobs  
- `GET /jobs/{id}` → Get job by ID
- `PATCH /jobs/{id}` → Update job status
- `DELETE /jobs/{id}` → Delete job by ID
