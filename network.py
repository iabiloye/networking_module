"""
Author: Abiloye Iyanuoluwa John
Project: Network Connection
Module: Networking  
"""

# Importing the socket module for network communication
import socket
import threading

def start_server():
    """server that listens for one client connection."""
    # Define server host and port
    server_host = '127.0.0.1'  # Localhost (my computer)
    server_port = 8080         # Port number for connection

    # Create a socket object (IPv4, TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind server to the host and port
    server_socket.bind((server_host, server_port))

    # Start listening for incoming connections
    server_socket.listen(1)
    print(f"Server started on {server_host}:{server_port}, waiting for a connection...")

    # Accept one connection
    conn, addr = server_socket.accept()
    print(f"Connected to client at {addr}")

    # Receive message from client
    data = conn.recv(1024).decode()
    print("Message from client:", data)

    # Send reply back to client
    conn.send("Hello Client! Connection successful.".encode())

    # Close the connection
    conn.close()
    print("Server closed connection.")

# -----------------------------
# CLIENT CODE
# -----------------------------
def start_client():
    """Creates a simple client that connects to the server and sends a message."""
    client_host = '127.0.0.1'  # Server host (same as localhost)
    client_port = 8080         # Must match server port

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((client_host, client_port))

    # Send a message to the server
    client_socket.send("Hello Server!".encode())

    # Receive reply from server
    data = client_socket.recv(1024).decode()
    print("Reply from server:", data)

    # Close the connection
    client_socket.close()

# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    # Run server and client in separate threads so both run in same program
    server_thread = threading.Thread(target=start_server)
    client_thread = threading.Thread(target=start_client)

    # Start server first, then client
    server_thread.start()
    client_thread.start()

    # Wait for both to finish
    server_thread.join()
    client_thread.join()

    print("\nNetwork communication completed successfully.")
