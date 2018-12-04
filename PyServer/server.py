import socket 
import pickle
from db import add_cred
from db import authenticate as auth
server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverAddress = "192.168.43.10"
serverPort = 12345

server_sock.bind((serverAddress,serverPort))

server_sock.listen(10)

def process(data):
    # Basically this must check the hash of the password (currently just match strings and return a value)
    credentials = data.decode().split("/0")
    if(credentials[0]=="zero"):
        try:
            add_cred(credentials)
        except:
            return False
        return True
    elif(credentials[0]=="one"):
        try:
            result = auth(credentials)
        except:
            return False
        return result

while(1):
    conn,addr = server_sock.accept()
    data = conn.recv(4096)
    print(data)
    result = process(data)
    out = str(result).encode()
    conn.send(out)
    print(out)