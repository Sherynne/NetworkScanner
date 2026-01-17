# PyScan-Sentinel v1.3

**PyScan-Sentinel** is a high-performance, multi-threaded network reconnaissance tool built with Python.
This project demonstrates core concepts in **network programming**, **concurrency** and **security auditing**, making it ideal for educational use and portfolio demonstration.

---

##  Key Features

* **Multi-threaded Scanning**
  Utilizes Python’s `threading` library to scan hundreds of ports simultaneously for maximum efficiency.

* **Service Banner Grabbing**
  Implements low-level socket communication to identify running services and versions (e.g., Intel AMT v12.0), which is essential for vulnerability mapping.

* **Real-Time Alert System**
  Integrated with the `plyer` library to deliver instant desktop notifications the moment an open port is discovered.

* **Automated Logging**
  Generates time-stamped text reports for every scan, ensuring full traceability for security audits and forensic analysis.

* **Refined Error Handling**
  Gracefully handles `socket.timeout`, `ConnectionRefusedError`, and `OSError` to maintain a stable and warning-free execution.

---

##  Technical Skills Demonstrated

### Networking & Security

* **TCP/IP Handshakes**
  Practical understanding of low-level connection states and handshake protocols.

* **Socket Programming**
  Direct interaction with network protocols for accurate port discovery.

* **Hostname Resolution**
  Dynamic conversion of domain names into target IP addresses.

### Software Engineering

* **Concurrency**
  Efficient management of shared resources and prevention of output collision using `threading.Lock`.

* **OS Integration**
  Seamless integration between Python logic and the Windows notification system via the `plyer` module.

* **CLI Development**
  Professional, user-friendly command-line interfaces built with `argparse`.

* **File I/O**
  Persistent data storage and structured logging to support forensic audit trails.

---

##  Usage Instructions

### 1. Install Dependencies

```bash
pip install plyer
```

### 2. Run the Scanner

```bash
python SentinelScanner.py -t <target_ip_or_domain> -s <start_port> -e <end_port>
```

#### Example

```bash
python SentinelScanner.py -t 127.0.0.1 -s 1 -e 1024
```

---

##  Disclaimer

This tool is intended **strictly for educational and ethical testing purposes**.
Unauthorized scanning or use against systems without explicit, mutual consent is illegal.
The end user is solely responsible for complying with all applicable local, state and federal laws.

---

##  Version

**v1.3**

---


