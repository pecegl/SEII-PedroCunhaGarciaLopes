import socket
import select

UDP_IP = "127.0.0.1" #ip
IN_PORT = 5005 #porta
timeout = 3 #tempo


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #classe e tipo de entrada e saída
sock.bind((UDP_IP, IN_PORT)) #atribui um endereço de IP e um número de porta

while True:
    data, addr = sock.recvfrom(1024)
    if data: #se não é nulo
        print("File name:", data)
        file_name = data.strip()

    f = open(file_name, 'wb') #abre arquivo

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data) #escrita
        else:
            print("%s Finish!" % file_name)
            f.close()
            break