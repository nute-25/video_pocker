from flask import Flask, session, render_template, request
from module_tirage import premier_tirage, deuxieme_tirage
from module_gain import partie
import random

app = Flask(__name__)
app.secret_key = "MySecretKey"
deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/premier_tirage', methods=['POST'])
def init():
    pseudo = request.form['pseudo']
    session['bankroll'] = int(request.form['cagnotte'])
    session['mise'] = int(request.form['mise'])
    tirage, new_deck = premier_tirage(deck)
    return render_template('premier_tirage.html', tirage = tirage, cagnotte = session['bankroll'])

@app.route('/deuxieme_tirage', methods=['POST'])
def jeu_final():
    # choix des cartes
    jeu = []
    for key in request.form:
        jeu.append(key)
    tirage_final = deuxieme_tirage(jeu, deck)

    # decomposition du jeu final, test des combinaisons et calcul des gains
    combinaison, resultat, cagnotte = partie(tirage_final, session['mise'],session['bankroll'])

    return render_template(
        'second_tirage.html', 
        tirage = tirage_final, combinaison = combinaison, resultat = resultat, cagnotte = cagnotte
    )




# def mise_possible(bankroll: int, mise: int):
#     while not(bankroll >= mise > 0):
#         mise = int(input("La mise doit être inférieure ou égale à votre cagnotte, merci de modifier votre mise : "))
#     return mise

# mise = mise_possible(bankroll, mise)
# print(mise)

# while bankroll - mise >= 0:
#     resultat, bankroll = partie(mise, bankroll)
#     print(resultat)
#     print(f'Il reste {bankroll}€ dans votre cagnotte')
#     if bankroll == 0:
#         print('C\'est perdu...')
#         break
#     else:
#         if reponse_booleenne('Voulez-vous continuer à jouer ?'):
#             mise = int(input("Faites vos jeux : "))
#             mise = mise_possible(bankroll, mise)
#         else:
#             print(f'Vous récuperez {bankroll}€, bien joué !')
#             break

if __name__ == "__main__":
    app.run(debug=True)