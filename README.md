# Job Tracker API

A mock FastAPI project that simulates job submission and tracking, inspired by CERN's LHCb use of DIRAC. It is fully containerized using Docker Compose and includes PostgreSQL and pgAdmin.

## 🚀 Features

- Submit and track simulated jobs
- PostgreSQL-backed database
- Fully dockerized (no local setup required)
- Auto-generated Swagger docs
- pgAdmin UI for database inspection

## 🛠️ Stack

- **Backend**: Python 3.11 + FastAPI
- **Database**: PostgreSQL 15
- **Admin UI**: pgAdmin 4
- **Containerized**: Docker & Docker Compose

---

## 📦 Project Structure

job-tracker-api/
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── routers/ # API routes (modular)
├── Dockerfile # API container
├── docker-compose.yml # Full-stack services
├── requirements.txt # Python deps
├── .env # DB connection vars
├── .dockerignore
└── README.md

---


---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/job-tracker-api.git
cd job-tracker-api
```

### 2. Start all services

```bash
docker-compose up --build
```

### 3. Open the app

- FastAPI Swagger UI: <http://localhost:8000/docs>

- pgAdmin: <http://localhost:5050>
  - Email: <admin@example.com>
  - Password: admin

## 📌 Environment Variables

Create a `.env` file in the root folder with the following contents:

```env
# Example values (for local development only)
POSTGRES_DB=jobtracker
POSTGRES_USER=jobuser
POSTGRES_PASSWORD=jobpass
DATABASE_URL=postgresql://jobuser:jobpass@db:5432/jobtracker
```
