import socket
import termcolor


def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port Opened " + str(port))
    except:
        print(f"[-] Port Closed " + str(port))


targets = input("[*] Enter Targets IP Address (split them by comma): ")
ports = int(input("[*] Enter how many ports you want to scan: "))
if "," in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "), ports)

           
        