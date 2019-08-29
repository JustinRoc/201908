import time
import socket


mcast_group_ip = '225.0.0.1'
mcast_group_port = 5001


def sender():
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = b'\xEE\xCC\x01\x02'
        send_sock.sendto(message, (mcast_group_ip, mcast_group_port))
        time.sleep(2)


if __name__ == "__main__":
    sender()