from models.models import Patient

class PatientService:

    def __init__(self, patient_repository):

        self.patient_repository = patient_repository

    def create_patient(
        self,
        name,
        surname,
        gender,
        birth_date
    ):

        patient = Patient(
            name=name,
            surname=surname,
            gender=gender,
            birth_date=birth_date
        )

        return self.patient_repository.create(
            patient
        )

    def list_patients(self):

        return self.patient_repository.get_all()

    def update_patient(
        self,
        patient_id,
        name,
        surname,
        gender,
        birth_date
    ):

        patient = Patient(
            name=name,
            surname=surname,
            gender=gender,
            birth_date=birth_date
        )

        return self.patient_repository.update(
            patient_id,
            patient.model_dump()
        )

    def delete_patient(self, patient_id):

        return self.patient_repository.delete(
            patient_id
        )