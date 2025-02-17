from resourceManaging import ResourceManager
import random

def initgame():
    resources = {
        'population': 500,
        'money': 1000000,
        'food': 2000,
        'wood': 300,
        'stone': 150,
        'basic_houses': 50,
        'income': resources['population'] / 5,
    }
    return resources

def data(resources):
   print(f"Voici les données de votre ville:\nPopulation: {resources['population']}\nMonnaie: {resources['money']}$\nNourriture: {resources['food']}kilos\nBois: {resources['wood']}unite\nPierre: {resources['stone']}unite\nNombre de maisons basiques: {resources['basic_houses']}\nRevenus: {resources['income']}$")
   action = input("Que voulez-vous faire ? (1) Construire un batiment (2) Aller à la boutique (3) Passer au tour suivant ")
   return action

answer = input("Bienvenue dans Metropolis 1800, je suis Patrick votre conseiller municipale, dans ce jeu vous devez bâtir une ville au Etats-Unis à la belle époque, gérez votre population, leur satisfaction et leurs besoins comme la nourriture, le logement, l'emploi. Le but? Devenir une grande métropole. Souhaitez-vous commencer? (oui/non) ")

if answer == "oui":
    resources = initgame()
    action = data(resources)

elif answer == "non":
    print("À une prochaine fois!")
    quit()
else:
    print("Réponse non reconnue.")
    quit()

if action == 1:
    if random.randint(1,2) == 1:
        input("Que voulez voulez vous construire (1) 5 Maisons basique, ce la coutera   ")
    else:
        input("Que voulez voulez vous construire (1)")

    

random.randint(1,2)