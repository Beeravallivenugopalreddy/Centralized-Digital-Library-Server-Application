import socket
import threading
PORT = 100
i=0
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created successfully')
s.bind(('Localhost', PORT))
print(f'Socket binded to port {PORT}')
s.listen()
print('Waiting for connection...')
def language(c):

    data = c.recv(1024).decode('utf-8')
    l = data.split(',',2)
    operation = l[0]
    
    if operation == 'english':
        lang = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        lang.connect(('Localhost',101))
        lang.send(data.encode())
        result = lang.recv(1024).decode()
        lang.close()
    elif operation == 'telugu':
        lang = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        lang.connect(('Localhost',102))
        lang.send(data.encode())
        result = lang.recv(1024).decode()
        lang.close()
    elif operation == 'hindi':
        lang = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        lang.connect(('Localhost',103))
        lang.send(data.encode())
        result = lang.recv(1024).decode()
        lang.close()
    c.send(str(result).encode('utf-8'))
    print("client disconnected\n")
    c.close()
    
while True:
    c,addr = s.accept()
    print("Client connected\n")
    thread = threading.Thread(target=language,args=(c,))
    thread.start()
    
    
            

