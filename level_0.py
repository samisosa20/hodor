#!/usr/bin/python3
import requests

URL ="http://158.69.76.135/level0.php"
PARAMS = {"id": "1449", "holdthedoor": "submit"}
for i in range(1024):
   requests.post(URL, PARAMS)
