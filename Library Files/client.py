import socket
c = socket.socket()
c.connect(('Localhost',100))
print("Languages of books available are\n1.english\n2.telugu\n3.hindi\n")
print("Types of books available are\n1.horror\n2.detective\n3.technical\n")
a = input('Enter language of the book required\n')
b = input('Enter type of book required\n')
l = str(a)+','+str(b)
print(l)
c.send(l.encode())
# result = c.recv(1024).decode()
# print('result = ',result)
f=open('clientrequired.txt','w')
l=c.recv(1024).decode()
size=0
while l:
    f.write(l)
    print('file size =',len(l)/1024,'kb downloaded ')
    size+=len(l)
    l=c.recv(1024).decode()
    p=l.split(',',2)
    
    if p[0]=='' or p[1]=='End of SERVICE':
        f.write(l)
        print('file size =',len(l)/1024,'kb downloaded ')
        size+=len(l)
        f.close()
        break
print('Total file size :',size/1024 ,'kb downloaded')
print('file downloaded successfully')
c.close()
