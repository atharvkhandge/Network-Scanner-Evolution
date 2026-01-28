# check if the lib are available
try:
    import tqdm
    import prettytable
except ImportError:
    print("=" * 60)
    print("Error: You are missing 'tqdm' or 'prettytable'!")
    print("Please run: pip install tqdm and pip install prettytable")
    print("=" * 60)
    exit()

import socket
from concurrent.futures import ThreadPoolExecutor
from prettytable import PrettyTable
from tqdm import tqdm # You'll need to run: pip install tqdm

# taking user input for IP and Port
target = input("Target IP: ").strip()
start_p = int(input("Start port: "))
end_p = int(input("End port: "))

# organizing the table
table = PrettyTable()
table.field_names = ["PORT", "STATUS", "BANNER"]

# initiating scan
def scan(port):
    try: #setting time out and banner grabbing
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            if s.connect_ex((target, port)) == 0:
                try:
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No banner"
                table.add_row([port, "OPEN", banner])
    except:
        pass

# the tqdm part here wraps the range to show the progress bar
print(f"Scanning {target}...")
port_range = range(start_p, end_p + 1)

# double the workers from v2
with ThreadPoolExecutor(max_workers=100) as executor:
    list(tqdm(executor.map(scan, port_range), total=len(port_range), desc="Progress"))

print("\n", table)
print("Finished!")
