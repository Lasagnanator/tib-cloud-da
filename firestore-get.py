#!/usr/bin/env python

import requests
import json

url = "https://firestore.googleapis.com/v1/projects/tib-cloud-da/databases/(default)/documents/users"
response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2))
for name in data["documents"]:
    print(name["fields"]["name"]["stringValue"])
