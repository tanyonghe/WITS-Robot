import struct
import socket
IP = "127.0.0.1"
IP = "192.168.0.44"
PORT = 5001

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((IP, PORT))

while True:
    data, addr = serverSock.recvfrom(4)
    print(type(data))
    print(struct.unpack("i", data))
    #print ("Message: ", data)
    #print ("Message: ", int(data, 2))
    #string = data.decode("utf-8")
    #print ("Message: ", string)
