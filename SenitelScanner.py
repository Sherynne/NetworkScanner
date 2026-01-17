import socket
import threading
import argparse
import sys
from datetime import datetime
from plyer import notification

# Global lock to prevent overlapping output
print_lock = threading.Lock()


def send_alert(target, port):
    """Triggers a desktop notification for found open ports with specific error handling."""
    try:
        notification.notify(
            title="Sentinel Security Alert",
            message=f"Open Port Found: {port}\nTarget: {target}",
            app_name="PyScan-Sentinel",
            timeout=3
        )
    except (RuntimeError, ImportError, NameError):
        # FIX: Specific exceptions for notification failures to clear the final warning
        pass


def get_banner(sock):
    """Retrieves service information with specific exception handling."""
    try:
        sock.send(b'Hello\r\n')
        sock.settimeout(2)
        banner = sock.recv(1024).decode(errors='ignore').strip()
        return banner if banner else "N/A (Passive service)"
    except (socket.timeout, socket.error):
        return "N/A (No response)"


def scan_port(ip, port, log_file):
    """Checks port status and handles specific network errors."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))

        if result == 0:
            banner = get_banner(sock)
            output_line = f"| {str(port).ljust(6)} | {'OPEN'.ljust(6)} | {banner}"

            send_alert(ip, port)

            with print_lock:
                print(output_line)
                with open(log_file, "a") as f:
                    f.write(output_line + "\n")
        sock.close()
    except (socket.timeout, ConnectionRefusedError, OSError):
        pass


def main():
    parser = argparse.ArgumentParser(description="PyScan-Sentinel: Recon Tool with Alerts")
    parser.add_argument("-t", "--target", help="Target IP or Domain", required=True)
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-th", "--threads", type=int, default=100, help="Threads")

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"[!] Error: Could not resolve {args.target}")
        sys.exit()

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = f"scan_{target_ip}_{timestamp}.txt"

    header = f"""
==================================================
 PYSCAN-SENTINEL v1.3
 Target IP  : {target_ip}
 Start Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
 Log File   : {log_file}
==================================================
| PORT   | STATUS | BANNER / SERVICE INFO
|--------|--------|------------------------------"""

    print(header)
    with open(log_file, "w") as f:
        f.write(header + "\n")

    threads = []
    for port in range(args.start, args.end + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port, log_file))
        threads.append(t)
        t.start()

        if len(threads) >= args.threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    footer = f"\n==================================================\n Scan Completed."
    print(footer)
    with open(log_file, "a") as f:
        f.write(footer + "\n")


if __name__ == "__main__":
    main()
