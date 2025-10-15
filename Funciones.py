import random

PALOS = ['♠', '♥', '♦', '♣']
VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def crear_baraja():
    return [v + p for p in PALOS for v in VALORES]

def repartir_cartas(num_jugadores):
    baraja = crear_baraja()
    random.shuffle(baraja)
    return [baraja[i*2:(i+1)*2] for i in range(num_jugadores)]
