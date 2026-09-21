from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/patients", tags=["patients"])


@router.post("")
def create_patient():
    raise HTTPException(status_code=501, detail="Not implemented")
