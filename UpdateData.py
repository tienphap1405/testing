#setup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("Credential.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#Update data - known key
# db.collection('Reservations').document('John').update({'Number_guests': 10})

#the increment will increment the number of integer to the value that assign
# db.collection('Reservations').document('John').update({'Number_guests':firestore.Increment(10)})

#Update data - Unknown key
docs = db.collection('Reservations').where('Number_guests', '>', 100).get()
for doc in docs:
    db.collection('Reservations').document(doc.id).update({'Number_guests': 10})
