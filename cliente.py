import socket
import threading

def handle_receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
            else:
                break
        except Exception as e:
            print(f"[ERROR] {e}")
            break
    client_socket.close()

def send_message(server_socket):
    while True:
        message = input("Enter message to send: ")
        server_socket.send(message.encode('utf-8'))

def start_client():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5002))  # Escuchar en el puerto 5002
    server_socket.listen(1)  # Permitir una conexión

    print("Waiting for a connection...")
    client_socket, addr = server_socket.accept()  # Aceptar la conexión
    print(f"Connection established with {addr}")

    # Crear hilos para enviar y recibir mensajes
    thread_receive = threading.Thread(target=handle_receive, args=(client_socket,))
    thread_receive.start()

    send_message(client_socket)

if __name__ == "__main__":
    start_client()
