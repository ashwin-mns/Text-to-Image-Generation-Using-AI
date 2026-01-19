import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")

# Explicit URL for OpenJourney
url = "https://api-inference.huggingface.co/models/prompthero/openjourney"

print(f"Testing URL: {url}")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

try:
    response = requests.post(url, headers=headers, json={"inputs": "A cyberpunk city"})
    print(f"Status: {response.status_code}")
    print(f"Content-Type: {response.headers.get('content-type')}")
    
    if response.status_code == 200:
        print("Success! Image data received.")
    else:
        print(f"Error: {response.text[:200]}")
except Exception as e:
    print(f"Exception: {e}")
