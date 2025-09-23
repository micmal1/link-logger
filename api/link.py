from http.server import BaseHTTPRequestHandler
import requests
import json

WEBHOOK_URL = "https://discord.com/api/webhooks/XXXXXX/XXXXXX"

def get_public_ip():
    try:
        resp = requests.get("https://api.ipify.org?format=json", timeout=5)
        resp.raise_for_status()
        return resp.json().get("ip")
    except Exception as e:
        return f"error: {e}"

def send_message(content: str):
    data = {"content": content}
    try:
        requests.post(WEBHOOK_URL, json=data, timeout=5)
    except Exception:
        pass

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = get_public_ip()
        send_message(f"IP received: {ip}")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"ip": ip}).encode("utf-8"))
