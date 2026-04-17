import socket
import threading
from datetime import datetime

open_ports = []

COMMON_PORTS = {
    21:   "FTP  (File Transfer)",
    22:   "SSH  (Secure Shell / Remote Login)",
    23:   "Telnet (Unsecured Remote Login)",
    25:   "SMTP (Sending Emails)",
    53:   "DNS  (Domain Name System)",
    80:   "HTTP (Website - No Encryption)",
    110:  "POP3 (Receiving Emails)",
    143:  "IMAP (Email Access)",
    443:  "HTTPS (Website - Encrypted)",
    3306: "MySQL (Database)",
    3389: "RDP  (Windows Remote Desktop)",
    5432: "PostgreSQL (Database)",
    6379: "Redis (Cache/Database)",
    8080: "HTTP-Alt (Dev/Proxy Server)",
    27017:"MongoDB (NoSQL Database)",
}

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown Service")
            open_ports.append((port, service))
            print(f"  [OPEN]  Port {port:<6} → {service}")
        sock.close()
    except socket.error:
        pass

def scan_range(target_ip, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print(f"\n[ERROR] Could not resolve '{target}'. Check the hostname.")
        return None

def print_summary(target, ip, start, end, duration):
    print("\n" + "=" * 55)
    print("                   SCAN SUMMARY")
    print("=" * 55)
    print(f"  Target       : {target}  ({ip})")
    print(f"  Port Range   : {start} → {end}  ({end - start + 1} ports scanned)")
    print(f"  Time Taken   : {duration:.2f} seconds")
    print(f"  Open Ports   : {len(open_ports)} found")
    print("=" * 55)
    if open_ports:
        print("\n  PORT    SERVICE")
        print("  ------  " + "-" * 30)
        for port, service in sorted(open_ports):
            print(f"  {port:<7} {service}")
    else:
        print("\n  No open ports found in this range.")
    print("=" * 55)

def main():
    print("=" * 55)
    print("         PYTHON PORT SCANNER v1.0")
    print("=" * 55)

    target = input("\nEnter target (IP or hostname): ").strip()
    if not target:
        print("[ERROR] No target entered.")
        return

    ip = resolve_target(target)
    if not ip:
        return
    print(f"[INFO] Resolved to IP: {ip}")

    try:
        start_port = int(input("Start port (e.g. 1):    ").strip())
        end_port   = int(input("End port   (e.g. 1024): ").strip())
    except ValueError:
        print("[ERROR] Please enter valid port numbers.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[ERROR] Ports must be between 1–65535 and start ≤ end.")
        return

    print(f"\n[INFO] Scanning {target} on ports {start_port}–{end_port}...")
    print("[INFO] Open ports will appear below:\n")

    start_time = datetime.now()
    scan_range(ip, start_port, end_port)
    end_time = datetime.now()

    duration = (end_time - start_time).total_seconds()
    print_summary(target, ip, start_port, end_port, duration)

if __name__ == "__main__":
    main()
