import socket

def is_host_alive(target):
    print("\n[+] Checking if host is alive...")

    try:
        socket.gethostbyname(target)
        print("[ALIVE] Host reachable")
        return True
    except:
        print("[DOWN] Host not reachable")
        return False