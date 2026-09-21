# Hospital Modernization — Student MVP

A 6-week student prototype demonstrating one complete patient journey:

**Patient Signup → Queue → Nurse Intake → Doctor Consultation → Voice Note → AI Rewrite → Doctor Approval → Lab/Prescription Order**

Dummy/synthetic patient data only. This is a prototype, not a production clinical system. See [`docs/PROJECT_MVP.md`](docs/PROJECT_MVP.md) and [`docs/BUILD_GUIDE.md`](docs/BUILD_GUIDE.md) for full scope and requirements.

## Stack

- **Frontend:** Next.js (App Router, TypeScript, Tailwind) — [`frontend/`](frontend/)
- **Backend:** FastAPI — [`backend/`](backend/)
- **Database:** PostgreSQL

## Quick Start

### With Docker

```bash
docker compose up
```

Frontend: http://localhost:3000 · Backend: http://localhost:8000/health

### Without Docker

**Backend:**

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # point DATABASE_URL at your local Postgres
uvicorn app.main:app --reload
```

**Frontend:**

```bash
cd frontend
npm install
npm run dev
```

## Documentation

| Doc | Contents |
|---|---|
| [`docs/PROJECT_MVP.md`](docs/PROJECT_MVP.md) | Project goal, scope, 5 development steps, schedule, acceptance criteria |
| [`docs/BUILD_GUIDE.md`](docs/BUILD_GUIDE.md) | Full functional requirements, architecture, voice/AI workflow rules |
| [`docs/DATA_MODEL.md`](docs/DATA_MODEL.md) | Entity definitions used by `backend/app/models/` |
| [`docs/API_CONTRACT.md`](docs/API_CONTRACT.md) | Endpoint list and implementation status |
| [`original-docs/`](original-docs/) | Source `.docx`/`.pdf` files this project is derived from |

## Team

| Student | Primary Area |
|---|---|
| 1 | Patient signup + queue |
| 2 | Nurse intake + document uploads |
| 3 | Doctor dashboard + patient record |
| 4 | Voice-to-text + AI note |
| 5 | Orders + backend integration + testing |

All work happens in this one shared repository — no student module is "done" until it works in the integrated app. See `docs/BUILD_GUIDE.md` §8 for the week-by-week plan.

## Status

Repository skeleton only — routes and endpoints are stubs. Next step per the build guide: **Patient Signup → Queue → Nurse Intake** vertical slice.
