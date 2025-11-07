

import socket
import threading

def start_server():
    
    server_host = '127.0.0.1'  # Localhost (my computer)
    server_port = 8080        

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((server_host, server_port))

    server_socket.listen(1)
    print(f"Server started on {server_host}:{server_port}, waiting for a connection...")

    conn, addr = server_socket.accept()
    print(f"Connected to client at {addr}")

    data = conn.recv(1024).decode()
    print("Message from client:", data)

    conn.send("Hello Client! Connection successful.".encode())

    conn.close()
    print("Server closed connection.")


def start_client():
    """Creates a simple client that connects to the server and sends a message."""
    client_host = '127.0.0.1'  # Server host (same as localhost)
    client_port = 8080         # Must match server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((client_host, client_port))

    client_socket.send("Hello Server!".encode())

    data = client_socket.recv(1024).decode()
    print("Reply from server:", data)

    client_socket.close()

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    client_thread = threading.Thread(target=start_client)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()

    print("\nNetwork communication completed successfully.")
