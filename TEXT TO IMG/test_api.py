import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")

models = [
    "https://router.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
    "https://router.huggingface.co/models/stabilityai/stable-diffusion-2-1",
    "https://router.huggingface.co/models/runwayml/stable-diffusion-v1-5",
    "https://router.huggingface.co/models/CompVis/stable-diffusion-v1-4",
    "https://router.huggingface.co/models/prompthero/openjourney"
]

headers = {"Authorization": f"Bearer {API_TOKEN}"}
payload = {"inputs": "test"}

print(f"Testing with Token: {API_TOKEN[:5]}...")

for url in models:
    print(f"\nTesting: {url}")
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("SUCCESS! This model works.")
            # Verify it's an image
            if "image" in response.headers.get("content-type", ""):
                print("Confirmed: Returned an image.")
            else:
                print(f"Warning: Content-Type is {response.headers.get('content-type')}")
        else:
            print(f"Failed. Response: {response.text[:200]}")
    except Exception as e:
        print(f"Error: {e}")
