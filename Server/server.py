import socket
import rsa
import socketrsa as sr

HOST = '192.168.106.1'
PORT = 8989

sysPub , sysPriv = sr.loadKeys()
virPub = sr.virKey()

def conn_chat(a):
    conn, addr = a.accept()
    print('Connected by', addr)
    while True:
            data = conn.recv(1024)
            virCipher = data
            virMesg = rsa.decrypt(virCipher, sysPriv).decode('utf-8')
            print("Client : ",virMesg)

            text = input("Enter your message here : ")
            sysCipher = rsa.encrypt(text.encode('utf-8'), virPub)
            conn.sendall(sysCipher)
       

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn_chat(s)