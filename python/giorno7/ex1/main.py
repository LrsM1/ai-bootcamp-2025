import random
import datetime
import time

import json


HIGH_SCORE_FILE = "high_score.json"

def carica_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salva_high_score(records):
       with open(HIGH_SCORE_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

def gioca():
    numero_random = random.randint(1, 100)
    tentativi = 0
    start_game = time.time()

    while True:
        try:
            numero_inserito = int(input("Inserisci un numero da 1 a 100 da indovinare>> "))
            tentativi += 1
            if 1 <= numero_inserito <= 100:
                if numero_inserito == numero_random:
                    end_game = time.time()
                    time_score = round(end_game - start_game, 2)
                    print(f"Hai indovinato al {tentativi}° tentativo, congratulazioni!")
                    return tentativi, time_score
                elif numero_inserito > numero_random:
                    print("Il numero è troppo alto! Ritenta")
                elif numero_inserito < numero_random:
                    print("Il numero è troppo basso! Ritenta")
            else:
                print("Ehi, ricordati di inserire un numero da 1 a 100!")

        except ValueError:
            print("Input non valido, per favore inserisci un numero!")
            continue

def main():
    high_scores = carica_high_score()
    while True:
        nome = input("Inserisci il tuo nome: ")
        tentativi, time_score = gioca()

        if not high_scores or tentativi < high_scores[0]["attempts"]:
            nuovo_record = {
                "name": nome,
                "attempts": tentativi,
                "timestamp": datetime.datetime.now().isoformat(),
                "duration": time_score
            }
            high_scores.append(nuovo_record)
            high_scores.sort(key=lambda x: x["attempts"])
            salva_high_score(high_scores)

        risposta = input("Vuoi continuare a giocare? (y/n): ").lower()
        if risposta != 'y':
            print("E' stato un piacere giocare con te! Arrivederci!")
            break

    print("High Scores:")
    for record in high_scores:
        print(f"Giocatore: {record['name']}, Tentativi: {record['attempts']}, Tempo: {record['duration']}s, Data: {record['timestamp']}")

if __name__ == "__main__":
    main()