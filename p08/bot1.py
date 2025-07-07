from urllib.request import urlopen, Request
import json

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


bot = Bot('nsiZifOpVATbMslNReqrZkzXvpSiChQPpVSNxUtx')

updates = bot.get_updates()
print(updates)

f = open("text.json" , "w+")
json.dump(updates , f , indent=4)
f.close()


for update in updates['result']:

    print("Message ID:", update['message']['message_id'])
    print("From:", update['message']['from']['username'])
    print("Text:", update['message']['text'])
    print("Date:", update['message']['date'])
    print("-" * 40)