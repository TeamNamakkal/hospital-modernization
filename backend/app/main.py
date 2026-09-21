from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import notes, patients, queue, visits

app = FastAPI(title="Hospital Modernization API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patients.router)
app.include_router(visits.router)
app.include_router(queue.router)
app.include_router(notes.router)


@app.get("/health")
def health():
    return {"status": "ok"}
