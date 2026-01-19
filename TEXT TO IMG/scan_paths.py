import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)
API_TOKEN = os.getenv("HF_API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}
model = "stabilityai/stable-diffusion-2-1"

base_domain = "https://router.huggingface.co"
paths = [
    f"/models/{model}",
    f"/hf-inference/models/{model}",
    f"/hf-inference/v1/models/{model}",
    f"/v1/models/{model}",
    f"/{model}",
    f"/api/models/{model}",
    f"/api/{model}",
    # Try just the base just in case
    "/", 
]

print(f"Scanning paths for {model} on {base_domain}...")

for path in paths:
    url = f"{base_domain}{path}"
    print(f"Testing {url}...")
    try:
        resp = requests.post(url, headers=headers, json={"inputs": "cat"})
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            print("FOUND IT!")
            break
        elif resp.status_code == 405: # Method Not Allowed
             print("405 (Maybe GET?)")
    except Exception as e:
        print(f"Error: {e}")
