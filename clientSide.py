import socket
import hashlib


c = socket.socket()
port = 9999

c.connect(('localhost',port))

a = c.recv(1024).decode()
data = c.recv(1024).decode()

print("\n welcome to the network")

c.close()

hexcode = hashlib.sha256(a.encode()).hexdigest()

if hexcode == data:
    print("\n integrity is maintained")
    print("message",a)
else:
    print("integrity is lost")
