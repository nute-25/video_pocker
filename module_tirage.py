import random
# from module_questionbooleenne import *


def premier_tirage(deck: list):
    tirage = []
    for _ in range(5):
        carte = random.choice(deck)
        tirage.append(carte)
        deck.remove(carte)
    return tirage

# def choix_carte(tirage: list):
#     jeu = []
#     for carte in tirage:
#         if reponse_booleenne(f'Voulez-vous garder la carte {carte} ?'):
#             jeu.append(carte)
#     return jeu

def deuxieme_tirage(jeu: list, deck: list):
    tirage_final = jeu
    nbr_cartes = len(jeu)
    if nbr_cartes < 5:
        tirage_final += random.sample(deck, 5 - nbr_cartes)
    return tirage_final


# def machine():
#     deck2 = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

#     tirage1, deck2 = premier_tirage(deck2)
#     print('premier tirage', tirage1)
    
#     jeu = choix_carte(tirage1)
#     tirage_final = deuxieme_tirage(jeu, deck2)
#     print('deuxieme tirage', tirage_final)
#     return tirage_final