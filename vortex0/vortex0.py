import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('vortex.labs.overthewire.org',5842))
total = 0
for x in range(0,4,1):
	data = s.recv(4)
	total+= struct.unpack("<I", data)[0]

total = struct.pack("<I",(total & 0xFFFFFFFF))
s.send(total)
response = s.recv(1000)
print("Recieved: %s" % response)

s.close()


