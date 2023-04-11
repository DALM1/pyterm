import socket


HOST = 'localhost'
PORT = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


s.listen()

print(f"Serveur en attente de connexion sur le port {PORT}...")


conn, addr = s.accept()
print(f"Connexion établie depuis {addr[0]}:{addr[1]}")

while True:
   
    data = conn.recv(1024)
    if not data:
        break

    
    print(f"Message reçu: {data.decode('utf-8')}")

    
    response = "Message reçu"
    conn.sendall(response.encode('utf-8'))


conn.close()
