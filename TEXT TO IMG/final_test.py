import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_API_TOKEN")

print(f"Token: {token[:10]}...")

# Try the most standard, reliable model on the new router
url = "https://router.huggingface.co/models/stabilityai/stable-diffusion-2-1"

print(f"Testing {url}...")
try:
    resp = requests.post(url, headers={"Authorization": f"Bearer {token}"}, json={"inputs": "A simple cat"})
    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"Body: {resp.text[:300]}")
except Exception as e:
    print(f"Crash: {e}")
