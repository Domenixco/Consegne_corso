"""
lista_parole = []
lista_parole2 = []

while True:
    parola = input("Inserisci una parola (oppure 'fine' per terminare): ")
    while True:
        lista_parole2.append(len(parola))
        break 
    if parola.lower() == 'fine':
        break  
    
    lista_parole.append(parola)

print(f"le parole inserite sono{lista_parole}")

print(f"il numero delle parole inserite e {lista_parole2}")
"""

import random
import string

tipo_password = input("deve essere una password semplice o complessa?")
lunghezza = int(input("inserisci quanti numero deve essere la password(massimo 8 per la semplice minimo 20 per la complessa):"))
if tipo_password == "semplice":
    if lunghezza > 8:
        print("per favore inserisci un numero minore di 8")
    elif lunghezza < 8:
        stringa_casuale = ''.join(random.choices(string.ascii_letters + string.digits, k=lunghezza))
        print("Stringa casuale:", stringa_casuale)
elif tipo_password == "complessa":
    if lunghezza < 20:
        print("per favore inserisci un numero maggiore di 20")
    elif lunghezza > 20:
        stringa_casuale = ''.join(random.choices(string.ascii_letters + string.digits, k=lunghezza))
        print("Stringa casuale:", stringa_casuale)


