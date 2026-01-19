import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")

print(f"Token loaded: {API_TOKEN[:5]}... (Length: {len(API_TOKEN) if API_TOKEN else 0})")

# 1. Check Token Validity
print("\n--- 1. Testing Token Validity ---")
try:
    whoami_resp = requests.get("https://huggingface.co/api/whoami-v2", headers={"Authorization": f"Bearer {API_TOKEN}"})
    print(f"Status: {whoami_resp.status_code}")
    if whoami_resp.status_code == 200:
        print(f"Success! Logged in as: {whoami_resp.json().get('name')}")
    else:
        print(f"Token Error: {whoami_resp.text}")
except Exception as e:
    print(f"Connection Error: {e}")

# 2. Test Router with a safe model (SD 2.1)
print("\n--- 2. Testing Image Gen (Router) ---")
url = "https://router.huggingface.co/models/stabilityai/stable-diffusion-2-1"
try:
    resp = requests.post(url, headers={"Authorization": f"Bearer {API_TOKEN}"}, json={"inputs": "cat"})
    print(f"URL: {url}")
    print(f"Status: {resp.status_code}")
    if resp.status_code == 200:
        print("Success! Image generated.")
    else:
        print(f"Error: {resp.text[:200]}")
except Exception as e:
    print(f"Error: {e}")

# 3. Test Old API with SD 1.5
print("\n--- 3. Testing Image Gen (Old API) ---")
url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
try:
    resp = requests.post(url, headers={"Authorization": f"Bearer {API_TOKEN}"}, json={"inputs": "cat"})
    print(f"URL: {url}")
    print(f"Status: {resp.status_code}")
    if resp.status_code == 200:
        print("Success! Image generated.")
    else:
        print(f"Error: {resp.text[:200]}")
except Exception as e:
    print(f"Error: {e}")
