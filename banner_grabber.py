import socket

def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))

        banner = sock.recv(1024).decode().strip()
        sock.close()

        return banner
    except:
        return "Unknown Service"