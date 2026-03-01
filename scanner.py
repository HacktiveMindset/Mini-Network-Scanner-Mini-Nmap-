from host_discovery import is_host_alive
from port_scanner import scan_ports
from banner_grabber import grab_banner

def main():
    print("=== Mini Network Scanner ===")

    target = input("Enter Target IP or Domain: ")

    if not is_host_alive(target):
        return

    open_ports = scan_ports(target)

    print("\n===== SERVICE DETECTION =====")

    for port in open_ports:
        banner = grab_banner(target, port)
        print(f"Port {port}: {banner}")

    print("\n===== SCAN COMPLETE =====")

if __name__ == "__main__":
    main()