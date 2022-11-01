#!/usr/bin/env python

import requests

# Change the last part of the url with the primary key
url = "https://firestore.googleapis.com/v1/projects/tib-cloud-da/databases/(default)/documents/users/TesPYGa8z5UFeTqX3xkV"

print(requests.delete(url))

# TODO: find a way to delete a record based on another attribute
