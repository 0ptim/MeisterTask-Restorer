import requests

url = "https://www.meistertask.com/api/projects"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer XXX",
}

response = requests.get(url, headers=headers)

print(response.text)
