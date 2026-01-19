import requests
import os
import shutil

# Ensure assets directory exists
if not os.path.exists('assets'):
    os.makedirs('assets')

def generate_and_save(prompt, filename):
    print(f"Generating: {prompt}...")
    # Using the same logic as app.py (Pollinations.ai)
    # URL encoded prompt manually or simple strings for this script
    url = f"https://image.pollinations.ai/prompt/{prompt}?width=600&height=400&nologo=true&seed=42"
    
    try:
        response = requests.get(url, stream=True, timeout=60)
        if response.status_code == 200:
            with open(f"assets/{filename}", 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
            print(f"Saved: assets/{filename}")
        else:
            print(f"Failed to generate {filename}: {response.status_code}")
    except Exception as e:
        print(f"Error generating {filename}: {e}")

# Generate 3 distinct examples
generate_and_save("futuristic cyberpunk city with neon lights at night", "sample_city.jpg")
generate_and_save("cute fluffy astronaut cat in space digital art", "sample_cat.jpg")
generate_and_save("serene mountain landscape with lake and sunset photorealistic", "sample_landscape.jpg")

print("Done generating assets.")
