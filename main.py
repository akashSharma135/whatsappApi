import requests
from time import sleep

instance_id = 'instance339103'
token_key = 'ew70poqie5g3cgvq'

# api-endpoint
URL = f'https://api.chat-api.com/{instance_id}/sendMessage?token={token_key}'

phone_list = ['+919810365208', '+918449495992', '+919810365208', '+918449495992', '+919810365208', '+918449495992']

count = 0

for phone in phone_list:
    count += 1
    data = {
        'phone': phone,
        'body': 'Hello!'
    }

    r = requests.post(url=URL, data=data)
    print(f'response: {r.text}')
    # msgs want to send before a break
    if count > 3:   # can set count value as per your need
        sleep(30)
        count = 0


