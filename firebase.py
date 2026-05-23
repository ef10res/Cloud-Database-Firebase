# import libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import threading

# Load firebase credentials
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize Firebase app
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

def on_snapshot(collection_snapshot, changes, read_time):
    print("Database changed!")

    for change in changes:
        if change.type.name == "ADDED":
            print("New document:", change.document.id, change.document.to_dict())

        elif change.type.name == "MODIFIED":
            print("Updated document:", change.document.id, change.document.to_dict())

        elif change.type.name == "REMOVED":
            print("Deleted document:", change.document.id)

# Watch the workouts collection
collection_ref = db.collection("workouts")
collection_watch = collection_ref.on_snapshot(on_snapshot)

def start_listener():
    collection_watch = collection_ref.on_snapshot(on_snapshot)
    print("Listening for Firestore changes...")
    threading.Event().wait()



