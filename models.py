from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    surname: str
    gender: str
    birth_date: str

class Tension(BaseModel):
    patient_id: str
    systolic: int
    diastolic: int
    method: str
    body_site: str
    cuff_size: str
    device: str
    state: str
    date: str
    description: str
    in_range: bool