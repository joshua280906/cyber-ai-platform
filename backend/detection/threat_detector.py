from collections import defaultdict
from colorama import Fore

# ---------------------------------------------------
# TRACK PACKET COUNTS
# ---------------------------------------------------

ip_packet_counter = defaultdict(int)

# ---------------------------------------------------
# TRACK PORT SCANS
# ---------------------------------------------------

ip_port_tracker = defaultdict(set)

# ---------------------------------------------------
# SUSPICIOUS PORTS
# ---------------------------------------------------

SUSPICIOUS_PORTS = {
    "4444",
    "5555",
    "6666",
    "1337",
    "31337"
}

# ---------------------------------------------------
# DETECT THREATS
# ---------------------------------------------------

def detect_threat(packet):

    alerts = []

    src_ip = packet["src_ip"]
    dst_port = str(packet["dst_port"])

    # ------------------------------------------------
    # PACKET COUNTING
    # ------------------------------------------------

    ip_packet_counter[src_ip] += 1

    # ------------------------------------------------
    # TRACK UNIQUE PORTS
    # ------------------------------------------------

    ip_port_tracker[src_ip].add(dst_port)

    # ------------------------------------------------
    # SUSPICIOUS PORT DETECTION
    # ------------------------------------------------

    if dst_port in SUSPICIOUS_PORTS:

        alerts.append(
            f"[ALERT] Suspicious Port Access → {dst_port}"
        )

    # ------------------------------------------------
    # HIGH TRAFFIC DETECTION
    # ------------------------------------------------

    if ip_packet_counter[src_ip] > 100:

        alerts.append(
            f"[ALERT] High Traffic Volume → {src_ip}"
        )

    # ------------------------------------------------
    # PORT SCAN DETECTION
    # ------------------------------------------------

    if len(ip_port_tracker[src_ip]) > 2:

        alerts.append(
            f"[ALERT] Possible Port Scan Detected From → {src_ip}"
        )

    # ------------------------------------------------
    # DISPLAY ALERTS
    # ------------------------------------------------

    for alert in alerts:

        print(Fore.RED + alert)

    return alerts