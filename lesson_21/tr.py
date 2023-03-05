import requests
resp = requests.get(url="http://api.open-notify.org/iss-now.json").json()
print(resp['iss_position'])