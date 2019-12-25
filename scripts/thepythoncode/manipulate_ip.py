# reference > https://www.thepythoncode.com/article/manipulate-ip-addresses-using-ipaddress-module-in-python
# doc > https://docs.python.org/3/howto/ipaddress.html

import ipaddress
# initlalize an IPv4 address
ip = ipaddress.IPv4Network("192.168.1.1")

# print True if the IP address is global
print("Is global:", ip.is_global)

# print True if the IP address is Link-Local
print("Is link-local:", ip.is_link_local)

# next ip address
# print(ip + 1)

# previous ip address
# print(ip - 1)

# initialize an IPv4 network
network = ipaddress.IPv4Network("192.168.1.0/24")

# get the network mask
print("Network mask:", network.netmask)

# get the bradcast address
print("Broadcast address:", network.broadcast_address)

# print the # of IP addresses under this network
print("Number of hosts under", str(network), ":", network.num_addresses)

# iterate over all the hosts under this network
print("Hosts under", str(network), ":")
for host in network.hosts():
    print(host)

# iterate over the subnets of this network
print("Subnets:")
for subnet in network.subnets(prefixlen_diff=2):
    print(subnet)

# get the supernet of this network
print("Supernet:", network.supernet(prefixlen_diff=1))

# tell if this network is under (or overlaps) 192.168.0.0/16
print("Overlaps 192.168.0.0/16:", network.overlaps(ipaddress.IPv4Network("192.168.0.0/16")))
