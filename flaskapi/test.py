import requests

BASE_URL = "http://127.0.0.1:5000"

# Add an App
response = requests.post(f"{BASE_URL}/add-app", json={
    "app_name": "TestApp",
    "version": "1.0",
    "description": "A test app"
})
print("POST /add-app:", response.json())
