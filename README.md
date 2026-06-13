# Basic-Network-Sniffer
A basic network packet sniffer built using Python and Scapy that captures live network traffic and displays source IP, destination IP, protocol, timestamps, and packet logs.
# Basic Network Sniffer

## Overview

A simple Network Sniffer built using Python and Scapy that captures live network traffic and displays source IP address, destination IP address, protocol type, timestamps, and packet count.

## Features

* Capture live network packets
* Detect Source IP Address
* Detect Destination IP Address
* Identify Protocols (TCP, UDP, ICMP)
* Packet Counter
* Timestamp Logging
* Save Packet Logs to File

## Technologies Used

* Python 3
* Scapy

## Installation

```bash
pip install scapy
```

## Run

```bash
python sniffer.py
```

## Sample Output

```text
Packet #1 [23:03:31] [TCP] 192.168.31.194 ---> 172.66.43.174
Packet #2 [23:03:32] [TCP] 192.168.31.194 ---> 13.107.137.11
```

## Learning Outcomes

* Packet Sniffing
* TCP/IP Networking
* Protocol Analysis
* Python Networking Fundamentals
