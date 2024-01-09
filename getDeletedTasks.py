import requests

projectId = "XXX"

url = f"https://www.meistertask.com/api/projects/{projectId}/tasks?status=trashed&sort=-status_updated_at&items=500"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer XXX",
}

response = requests.get(url, headers=headers)

# print(response.text)

# Save the response to a file with UTF-8 encoding
with open("result.json", "w", encoding="utf-8") as file:
    file.write(response.text)
