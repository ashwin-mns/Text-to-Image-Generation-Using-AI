import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

models = [
    "runwayml/stable-diffusion-v1-5",
    "CompVis/stable-diffusion-v1-4",
    "prompthero/openjourney",
    "stabilityai/stable-diffusion-2-1",
    "stabilityai/stable-diffusion-2",
    "stabilityai/sdxl-turbo",
    "stabilityai/stable-diffusion-3-medium-diffusers",
    "ByteDance/SDXL-Lightning",
    "cagliostrolab/animagine-xl-3.1",
    "dreamlike-art/dreamlike-photoreal-2.0",
    "hakurei/waifu-diffusion",
    "Lykon/DreamShaper"
]

print("Scanning Router...")

for model in models:
    url = f"https://router.huggingface.co/models/{model}"
    try:
        resp = requests.post(url, headers=headers, json={"inputs": "cat"})
        print(f"{model}: {resp.status_code}")
        if resp.status_code == 200:
            print(f"FOUND WORKING MODEL: {model}")
            # verify image
            if "image" in resp.headers.get("content-type", ""):
                print("Confirmed Image.")
                break
    except Exception as e:
        print(f"{model}: Error {e}")
