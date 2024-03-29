#!/usr/bin/env python3

from sys import argv
import socket
from colorama import Fore

def get_banner(ip, port=80, timeout=10, query=""): ##GET / HTTP/3\r\n\n\n
    hname = get_domain_name(ip)
    if not hname:
        return
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((hname, port))
    except socket.error as e:
        print(f"{Fore.RED}Socket error, could not connect {e}")
    #s.send(query.encode()) ## do we need to .encode('utf-8') it?
    #if query != "":
    #    s.send(query.encode()) 
    try:
        print(s.recv(1024)) #.decode()
    except socket.error as e:
        print(f"{Fore.RED}Socket error: {e}")
    s.close()

def get_domain_name(ip):
    try:
        hname = socket.gethostbyaddr(ip)[0]
        return hname
    except socket.error:
        print(f"{Fore.RED}Error: could not obtain hostname")
        return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="banner grabber", description="Your favorite banner grabber tool in python",
                                     epilog="python3 bangrab.py [port] [timeout] [GET]|[HEAD]")
    parser.add_argument("-t", "--target", required=True, help="ip or hostname of the target")
    parser.add_argument("-p", "--port", required=False, help="Select port number (default 80)")
    parser.add_argument("-to", "--timeout", required=False, help="Set timeout (default 10 seconds)")
    parser.add_argument("-q", "--query", required=False, help="(Optional) specify query")
    #parser.print_help()
    args = parser.parse_args()
    get_banner(args.target, args.port)
    #print(get_domain_name(argv[1]))
