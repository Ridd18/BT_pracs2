import hashlib

response = 'YES'

while(response == 'YES'):
    data = input("Enter your data: ")

    algorithm = input("select sny one algorithm: ")

    if algorithm == '1':
        output = hashlib.sha256(data.encode())
        print("Hash value in sha256 is",output.hexdigest())

    elif algorithm == '2':
        output = hashlib.sha512(data.encode())
        print("Hash value in sha512 is",output.hexdigest())

    elif algorithm == '3':
        output = hashlib.md5(data.encode())
        print("Hash value in md5 is",output.hexdigest())

    response = input("do you want to continue: ")
