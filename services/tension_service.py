from models.models import Tension

class TensionService:

    def __init__(
        self,
        tension_repository,
        patient_repository
    ):

        self.tension_repository = tension_repository
        self.patient_repository = patient_repository

    def create_tension(
        self,
        patient_reference,
        systolic,
        diastolic,
        method,
        body_site,
        cuff_size,
        device,
        state,
        date,
        description
    ):

        if self.patient_repository.get_by_id(
            patient_reference
        ) is None:

            raise ValueError(
                "El paciente no existe"
            )

        systolic = int(systolic)
        diastolic = int(diastolic)

        in_range = (
            systolic < 140 and diastolic < 90
        )

        tension = Tension(
            patient_reference=patient_reference,
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

        return self.tension_repository.create(
            tension
        )

    def list_all_tensions(self):

        return self.tension_repository.get_all()

    def list_tensions_by_patient(
        self,
        patient_reference
    ):

        return self.tension_repository.get_by_patient(
            patient_reference
        )

    def update_tension(
        self,
        tension_id,
        data
    ):

        data["systolic"] = int(
            data["systolic"]
        )

        data["diastolic"] = int(
            data["diastolic"]
        )

        data["in_range"] = (
            data["systolic"] < 140
            and
            data["diastolic"] < 90
        )

        tension = Tension(**data)

        return self.tension_repository.update(
            tension_id,
            tension.model_dump()
        )

    def delete_tension(
        self,
        tension_id
    ):

        return self.tension_repository.delete(
            tension_id
        )

    def average_tension(
        self,
        patient_reference
    ):

        tensions = (
            self.tension_repository.get_by_patient(
                patient_reference
            )
        )

        if not tensions:

            return None

        avg_sys = (
            sum(
                t["systolic"]
                for t in tensions
            ) / len(tensions)
        )

        avg_dia = (
            sum(
                t["diastolic"]
                for t in tensions
            ) / len(tensions)
        )

        return (
            round(avg_sys, 2),
            round(avg_dia, 2)
        )

    def last_tension(
        self,
        patient_reference
    ):

        tensions = (
            self.tension_repository.get_by_patient(
                patient_reference
            )
        )

        if not tensions:

            return None

        return tensions[-1]