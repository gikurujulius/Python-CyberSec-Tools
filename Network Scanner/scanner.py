from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)
from scapy.all import *
import sys

ports = [25, 80, 53, 443, 445, 8080, 8443]

def SynScan(host):
    ans,unans = sr(IP(dst=host)/TCP(sport = 5555, dport=ports, flags='S'), timeout = 2, retry=3, verbose=0)
    print("Open ports at %s: " % host)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].sport:    #Verifies if the destination port of the sent packet is the same as the source port of the received reply
            print(s[TCP].dport)
            
def DNSScan(host):
    ans,unans = sr(IP(dst=host)/UDP(sport = 5555, dport = 53)/DNS(rd=1, qd=DNSQR(qname='domain', qtype='A'),timeout=2, verbose=0))
    if ans:
        print("DNS Server at %s " %host)
        
ip_address = input("Enter host address: ")
host = ip_address

SynScan(host)
DNSScan(host)