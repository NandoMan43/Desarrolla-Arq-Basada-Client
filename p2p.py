import socket
import threading

HOST = '127.0.0.1'
PORT = 5002

def handle_receive(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        while True:
            msg = conn.recv(1024).decode('utf-8')
            if not msg:
                print(f"[DISCONNECTED] {addr} disconnected.")
                break
            print(f"[{addr}] {msg}")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()

def send_message(peer_socket):
    try:
        while True:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                print("[EXITING] Closing connection...")
                break
            peer_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        peer_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    try:
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_receive, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        server_socket.close()

def connect_to_peer(peer_host, peer_port):
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        peer_socket.connect((peer_host, peer_port))
        print(f"[CONNECTED] Connected to peer at {peer_host}:{peer_port}")

        thread_receive = threading.Thread(target=handle_receive, args=(peer_socket, (peer_host, peer_port)))
        thread_receive.start()

        thread_send = threading.Thread(target=send_message, args=(peer_socket,))
        thread_send.start()
    except Exception as e:
        print(f"[ERROR] Unable to connect to peer: {e}")
    finally:
        peer_socket.close()

def start_p2p():
    print("Welcome to the P2P network!")
    mode = input("Do you want to start a server (s) or connect to a peer (c)? ")

    if mode == 's':
        start_server()
    elif mode == 'c':
        peer_host = input("Enter peer's IP: ")
        peer_port = int(input("Enter peer's Port: "))
        connect_to_peer(peer_host, peer_port)
    else:
        print("Invalid option. Exiting.")

if __name__ == "__main__":
    start_p2p()
