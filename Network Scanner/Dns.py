
import sys
import socket
import dns
import dns.resolver

        
        
def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]]+result[1]
    except socket.herror:
        return None


def DnsRequest(target_domain):
    ips = []
    for record_type in record_types:
        try:
            result = dns.resolver.resolve(target_domain, record_type)
            if result:
                print(target_domain)
                for answer in result:
                    print(f"{record_type} records for {target_domain}: ")
                    print("Domain Names: %s" % ReverseDNS(answer.to_text()))
        except (dns.resolver.NXDOMAIN, dns.exception.Timeout, dns.resolver.NoAnswer):
            return []
    return ips
       
def Subdomain_Search(target_domain, dictionary, nums):
    for word in dictionary:
        subdomain = word+"." + target_domain
        DnsRequest(subdomain)
        if nums:
            for i in range(0,10):
                s = word + str(i) + "." + target_domain
                DnsRequest(s)
    
        
target_domain = input("Enter your target: ")
subdomain_files = "subdomains-top1million-110000.txt"
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
dictionary = []
with open(subdomain_files, "r") as f:
    dictionary = f.read().splitlines()
    
Subdomain_Search(target_domain, dictionary, True)
