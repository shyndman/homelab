#!/usr/bin/env -S python

import requests

import os

DIR = os.path.abspath(os.path.dirname(__file__))


# scott_image1 = open(f"{DIR}/images/scott1.png", "rb").read()
# scott_image2 = open(f"{DIR}/images/scott2.png", "rb").read()
# scott_image3 = open(f"{DIR}/images/scott3.png", "rb").read()

# response = requests.post(
#     "http://localhost:5000/v1/vision/face/delete",
#     data={"userid": "Scott Hyndman"},
#     timeout=1000,
# ).json()
# print(response)

# response = requests.post(
#     "http://localhost:5000/v1/vision/face/register",
#     files={
#         "image1": scott_image1,
#         "image2": scott_image2,
#         "image3": scott_image3
#     },
#     data={"userid": "Scott Hyndman"},
#     timeout=1000,
# ).json()
# print(response)

hil_image1 = open(f"{DIR}/images/hil1.png", "rb").read()
hil_image2 = open(f"{DIR}/images/hil2.png", "rb").read()
hil_image3 = open(f"{DIR}/images/hil3.png", "rb").read()
hil_image4 = open(f"{DIR}/images/hil4.png", "rb").read()

response = requests.post(
    "http://localhost:5000/v1/vision/face/delete",
    data={"userid": "Hilary Hacksel"},
    timeout=1000,
).json()
print(response)

response = requests.post(
    "http://localhost:5000/v1/vision/face/register",
    files={
        "image1": hil_image1,
        "image2": hil_image2,
        "image3": hil_image4
    },
    data={"userid": "Hilary Hacksel"},
    timeout=1000,
).json()
print(response)
