from socket import *
import time

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
user = 'Yo'
ADD = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADD)
while True:
    my_message = raw_input('> ')
    if not my_message:
        break
    tcpCliSock.send(user)
    tcpCliSock.send(time.strftime('%H:%M:%S',time.localtime()))
    tcpCliSock.send(my_message)
    her_name = tcpCliSock.recv(BUFSIZ)
    recv_time = tcpCliSock.recv(BUFSIZ)
    her_message = tcpCliSock.recv(BUFSIZ)
    if not her_message:
        break
    print '[%s][%s] %s' % (recv_time,her_name,her_message)

tcpCliSock.close()

