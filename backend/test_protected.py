import requests

# 1️⃣ First, Login to Get Access Token
login_url = "http://127.0.0.1:5000/auth/login"
login_data = {
    "email": "test@example.com",  # ✅ Use correct email
    "password": "securepass"
}

login_response = requests.post(login_url, json=login_data)
print("Login Response:", login_response.text)

if login_response.status_code == 200:
    access_token = login_response.json().get("access_token")

    # 2️⃣ Use Access Token to Test Protected Route
    protected_url = "http://127.0.0.1:5000/auth/protected"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    protected_response = requests.get(protected_url, headers=headers)
    print("Protected Route Response:", protected_response.text)
    print("Status Code:", protected_response.status_code)
else:
    print("Login Failed!")
