#!/usr/bin/env python3

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
    print(s.recv(10000).decode())
    s.close()

def get_domain_name(ip):
    try:
        hname = socket.gethostbyaddr(ip)[0]
        return hname
    except socket.error:
        print("Error: could not obtain hostname")
        return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="banner grabber", description="Your favorite banner grabber tool in python",
                                     epilog="python3 bangrab.py [port] [timeout] [GET]|[HEAD]")
    parser.add_argument("ip or hostname", help="ip or hostname of the target")
    parser.add_argument("-p", "--port", required=False, help="Select port number (default 80)")
    parser.add_argument("-t", "--timeout", required=False, help="Set timeout (default 10 seconds)")
    parser.add_argument("-q", "--query", required=False)
    #print(get_domain_name(argv[1]))