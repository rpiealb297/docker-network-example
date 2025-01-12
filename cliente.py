import sys
import socket

# Configuración del cliente
HOST = 'servidor'  # Nombre del contenedor del servidor
PORT = 2025        # Puerto de conexión

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Conectado a {HOST}:{PORT}")
        message = input("Escribe un mensaje para enviar: ")
        s.sendall(message.encode('utf-8'))

if __name__ == "__main__":
    main()

