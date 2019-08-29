import subprocess
from socket import *

ip_port = ('127.0.0.1', 8080)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
print('服务器端开始运行了...')

while True:
    conn, addr = tcp_server.accept()
    print('服务器端accept了一个新的双向链接...')
    print('双向链接是：', conn)
    print('客户端地址是：', addr)
    while True:
        try:
            cmd = conn.recv(buffer_size)
            if not cmd: break
            print('收到客户端的命令：', cmd)
            res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                    cmd_res = err
            else:
                cmd_res = res.stdout.read()
            conn.send(cmd_res)
            if not cmd_res:
                conn.send('执行成功'.encode('gbk'))
        except Exception as e:
            print(e)
            break
