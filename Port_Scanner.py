import socket
import termcolor


def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)  # Set a timeout for the connection attempt
        sock.connect((ipaddress, port))
        print(f"[+] Port Opened: {port}")
        sock.close()  # Close the socket after successful connection
    except socket.error:
        return True
  #      print(f"[-] Port Closed: {port}")



targets = input("[*] Enter Targets IP Address (split them by comma): ")
ports = int(input("[*] Enter how many ports you want to scan: "))
if "," in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "), ports)

print("scan is complete")

#notes future add on, provide user option to scan all ports or specific ports
#also look set program to while loop and provide user option to run program again
#also provide user option to save scan results to a file