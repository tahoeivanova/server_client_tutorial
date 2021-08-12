#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024 # размер буфера - 1 Кб
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
    print('waiting for connection...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    st = f'{ctime()}, {data}'.encode('utf-8')
    udpSerSock.sendto(st, addr)
    print('received from and returned to:', addr)

udpSerSock.close()
