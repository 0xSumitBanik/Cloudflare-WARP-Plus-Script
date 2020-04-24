import string as st
import requests
import json
import datetime
import random

url = 'https://api.cloudflareclient.com/v0a745/reg'
print('\n *** WARP+ Referrer Script *** \n\n\
\tModified by: TheSumitBanik\n')
referrer = input(" Enter 1.1.1.1 ID: \n > ")

retryTimes = 4

def generateInstallID(stringLength):
    letters = st.ascii_letters + st.digits
    return ''.join(random.choice(letters) for i in range(stringLength))





def run():
    install_id = generateInstallID(11)
    body = {"key": "{}=".format(generateInstallID(42)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, generateInstallID(134)),
            "referrer": referrer,
            "warp_enabled": True,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "en-IN"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }

    r = requests.post(url, data=bodyString, headers=headers)
    return r


for i in range(int(3)):
    result = run()
    if result.status_code == 200:
        ''' OK '''
        print('Crediting Data ...')
    else:
        print(i + 1, "Error")
        for r in range(retryTimes):
            retry = run()
            if retry.status_code == 200:
                print(i + 1, "Retry #" + str(r + 1), "OK")
                break
            else:
                print(i + 1, "Retry #" + str(r + 1), "Error")
                if r == retryTimes - 1:
                    exit()

print(f"\n Credited with 2GB at ID: {referrer}")
