PyScan-Sentinel v1.3
A high-performance, multi-threaded network reconnaissance tool built with Python. This project demonstrates core concepts in network programming, concurrency, and security auditing.

🚀 Features
Multi-threaded Scanning: Utilizes Python's threading library to scan hundreds of ports simultaneously.

Service Banner Grabbing: Implements low-level socket communication to identify running services and versions (e.g., Intel AMT v12.0), essential for vulnerability mapping.

Real-Time Alert System: Integrated with the plyer library to provide instant desktop notifications when a port is discovered.

Automated Logging: Generates time-stamped text reports for every scan, ensuring traceability for security audits.

Refined Error Handling: Specifically handles socket.timeout, ConnectionRefusedError, and OSError to ensure a stable, warning-free codebase.

🛠️ Technical Skills Demonstrated
Networking: TCP/IP handshakes, socket programming, and hostname resolution.

Concurrency: Managing shared resources and preventing output collision using threading.Lock.

OS Integration: Using the plyer module to bridge Python logic with the Windows notification system.

CLI Development: Building professional user-friendly interfaces with argparse.

File I/O: Persistent data storage and structured logging for forensic audit trails.

📋 Usage
Install Dependencies:

Bash

pip install plyer
Run the scanner via the terminal:

Bash

python sentinel_scanner.py -t <target_ip_or_domain> -s <start_port> -e <end_port>
Example:

Bash

python sentinel_scanner.py -t 127.0.0.1 -s 1 -e 1024
⚖️ Disclaimer
This tool is for educational and ethical testing purposes only. Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws.

Why this is a "Flex" for your Portfolio
Academic Excellence: By inc
