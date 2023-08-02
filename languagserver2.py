import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
s.bind(('Localhost', 102))
s.listen()
print('Waiting for connection...')
def handle_client(lan):
    data = lan.recv(1024).decode('utf-8')
    l = data.split(',',2)
    operation = l[1]
    
    if operation == 'horror':
        gen = socket.socket()
        gen.connect(('Localhost',107))
        gen.send(data.encode())
        result = gen.recv(1024).decode()
        gen.close()

    elif operation == 'detective':
        gen = socket.socket()
        gen.connect(('Localhost',108))
        gen.send(data.encode())
        result = gen.recv(1024).decode()
        gen.close()
    
    elif operation == 'technical':
        gen = socket.socket()
        gen.connect(('Localhost',109))
        gen.send(data.encode())
        result = gen.recv(1024).decode()
        gen.close()
        
    lan.send(str(result).encode('utf-8'))
    print("client disconnected")
    lan.close()


    
while True:
    lan, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(lan,))
    thread.start()
    print("Client connected")
    
    
            


