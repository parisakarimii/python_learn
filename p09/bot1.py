from urllib.request import urlopen, Request
import json
from time import *
import random
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
        
bot = Bot("FEpj2P7kNwpYjciyRVlqfWhk3PZUnoIzE99tONJp")
questions = [
    {
    'question' :'پایتخت کشور سوئیس کجاست؟'
    ,'choices' :['زوریخ', 'برن', 'وین']
    ,'answer': 1
    },
    {
    'question' :'کدام کشور بیشترین تولید پسته را در جهان دارد؟'
    ,'choices' :['آمریکا', 'ترکیه', 'ایران']
    ,'answer': 0
    },
    {
    'question' :'بهترین فوتبالیست دنیا کیست؟'
    ,'choices' :['مسی', 'رونالدو','نیمار'] 
    ,'answer': 0
    },
    {
    'question' :'پایتخت ایران کجاست؟'
    ,'choices' :['مشهد','تهران', 'اصفهان']
    ,'answer': 1
    }
]
count = 0
ids = set()
info = dict()
while True :
    s = bot.get_updates()
    length = len(s["result"])
    if count < length:
        diff = length - count
        for i in range(diff):
            idx = count
            a = s["result"][idx]
            z = str(a["message"]["chat"]["id"])
            r = a["message"]["text"]
            if not z in ids:
                ids.add(z)
                info[z] = {"score": 0,
                            "shown_q": [],
                            "last_answered": True
                            }
            if r == "/start":
                remain_index = []
                for i in range(len(questions)):
                    if not i in info[z]["shown_q"]:
                        remain_index.append(i)
                if len(remain_index) < 1:
                    data = {
                        "chat_id": z,
                        "text": "all shown!"
                            }
                    data = json.dumps(data)
                    data = data.encode()
                    bot.send_message(data)
                else:
                    q_index = random.choice(remain_index)
                    data = {
                        "chat_id":z ,
                        "text": questions[q_index]["question"] + "\n" + ("1. "
                        + questions[q_index]["choices"][0]) + "\n" + ("2. " +
                        questions[q_index]["choices"][1]) + "\n" + ("3. " +
                        questions[q_index]["choices"][2])
                        }
                    data = json.dumps(data)
                    data = data.encode()
                    bot.send_message(data)
                    info[z]['shown_q'].append(q_index)
                    info[z]["last_answered"] = False
            elif r in ["3", "1", "2" , 1 , 2 , 3]:
                if not info[z]["last_answered"]:
                    last_q = info[z]["shown_q"][-1]
                    last_q = questions[last_q]
                    info[z]["last_answered"] = True
                    data = {
                    "chat_id":z ,
                    "text": "Received!"
                    }
                    data = json.dumps(data)
                    data = data.encode()
                    bot.send_message(data)
            else:
                data = {
                "chat_id":z ,
                "text":"متوجه نشدم"
                }
                data = json.dumps(data)
                data = data.encode()
                bot.send_message(data)
            count = count + 1
        sleep(3)