import socket
import uuid

SERVER_IP = "127.0.0.1"
PORT = 5000

def iniciar_cliente():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))

    print("Conectado al servidor DNS")

    while True:
        opcion = input("Escribe 'query', 'add' o 'salir': ").lower()
        if opcion == "salir":
            break

        consulta_id = str(uuid.uuid4())[:8]

        if opcion == "query":
            nombre = input("Introduce el nombre a resolver: ")
            mensaje = f"{consulta_id} QUERY {nombre}"
        elif opcion == "add":
            nombre = input("Nombre a agregar: ")
            ip = input("IP del nombre: ")
            ttl = input("TTL en segundos: ")
            mensaje = f"{consulta_id} ADD {nombre} {ip} {ttl}"
        else:
            print("Opción no válida")
            continue

        client.sendall((mensaje + "\r\n").encode())
        respuesta = client.recv(1024).decode().strip()
        print("Respuesta:", respuesta)

    client.close()

if __name__ == "__main__":
    iniciar_cliente()
