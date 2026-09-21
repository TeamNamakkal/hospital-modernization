from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/visits", tags=["visits"])


@router.post("")
def create_visit():
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{visit_id}")
def get_visit(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.patch("/{visit_id}/status")
def update_visit_status(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{visit_id}/vitals")
def save_vitals(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{visit_id}/documents")
def upload_document(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{visit_id}/audio")
def save_audio(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{visit_id}/transcribe")
def transcribe_audio(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{visit_id}/rewrite-note")
def rewrite_note(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{visit_id}/prescriptions")
def create_prescription(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{visit_id}/lab-orders")
def create_lab_order(visit_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")
