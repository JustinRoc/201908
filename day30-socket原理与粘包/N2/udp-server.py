from socket import *
ip_port = ('10.0.0.14', 8080)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)  #数据报
udp_server.bind(ip_port)

while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print(data[1])