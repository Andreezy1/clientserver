import socket
#connect
def connectclient():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    print('connected:', addr)
    return conn


