# import libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Load firebase credentials
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize Firebase app
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()




