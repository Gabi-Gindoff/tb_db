from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timezone

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["turtlebot_db"]
collection = db["logs"]

def create_document(data):
    result = collection.insert_one(log_entry)
    print(f'Document inserted with id: {result.inserted_id}')

def read_documents():
    documents = collection.find()
    for doc in documents:
        print(doc)

def read_document_by_id(doc_id):
    document = collection.find_one({"_id": ObjectId(doc_id)})
    print(document)

def update_document(doc_id, updated_data):
    result = collection.update_one({"_id": ObjectId(doc_id)}, {"$set": updated_data})
    print(f'Modified count: {result.modified_count}')

def delete_document(doc_id):
    result = collection.delete_one({"_id": ObjectId(doc_id)})
    print(f'Deleted count: {result.deleted_count}')

# Example usage
if __name__ == "__main__":

    log_entry = {
    "timestamp": "2025-03-04T14:25:00Z",
    "robot_id": "TB3_001",
    "movement": {
        "command": "move_forward",
        "distance_m": 1.5,
        "speed_mps": 0.2,
        "position": {"x": 1.0, "y": 1.2, "theta": -0.1}
    },
    "sensor": {
        "LiDAR": {"obstacle_detected": true, "distance_m": 0.5},
        "IMU": {"acceleration_z": 9.81, "gyro_z": 0.05}
    },
    "error": {
        "code": 101,
        "message": "Wheel encoder failure"
    },
    "action": {
        "name": "pick_up_object",
        "status": "success"
    },
    "system": {
        "battery": 85
    }
}

    create_document(log_entry)  # Insert a new TurtleBot log entry
    read_documents()
