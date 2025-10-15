import socket
import threading
from Funciones import repartir_cartas

HOST = '127.0.0.1'
PORT = 65432
clients = []

def manejar_cliente(conn, addr):
    print(f"Jugador conectado: {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"{addr}: {data}")
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Servidor esperando jugadores...")

    while len(clients) < 2:  # Ejemplo: 2 jugadores
        conn, addr = server.accept()
        clients.append(conn)
        threading.Thread(target=manejar_cliente, args=(conn, addr)).start()

    cartas = repartir_cartas(len(clients))
    for i, conn in enumerate(clients):
        conn.send(f"Tus cartas: {cartas[i]}".encode())

if __name__ == "__main__":
    main()
