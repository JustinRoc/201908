from socket import *
import time
import codecs
# import numpy as np

ip_port = ('10.0.0.131', 8080)
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)
while True:
    # a = [0x25, 0x11]
    # msg = np.array(a)
    # print(msg)
    h = 'EECC1234'
    i = codecs.decode(h.encode('utf-8'), 'hex')
    udp_client.sendto(i, ip_port)
    time.sleep(2)