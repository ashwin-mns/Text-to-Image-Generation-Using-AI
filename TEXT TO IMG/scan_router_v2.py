import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)
API_TOKEN = os.getenv("HF_API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Newer models that are likely on the router
models = [
    "black-forest-labs/FLUX.1-schnell",
    "black-forest-labs/FLUX.1-dev",
    "stabilityai/stable-diffusion-3-medium-diffusers",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "meta-llama/Meta-Llama-3-8B-Instruct" # Text model just to check router life
]

base_url = "https://router.huggingface.co/models"

print("Scanning Router...")

for model in models:
    url = f"{base_url}/{model}"
    print(f"Testing {model}...")
    try:
        # Simple payload
        payload = {"inputs": "A simple cat"}
        resp = requests.post(url, headers=headers, json=payload)
        
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            print(f"*** FOUND WORKING MODEL: {model} ***")
            break
        elif resp.status_code == 401:
            print("401 Unauthorized (Check Permissions)")
        elif resp.status_code == 404:
            print("404 Not Found (Model not on router)")
        else:
            print(f"Error {resp.status_code}: {resp.text[:100]}")
    except Exception as e:
        print(f"Exception: {e}")
