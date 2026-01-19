from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
import io

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_ID = "prompthero/openjourney"

print(f"Testing client with model: {MODEL_ID}")
print(f"Token present: {bool(API_TOKEN)}")

try:
    client = InferenceClient(model=MODEL_ID, token=API_TOKEN)
    print("Client initialized. Sending request...")
    image = client.text_to_image("A cute cat")
    print("Image generated successfully!")
    print(f"Image format: {image.format}, Size: {image.size}")
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    import traceback
    traceback.print_exc()
