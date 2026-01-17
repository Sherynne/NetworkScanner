# PyScan-Sentinel v1.2

A high-performance, multi-threaded network reconnaissance tool built with Python. This project demonstrates core concepts in network programming, concurrency, and security auditing.

##  Features
- **Multi-threaded Scanning:** Utilizes Python's `threading` library to scan hundreds of ports simultaneously.
- **Service Banner Grabbing:** Identifies running services and versions to assist in vulnerability assessment.
- **Automated Logging:** Generates time-stamped text reports for every scan, ensuring traceability for security audits.
- **Robust Error Handling:** Specifically handles socket timeouts and connection errors to ensure stability.

##  Technical Skills Demonstrated
- **Networking:** TCP/IP handshakes, socket programming, and hostname resolution.
- **Concurrency:** Managing shared resources using `threading.Lock`.
- **CLI Development:** Building user-friendly interfaces with `argparse`.
- **File I/O:** Persistent data storage and structured logging.

##  Usage
Clone the repository and run the scanner via the terminal:
```bash
python sentinel_scanner.py -t <target_ip_or_domain> -s <start_port> -e <end_port>
Example:

Bash

python sentinel_scanner.py -t 127.0.0.1 -s 1 -e 1024
⚖️ Disclaimer
This tool is for educational and ethical testing purposes only. Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws.
