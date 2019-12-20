# https://www.thepythoncode.com/article/building-network-scanner-using-scapy

from scapy.all import ARP, Ether, srp

target_ip = "10.165.73.151/24"
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3)[0]

# alist of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to 'clients' list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))

# the result
"""
root@debian:~# pip3 install scapy
Collecting scapy
  Downloading https://files.pythonhosted.org/packages/52/e7/464079606a9cf97ad04936c52a5324d14dae36215f9319bf3faa46a7907d/scapy-2.4.3.tar.gz (905kB)
    100% |████████████████████████████████| 911kB 1.3MB/s
Building wheels for collected packages: scapy
  Running setup.py bdist_wheel for scapy ... done
  Stored in directory: /root/.cache/pip/wheels/95/bf/51/905b3e84ec4ca910ce4ae92173c7334623105a265bdd1d9438
Successfully built scapy
Installing collected packages: scapy
Successfully installed scapy-2.4.3
root@debian:~# cd /home/jeff/Downloads/scratch/instguid.git/ai/scripts/gen/
root@debian:/home/jeff/Downloads/scratch/instguid.git/ai/scripts/gen# python3 network_scanner_scapy.py
Begin emission:
Finished sending 256 packets.
****.................................................................................................
Received 101 packets, got 4 answers, remaining 252 packets
Available devices in the network:
IP                  MAC
10.165.73.191       c0:a5:dd:72:26:2b
10.165.73.151       30:23:03:34:63:12
10.165.73.104       b4:b6:76:02:40:36
10.165.73.143       c0:a5:dd:72:26:3d
"""
