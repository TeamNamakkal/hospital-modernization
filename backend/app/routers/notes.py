from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/notes", tags=["notes"])


@router.post("/{note_id}/approve")
def approve_note(note_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")
