# Simple Port Scanner using socket
import socket

# Target to scan
target = input("Enter the IP address or hostname to scan: ")
# Common ports to scan
#common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

#OR scan using range
start = int(input("Enter your start port: \t"))
stop = int(input("Enter your stop port: \t"))


print(f"\nStarting scan on {target}...\n")

for port in range(start, stop, + 1):
#Uncomment this if you want to use the common port
#for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout for responsiveness

    result = sock.connect_ex((target, port))  # 0 means open
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED or FILTERED")
    sock.close()
