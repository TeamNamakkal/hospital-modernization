from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/queue", tags=["queue"])


@router.get("")
def list_queue():
    raise HTTPException(status_code=501, detail="Not implemented")
