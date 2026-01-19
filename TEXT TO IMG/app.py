from flask import Flask, render_template, request, jsonify
import requests
import base64
import sys
import time

app = Flask(__name__)

# Pollinations AI - Free, fast, no token required
API_URL = "https://image.pollinations.ai/prompt/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Get optional parameters with defaults
    width = data.get('width', 512)
    height = data.get('height', 512)
    seed = data.get('seed') # None if not provided

    print(f"DEBUG: Generating '{prompt}' (Size: {width}x{height}, Seed: {seed})", file=sys.stderr)

    try:
        # Construct URL
        import urllib.parse
        safe_prompt = urllib.parse.quote(prompt)
        url = f"{API_URL}{safe_prompt}?width={width}&height={height}&nologo=true"
        
        # Determine seed
        if seed is not None:
             url += f"&seed={seed}"
        else:
             import random
             random_seed = random.randint(0, 1000000)
             url += f"&seed={random_seed}"

        print(f"DEBUG: Fetching {url}", file=sys.stderr)
        
        response = requests.get(url, timeout=120)
        
        if response.status_code != 200:
             print(f"DEBUG: API Error: {response.status_code} - {response.text}", file=sys.stderr)
             return jsonify({"error": f"API Error ({response.status_code})"}), 500

        # Check content type
        content_type = response.headers.get("content-type", "")
        if "image" not in content_type:
             print(f"DEBUG: Not an image: {content_type}", file=sys.stderr)
             return jsonify({"error": f"API returned text instead of image"}), 500

        image_data = base64.b64encode(response.content).decode('utf-8')
        return jsonify({"image": f"data:image/jpeg;base64,{image_data}"})

    except Exception as e:
        print(f"DEBUG: Exception: {e}", file=sys.stderr)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)
    app.run(debug=True)
