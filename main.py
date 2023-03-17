import socket

# configuration du serveur
HOST = 'localhost'
PORT = 8080

# Création du socket et liaison au port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# écoute de nouvelles connexions entrantes
s.listen()

print(f"Serveur en attente de connexion sur le port {PORT}...")

# accepte une nouvelle connexion entrante
conn, addr = s.accept()
print(f"Connexion établie depuis {addr[0]}:{addr[1]}")

while True:
    # attendre un message de l'utilisateur connecté
    data = conn.recv(1024)
    if not data:
        break

    # afficher le message reçu
    print(f"Message reçu: {data.decode('utf-8')}")

    # envoyer un message de réponse à l'utilisateur connecté
    response = "Message reçu"
    conn.sendall(response.encode('utf-8'))

# fermer la connexion
conn.close()
