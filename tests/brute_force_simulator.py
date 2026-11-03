from scapy.all import IP, TCP, wrpcap
from pathlib import Path
from datetime import datetime

packets = []

source_ip = "192.168.56.10"
target_ip = "192.168.56.20"

# Simula 30 tentativas de conexão SSH
for attempt in range(30):
    packet = (
        IP(src=source_ip, dst=target_ip)
        / TCP(
            sport=45000 + attempt,
            dport=22,
            flags="S",
            seq=attempt
        )
    )

    packets.append(packet)

Path("tests").mkdir(exist_ok=True)

wrpcap("tests/brute_force_test.pcap", packets)

print("[+] Brute force simulation created")
print(f"[+] Simulated connection attempts: {len(packets)}")
print(f"[+] Source IP: {source_ip}")
print(f"[+] Target IP: {target_ip}")
print("[+] Target service: SSH (port 22)")
