import struct
import time
import socket


mcast_group_ip = '225.0.0.1'
mcast_group_port = 5001    #既是组播端口也是本地端口


def receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 获取本地IP地址
    local_ip = socket.gethostbyname(socket.gethostname())
    # 监听端口，已测试过其实可以直接bind 0.0.0.0；但注意不要bind 127.0.0.1不然其他机器发的组播包就收不到了
    sock.bind((local_ip, mcast_group_port))
    # 加入组播组
    mreq = struct.pack("=4sl", socket.inet_aton(mcast_group_ip), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)


    # 允许端口复用
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 设置非阻塞
    # sock.setblocking(0)


    while True:
        try:
            message, addr = sock.recvfrom(1024)
            print(message.decode('utf-8'))
        except :

            print("while receive message error occur")


if __name__ == "__main__":
    receiver()