import socket

# takes target from the user
target_ip = input("enter Target IP:").strip()
port_range = range(1, 1025)

print(f"Scanning target: {target_ip}...")

for port in port_range :
    # create a TCP socket & set timeout
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.settimeout(0.1)

        # to return the 0 instead of using .connect() which gives exception
        result = client_socket.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")

print("Scan complete.")
