import json

import requests

# Replace these with your values
api_key = "<API_KEY>"
db_path = "<DB_NAME>"
endpoint = "https://api-gateway-electron.onrender.com/add"

def send_post_request(bookmark):
    title = bookmark['title']
    url = bookmark['author']
    
    # Create the data payload for the request
    data = {
        "apiKey": api_key,
        "dbPath": db_path,
        "data": title,
        "metadata": {
            "author": url,
            "title": title
        }
    }

    # Send the POST request
    response = requests.post(endpoint, json=data, headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        print(f"Successfully added: {title}")
    else:
        print(f"Failed to add: {title}, Status code: {response.status_code}, Response: {response.text}")

def process_bookmarks(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    for bookmark in bookmarks:
        send_post_request(bookmark)

if __name__ == "__main__":
    json_file_path = 'bookmarks.json'  # Replace with your actual bookmarks JSON file
    process_bookmarks(json_file_path)
