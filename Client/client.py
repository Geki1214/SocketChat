import socket
import socketrsa as sr
import rsa

HOST = '192.168.106.1'
PORT = 8989

virPub, virPriv = sr.loadKeys()
sysPub = sr.sysKey()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        text=input("Enter your message here : ")
        virCipher= rsa.encrypt(text.encode('utf-8'), sysPub)
        s.sendall(virCipher)
        
        data = s.recv(1024)
        sysCipher = data
        sysMesg = rsa.decrypt(sysCipher, virPriv).decode('utf-8')
        print('Server : ',sysMesg)
        
# repr files to string
