import random

numero_random = random.randint(1, 100)
tentativi = 0

while True:
    try:
        numero_inserito = int(input("Inserisci un numero da 1 a 100 da indovinare>> "))
        tentativi += 1
        if 1 <= numero_inserito <= 100:
            if numero_inserito == numero_random:
                print(f"Hai indovinato al {tentativi}° tentativo, congratulazioni!")
                break
            elif numero_inserito > numero_random:
                print("Il numero è troppo alto! Ritenta")
            elif numero_inserito < numero_random:
                print("Il numero è troppo basso! Ritenta")
        else:
            print("Ehi, ricordati di inserire un numero da 1 a 100!")

    except ValueError:
        print("Input non valido, per favore inserisci un numero!")
        continue