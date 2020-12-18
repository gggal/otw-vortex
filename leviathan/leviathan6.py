import itertools
import subprocess
import time

# prints all key variations until it gets to the right one
for key in itertools.product('123456789', repeat=4):
    print("".join(key))
    res = subprocess.run("/home/leviathan6/leviathan6 " + "".join(key), shell=True, check=True, stdout=subprocess.PIPE)
    time.sleep(0.001)
