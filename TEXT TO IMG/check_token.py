import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_API_TOKEN")

print(f"Checking token: {token[:5]}...")

response = requests.get("https://huggingface.co/api/whoami-v2", headers={"Authorization": f"Bearer {token}"})

if response.status_code == 200:
    data = response.json()
    print(f"User: {data.get('name')}")
    print(f"Type: {data.get('type')}")
    print(f"Auth: {data.get('auth')}")
    
    # Check headers for scopes
    print(f"Scopes: {response.headers.get('x-oauth-scopes')}")
    print(f"Accepted Scopes: {response.headers.get('x-oauth-accepted-scopes')}")
else:
    print(f"Error: {response.text}")
