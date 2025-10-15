import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024).decode()
        if not data:
            break
        print(data)
        mensaje = input("Tu jugada: ")
        s.send(mensaje.encode())
