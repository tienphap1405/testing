#setup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("Credential.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#Create a data variable that contains the field with data values
data = {
    'Comment': 'skdflkdfafs',
    'Date_Added': '18-06-2024',
    'Email': 'kalsjda@gmail.com',
    'Name': 'aklsdj',
    'Number_guests': 220,
    'Phone': '+1 (123) 23123-12445'

}

#Create a collection and connect the data to create the doccument
#Create a varible connect the collection (if exist) or create the collection if not
doc_ref = db.collection('Reservations').document('John')

#Connect the doc_ref variable to the data for exports the data to the database of the firestore within that collection
doc_ref.set(data)
