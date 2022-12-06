import socket
import hashlib

a = input("Enter the message : ")

sha256hex = hashlib.sha256(a.encode()).hexdigest()

s = socket.socket()
print('\n socket successfuly created')
port = 9999

s.bind(('localhost',port))
print("\n socket binded to : %s "%(port))

s.listen(1)
print("\n socket is listening.... ")

while True:
    c,addr = s.accept()
    print("\n got connection from : ", addr)
    c.send(a.encode())
    c.send(sha256hex.encode())
    print("\n message has been sent")
    c.close()
    break
