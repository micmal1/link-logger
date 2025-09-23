from http.server import BaseHTTPRequestHandler
import requests
import json
import os

# pobierz webhook z ENV (w Vercelu ustaw w Settings > Environment Variables)
WEBHOOK_URL = os.environ.get("https://discord.com/api/webhooks/1418597405871439933/8YsY9-WYZfq19AHicu8ua8ZPWgVxS1_I-4CiQ-LtZLS5HtzPfHOW8dpBwdrh84Pm80NR")

def get_public_ip():
    try:
        resp = requests.get("https://api.ipify.org?format=json", timeout=5)
        resp.raise_for_status()
        return resp.json().get("ip")
    except Exception as e:
        return f"error: {e}"

def send_message(content: str):
    if not WEBHOOK_URL:
        return
    try:
        requests.post(WEBHOOK_URL, json={"content": content}, timeout=5)
    except Exception as e:
        print("Błąd wysyłania do webhooka:", e)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = get_public_ip()
        send_message(f"IP received: {ip}")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"ip": ip}).encode("utf-8"))
