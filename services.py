from models import Patient, Tension

class PatientService:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository

    def create_patient(self, name, surname, gender, birth_date):
        patient = Patient(
            name=name,
            surname=surname,
            gender=gender,
            birth_date=birth_date
        )
        return self.patient_repository.create(patient)

    def list_patients(self):
        return self.patient_repository.get_all()

    def update_patient(self, patient_id, name, surname, gender, birth_date):
        data = {
            "name": name,
            "surname": surname,
            "gender": gender,
            "birth_date": birth_date
        }
        return self.patient_repository.update(patient_id, data)

    def delete_patient(self, patient_id):
        return self.patient_repository.delete(patient_id)


class TensionService:
    def __init__(self, tension_repository):
        self.tension_repository = tension_repository

    def create_tension(self, patient_id, systolic, diastolic, method,
                       body_site, cuff_size, device, state, date, description):

        systolic = int(systolic)
        diastolic = int(diastolic)
        in_range = systolic < 140 and diastolic < 90

        tension = Tension(
            patient_id=patient_id,
            systolic=systolic,
            diastolic=diastolic,
            method=method,
            body_site=body_site,
            cuff_size=cuff_size,
            device=device,
            state=state,
            date=date,
            description=description,
            in_range=in_range
        )

        return self.tension_repository.create(tension)

    def list_all_tensions(self):
        return self.tension_repository.get_all()

    def list_tensions_by_patient(self, patient_id):
        return self.tension_repository.get_by_patient(patient_id)

    def update_tension(self, tension_id, data):
        data["systolic"] = int(data["systolic"])
        data["diastolic"] = int(data["diastolic"])
        data["in_range"] = data["systolic"] < 140 and data["diastolic"] < 90
        return self.tension_repository.update(tension_id, data)

    def delete_tension(self, tension_id):
        return self.tension_repository.delete(tension_id)

    def average_tension(self, patient_id):
        tensions = self.tension_repository.get_by_patient(patient_id)

        if not tensions:
            return None

        avg_sys = sum(t["systolic"] for t in tensions) / len(tensions)
        avg_dia = sum(t["diastolic"] for t in tensions) / len(tensions)

        return round(avg_sys, 2), round(avg_dia, 2)

    def last_tension(self, patient_id):
        tensions = self.tension_repository.get_by_patient(patient_id)

        if not tensions:
            return None

        return tensions[-1]