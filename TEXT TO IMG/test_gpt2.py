import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")

url = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

print(f"Testing GPT2: {url}")
resp = requests.post(url, headers=headers, json={"inputs": "Hello"})
print(f"Status: {resp.status_code}")
print(f"Response: {resp.text[:100]}")
