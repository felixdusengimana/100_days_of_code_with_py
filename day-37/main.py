import requests
from datetime import datetime

USER_NAME = "phelix"
GRAPH_ID = "graph1"
# POSTING, DELETING, PUTTING WITH requests

pixela_endpoint = ""

user_params ={
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": ""
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixela_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixela_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74",
}

# response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)

updated_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixela_data = {
    "quantity": "4.5"
}

# requests.put(url=updated_endpoint, json=new_pixela_data, headers=headers)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
