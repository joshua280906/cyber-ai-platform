from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime
import requests

BACKEND_URL = "http://127.0.0.1:8000/traffic/ingest"

print("[+] Live Packet Ingestion Started...\n")


def process_packet(packet):

    if packet.haslayer(IP):

        timestamp = datetime.now().strftime("%H:%M:%S")

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = "OTHER"
        src_port = "N/A"
        dst_port = "N/A"

        if packet.haslayer(TCP):

            protocol = "TCP"

            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif packet.haslayer(UDP):

            protocol = "UDP"

            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        elif packet.haslayer(ICMP):

            protocol = "ICMP"

        packet_data = {

            "timestamp": timestamp,
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "protocol": protocol,
            "src_port": src_port,
            "dst_port": dst_port,
            "packet_size": len(packet)
        }

        print(packet_data)

        try:

            requests.post(
                BACKEND_URL,
                json=packet_data
            )

        except Exception as e:

            print(f"[ERROR] Backend connection failed: {e}")


sniff(prn=process_packet, store=False)