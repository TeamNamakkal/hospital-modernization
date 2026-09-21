# API Contract

Minimum API contract per `BUILD_GUIDE.md` §7. Endpoint naming can change, but each operation below must exist in some form. Agree on any changes as a team before diverging frontend/backend work.

All endpoints are currently scaffolded in `backend/app/routers/` as stubs returning `501 Not Implemented` until built out.

| Method | Endpoint | Purpose | Used By | Status |
|---|---|---|---|---|
| POST | `/api/patients` | Create patient | Front desk | stub |
| POST | `/api/visits` | Create/check-in visit | Front desk | stub |
| GET | `/api/queue` | List active queue | All clinical roles | stub |
| PATCH | `/api/visits/{id}/status` | Change queue/visit status | Nurse/Doctor | stub |
| POST | `/api/visits/{id}/vitals` | Save vitals | Nurse | stub |
| POST | `/api/visits/{id}/documents` | Upload report | Nurse | stub |
| GET | `/api/visits/{id}` | Load complete visit record | Doctor | stub |
| POST | `/api/visits/{id}/audio` | Save dictation audio | Doctor | stub |
| POST | `/api/visits/{id}/transcribe` | Generate raw transcript | Doctor | stub |
| POST | `/api/visits/{id}/rewrite-note` | Create AI-organized draft | Doctor | stub |
| POST | `/api/notes/{id}/approve` | Approve final note | Doctor | stub |
| POST | `/api/visits/{id}/prescriptions` | Create prescription | Doctor | stub |
| POST | `/api/visits/{id}/lab-orders` | Create lab order | Doctor | stub |

Also present:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Backend health check (returns `{"status": "ok"}`) |
