from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024 # размер буфера - 1 Кб
ADDR = (HOST, PORT)

tcpSerSocket = socket(AF_INET, SOCK_STREAM)

tcpSerSocket.bind(ADDR) # Привязка сокета к адресу

'''listen -  Прослушивание запросов на соединение/ 5 - максимальное количество
    входящих запросов на установление соединения, которые могут быть приняты, пре­
    жде чем сервер начнет отклонять поступающие запросы или отказывать в их выпол­
    нении.'''
tcpSerSocket.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSocket.accept()
    print('...connected from', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        st = f'{ctime()}, {data}'.encode('utf-8')
        tcpCliSock.send(st)
    tcpCliSock.close()
tcpSerSocket.close()
