#!/usr/bin/env python3
# coding: utf-8
#
# Ejemplo para imprimir dos manos de cinco cartas

import requests

PALOS={
  "SPADES": "\u2660", 
  "HEARTS": "\u2661", 
  "DIAMONDS": "\u2662", 
  "CLUBS": "\u2663"
}

CARTAS={
    "2": "Dos",
    "3": "Tres",
    "4": "Cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve",
    "10": "Diez",
    "JACK": "Jota",
    "QUEEN": "Reina",
    "KING": "Rey",
    "ACE": "As"
}

mazo=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()["deck_id"]
mano1=[ CARTAS[card["value"]]+" de "+PALOS[card["suit"]] for card in requests.get("https://deckofcardsapi.com/api/deck/"+mazo+"/draw/?count=5").json()["cards"] ]
mano2=[ CARTAS[card["value"]]+" de "+PALOS[card["suit"]] for card in requests.get("https://deckofcardsapi.com/api/deck/"+mazo+"/draw/?count=5").json()["cards"] ]

print("Primera mano:",", ".join(mano1))
print("Segunda mano:",", ".join(mano2))
