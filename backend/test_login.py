import requests

url = "http://127.0.0.1:5000/auth/login"

# Ensure the JSON keys match your Flask API (e.g., "username" and "password")
data = {
    "email": "test@example.com",
    "password": "securepass"
}

headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Debugging: Print the raw response
print("Raw Response:", response.text)
print("Status Code:", response.status_code)
