import socket
import time
import sys

UDP_IP = "127.0.0.1" #IP
UDP_PORT = 5005 #porta
buf = 1024
file_name = sys.argv[1]


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #classe e tipo de entrada e saída
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print("Sending %s ..." % file_name)

f = open(file_name, "r") # abre o file_name
data = f.read(buf) #leitura
while(data): #enquanto não seja nula
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf) #leitura
        time.sleep(0.02) # Delay

sock.close()
f.close()