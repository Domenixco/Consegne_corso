import socket

SRV_ADDRS = "127.0.0.1"
SRV_PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

s.bind((SRV_ADDRS, SRV_PORT))

print("Sono in ascolto")

while True:

    data, address = s.recvfrom(1024)
    print(f"Pacchetto ricevuto (dimensione: {len(data)} byte): {data.decode()[:4]}...")
    if data:
        s.sendto(b"Messaggio ricevuto", address)