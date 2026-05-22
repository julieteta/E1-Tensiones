from bson import ObjectId

class PatientRepository:

    def __init__(self, db):
        self.collection = db["patients"]

    def create(self, patient):
        return self.collection.insert_one(
            patient.model_dump()
        )

    def get_all(self):
        return list(self.collection.find())

    def get_by_id(self, patient_id):

        return self.collection.find_one(
            {"_id": ObjectId(patient_id)}
        )

    def update(self, patient_id, data):

        return self.collection.update_one(
            {"_id": ObjectId(patient_id)},
            {"$set": data}
        )

    def delete(self, patient_id):

        return self.collection.delete_one(
            {"_id": ObjectId(patient_id)}
        )

