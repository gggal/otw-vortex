from socket import *
import struct

# binding the socket
s = socket(AF_INET, SOCK_STREAM)
s.connect(('vortex.labs.overthewire.org',5842))

# 4 values are to be read from server
res = 0
for x in range(0,4,1):
	data = s.recv(4)

        # each value should be a Little-Endian unsigned int
	res += struct.unpack("<I", data)[0]

# trim the result to be a 4 byte Little-Endian unsigned int
res = struct.pack("<I",(res & 0xFFFFFFFF))
s.send(res)
response = s.recv(1000)

print("Credentials are: %s" % response)

s.close()


