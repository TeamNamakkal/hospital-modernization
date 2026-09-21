# Hospital Modernization — Student MVP Project

6-Week University Project | 5 Students | 4 Development Weeks
Project Platform: www.exploreN2P.com

## Project Goal

Build a working prototype that demonstrates one complete patient journey from registration to doctor-approved notes and a lab or prescription order.

**Dummy/synthetic patient data only.**

## Project Scope

The prototype follows the hospital workflow shown in the modernization diagram (see `original-docs/GF_HOSPITAL MODERNIZATION.pdf`): patient registration, queue management, nurse intake, doctor consultation, laboratory/pharmacy orders, record storage, and patient information access.

**Final MVP Flow:**

Patient Signup → Queue → Nurse Intake → Doctor Consultation → Voice Note → AI Rewrite → Doctor Approval → Lab/Prescription Order

## The 5 Development Steps

### 1. Patient Signup + Queue
Create a simple web form for a dummy patient and place the patient into a queue.
- Patient registration form
- Patient queue/status screen
- Basic desktop/web notification

### 2. Nurse Intake + Patient Record
Create the patient record used by the clinical team.
- Enter vitals and basic patient information
- Enter insurance/administrative details
- Upload sample medical reports

### 3. Doctor Consultation + Voice AI
Allow the doctor to review the patient record and create consultation notes by voice.
- Record doctor dictation
- Convert voice to text
- AI organizes/re-writes the note
- Doctor edits and reviews the note
- Doctor approves the final note
- Store: raw material/transcript, doctor-edited version, final approved version

### 4. Prescription + Lab Order
Allow the doctor to create a prescription or diagnostic test request.
- Create prescription order
- Create lab/test order
- Simulate sending the order
- Store order and status in the patient record

### 5. Integration + Final Demo
Connect all modules into one working patient journey and prepare the handover.
- End-to-end testing
- Fix major issues
- Final demonstration
- Short technical documentation
- Source-code and setup handover

## 5-Student Work Assignment

| Student | Primary Area | Main Responsibility |
|---|---|---|
| Student 1 | Patient + Queue | Signup, patient queue, status screen |
| Student 2 | Nurse + Records | Vitals, intake, document upload |
| Student 3 | Doctor UI | Doctor dashboard and consultation workflow |
| Student 4 | Voice AI | Voice-to-text, AI rewrite, edit/approval flow |
| Student 5 | Orders + Integration | Prescription/lab order, integration and testing |

## 6-Week Schedule

| Week | Focus | Expected Output |
|---|---|---|
| 1 | Introduction + planning | Access, requirements, design, task assignment |
| 2 | Build Sprint 1 | Patient signup, queue, nurse intake |
| 3 | Build Sprint 2 | Doctor dashboard + patient record |
| 4 | Build Sprint 3 | Voice AI + doctor approval |
| 5 | Build Sprint 4 | Lab/prescription orders + full integration |
| 6 | Documentation + final demo | Testing, handover, final presentation |

## Student Rules

- Use only dummy/synthetic patient data.
- Keep the prototype simple and working; avoid unnecessary features.
- All project access, testing, boards, and documents will be managed through www.exploreN2P.com.
- Integrate work continuously; do not build five separate applications.
- AI scope in this phase is limited to doctor voice documentation and rewriting.
- AI diagnosis, scan analysis, blood-work analysis, and clinical recommendations are future phases.

## Final Acceptance Criteria

- A dummy patient can register and enter the queue.
- A nurse can enter vitals and upload a sample report.
- A doctor can open and review the patient record.
- The doctor can dictate a note and receive voice-to-text output.
- AI can organize/rewrite the dictated note.
- The doctor can edit and approve the final note.
- The required note versions are saved in the patient record.
- The doctor can create and send a simulated prescription or lab order.
- The complete workflow can be demonstrated from start to finish.

## Future Phase — Not Part of This Student MVP

Future versions may analyze the patient's history, blood-work results, scan reports, and other clinical information. These capabilities are intentionally excluded from this six-week project.

*Reference: Hospital Modernization workflow diagram supplied for this project (`original-docs/GF_HOSPITAL MODERNIZATION.pdf`).*
