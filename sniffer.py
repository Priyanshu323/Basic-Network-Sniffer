from scapy.all import *
from datetime import datetime

packet_count = 0

def packet_callback(packet):

    global packet_count

    if packet.haslayer(IP):

        packet_count += 1

        src = packet[IP].src
        dst = packet[IP].dst

        if packet.haslayer(TCP):
            proto = "TCP"

        elif packet.haslayer(UDP):
            proto = "UDP"

        elif packet.haslayer(ICMP):
            proto = "ICMP"

        else:
            proto = "OTHER"

        current_time = datetime.now().strftime("%H:%M:%S")

        output = f"Packet #{packet_count} [{current_time}] [{proto}] {src} ---> {dst}"

        print(output)

        with open("packets.txt", "a") as file:
            file.write(output + "\n")

sniff(prn=packet_callback, store=False, count=20)