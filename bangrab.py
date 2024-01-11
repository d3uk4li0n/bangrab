from sys import argv
import socket

def get_banner(ip, port=80, timeout=10, query="GET / HTTP/3\r\n\n\n"):
    hname = get_domain_name(ip)
    if not hname:
        return
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((hname, port))
    s.send(query.encode()) ## do we need to .encode('utf-8') it?
    print(s.recv(10000))
    s.close()

def get_domain_name(ip):
    try:
        hname = socket.gethostbyaddr(ip)[0]
        return hname
    except socket.error:
        print("Error: could not obtain hostname")
        return ""

if __name__ == "__main__":
    print(get_domain_name(argv[1]))
