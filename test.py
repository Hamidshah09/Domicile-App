import socket
# import struct
import wmi
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    parts_of_ip = local_ip.split('.')
    print(f"sub netmask :{parts_of_ip[2]}")
    s.close()
    return local_ip
def get_network_address():
    ips = []
    for interface in socket.if_nameindex():
        print(interface)
        for ip in socket.getaddrinfo(interface[1], None):
            print(ip)
            if ip[1] == socket.SOCK_STREAM:
                ips.append(ip[4][0])
    print(f"Local IP addresses: {', '.join(ips)}")
print(f"Local IP address: {get_local_ip()}")
# get_network_address()
