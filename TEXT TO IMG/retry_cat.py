import requests
import time

url = "https://image.pollinations.ai/prompt/cute%20astronaut%20cat?width=600&height=400&nologo=true&seed=999"
print(f"Fetching {url}...")
try:
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        with open('assets/sample_cat.jpg', 'wb') as f:
            f.write(response.content)
        print("Success: Saved assets/sample_cat.jpg")
    else:
        print(f"Failed: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
