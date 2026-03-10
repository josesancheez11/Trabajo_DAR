import socket
import threading
from protocol import procesar_mensaje
from cache import limpiar_cache

HOST = "0.0.0.0"
PORT = 5000

def manejar_cliente(conn, addr):
    print(f"Cliente conectado: {addr}")

    try:
        while True:
            data = conn.recv(1024)

            if not data:
                break

            mensaje = data.decode()
            print("Recibido:", mensaje)

            respuesta = procesar_mensaje(mensaje)

            conn.sendall((respuesta + "\n").encode())

    finally:
        conn.close()
        print(f"Cliente desconectado: {addr}")

def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Servidor DNS escuchando en puerto", PORT)

    while True:
        limpiar_cache()

        conn, addr = server.accept()

        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
        hilo.start()

if __name__ == "__main__":
    iniciar_servidor()   hilo.start()

if __name__ == "__main__":
    iniciar_servidor()
