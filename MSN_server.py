from socket import *
import time

HOST = ''
PORT = 21567
BUFSIZ = 1024
user = 'La'
ADD = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADD)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:',addr
    while True:
        his_name = tcpCliSock.recv(BUFSIZ)
        recv_time = tcpCliSock.recv(BUFSIZ)
        his_message = tcpCliSock.recv(BUFSIZ)
        if not (his_message and recv_time and his_name):
            break
        print '[%s][%s] %s' % (recv_time,his_name,his_message)
        my_message = raw_input('>')
        if not my_message:
            break
        tcpCliSock.send(user)
        tcpCliSock.send(time.strftime('%H:%M:%S',time.localtime()))
        tcpCliSock.send(my_message)
    tcpCliSock.close()
tcpSerSock.close()
