# Data Model

Minimum entities for the MVP, per `BUILD_GUIDE.md` §6. Implemented as SQLAlchemy models in `backend/app/models/`.

## Patient
- `id` (PK)
- `name`
- `dob`
- `sex`
- `phone`
- `email` (optional)
- `insurance_id` (optional, dummy)
- One patient → many visits

## Visit
- `id` (PK)
- `patient_id` (FK → Patient)
- `queue_number`
- `status` — one of: `waiting`, `in_intake`, `ready_for_doctor`, `with_doctor`, `completed`
- `created_at`, `updated_at`
- Central unit for the MVP workflow; everything below hangs off a visit.

## Vitals
- `id` (PK)
- `visit_id` (FK → Visit)
- `blood_pressure`
- `temperature`
- `pulse`
- `spo2`
- `weight`
- `intake_note`
- Entered by nurse.

## Document
- `id` (PK)
- `visit_id` (FK → Visit)
- `filename`
- `type` (e.g. `pdf`, `image`)
- `file_url`
- Sample reports only.

## DoctorNote
- `id` (PK)
- `visit_id` (FK → Visit)
- `raw_transcript`
- `edited_note`
- `final_note`
- `approved_at` (nullable — set on approval, note becomes read-only)
- Core voice-AI record. See `BUILD_GUIDE.md` §4 for the version-storage rule (raw transcript and final note are never edited after their respective lock points).

## Audio
- `id` (PK)
- `note_id` (FK → DoctorNote)
- `audio_file_url`
- `created_at`
- Keeps the original dictation.

## Prescription
- `id` (PK)
- `visit_id` (FK → Visit)
- `medicine`
- `instructions`
- `duration`
- `pharmacy_name` (optional)
- `status` — one of: `draft`, `sent`, `received`
- Simulated sending only.

## LabOrder
- `id` (PK)
- `visit_id` (FK → Visit)
- `test_name`
- `notes`
- `lab_name` (optional)
- `status` — one of: `draft`, `sent`, `completed`
- Simulated sending only.

## User
- `id` (PK)
- `name`
- `role` — one of: `front_desk`, `nurse`, `doctor`, `admin`
- `login_identifier`
- Prototype role access only (single shared login page is acceptable per the guide).

## Relationships

```
Patient 1───* Visit 1───1 Vitals
                   │
                   ├──* Document
                   ├──* DoctorNote 1───1 Audio
                   ├──* Prescription
                   └──* LabOrder
```
