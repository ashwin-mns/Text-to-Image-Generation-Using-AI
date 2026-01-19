import requests

prompt = "A futuristic city"
url = f"https://image.pollinations.ai/prompt/{prompt}"

print(f"Testing Pollinations: {url}")
try:
    resp = requests.get(url)
    print(f"Status: {resp.status_code}")
    print(f"Content-Type: {resp.headers.get('content-type')}")
    if resp.status_code == 200:
        print("Success! Image received.")
    else:
        print("Failed.")
except Exception as e:
    print(f"Error: {e}")
