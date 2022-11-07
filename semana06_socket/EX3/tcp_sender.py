import socket
import sys

TCP_IP = "127.0.0.1" #ip
FILE_PORT = 5005 #porta do arquivo
DATA_PORT = 5006 #porta de dados
buf = 1024
file_name = sys.argv[1]


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #classe e tipo de entrada e saída
    sock.connect((TCP_IP, FILE_PORT)) #conexão ip e porta
    sock.send(file_name) #envio
    sock.close()

    print("Sending %s ..." % file_name)

    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #classe e tipo de entrada e saída
    sock.connect((TCP_IP, DATA_PORT)) #conexão ip e porta
    data = f.read() #leitura
    sock.send(data) #envio

finally:
    sock.close()
    f.close()