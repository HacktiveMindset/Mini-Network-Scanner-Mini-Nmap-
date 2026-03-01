import socket

COMMON_PORTS = range(1, 1025)

def scan_ports(target):
    open_ports = []

    print("\n[+] Scanning ports...")

    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    return open_ports