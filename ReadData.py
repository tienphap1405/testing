#setup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("Credential.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#Read data
#Getting a specific document with a knowned ID
# result = db.collection('Reservations').document('John').get()

#if the input document ID exists it will print out the data of that document by using to_dict()
# if result.exists:
#     print(result.to_dict())


#Read and get all of the documents in a collection
# docs = db.collection('Reservations').get()
# for doc in docs:
#     print(doc.to_dict())


#Querying similar to SQL, where is the condition to find a specific information based on the WHERE clause
docs = db.collection('Reservations').where("Reservation_Date", "array_contains", "1972-07-09").get()
for doc in docs:
    print(doc.to_dict())
