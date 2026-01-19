from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv(override=True)
API_TOKEN = os.getenv("HF_API_TOKEN")

# Try to force the router URL
base_url = "https://router.huggingface.co/hf-inference"
print(f"Testing with base_url: {base_url}")

client = InferenceClient(token=API_TOKEN)

try:
    # We pass the full URL or relative to base?
    # Actually InferenceClient(model=...) usually takes the model ID.
    # If we want to check connectivity, let's try to generate.
    
    # We can also try to pass the URL as the model if it supports it?
    # Or use constructor argument if available (it is in newer versions)
    
    # Attempt 1: Constructor hook (if exists in this version)
    try:
        c2 = InferenceClient(model="prompthero/openjourney", token=API_TOKEN)
        # Hack to overwrite the base URL if possible
        # but let's see if we can just pass the URL as model
        url = "https://router.huggingface.co/hf-inference/models/prompthero/openjourney"
        print(f"Trying direct URL: {url}")
        res = c2.post(json={"inputs": "test"}, model=url)
        print("Success with c2.post details!")
        print(res.status_code)
    except Exception as e:
        print(f"Direct URL Test Failed: {e}")

except Exception as e:
    print(f"Error: {e}")
