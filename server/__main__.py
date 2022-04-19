import socket
import config
import os
import hashlib
import time

try:
    os.mkdir("snippets")
except FileExistsError:
    pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = config.ip
port = config.port

s.bind((host, port))
s.listen(5)

def hash_time():
    return hashlib.md5(str(time.time()).encode("ascii")).hexdigest()

while True:
    clientsocket, addr = s.accept()

    msg = clientsocket.recv(1024)
    msg = msg.decode("ascii")
    print(msg)
    exec("msg = " + msg)
    if msg[0] == "UPLOAD":
        open("snippets/" + hash_time() + ".file", "w").write(msg[1])
        clientsocket.send(hash_time().encode("ascii"))
    elif msg[0] == "DOWNLOAD":
        clientsocket.send(open("snippets/" + msg[1] + ".file", "r").read().encode("ascii"))

    clientsocket.close()