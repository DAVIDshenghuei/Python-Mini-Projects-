#This is a simple Python program that uses the requests module to send HTTP POST requests and interact with the Baidu Translation API.

import requests
from opencc import OpenCC

#Set the URL you want to request, here is the suggested API for Baidu Translation.
url = 'https://fanyi.baidu.com/sug'
#"opencc" Convert Traditional Chinese text input to Simplified Chinese
cc = OpenCC('t2s')

while True:
    text = cc.convert(input('Please input English or Chinese word:').strip())
    if text == 'q':
        break

    data = {'kw': text}

    resp = requests.post(url, data)

    found = False
    #Check that the status code of the HTTP response is 200, indicating that the request was successful.
    if resp.status_code == 200:
    #Converting JSON-formatted response data to Python dictionaries
        data = resp.json()
        if data['errno'] == 0:
    #List of suggested terms in the "data" returned by the API
            ds = data['data']
            for kv in ds:
                if kv['k'] == text:
                    found = True
                    print(kv['v'])
            if not found:
                print('Not found')
        else:
            print(data)
    else:
        print(resp.content)
    #If the status code of the HTTP response is not 200, the content of the HTTP response is printed. This can be used to check why the request failed.
