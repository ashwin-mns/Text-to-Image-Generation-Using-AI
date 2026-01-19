import logging
from huggingface_hub import InferenceClient, __version__
import os
from dotenv import load_dotenv

# Setup full logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv(override=True)
API_TOKEN = os.getenv("HF_API_TOKEN")

print(f"Hub Version: {__version__}")
print(f"Token: {API_TOKEN[:5]}...")

client = InferenceClient(model="gpt2", token=API_TOKEN)

try:
    print("Attempting generation...")
    # gpt2 is text-to-text, just testing connectivity
    res = client.text_generation("Hello", max_new_tokens=10)
    print(f"Success: {res}")
except Exception as e:
    print(f"Error: {e}")
