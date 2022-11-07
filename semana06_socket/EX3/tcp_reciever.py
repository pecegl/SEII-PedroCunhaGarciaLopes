import socket

TCP_IP = "127.0.0.1"
FILE_PORT = 5005 #porta do arquivo
DATA_PORT = 5006 #porta de dados
timeout = 3 #tempo
buf = 1024


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #classe e tipo de entrada e saída
sock_f.bind((TCP_IP, FILE_PORT)) #atribui um endereço de IP e um número de porta
sock_f.listen(1) #ouve

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT))
sock_d.listen(1)


while True:
    conn, addr = sock_f.accept()
    data = conn.recv(buf)
    if data:
        print("File name:", data)
        file_name = data.strip()

    f = open(file_name, 'wb')

    conn, addr = sock_d.accept()
    while True:
        data = conn.recv(buf)
        if not data:
            break
        f.write(data)

    print("%s Finish!" % file_name)
    f.close()