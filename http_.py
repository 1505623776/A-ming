import socket

HOST,PORT = '',8005

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen(30)
print ('Serving HTTP on port %s' %PORT)
while True:
    conn,addr = socket.accept()
    reuest = conn.recv(1024)
    with open('/Users/huangrenming/Desktop/test.html','r') as http_response:
        data = http_response.read()
    response = """\
        HTTP/1.1 200 OK
        
        
        """
        
    conn.sendall(bytes(response,'utf-8'))
    conn.close()
    socket.close()