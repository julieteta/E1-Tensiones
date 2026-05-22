from pydantic import BaseModel, field_validator
from typing import Literal
from datetime import datetime

class Patient(BaseModel):
    name: str
    surname: str
    gender: Literal["male", "female", "other", "unknown"]
    birth_date: str

    @field_validator("name", "surname", "birth_date")
    @classmethod
    def not_empty(cls, value):
        if not value.strip():
            raise ValueError("Este campo no puede estar vacío")
        return value

    @field_validator("birth_date")
    @classmethod
    def valid_date(cls, value):
        datetime.strptime(value, "%Y-%m-%d")
        return value


class Tension(BaseModel):
    patient_reference: str
    systolic: int
    diastolic: int
    method: str
    body_site: str
    cuff_size: str
    device: str
    state: Literal[
        "registered", "preliminary", "final", "amended",
        "corrected", "cancelled", "entered-in-error", "unknown"
    ]
    date: str
    description: str
    in_range: bool

    @field_validator("patient_reference", "method", "body_site", "cuff_size", "device", "date", "description")
    @classmethod
    def not_empty(cls, value):
        if not value.strip():
            raise ValueError("Este campo no puede estar vacío")
        return value

    @field_validator("date")
    @classmethod
    def valid_date(cls, value):
        datetime.strptime(value, "%Y-%m-%d")
        return value

    @field_validator("systolic")
    @classmethod
    def valid_systolic(cls, value):
        if value < 1 or value > 300:
            raise ValueError("La sistólica debe estar entre 1 y 300")
        return value

    @field_validator("diastolic")
    @classmethod
    def valid_diastolic(cls, value):
        if value < 1 or value > 200:
            raise ValueError("La diastólica debe estar entre 1 y 200")
        return value