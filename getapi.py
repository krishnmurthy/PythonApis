import requests


data = {"name": "Alice", "job": "Developer"}
url="http://127.0.0.1:5000/api/users"
response = requests.post(url,  json=data);
print(response.text);