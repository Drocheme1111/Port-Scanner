# Port-Scanner

🔍 Simple Port Scanner (Python)

This is a basic port scanner written in Python using the socket module. It allows users to input a target IP address or hostname and specify a custom range of ports to scan. The scanner attempts TCP connections to determine if a port is open, closed, or filtered.

🚀 Features

Simple and beginner-friendly

Accepts target IP or hostname

Customizable port range scanning

Uses TCP protocol for connection attempts

Timeout implemented for responsiveness

🧰 Requirements

Python 3.x

No external libraries are needed—only Python's built-in socket module is used.

📅 Installation

Clone the repository or download the Python script:

git clone https://github.com/your-username/simple-port-scanner.git
cd simple-port-scanner

▶️ Usage

Run the script using Python:

python3 port_scanner.py

You’ll be prompted to enter:

The IP address or hostname to scan

The start port number

The stop port number

Example

Enter the IP address or hostname to scan: 192.168.1.1
Enter your start port: 20
Enter your stop port: 100

Starting scan on 192.168.1.1...

Port 20 is CLOSED or FILTERED
Port 21 is OPEN
Port 22 is OPEN
...

🧠 Note

The scan uses TCP (socket.SOCK_STREAM) to attempt to connect to each port.

If a port is open, it prints: Port XX is OPEN.

Otherwise, it prints: Port XX is CLOSED or FILTERED.

📌 TODO

Add multi-threading for faster scanning

Add options for scanning common ports

Add logging to file

🛡️ Disclaimer

This script is intended for educational and ethical use only. Do not scan IPs or hosts you do not own or have explicit permission to test.

📄 License

This project is open-source and available under the MIT License.

Feel free to contribute or modify the script to add more advanced scanning features!
