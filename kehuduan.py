import socket
from tkinter import *
from threading import Thread


def main():
    HOST = '192.168.1.102'
    PORT = 8000
    global me
    me = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    me.connect((HOST,PORT))
    rec = Thread(target=get_msg)
    rec.start()

def get_msg():
    while True:
        try:
            msg = me.recv(1024).decode("utf-8")
            text_message.insert(END,msg)
        except:
            break
def send():
    send_msg  = text_input.get('0.0',END)
    me.sendall(bytes(send_msg,'utf-8'))
    text_input.delete('0.0',END)

if __name__ == "__main__":
    root = Tk()
    root.title("044031专用无内鬼聊天室")
    message_frame = Frame(width = 400,height = 300)
    text_frame = Frame(width = 400, height = 100)
    send_frame = Frame(width = 400,height = 30)
    text_message = Text(message_frame,backgroun="white",state = 'normal')
    text_input = Text(text_frame)
    text_send = Button(send_frame,text = 'send',command = send)
    message_frame.grid(row = 0,column = 0,padx = 3,pady = 6)
    text_frame.grid(row = 1,column = 0)
    send_frame.grid(row = 2,column = 0)
    text_message.grid()
    text_input.grid()
    text_send.grid()
    main() 
    root.mainloop()
    