import random

# liste de mots
mots_possibles = [
    "chat", "chien", "éléphant", "girafe", "lion", "tigre", "ours", "loup",
    "renard", "lapin", "souris", "cheval", "vache", "mouton", "cochon", "poule",
    "canard", "aigle", "hibou", "serpent", "tortue", "crocodile", "dauphin", "baleine",
    "requin", "poisson", "papillon", "abeille", "fourmi", "araignée", "grenouille",
   
    "pomme", "poire", "banane", "orange", "citron", "fraise", "cerise", "raisin",
    "melon", "pastèque", "ananas", "mangue", "kiwi", "pêche", "abricot", "prune",
    "tomate", "carotte", "pomme de terre", "salade", "chou", "haricot", "petit pois",
    "courgette", "aubergine", "poivron", "concombre", "radis", "navet", "poireau",
   
    "médecin", "infirmier", "professeur", "avocat", "ingénieur", "architecte",
    "boulanger", "pâtissier", "cuisinier", "serveur", "policier", "pompier",
    "menuisier", "plombier", "électricien", "jardinier", "fleuriste", "coiffeur",
    "pharmacien", "vétérinaire", "dentiste", "photographe", "journaliste", "écrivain",
    
    "table", "chaise", "lit", "armoire", "canapé", "lampe", "miroir", "horloge",
    "téléphone", "ordinateur", "télévision", "radio", "appareil", "livre", "cahier",
    "stylo", "crayon", "gomme", "règle", "ciseaux", "colle", "pinceau", "palette",
    "brosse", "peigne", "serviette", "couverture", "oreiller", "rideau", "tapis",
    
    "chemise", "pantalon", "jupe", "robe", "veste", "manteau", "pull", "tshirt",
    "chaussure", "botte", "sandale", "chaussette", "bonnet", "chapeau", "casquette",
    "écharpe", "gant", "ceinture", "cravate", "foulard", "lunettes", "montre",
    
    "pain", "fromage", "beurre", "lait", "yaourt", "chocolat", "gâteau", "biscuit",
    "confiture", "miel", "sucre", "sel", "poivre", "farine", "riz", "pâtes",
    "viande", "poulet", "jambon", "saucisse", "oeuf", "soupe", "salade", "sandwich",
    
    "arbre", "fleur", "herbe", "feuille", "branche", "racine", "forêt", "montagne",
    "rivière", "lac", "mer", "océan", "plage", "désert", "volcan", "cascade",
    "nuage", "pluie", "neige", "soleil", "lune", "étoile", "planète", "ciel",
    
    "appartement", "école", "hôpital", "bibliothèque", "musée", "cinéma",
    "restaurant", "café", "boulangerie", "supermarché", "banque", "poste", "gare",
    "aéroport", "port", "stade", "piscine", "parc", "jardin", "place", "rue",
    
    
    "voiture", "vélo", "moto", "bus", "train", "avion", "bateau", "navire",
    "camion", "tracteur", "hélicoptère", "fusée", "métro", "tramway", "scooter",
    
    
    "football", "basketball", "tennis", "natation", "cyclisme", "course", "danse",
    "musique", "guitare", "piano", "violon", "chant", "peinture", "dessin",
    "lecture", "cinéma", "théâtre", "voyage", "camping", "randonnée", "escalade",
    
    
    "tête", "cheveux", "oeil", "nez", "bouche", "oreille", "dent", "langue",
    "cou", "épaule", "bras", "main", "doigt", "poitrine", "ventre", "dos",
    "jambe", "genou", "pied", "orteil", "coeur", "poumon", "estomac", "cerveau",
    
    
    "rouge", "bleu", "vert", "jaune", "orange", "violet", "rose", "noir",
    "blanc", "gris", "marron", "cercle", "carré", "triangle", "rectangle",
    
    
    "grand", "petit", "gros", "mince", "long", "court", "haut", "bas",
    "rapide", "lent", "fort", "faible", "chaud", "froid", "nouveau", "vieux",
    "jeune", "ancien", "moderne", "beau", "joli", "laid", "bon", "mauvais",
   
    "manger", "boire", "dormir", "marcher", "courir", "sauter", "danser", "chanter",
    "parler", "écouter", "regarder", "lire", "écrire", "dessiner", "jouer", "travailler",
    "étudier", "apprendre", "enseigner", "voyager", "conduire", "nager", "voler",
    
    "amour", "bonheur", "joie", "tristesse", "colère", "peur", "surprise", "rêve",
    "temps", "jour", "nuit", "matin", "soir", "semaine", "mois", "année",
    "printemps", "été", "automne", "hiver", "famille", "ami", "voisin", "enfant",
    "adulte", "personne", "monde", "pays", "ville", "village", "histoire", "aventure"
]

mot = random.choice(mots_possibles).lower()

affichage = ["_"] * len(mot)
erreurs = 0
lettres_devinees = []
max_erreurs = 6

pendu = [
"""
 -----
 |   |
     |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
-|   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
-|-  |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
-|-  |
|    |
     |
=========
""",
"""
 -----
 |   |
 O   |
-|-  |
| |  |
     |
=========
"""
]

print("=== JEU DU PENDU ===\n")
print("Devine le mot lettre par lettre !")
print("Tu as droit à 6 erreurs maximum.\n")

while True:
    print(pendu[erreurs])
    print("\nMot à deviner :", " ".join(affichage))
    print("Lettres déjà essayées :", ", ".join(sorted(lettres_devinees)) if lettres_devinees else "Aucune")
    print(f"Erreurs : {erreurs}/{max_erreurs}")

    lettre = input("\nDevine une lettre : ").lower()

    # Validation de l'entrée
    if len(lettre) != 1 or not lettre.isalpha():
        print("Entre une seule lettre valide !\n")
        continue

    if lettre in lettres_devinees:
        print("Tu as déjà essayé cette lettre !\n")
        continue

    lettres_devinees.append(lettre)

    if lettre in mot:
        for i, l in enumerate(mot):
            if l == lettre:
                affichage[i] = lettre
        print("Bien joué !\n")
    else:
        erreurs += 1
        print("Mauvaise lettre...\n")

    if "_" not in affichage:
        print("=" * 40)
        print("FÉLICITATIONS ! Tu as trouvé le mot :", mot.upper())
        print("=" * 40)
        break
    
    if erreurs >= max_erreurs:
        print(pendu[erreurs])
        print("=" * 40)
        print("PERDU ! Le mot était :", mot.upper())
        print("=" * 40)
        break
