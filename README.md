# Port Scanner

## Description
This project is a Python-based Port Scanner that scans a target system to identify open ports and the services running on them. It uses socket programming to attempt connections to multiple ports and determines their status.

## Features
- Scans ports (1–1024)
- Identifies open ports
- Detects common services (HTTP, HTTPS, etc.)
- Displays results in real-time
- Logs scan results to a file

## Tools Used
- Python
- Socket Programming

## How It Works
The scanner attempts to establish a TCP connection to each port on the target system. If the connection is successful, the port is marked as open. The program also tries to identify the service associated with the port.

## How to Run
python port_scanner.py

## Output
<img width="921" height="168" alt="Screenshot 2026-04-25 221048" src="https://github.com/user-attachments/assets/b5f0059b-8a01-453a-b82d-7b02076e4727" />
