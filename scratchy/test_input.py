# use this script to see if http/api input is working

import requests, json
url = "http://127.0.0.1:5000/"
data = {'int1': '144', 'int2': '444'}

r = requests.post(url, data=json.dumps(data))
