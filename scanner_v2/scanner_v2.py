import socket
from concurrent.futures import ThreadPoolExecutor

# taking user input
target = input("Enter Target IP: ").strip()

def scan_port(port):
    try:   # Creating the socket and socket timeout so it doesn't hang
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.5)
            # Try to connect and grab banner
            if s.connect_ex((target, port)) == 0:
                try:
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No banner received"
                print(f"[+] Port {port} is OPEN | {banner}")
    except:
        pass

print(f"Starting multi-threaded scan on {target}...")

# This runs 50 ports simultaneously so it finishes way faster
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, range(1, 1025))

print("Scan finished!BD")
