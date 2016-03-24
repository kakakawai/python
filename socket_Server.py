from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADD = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADD)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print tcpCliSock,addr
    print '...connected from:',addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(),data))
    tcpCliSock.close()
tcpSerSock.close()
