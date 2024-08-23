#!/usr/bin/env -S python

import requests

import os

DIR = os.path.abspath(os.path.dirname(__file__))

print("scotttest1.png")

response = requests.post(
    "http://localhost:5000/v1/vision/face/recognize",
    files={"image": open(f"{DIR}/images/scotttest1.png", "rb").read()},
).json()

for user in response["predictions"]:
    print(user["userid"])

# print("hiltest.png")

# response = requests.post(
#     "http://localhost:5000/v1/vision/face/recognize",
#     files={"image": open(f"{DIR}/images/hiltest.png", "rb").read()},
# ).json()

# for user in response["predictions"]:
#     print(user["userid"])

# print("Full Response: ", response)
