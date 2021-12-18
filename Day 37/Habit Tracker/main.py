import requests
from datetime import datetime

USERNAME = "burakcode"
TOKEN = "0"
GRAPH_ID = "graph1"
today = datetime(year=2021, month=12, day=15)

#----------------------------------CREATE USER-----------------------------#
pixela_user_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_user_endpoint, json=user_params)

#----------------------------------CREATE GRAPH-----------------------------#
pixela_graph_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)

#----------------------------------POST VALUE-----------------------------#
pixela_postvalue_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.50",
}
# response = requests.post(url=pixela_postvalue_endpoint, json=post_config, headers=headers)

#----------------------------------UPDATE VALUE-----------------------------#
pixela_update_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "1.45"
}
# response = requests.put(url=pixela_update_endpoint, json=update_config, headers=headers)

#----------------------------------DELETE VALUE-----------------------------#
pixela_delete_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=pixela_delete_endpoint, headers=headers)