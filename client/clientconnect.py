import socket


def serverconnect():
    sock = socket.socket()
    sock.connect(('192.168.0.29', 9090))
    return sock
