#!/usr/bin/env python

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./firestore-credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

users_ref = db.collection(u'users')
docs = users_ref.stream()


def get_names():
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()[("name")]}')
    #    print(f'{doc.id} => {doc.to_dict()}')


def add_lovelace():
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'name': u'Ada',
        u'surname': u'Lovelace',
        u'date': 1815
    })


def first_two():
    users = db.collection('users')
    query = users.order_by('name').limit_to_last(2)
    results = query.get()
    for person in results:
        print(person.to_dict()[('name')])


get_names()
print("\n~~~~~~~~~~\n")
# add_lovelace()
# print("\n~~~~~~~~~~\n")
first_two()
