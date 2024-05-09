import requests

url = "https://api.ultramsg.com/instance85185/messages/chat"

payload = "token=mpls72jvejym2ng7&to=&body="
payload = payload.encode('utf8').decode('iso-8859-1')
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)