from bson import ObjectId

class PatientRepository:
    def __init__(self, db):
        self.collection = db["patients"]

    def create(self, patient):
        return self.collection.insert_one(patient.model_dump())

    def get_all(self):
        return list(self.collection.find())

    def update(self, patient_id, data):
        return self.collection.update_one(
            {"_id": ObjectId(patient_id)},
            {"$set": data}
        )

    def delete(self, patient_id):
        return self.collection.delete_one(
            {"_id": ObjectId(patient_id)}
        )


class TensionRepository:
    def __init__(self, db):
        self.collection = db["tensions"]

    def create(self, tension):
        return self.collection.insert_one(tension.model_dump())

    def get_all(self):
        return list(self.collection.find())

    def get_by_patient(self, patient_id):
        return list(self.collection.find({"patient_id": patient_id}))

    def update(self, tension_id, data):
        return self.collection.update_one(
            {"_id": ObjectId(tension_id)},
            {"$set": data}
        )

    def delete(self, tension_id):
        return self.collection.delete_one(
            {"_id": ObjectId(tension_id)}
        )