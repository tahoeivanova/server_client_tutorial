from socket import *

HOST = 'localhost'
PORT = 21568
BUFSIZ = 1024 # размер буфера - 1 Кб
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)

tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    st = data.encode('utf-8')
    tcpCliSock.send(st)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip())

    tcpCliSock.close()
