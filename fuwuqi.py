import socket
from threading import Thread
def handle_client_in(conn,addr):
    nickname = conn.recv(1024).decode("utf-8")
    welcome = f'欢迎{nickname}'
    client[conn] = nickname
    print(client)
    broadcast(bytes(welcome,'utf-8'))
    while True:
        try:
            msg = conn.recv(1024)
            broadcast(msg,nickname+':')
        except:
            conn.close()
            del client[conn]
            broadcast(bytes(f'{nickname}out','utf-8'))

    
def broadcast(msg,nickname = ""):
    for conn in client:
        conn.sendall(bytes(nickname,'utf-8')+msg)


if __name__ == "__main__":
    HOST = ''
    PORT = 8000
    me = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    me.bind((HOST,PORT))
    me.listen(4)
    client = {}
    address = {}
    while True:
        conn,addr = me.accept()
        print(address,"建立连接")
        conn.send("你的名字：".encode("utf-8"))
        address[conn] = address
        print(address)
        Thread(target=handle_client_in,args=(conn,addr)).start()
    me.close()
