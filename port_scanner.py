import socket
target = "127.0.0.1"

print(f"\n Scanning target: {target}\n")

OUTPUT_FILE = "scan_results.txt"

with open(OUTPUT_FILE, "w") as f:
  f.write(f"Scan results for {target}\n")

for port in range(1,1025): #scan first 1024 ports
  # print(f"Scanning poet {port}...")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.socket creates a network  connection tool.
  s.settimeout(0.1)

  result = s.connect_ex((target, port)) #connect_ex tries to connect to a port

  if result == 0:
    try:
      service = socket.getservbyport(port)
    except:
      service = "Unknown"

    output = f"[OPEN] Port {port} ({service})"
    print(output)

    with open(OUTPUT_FILE, "a") as f:
      f.write(output + "\n")

  s.close()