import socket
import config
import sys

# create a client socket and send a message to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((config.ip, config.port))

args = sys.argv

if args[1] == "1":
    s.send(("[\"UPLOAD\", \"\"\"" + open(args[2], "r").read() + "\"\"\"]").encode("ascii"))
    print(s.recv(1024).decode("ascii"))
elif args[1] == "2":
    s.send(("[\"DOWNLOAD\", \"" + args[2] + "\"]").encode("ascii"))
    print(s.recv(1024).decode("ascii"))
elif args[1] == "help":
    print("upload = 1 <filename>")
    print("download = 2 <key>")