import math
import socket
from struct import *

 
#UDP_IP = "96.49.100.238"
#UDP_IP = "127.0.0.1"
UDP_IP = socket.gethostbyname(socket.gethostname())
print("Receiver IP: ", UDP_IP)
#UDP_PORT = 6000
UDP_PORT = 5001
print("Port: ", UDP_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
 
queue = [0] * 100


def euclidean(x, y, z):
    return math.sqrt(float(x)**2 + float(y)**2 + float(z)**2)

 
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print "received message:", data    
    #print "received message: %1.3f %1.3f %1.3f %1.3f", unpack_from ('!f', data, 0), unpack_from ('!f', data, 4), unpack_from ('!f', data, 8), unpack_from ('!f', data, 12)     
    A_X = "%1.4f" %unpack_from ('!f', data, 0)
    A_Y = "%1.4f" %unpack_from ('!f', data, 4)
    A_Z = "%1.4f" %unpack_from ('!f', data, 8)
    #print("received message: ", A_X, "%1.4f" %unpack_from ('!f', data, 4), "%1.4f" %unpack_from ('!f', data, 8), "%1.4f" %unpack_from ('!f', data, 12),"%1.4f" %unpack_from ('!f', data, 16), "%1.4f" %unpack_from ('!f', data, 20), "%1.4f" %unpack_from ('!f', data, 24), "%1.4f" %unpack_from ('!f', data, 28),"%1.4f" %unpack_from ('!f', data, 32), "%1.4f" %unpack_from ('!f', data, 36), "%1.4f" %unpack_from ('!f', data, 40), "%1.4f" %unpack_from ('!f', data, 44), "%1.4f" %unpack_from ('!f', data, 48), "%1.4f" %unpack_from ('!f', data, 52), "%1.4f" %unpack_from ('!f', data, 56), "%1.4f" %unpack_from ('!f', data, 60), "%1.4f" %unpack_from ('!f', data, 64), "%1.4f" %unpack_from ('!f', data, 68), "%1.4f" %unpack_from ('!f', data, 72), "%1.4f" %unpack_from ('!f', data, 76), "%1.4f" %unpack_from ('!f', data, 80), "%1.4f" %unpack_from ('!f', data, 84), "%1.4f" %unpack_from ('!f', data, 88), "%1.4f" %unpack_from ('!f', data, 92))
    print("A_X: ", A_X)
    print("A_Y: ", A_Y)
    print("A_Z: ", A_Z)
    print(euclidean(A_X, A_Y, A_Z))
