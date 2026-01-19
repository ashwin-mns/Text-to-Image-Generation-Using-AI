from huggingface_hub import InferenceClient, __version__
import os
from dotenv import load_dotenv
import huggingface_hub

load_dotenv(override=True)
API_TOKEN = os.getenv("HF_API_TOKEN")

print(f"Hub Version: {__version__}")
print(f"Location: {huggingface_hub.__file__}")

client = InferenceClient(model="prompthero/openjourney", token=API_TOKEN)

try:
    print("Testing...")
    # Just check model status or simple gen
    res = client.text_to_image("Test")
    print("Success!")
except Exception as e:
    print("CAUGHT EXCEPTION:")
    print(e)
