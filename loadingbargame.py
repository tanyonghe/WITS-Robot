import math
import socket
from struct import *
import sys
import time


UDP_IP = socket.gethostbyname(socket.gethostname())
#print("Receiver IP: ", UDP_IP)
UDP_PORT = 5001
#print("Port: ", UDP_PORT)

sys.stdout.write('Shake your device as fast as possible to reach 100%!\n')
sys.stdout.write('The game starts in 3...')
sys.stdout.flush()
time.sleep(1)
sys.stdout.write('\b\b\b\b2...')
sys.stdout.flush()
time.sleep(1)
sys.stdout.write('\b\b\b\b1...')
sys.stdout.flush()
time.sleep(1)
sys.stdout.write('\r' + ' ' * 23)
sys.stdout.write('\rGame Start!\n')
start_time = time.time()

filled = 0
unfilled = 1000
sys.stdout.write('[' + ' ' * 100 + ']   0%')
sys.stdout.flush()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


def euclidean(x, y, z):
    return math.sqrt(float(x)**2 + float(y)**2 + float(z)**2)


while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    A_X = "%1.4f" %unpack_from ('!f', data, 40)
    A_Y = "%1.4f" %unpack_from ('!f', data, 4)
    A_Z = "%1.4f" %unpack_from ('!f', data, 8)
    A_XYZ = euclidean(A_X, A_Y, A_Z)
	
    if A_XYZ > 0:
        sys.stdout.write('\r')
        filled += 1
        unfilled -= 1
        sys.stdout.write('[' + math.floor(filled/10)* '=')
        sys.stdout.write(math.ceil(unfilled/10)* ' ' + '] ')
        sys.stdout.write(str(math.floor(filled/10)).rjust(3) + '%')
        sys.stdout.flush()
        if filled == 1000:
            elapsed_time = time.time() - start_time
            sys.stdout.write('\nCongrats! Total time taken: ' + str(elapsed_time) + ' seconds!')
            break
