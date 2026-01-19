from huggingface_hub import InferenceClient, __version__
import os
from dotenv import load_dotenv
import traceback

load_dotenv(override=True)
API_TOKEN = os.getenv("HF_API_TOKEN")

print(f"Hub Version: {__version__}")

client = InferenceClient(model="prompthero/openjourney", token=API_TOKEN)

try:
    print("Testing connectivity...")
    # Just check model status or simple gen
    res = client.text_to_image("Test")
    print("Success!")
except Exception:
    print("CAUGHT EXCEPTION:")
    traceback.print_exc()
