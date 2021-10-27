import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

r = requests.get('https://store-content-ipv4.ak.epicgames.com/api/en-US/content/products/grand-theft-auto-v')
print(r.json())

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(r.json(), f)