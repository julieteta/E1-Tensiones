from bson import ObjectId
class TensionRepository:

    def __init__(self, db):
        self.collection = db["tensions"]

    def create(self, tension):

        return self.collection.insert_one(
            tension.model_dump()
        )

    def get_all(self):

        return list(self.collection.find())

    def get_by_patient(self, patient_reference):

        return list(
            self.collection.find(
                {"patient_reference": patient_reference}
            )
        )

    def update(self, tension_id, data):

        return self.collection.update_one(
            {"_id": ObjectId(tension_id)},
            {"$set": data}
        )

    def delete(self, tension_id):

        return self.collection.delete_one(
            {"_id": ObjectId(tension_id)}
        )