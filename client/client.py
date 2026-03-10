import socket

SERVER_IP = "127.0.0.1"
PORT = 5000

def iniciar_cliente():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))

    print("Conectado al servidor DNS")

    while True:
        mensaje = input("Introduce consulta: ")

        client.sendall((mensaje + "\n").encode())

        respuesta = client.recv(1024).decode()

        print("Respuesta:", respuesta)

if __name__ == "__main__":
    iniciar_cliente()
