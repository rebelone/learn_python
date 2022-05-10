import requests

r = requests.get("https://resoort.eu")
print(r.status_code)
print(r.ok)