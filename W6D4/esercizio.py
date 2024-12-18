simple_list = ["rettangolo", "quadrato", "cerchio"]
area = 0

while True:
    figure_rimanenti = ", ".join(simple_list)
    figura = input("inserisci una figura tra le seguenti: " + figure_rimanenti + "\n")
    if figura in simple_list:
        break
    else:
        print("figura inserita non valida")

if figura == "rettangolo":
    base= int(input("inserisci la base: "))
    altezza= int(input("inserisci l'altezza: "))
    print("il perimetro del rettangolo è: ", base * 2 + altezza *2)
elif figura == "quadrato":
    lato= int(input("inserisci il lato: "))
    print("il perimetro del quadrato e: ", lato * 4)
elif figura == "cerchio":
    raggio= int(input("inserisci il raggio: "))
    print("il perimetro del cerchio e: ", 2 * 3.14 * raggio)


"""
simple_list = ["rettangolo", "quadrato", "cerchio"]
area = 0

while True:
    figure_rimanenti = ", ".join(simple_list)
    figura = input("inserisci una figura tra le seguenti: " + figure_rimanenti + "\n")
    if figura in simple_list:
        if area == 0:
            while True:
                lato= int(input("inserisci il lato: "))
                if lato > 0:
                    break
                else:
                    print("lato inserito non maggiore di 0")
        else:
            lato= area

        if figura == "rettangolo":
            perimetro = (lato * 2) + ((lato / 2) * 2)
            area = lato * (lato / 2)
            print("l'area del rettangolo è: ", area)
            print("il perimetro del rettangolo e: ", perimetro)
            simple_list.remove("rettangolo")
        elif figura == "quadrato":
            perimetro = lato * 4
            area = lato * lato
            print("l'area del quadrato è: ", area)
            print("il perimetro del quadrato e: ", perimetro)
            simple_list.remove("quadrato")
        elif figura == "cerchio":
            perimetro = 2 * 3.14 * lato
            area = lato**2 * 3.14
            print("l'area del cerchio è: ", area)
            print("il perimetro del cerchio e: ", perimetro)
            simple_list.remove("cerchio")
    else:
        print("figura inserita non valida")
        
    if not simple_list:
        break
"""


