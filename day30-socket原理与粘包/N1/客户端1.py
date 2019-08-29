from socket import *

ip_port = ('10.0.0.15', 8080)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input(">>: ")
    # if not msg:
    #     continue
    tcp_client.send(msg.encode('utf-8'))
    print('客户端已发送消息！')
    data = tcp_client.recv(buffer_size)
    print('收到服务端来的消息：', data.decode('utf-8'))

# tcp_client.close()