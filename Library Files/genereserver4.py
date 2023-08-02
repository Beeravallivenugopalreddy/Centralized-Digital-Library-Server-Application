import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
s.bind(('Localhost', 107))
s.listen()
print('Waiting for connection...')
while True:
    gen,addr = s.accept()
    print("Client connected")
    data = gen.recv(1024).decode('utf-8')
    if not data:
        break
    l = data.split(',',2)
    operation = l[1]
    if operation == 'horror':
        f=open('hindihorror.txt','r')
        p=f.read(1024)
        while(p):
            gen.send(p.encode())
            p=f.read(1024)
        print('file sent successfuly')
        f.close()
        print("client disconnected")
        gen.close()
    else:
        quit
