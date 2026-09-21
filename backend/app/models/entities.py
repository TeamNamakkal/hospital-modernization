from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    dob: Mapped[str] = mapped_column(String)
    sex: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str | None] = mapped_column(String, nullable=True)
    insurance_id: Mapped[str | None] = mapped_column(String, nullable=True)

    visits: Mapped[list["Visit"]] = relationship(back_populates="patient")


class Visit(Base):
    __tablename__ = "visits"

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    queue_number: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column(String, default="waiting")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    patient: Mapped["Patient"] = relationship(back_populates="visits")
    vitals: Mapped["Vitals | None"] = relationship(back_populates="visit", uselist=False)
    documents: Mapped[list["Document"]] = relationship(back_populates="visit")
    notes: Mapped[list["DoctorNote"]] = relationship(back_populates="visit")
    prescriptions: Mapped[list["Prescription"]] = relationship(back_populates="visit")
    lab_orders: Mapped[list["LabOrder"]] = relationship(back_populates="visit")


class Vitals(Base):
    __tablename__ = "vitals"

    id: Mapped[int] = mapped_column(primary_key=True)
    visit_id: Mapped[int] = mapped_column(ForeignKey("visits.id"))
    blood_pressure: Mapped[str | None] = mapped_column(String, nullable=True)
    temperature: Mapped[str | None] = mapped_column(String, nullable=True)
    pulse: Mapped[str | None] = mapped_column(String, nullable=True)
    spo2: Mapped[str | None] = mapped_column(String, nullable=True)
    weight: Mapped[str | None] = mapped_column(String, nullable=True)
    intake_note: Mapped[str | None] = mapped_column(String, nullable=True)

    visit: Mapped["Visit"] = relationship(back_populates="vitals")


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    visit_id: Mapped[int] = mapped_column(ForeignKey("visits.id"))
    filename: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    file_url: Mapped[str] = mapped_column(String)

    visit: Mapped["Visit"] = relationship(back_populates="documents")


class DoctorNote(Base):
    __tablename__ = "doctor_notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    visit_id: Mapped[int] = mapped_column(ForeignKey("visits.id"))
    raw_transcript: Mapped[str | None] = mapped_column(String, nullable=True)
    edited_note: Mapped[str | None] = mapped_column(String, nullable=True)
    final_note: Mapped[str | None] = mapped_column(String, nullable=True)
    approved_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    visit: Mapped["Visit"] = relationship(back_populates="notes")
    audio: Mapped["Audio | None"] = relationship(back_populates="note", uselist=False)


class Audio(Base):
    __tablename__ = "audio"

    id: Mapped[int] = mapped_column(primary_key=True)
    note_id: Mapped[int] = mapped_column(ForeignKey("doctor_notes.id"))
    audio_file_url: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    note: Mapped["DoctorNote"] = relationship(back_populates="audio")


class Prescription(Base):
    __tablename__ = "prescriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    visit_id: Mapped[int] = mapped_column(ForeignKey("visits.id"))
    medicine: Mapped[str] = mapped_column(String)
    instructions: Mapped[str | None] = mapped_column(String, nullable=True)
    duration: Mapped[str | None] = mapped_column(String, nullable=True)
    pharmacy_name: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, default="draft")

    visit: Mapped["Visit"] = relationship(back_populates="prescriptions")


class LabOrder(Base):
    __tablename__ = "lab_orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    visit_id: Mapped[int] = mapped_column(ForeignKey("visits.id"))
    test_name: Mapped[str] = mapped_column(String)
    notes: Mapped[str | None] = mapped_column(String, nullable=True)
    lab_name: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, default="draft")

    visit: Mapped["Visit"] = relationship(back_populates="lab_orders")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
    login_identifier: Mapped[str] = mapped_column(String, unique=True)
