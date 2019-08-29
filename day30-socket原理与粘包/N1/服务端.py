from socket import *

ip_port = ('10.0.0.14', 8080)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)#对应客户端的connect(),相当于把客户端的socket先放在一个仓库里面，一会accept
print('服务器端开始运行了...') #来取，才可以使用


#本客户端不能实现并发
while True:
    conn, addr = tcp_server.accept()#将客户端的socket对象收进来
    print('服务器端accept了一个新的双向链接...')
    print('双向链接是：', conn)
    print('客户端地址是：', addr)

    while True:
        try:
            data = conn.recv(buffer_size)
            if not data:
                break
            print('客户端发来的消息是：', data.decode('utf-8'))
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break
