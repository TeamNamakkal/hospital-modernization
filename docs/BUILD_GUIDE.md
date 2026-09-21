# Hospital Modernization — Student Project Build Guide

MVP Prototype | 5 Students | 6 Weeks
Project Platform: www.exploreN2P.com

**Purpose:** Give the student team enough functional and technical information to begin development immediately and deliver one complete working patient journey.

## Project Boundary

Use only dummy/synthetic patient data. This is a prototype, not a production clinical system. Real hospital integrations, real patient data, AI diagnosis, scan analysis, and clinical recommendations are outside this student phase.

Source workflow: Hospital Modernization concept diagram supplied by the project team (`original-docs/GF_HOSPITAL MODERNIZATION.pdf`).

## 1. What You Are Building

The student team will build one connected web prototype. The goal is not to create every hospital feature. The goal is to prove the core patient workflow from registration through consultation and ordering.

### Five Development Steps

- **Step 1 — Patient Signup + Queue:** Create a patient using dummy data, assign a visit, and show the patient in a queue.
- **Step 2 — Nurse Intake + Patient Record:** Enter vitals and basic details, then upload sample reports into the visit record.
- **Step 3 — Doctor Consultation + Voice AI:** Doctor reviews the visit, dictates notes, receives text, reviews the AI rewrite, edits it, and approves the final version.
- **Step 4 — Prescription + Lab Order:** Doctor creates a simulated prescription or laboratory/test order and stores its status.
- **Step 5 — Integration + Final Demo:** Connect all screens and data into one reliable end-to-end demonstration.

**Definition of Done:** A new dummy patient can move through the entire workflow without manual database changes or disconnected screens.

## 2. Users and Screens

Use simple role-based access. A single login page may be used for the prototype. Each user sees only the screens needed for the role.

| Role | Required Screens | Main Actions |
|---|---|---|
| Front Desk / Patient | Patient Signup, Queue | Create patient, start visit, view queue status |
| Nurse | Queue, Nurse Intake, Patient Record | Open queued patient, enter vitals, upload report |
| Doctor | Patient Record, Consultation, Voice Note, Orders | Review record, dictate/edit/approve note, create order |
| Admin / Demo | Dashboard | View demo data and basic system status |

## 3. Functional Requirements

### Patient Signup + Queue
- Create patient: name, DOB, sex, phone, optional email, dummy insurance ID.
- Create a visit when the patient checks in.
- Assign a queue number and status: Waiting, In Intake, Ready for Doctor, With Doctor, Completed.
- Show a queue list that refreshes after a status change.

### Nurse Intake
- Open a patient visit from the queue.
- Enter blood pressure, temperature, pulse, oxygen saturation, weight, and short intake note.
- Upload one or more sample PDF/image reports.
- Mark the visit Ready for Doctor.

### Doctor Consultation
- Display patient demographics, current visit, vitals, uploaded documents, and previous prototype notes if available.
- Provide a Record / Stop control for voice dictation.
- Show raw speech-to-text output before AI rewriting.
- Generate an AI-organized note without adding new clinical facts.
- Allow doctor edits before approval.
- After approval, lock the final note from normal editing and save approval date/time.

### Prescription / Lab Order
- Choose Prescription or Lab Order.
- Prescription: medicine, dose/instructions, duration, optional pharmacy name.
- Lab: test name, notes, optional lab name.
- Status for prototype: Draft, Sent, Received/Completed (simulated).

### Patient Record
- Keep the current visit data linked under one patient ID.
- Show vitals, documents, doctor note versions, prescription/lab orders, and timestamps.
- Keep the original audio file linked to the doctor note when technically feasible.

## 4. Voice-to-Text and AI Note Workflow

**Important AI Rule:** The AI may improve grammar, organization, headings, and readability. It must not invent symptoms, diagnoses, medication, test results, or other clinical facts that were not dictated or already present in the input.

### Versions to Store

| Version | Stored? | Editable? | Purpose |
|---|---|---|---|
| Original audio | Yes | No | Backup/reference |
| Raw transcript | Yes | No after creation | Exact STT result |
| AI draft / doctor-edited note | Yes | Yes until approval | Working version |
| Final approved note | Yes | No after approval | Official prototype note |

## 5. Recommended Technical Architecture

Recommended reference stack: React or Next.js for the web UI, a simple REST backend (FastAPI, Node/Express, or the team's approved equivalent), PostgreSQL for structured data, object/file storage for reports and audio, and an API-based speech-to-text + LLM service for the voice workflow. Keep all external services behind backend endpoints so they can be replaced later.

**Do Not Overbuild:** One web application, one backend, one database, and one shared repository are enough. Avoid microservices, complex cloud automation, mobile apps, RFID, barcode hardware, real pharmacy interfaces, and real lab interfaces in this phase.

## 6. Minimum Data Model

| Object | Must Contain | Notes |
|---|---|---|
| Patient | ID, name, DOB, phone, demographics | One patient can have many visits |
| Visit | ID, patient ID, queue number, status, timestamps | Central unit for the MVP workflow |
| Vitals | Visit ID, BP, temp, pulse, SpO2, weight | Entered by nurse |
| Document | Visit ID, filename, type, file URL | Sample reports only |
| Doctor Note | Visit ID, raw transcript, edited note, final note, approval timestamp | Core voice-AI record |
| Audio | Note ID, audio file URL, timestamp | Keep original dictation |
| Prescription | Visit ID, medicine/instructions/status | Simulated sending |
| Lab Order | Visit ID, test/notes/status | Simulated sending |
| User | ID, name, role, login identifier | Prototype role access |

(See `docs/DATA_MODEL.md` for the working schema derived from this table.)

## 7. Minimum API Contract

The exact URL naming can change, but the application should provide equivalent operations. Students should agree on the contract before coding frontend and backend independently.

| Method | Endpoint Example | Purpose | Used By |
|---|---|---|---|
| POST | /api/patients | Create patient | Front desk |
| POST | /api/visits | Create/check-in visit | Front desk |
| GET | /api/queue | List active queue | All clinical roles |
| PATCH | /api/visits/{id}/status | Change queue/visit status | Nurse/Doctor |
| POST | /api/visits/{id}/vitals | Save vitals | Nurse |
| POST | /api/visits/{id}/documents | Upload report | Nurse |
| GET | /api/visits/{id} | Load complete visit record | Doctor |
| POST | /api/visits/{id}/audio | Save dictation audio | Doctor |
| POST | /api/visits/{id}/transcribe | Generate raw transcript | Doctor |
| POST | /api/visits/{id}/rewrite-note | Create AI-organized draft | Doctor |
| POST | /api/notes/{id}/approve | Approve final note | Doctor |
| POST | /api/visits/{id}/prescriptions | Create prescription | Doctor |
| POST | /api/visits/{id}/lab-orders | Create lab order | Doctor |

(See `docs/API_CONTRACT.md` for the same contract with implementation status.)

## 8. Team Assignment and 6-Week Plan

| Student | Primary Ownership | Integration Responsibility |
|---|---|---|
| 1 | Patient signup + queue | Connect patient/visit IDs to nurse workflow |
| 2 | Nurse intake + uploads | Ensure data appears correctly for doctor |
| 3 | Doctor dashboard + record view | Integrate consultation and orders |
| 4 | Voice-to-text + AI note | Implement version storage and approval flow |
| 5 | Orders + backend integration + testing | Help merge modules and own end-to-end test |

All students: use one shared repository, review each other's code, and integrate every week. No student module is considered complete until it works in the shared application.

| Week | Focus | Required Checkpoint | Output |
|---|---|---|---|
| 1 | Introduction + design | Architecture, data model, API contract agreed | Repository + basic app skeleton |
| 2 | Build 1 | Patient signup → queue → nurse intake works | First integrated demo |
| 3 | Build 2 | Doctor can open complete visit record | Second integrated demo |
| 4 | Build 3 | Voice → transcript → AI draft → edit works | Voice workflow demo |
| 5 | Build 4 | Approval + prescription/lab order + end-to-end flow | Feature complete MVP |
| 6 | Test + document | Acceptance tests pass | Final demo + handover |

## 9. Acceptance Test — Final Demonstration

The final demo should be performed as one continuous scenario. Use one prepared dummy patient and do not edit database records manually during the demonstration.

1. Create the dummy patient and start a visit.
2. Patient appears in the queue with a queue number.
3. Nurse opens the visit, enters vitals, uploads a sample report, and marks Ready for Doctor.
4. Doctor opens the same visit and sees patient details, vitals, and uploaded report.
5. Doctor records a short consultation note.
6. System saves audio and generates the raw transcript.
7. AI creates an organized note without adding new facts.
8. Doctor changes at least one sentence and approves the note.
9. System shows the stored raw transcript, edited note, final approved note, and timestamps.
10. Doctor creates either a prescription or lab order and marks it Sent.
11. Visit record shows the completed workflow and all linked information.

**MVP Pass Condition:** If the team can complete the scenario above reliably from the web interface, the student project is successful.

## 10. Required Handover

- Complete source code in the agreed project repository.
- README with setup/start instructions and required environment variables.
- Database schema or migration files and dummy seed data.
- List of API endpoints.
- Short test report showing which acceptance tests passed.
- Known limitations and recommended next steps.
- Final presentation/demo material stored in the ExploreN2P project document repository.

### Out of Scope for This Student MVP

The original modernization concept also includes broader registration channels, mobile access, external pharmacy/laboratory connections, cloud/local redundancy, and richer patient access. Those ideas remain part of the larger hospital modernization vision, but they are intentionally deferred so this six-week student project stays achievable.

### Start Here on Day 1

Create the shared repository and app skeleton, agree on the data model and API contract in this guide, load dummy data, and make the first vertical slice work: Patient Signup → Queue → Nurse Intake. Do not wait for every screen to be designed before integration begins.
