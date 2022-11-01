#!/usr/bin/env python

import requests
import json

url = "https://firestore.googleapis.com/v1/projects/tib-cloud-da/databases/(default)/documents/users"
body = {
    "fields": {
        "name": {
            "stringValue": "Jáson"
        }
    }
}
data = json.dumps(body)

print(requests.post(url, data=data).json())
