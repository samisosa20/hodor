#!/usr/bin/python3
import requests

URL ="http://158.69.76.135/level1.php"

for i in range(4096):
   print(i)
   rq = requests.get(URL)
   cookie = rq.cookies['HoldTheDoor']
   PARAMS = {"id": "1449", "holdthedoor": "submit", "key": cookie}
   cookiejson = {'HoldTheDoor': cookie}
   requests.post(URL, PARAMS, cookies=cookiejson)
