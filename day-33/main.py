import requests

response = requests.get(url="")
response.raise_for_status()