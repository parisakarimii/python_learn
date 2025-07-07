from urllib.request import urlopen, Request
import json
import time

class Bot():
    def __init__(self, token: str):
        self.token = token
        self.get_url = f"https://tapi.bale.ai/bot{token}/getUpdates"
        self.send_url = f"https://tapi.bale.ai/bot{token}/sendMessage"

    def get_updates(self):
        with urlopen(self.get_url) as resp:
            return json.loads(resp.read())

    def send_message(self, data):
        req = Request(self.send_url, method='POST')
        req.add_header('Content-Type', 'application/json')
        with urlopen(req, data=data) as resp:
            return json.loads(resp.read())


bot = Bot("nsiZifOpVATbMslNReqrZkzXvpSiChQPpVSNxUtx")
count = 0
recent_updates = []
while True:
    response = bot.get_updates()
    length = len(response['result'])
    if length > count:
        diff = length - count
        for i in range(diff):
            idx = count + i
            print(idx)
            m = response['result'][idx]
            text = m['message']['text']
            id = m['message']['from']['id']
            update_info = {
            'user_id': id,
            'text': text
            }
            recent_updates.append(update_info)
            print(update_info)
            print(recent_updates)
        count = length
    time.sleep(5)
