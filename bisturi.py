from subprocess import call
from ipaddress import ip_network

ip_range = input("Ip range: ")

hosts = [x for x in ip_network(ip_range).hosts()]

print(hosts)

out_buffer = None
value = call(['nmap'], stdout=out_buffer)

print(out_buffer)
