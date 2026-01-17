import requests

response = requests.get("https://www.google.com")

print("Статус-код:", response.status_code)
