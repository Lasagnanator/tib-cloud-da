#!/usr/bin/env python

import requests
import json

url = "https://firestore.googleapis.com/v1/projects/tib-cloud-da/databases/(default)/documents/users/tHHm8ZCkucyAKhe9CXE6"
body = {
    "fields": {
        "name": {
            "stringValue": "Jean-Claude"
        }
    }
}
data = json.dumps(body)

print(requests.patch(url, data=data).json())
