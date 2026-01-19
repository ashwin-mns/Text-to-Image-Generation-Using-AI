import requests
import os
from dotenv import load_dotenv
import sys

# Force reload dotenv to be sure
load_dotenv(override=True)

API_TOKEN = os.getenv("HF_API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

base_models = [
    "prompthero/openjourney",
    "stabilityai/stable-diffusion-2-1",
    "gpt2"
]

formats = [
    "https://router.huggingface.co/hf-inference/models/{}",
    "https://router.huggingface.co/hf-inference/{}",
    "https://router.huggingface.co/v1/{}",
    "https://router.huggingface.co/models/{}" 
]

for model in base_models:
    print(f"\n--- Testing Model: {model} ---")
    for fmt in formats:
        url = fmt.format(model)
        print(f"Testing URL: {url}")
        try:
            # Use a simple payload that works for both text and image
            response = requests.post(url, headers=headers, json={"inputs": "test"})
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                print("SUCCESS! Found working endpoint.")
                break
            elif response.status_code == 401:
                print("401 Unauthorized - Token issue?")
            elif response.status_code == 404:
                print("404 Not Found")
            else:
                print(f"Failed with {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
