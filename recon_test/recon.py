import time
import sys
import os
import requests
import socket
import art
from colorama import Fore
import secrets
import pythonping
import config
import threading
import netifaces

commands = {
    "help": {"des": "shows help", "func": "help()"},
    "exit": {"des": "exit the recon panel", "func": "sys.exit()"},
    "clear": {"des": "clears terminal", "func": "clear()"},
    "lhost": {"des": "shows locals hostname", "func": "shost()"},
    "lip": {"des": "shows local ip", "func": "sip()"},
    "ping": {"des": "pings target ip", "func": "ping"},
    "scan": {"des": "scans ip for open ports", "func": "scan"},
    "router": {"des": "scans local network for active connections", "func": "router()"},
    "gip": {"des": "grab ip of dns domain (google.com/142.251.209.142)", "func": "check_ip"},
    "dos": {"des": "floats target with data", "func": "dos"},
}

def router():
    try:
        gateway = netifaces.gateways()
        gateway = gateway.get("default")
        router = gateway.get(netifaces.AF_INET)
        router = router[0]
        router_hostname = str(socket.gethostbyaddr(router)[0])
        base_ip = str(router).rstrip("1")

        print("")

        for i in range(1, 255 + 1):
            ip = base_ip + str(i)
            response = pythonping.ping(ip, count=1, timeout=0.1)
            if response.success():
                hostname = socket.gethostbyaddr(ip)[0]
                print(f"{Fore.WHITE}{ip}: {Fore.GREEN}online{Fore.WHITE} [{hostname}]")
        
        print("")
    except:
        print(Fore.RED, "Error", Fore.WHITE)


def dos(target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = 80
        print(f"""{Fore.MAGENTA}[{secrets.token_bytes(1)}]{Fore.WHITE} (dos) {Fore.GREEN}{target}{Fore.BLUE}""")
        print("")
        total_bytes = 0
        for i in range(1, 1000000):
            msg = f"{f'A'*10**4}".encode("utf-8")
            sock.sendto(msg, (target, port))
            total_bytes = total_bytes + 1 * 10 ** 4
        print(f"""{Fore.WHITE} Total Transfer: {total_bytes} B {Fore.GREEN}{target}{Fore.BLUE} done!""")
    except:
        print(Fore.RED, "Error", Fore.WHITE)


def get_username():
    return os.getenv("USERNAME")

def clear():
    show_icon()
    check_input()

def scan(ip, timeout=0.1):
    try:
        print(f"""{Fore.MAGENTA}[{secrets.token_bytes(1)}]{Fore.WHITE} (scanning) {Fore.GREEN}{ip}{Fore.BLUE}""")
        print(Fore.BLUE)
        for port in config.important_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"{Fore.WHITE}Port: {Fore.BLUE}{port}{Fore.CYAN} [{config.important_ports_dict[port]}] {Fore.GREEN}offen{Fore.WHITE} !")
    except:
        print(Fore.RED, "Error", Fore.WHITE)

def check_ip(domain):
    try:
        host = socket.gethostbyname(domain)
        print(f"""{Fore.MAGENTA}[{secrets.token_bytes(1)}]{Fore.WHITE} (real_ip) = {Fore.BLUE}{host}""")
    except:
        print(Fore.RED, "Error", Fore.WHITE)

def sip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        print(f"""{Fore.MAGENTA}[{secrets.token_bytes(1)}]{Fore.WHITE} (local_ip) = {Fore.BLUE}{local_ip}""")
    except:
        print(Fore.RED, "Error", Fore.WHITE)

def shost():
    try:
        hostname = socket.gethostname()
        print(f"""{Fore.MAGENTA}[{secrets.token_bytes(1)}]{Fore.WHITE} (hostname) = {Fore.BLUE}{hostname}""")
    except:
        print(Fore.RED, "Error", Fore.WHITE)

def help():
    try:
        print(Fore.WHITE)
        print("------------------------------------", Fore.BLUE)
        for item in commands:
            print(f"{Fore.YELLOW}{item}{Fore.WHITE} = {Fore.BLUE}{commands[item]['des']}")
        
        print(Fore.WHITE, "------------------------------------")
    except:
        print(Fore.RED, "Error", Fore.WHITE)

def show_icon():
    os.system("cls")
    icon = art.text2art("Recon", font="random-large")
    print(Fore.RED, icon, Fore.YELLOW)

def ping(ip, interval=1, count=5):
    try:
        print(f"""{Fore.MAGENTA}[{secrets.token_bytes(1)}]{Fore.WHITE} (ping) {Fore.GREEN}{ip}{Fore.BLUE}""")
        print("")
        pythonping.ping((ip), verbose=True, interval=interval, count=count)
    except:
        print(Fore.RED, "Error", Fore.WHITE)

def check_input():
    eingabe = input(f"""\n{Fore.YELLOW}|{secrets.token_hex(1)}|{secrets.token_hex(1)}|{secrets.token_hex(1)}|{secrets.token_hex(1)}||{secrets.token_hex(1)}|{secrets.token_hex(1)}||{secrets.token_hex(1)}|{secrets.token_hex(1)}| {Fore.BLUE}[ by harimtim © ]{Fore.MAGENTA}
|{secrets.token_hex(1)}|
|{secrets.token_hex(1)}|
|{secrets.token_hex(1)}|{Fore.CYAN} [~/{get_username()}] ---> {Fore.WHITE}:{Fore.CYAN}  """)
    eingabe = eingabe.split()
    teil1 = eingabe[0]
    if teil1 in commands:
        if len(eingabe) > 1:
                eval(f"{commands[teil1]['func']}('{eingabe[1]}')")
        else:
            eval(f"{commands[teil1]['func']}")
            
    else:
        check_input()

def start():
    show_icon()
    while True:
        check_input()

if __name__ == "__main__":
    show_icon()
    while True:
        check_input()