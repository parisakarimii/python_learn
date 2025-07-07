from urllib.request import urlopen, Request
import json
from time import *
class Bot():
    def __init__(self, token: str):
        self.token = token
        self.get_url = "https://tapi.bale.ai/bot{}/getUpdates".format(token)
        self.send_url = "https://tapi.bale.ai/bot{}/sendMessage".format(token)
    def get_updates(self):
        with urlopen(self.get_url) as resp:
            return json.loads(resp.read())
    def send_message(self, data):
        req = Request(self.send_url, method='POST')
        req.add_header('Content-Type', 'application/json')
        with urlopen(req, data=data) as resp:
            return json.loads(resp.read())
        
questions = [
    {
    'question' : 'پایتخت کشور سوئیس کجاست؟'
    ,'choices' : ['زوریخ', 'برن', 'وین']
    ,'answer': 1
    },
    {
    'question': 'کدام کشور بیشترین تولید پسته را در جهان دارد؟'
    ,'choices' : ['آمریکا', 'ترکیه', 'ایران']
    ,'answer': 0
    }
]
bot = Bot("nsiZifOpVATbMslNReqrZkzXvpSiChQPpVSNxUtx")
count = 0
recent_updates = []

while True:
    response = bot.get_updates()
    length = len(response['result'])
    if length > count:
        diff = length - count
        for i in range(diff):
            idx = count
            m = response['result'][idx]
            text = m['message']['text']
            id = m['message']['from']['id']
            update_info = {
            'user_id': id,
            'text': text
            }
            recent_updates.append(update_info)
            print(update_info)
            if text == '/start':
                data = {
                'chat_id': str(id),
                'text': questions[0]['question'] + ('\n' + '1. ' +
                questions[0]['choices'][0]) + ('\n' + '2. ' + questions[0]['choices'][1])
                + ('\n' + '3. ' + questions[0]['choices'][2])
                }
                data = json.dumps(data)
                data = data.encode()
                bot.send_message(data)
                
            else:
                data = {
                'chat_id': str(id),
                'text' : '.متوجه نشدم' 
                }
                data = json.dumps(data)
                data = data.encode()
                bot.send_message(data)
            count = count + 1
        print(recent_updates)
    sleep(5)