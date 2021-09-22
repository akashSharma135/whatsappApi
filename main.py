import requests
  
# api-endpoint
URL = 'https://api.chat-api.com/instance339103/sendMessage?token=ew70poqie5g3cgvq'

phone_list = ['+919810365208']

for phone in phone_list:
    data = {
        'phone': phone,
        'body': 'Hello! bdkjabfs dysfjh yasfjhahsbfj asgdasbhj syagyab sabhjasb. sahfbsabgyuas usiafihk ysagiusa'
    }

    r = requests.post(url=URL, data=data)

pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)

# URL = 'https://api.chat-api.com/instance339103/messagesHistory?token=ew70poqie5g3cgvq'

# r = requests.get(url=URL)
# print(r.text)