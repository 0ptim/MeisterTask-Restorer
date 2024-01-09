import requests

import json


def process_json_data():
    output = []

    try:
        with open("./result.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            # Extract the required fields from each item
            processed_item = {
                "id": item.get("id"),
                "payload": {
                    "assigned_to_id": item.get("assigned_to_id"),
                    "due": item.get("due"),
                    "name": item.get("name"),
                    "notes": item.get("notes"),
                    "section_id": item.get("section_id"),
                    "status": 1,
                },
            }
            output.append(processed_item)

        return output

    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_tasks(task_items):
    base_url = "https://www.meistertask.com/api/tasks/"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer XXX",
    }

    for item in task_items:
        # Construct the URL and payload for each task
        task_id = item.get("id")  # assuming each item has an 'id' field
        if not task_id:
            print("Task ID missing for item:", item)
            continue

        url = base_url + str(task_id)
        print(f"Updating task ID {task_id} at URL: {url}")

        item_payload = item.get("payload")
        filtered_payload = {k: v for k, v in item_payload.items() if v is not None}

        # Make the PUT request
        response = requests.put(url, json=filtered_payload, headers=headers)
        print(f"Task ID {task_id} update response: {response.text}")


# Call the function and get the result
result = process_json_data()
print(result)

# Update the tasks
update_tasks(result)
