# FastAPI Starter Template

A modern, high-performance FastAPI starter template emphasizing async architecture, type safety, modular structure, and clean Python tooling.

## Prerequisites & Package Manager

This project exclusively uses **uv**, a blazingly fast Python package manager written in Rust. Before starting, check if you have it installed:

```bash
uv --version
```

### Installing uv (If not installed)

If the command above is not recognized, install `uv` using one of the following official methods for your OS:

* **macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

* **Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Quick Start

Setting up the project environment takes just a single command.

1. **Install all dependencies and setup environment:**

```bash
uv sync
```

*This command automatically creates an isolated virtual environment (`.venv`) and installs both core project dependencies and development tools.*

2. **Activate the virtual environment:**

* **Windows (Command Prompt):**

```cmd
.venv\Scripts\activate
```

* **macOS / Linux:**

```bash
source .venv/bin/activate
```

3. **Install Git pre-commit hooks (required after cloning):**

```bash
uv run pre-commit install
```

*(Note: Using `uv run` ensures `pre-commit` is executed directly from your project's isolated virtual environment).*

---

## Project Architecture

To maintain code readability and scalability, this template uses a clean, modular structure inside the `app/` directory:

```text
app/
├── api/                  # API routers and versioning (v1, v2, etc.)
│   └── v1/
│       ├── endpoints/    # Individual domain endpoints (health, auth, etc.)
│       └── router.py     # Main API Router aggregating all v1 routes
├── core/                 # Core configs, security settings, and app handlers
│   └── config.py         # Pydantic Settings management
├── db/                   # Database engine, session management, and Base ORM
│   ├── base.py           # Centralized Base import for Alembic
│   └── session.py        # Async SQLAlchemy session provider
├── models/               # SQLAlchemy ORM Models
├── schemas/              # Pydantic Schemas (Request / Response validation)
├── services/             # Business logic layer
└── main.py               # FastAPI application entrypoint & lifespan
```

### Adding New API Endpoints

1. Create a new module inside `app/api/v1/endpoints/` (e.g., `users.py`).
2. Define your `APIRouter()` and endpoint routes.
3. Include the new router inside `app/api/v1/router.py`:

```python
from app.api.v1.endpoints import users

api_router.include_router(users.router, prefix="/users", tags=["Users"])
```

---

## Code Quality & Manual Ruff Controls

We use **Ruff** for linting and formatting. It replaces Flake8, Isort, and Black with a single, blazingly fast tool.
While checking occurs automatically on every commit via the `pre-commit` pipeline, you can run Ruff manually without creating a commit:

```bash
# Run static analysis (Linter) on all files
uv run ruff check .
```

```bash
# Run static analysis and automatically fix safe violations
uv run ruff check . --fix
```

```bash
# Format all Python files according to style guidelines
uv run ruff format .
```

```bash
# Run checks manually via pre-commit on all files
uv run pre-commit run --all-files
```

---

## Testing & Coverage Suite

The project utilizes `pytest` with `pytest-asyncio` and `httpx` for testing async endpoints.

```bash
# Run full test suite
uv run pytest
```

```bash
# Run tests with verbose output
uv run pytest -v
```

```bash
# Run tests and show local variables on failures
uv run pytest --showlocals
```

---

## Configuration & Security

1. **Environment Variables:**
   Copy the example environment file and fill in your local settings:

```bash
cp .env.example .env
```

2. **Secret Key & Security Settings:**
   **CRITICAL:** Ensure you update `SECRET_KEY` in your `.env` file before deploying to production. You can generate a secure random string using Python:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

3. **CORS Configuration:**
   Configure `BACKEND_CORS_ORIGINS` in your `.env` to restrict cross-origin requests to your trusted frontend domains:

```env
BACKEND_CORS_ORIGINS="http://localhost:3000,http://localhost:5173"
```

---

## Database Infrastructure & Migrations

This template is configured for **PostgreSQL** using **SQLAlchemy 2.0 (Async)** and **asyncpg**. Database migrations are managed via **Alembic**.

1. Ensure your PostgreSQL server is running.
2. Update database credentials in `.env` (`POSTGRES_SERVER`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`).
3. Generate a new migration revision:

```bash
uv run alembic revision --autogenerate -m "Initial migration"
```

4. Apply migrations to the database:

```bash
uv run alembic upgrade head
```

---

## Running the Development Server

Once migrations are applied, start the FastAPI ASGI server with auto-reload:

```bash
uv run uvicorn app.main:app --reload
```

* **Interactive API Docs (Swagger UI):** `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)`
* **Alternative API Docs (ReDoc):** `[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)`
* **Health Check Endpoint:** `[http://127.0.0.1:8000/api/v1/health](http://127.0.0.1:8000/api/v1/health)`

---

## Updates

- **To update project dependencies and sync lockfile:**

```bash
uv lock --upgrade && uv sync
```

- **To update pre-commit hooks:**

```bash
uv run pre-commit autoupdate
```
