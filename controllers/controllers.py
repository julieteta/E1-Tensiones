class AppController:

    def __init__(self, patient_service, tension_service):

        self.patient_service = patient_service
        self.tension_service = tension_service

    def create_patient(self, name, surname, gender, birth_date):

        return self.patient_service.create_patient(
            name,
            surname,
            gender,
            birth_date
        )

    def get_patients(self):

        return self.patient_service.list_patients()

    def update_patient(
        self,
        patient_id,
        name,
        surname,
        gender,
        birth_date
    ):

        return self.patient_service.update_patient(
            patient_id,
            name,
            surname,
            gender,
            birth_date
        )

    def delete_patient(self, patient_id):

        return self.patient_service.delete_patient(
            patient_id
        )

    def create_tension(self, data):

        return self.tension_service.create_tension(
            **data
        )

    def get_all_tensions(self):

        return self.tension_service.list_all_tensions()

    def get_tensions_by_patient(self, patient_reference):

        return self.tension_service.list_tensions_by_patient(
            patient_reference
        )

    def update_tension(self, tension_id, data):

        return self.tension_service.update_tension(
            tension_id,
            data
        )

    def delete_tension(self, tension_id):

        return self.tension_service.delete_tension(
            tension_id
        )

    def get_average(self, patient_reference):

        return self.tension_service.average_tension(
            patient_reference
        )

    def get_last_tension(self, patient_reference):

        return self.tension_service.last_tension(
            patient_reference
        )