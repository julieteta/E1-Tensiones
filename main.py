from database.db import DatabaseConnection
from repositories.repositories import PatientRepository, TensionRepository
from services.services import PatientService, TensionService
from controllers.controllers import AppController
from views.view import MainView

def main():
    db = DatabaseConnection().get_database()

    patient_repository = PatientRepository(db)
    tension_repository = TensionRepository(db)

    patient_service = PatientService(patient_repository)
    tension_service = TensionService(tension_repository, patient_repository)

    controller = AppController(patient_service, tension_service)

    app = MainView(controller)
    app.run()

if __name__ == "__main__":
    main()