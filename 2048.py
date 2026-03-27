# Auteur : Ruben ten Cate
# Version : 2.0
# Date : 03.03.2026
# Jeu 2048 en Python avec Tkinter

#Librairies
import tkinter as tk
from tkinter import messagebox
import os
import random as rand


# ---- 1. Configuration de la fenêtre principale tkinter ----

alpha = tk.Tk() # La fenêtre principale s'appelle alpha et non root 
alpha.title("Jeu 2048 - Ruben ten Cate") # Titre de la fenêtre principale
tk.background = "#252528" # Couleur de fond de la fenêtre principale
alpha.configure(bg=tk.background)
alpha.resizable(False, False) # Empêche la redimension de la fenêtre principale

# Titre du jeu dans la fenêtre principale
title_label = tk.Label(alpha, text="2048", font=("Helvetica", 48, "bold"), bg="#252528", fg="white")
title_label.pack(pady=10)

# Label pour afficher le meilleur score
best_score_label = tk.Label(alpha, text="Meilleur score : 0", font=("Helvetica", 16, "bold"), bg="#252528", fg="white")
best_score_label.pack(pady=5)

# ---- Sous‑titre (vide au début, s'affiche a la victoire) ----
win_label = tk.Label(alpha, text="", font=("Helvetica", 1, "bold"), bg="#252528", fg="white")
win_label.pack(pady=1)




## Ajout de mon icône personnalisée
icone = os.path.dirname(__file__) #.dirname(__file__) donne le chemin du dossier du script en cours
icon_path = os.path.join(icone, "assets", "letter_r.ico") # Construire le chemin complet de l'icône avec les variables ci-dessus
alpha.iconbitmap(icon_path) #Créer une icone personnalisée (fichier .ico) avec -iconbitmap comme attribut


# ----- Variables de configuration de la grille ----
grid_padding = 10 # Espacement entre les cellules en pixels
grid_size = 4 # Taille de la grille (4x4)


# --- 2. Grille logique du jeu ---

# Création d'un maquette de début, milieu et avancé du jeu pour voir l'affichage ensuite
game_start = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 0],
    [2, 0, 0, 0],
]

game_middle = [
    [2,   2,   32,   8],
    [32,  8,  8,   8],
    [256,   128, 32, 0],
    [512,   256,   16, 8],
]

game_advanced = [
    [512,   16,   0,   0],
    [32,  8,  4,   2],
    [2048,   128, 64, 256],
    [8192,   4096,   1024, 8],
]

game_2048 = [
    [512,   16,   0,   0],
    [32,  8,  4,   2],
    [1024,   1024, 64, 1024],
    [8192,   4096,   1024, 8],
]


# Grille Graphique (labels Tkinter)
labels_grid = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None]]

# Fonction de calcul de score :

def calculer_score_debut(grille):
    total = 0
    for row in range(grid_size):
        for col in range(grid_size):
            total += grille[row][col]
    return total

# Choix du tableau à afficher

game = game_start      # début du jeu
#game = game_middle    # milieu du jeu
#game = game_2048      # 2048 dans le jeu
#game = game_advanced  # fin du jeu

# Variable pour stocker le score du jeu
score = calculer_score_debut(game)

# Variable pour le meilleur score
best_score = 0

# Fonction pour mettre à jour l'affichage du meilleur score
def update_best_score_display():
    best_score_label.config(text=f"Meilleur score : {best_score}")

# Fonction pour recommencer la partie depuis le début
def new_game():
    global game, score, winner
    game = [
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0],
    ]
    score = calculer_score_debut(game)  # Score réinitialisé
    winner = False  # Si winner était sur True, c'est False à nouveau
    win_label.config(text="")  # Effacer le texte de victoire
    draw_game(game)
                    
# Afficher le score dans la fenêtre principale
def label_score():

    win_label.config(text=f"Score : {score}", font=("Helvetica", 30, "bold")) 
    win_label.pack_configure(pady=5) 

# Variables booleennes pour savoir si le jeu est gagné ou perdu.
winner = False

# ---- 3. Création d'un dictionnaire de couleur pour les blocs du jeu ----
colors = {
    0: "#252528", # Couleur de fond pour les cases vides
    2: "#FFEECC",
    4: "#FFEEDD",
    8: "#FFD9B0",
    16: "#FDAA60",
    32: "#FF8657", 
    64: "#FF7621",
    128: "#FF5900",
    256: "#FA3200",
    512: "#FF7480",
    1024: "#FF5160",
    2048: "#FF2C3F",
    4096: "#FF172C",
    8192: "#FF0004",
}

# Comme j'ai des couleurs de texte différentes je crée aussi un dictionnaire pour la couleur du texte

text_colors = {
    0: "#252528",
    2: "black",
    4: "black",
    8: "white",
    16: "white",
    32: "white",
    64: "white",
    128: "white",
    256: "white",
    512: "white",
    1024: "white",
    2048: "white",
    4096: "white",
    8192: "white",
}

# ---- 4. Fonctions pour le jeu ----

# 4.1 Fonction pour dessiner la grille du jeu à partir de la grille logique

def draw_game(game):
    for row in range(grid_size):
        for col in range(grid_size):
            value = game[row][col] #Va chercher les valeurs de la liste de listes
            font_color = text_colors.get(value, "white") # Récupère la couleur du texte à partir du dictionnaire, ou "white" par défaut
            labels_grid[row][col].configure(text=(value), bg=colors[value], fg=font_color) # Configure le label avec la valeur, la couleur de fond et la couleur du texte

# 4.2 Frame pour placer les blocs du jeu

grid_frame = tk.Frame(alpha, bg="#9B9B9B", relief="groove", padx=12, pady=12) 
grid_frame.pack(padx=10, pady=10) # Espacement entre la grille et les bords de la fenêtre


# 4.3 Définition de la fonction pack4 pour compresser les valeurs d'une ligne ou d'une colonne du jeu 2048

def pack4(a, b, c, d): 

    # Déplacement des mouvement vers la gauche
    
    # si c est égal à zéro, décalage de d vers c et mise à zéro de d
    if c == 0:
        c, d = d, 0

    # si b est égal à zéro, décalage de c vers b et de d vers c, et mise à zéro de d
    if b == 0:
        b, c, d = c, d, 0

    # si a est égal à zéro, décalage de b vers a, de c vers b et de d vers c, et mise à zéro de d
    if a == 0:    
        a, b, c, d = b, c, d, 0
    
    # si a est égal à b, a = 2*a, puis b est mis à zéro, puis on décale c vers b et d vers c, et mise à zéro de d
    if a == b:
        a, b, c, d = 2*a, c, d, 0

    # si b est égal à c, b =  c à zéro, puis on décale d vers c et mise à zéro de d
    if b == c:
        b, c, d = 2*b, d, 0
    
    # si c est égal à d, on les combine en doublant c et en mettant d à zéro
    if c == d:
        c, d = 2*c, 0

    return a, b, c, d # Retourne les valeurs compressées après le déplacement et la fusion des blocs selon les règles du jeu 2048
"""
print(pack4(0, 2, 4, 4))
print (pack4(2, 4, 4, 0))
print (pack4(2, 2, 2, 2))
print (pack4(0,0,0,2))
"""

# 4.4 Fonction pour générer une valeur aléatoire pour la nouvelle tuile (2 ou 4) / sprint 3
def valeur_tuile_aleatoire():
    rand_num = rand.randint(1, 100) # Génère un nombre aléatoire entre 1 et 100
    if rand_num <= 80: # 80% de chances d'obtenir une tuile de valeur 2
        return 2
    else: # 20% de chances d'obtenir une tuile de valeur 4
        return 4
    

# 4.5 Fonction nouvelle tuile / sprint 3
def new_tile():

    liste_Null = [] # Liste pour stocker les positions des cases vides (valeur 0) dans la grille
    
    # Parcours de la grille pour trouver les cases vides (valeur Null ou 0)
    for line in range (grid_size):
        for col in range (grid_size):
            
            # Si la case est vide (valeur 0), on ajoute sa position à la liste des cases vides
            if game[line][col] == 0:
                liste_Null.append((line, col)) # Créer un tuple des cases vides (ligne, colonne))
                
                
                # Si il n'y a pas de cases vides, on ne peut pas ajouter de nouvelle tuile
                if len(liste_Null) == 0: 
                    return
                
    # choix aléatoire d'une position parmi le tuple des cases vides
    line, col = rand.choice(liste_Null)
    # print("Position case vide choisi : :", (line, col)) #Affiche sur la console ou la case est ajoutée (débogage)

    # Choix aléatoire de la valeur de la nouvelle tuile (2 ou 4) avec la fonction valeur_tuile_aleatoire()
    new_tile_value = valeur_tuile_aleatoire()
    # print("valeur tuile aléatoire choisie : ", valeur_tuile_aleatoire())

    # Placer la nouvelle tuile dans la grille logique à la position choisie 
    game[line][col] = new_tile_value

    draw_game(game) # Mise à jour de la grille graphique 
    #print(f"nouvelle tuile ajoutée à la position ({line}, {col}), de valeur : {new_tile_value}")
    
    # Mise à jour du score total avec la nouvelle tuile
    global score
    score += new_tile_value
    label_score()
    #print("score du jeu :", score)

# Fonction pour checker si il y a une victoire

def did_i_win(game):
    global winner, best_score
    if score >= 2048 and winner == False: # si le score est plus petit ou égal à 2048 et que la variable winner est False
        for row in range(grid_size):
            for col in range(grid_size):
                if game [row][col] == 2048: # si il y a un 2048 dans le jeu
                    winner = True # La variable booleenne winner devient True

                    # Mettre à jour le meilleur score si nécessaire
                    if score > best_score:
                        best_score = score
                        update_best_score_display()

                    # Message box Tkinter
                    question = messagebox.askquestion(
                        "Victoire ! 2048 a été atteint",
                        "Veux-tu continuer la partie ?",
                    )
                    if question == "no":
                        alpha.destroy()
                    else : return


def did_i_lose(game):
    for row in range(grid_size):
        for col in range(grid_size):
            if game [row][col] == 0:
                return False
                
    # Recherche des jumaux horizontaux

    for row in range(grid_size): # Pour chaque ligne en range 3
        for col in range(grid_size -1): # Pour chaque colonne en range de 2 (pas 4) : 0, 1, 2 --> aide avec l'ia pour comprendre l'histoire du range
           if game [row][col] == game [row][col+1]:
                return False
           

    for col in range(grid_size): # Pour chaque ligne en range 3
        for row in range(grid_size -1): # Pour chaque colonne en range de 2 (pas 4) : 0, 1, 2 --> aide avec l'ia pour comprendre l'histoire du range
           if game [row][col] == game [row+1][col]:
                return False

   
    return True

# 4.6 Fonction pour traiter les touches du clavier et faire bouger les blocs du jeu
def key_pressed(event):
    touche = event.keysym
    mem_game = [ligne[:] for ligne in game] # Crée une copie de la grille actuelle pour comparer après le mouvement 
    if (touche == "Right" or touche == "d" or touche == "D"):
        droite()
    if (touche == "Left" or touche == "a" or touche == "A"):
        gauche()
    if (touche == "Up" or touche == "w" or touche == "W"):
        haut()
    if (touche == "Down" or touche == "s" or touche == "S"):
        bas()
    # print (game)
    # print (mem_game)

    # Si la grille a changé après le mouvement, on ajoute une nouvelle tuile avec la fonction new_tile()
    if mem_game != game:
        new_tile()

    # Appel de Fonction pour checker si on a gagné
    did_i_win(game)

    # Appel de Fonction pour chercher si on a perdu
    if did_i_lose(game) : # Le if est vrai avec True et va exécuter la suite
        
        # Mettre à jour le meilleur score si nécessaire
        global best_score
        if score > best_score:
            best_score = score
            update_best_score_display()
        
        # Message box Tkinter (askyesno) pour donner la possibilité de recommener
        recommencer = messagebox.askyesno(
            "Hah gros loser !",
            "Tu as perdu la partie. \nRecommencer ?"
        )
        if recommencer:
            new_game()
        else :
            alpha.destroy()

# -- 4.7 Fonctions pour compresser les valeurs dans la bonne direction --

# Fonction pour le bouton droite en intégrant pack4
def droite():
    for row in range(grid_size):
        game[row][3], game[row][2], game[row][1], game[row][0] = pack4(game[row][3], game[row][2], game[row][1], game[row][0])
    
    draw_game(game)


# Fonction pour le bouton gauche en intégrant pack4
def gauche():
    for row in range(grid_size):
        game[row][0], game[row][1], game[row][2], game[row][3] = pack4(game[row][0], game[row][1], game[row][2], game[row][3])
        
    draw_game(game)

    
#Fonction pour le bouton haut en intégrant pack4
def haut():
    
    for col in range(grid_size):
        game[0][col], game[1][col], game[2][col], game[3][col]  = pack4(game[0][col], game[1][col], game[2][col], game[3][col])
        
    draw_game(game)

#Fonction pour le bouton bas en intégrant pack4
def bas(): 
    for col in range(grid_size):
        game[3][col], game[2][col], game[1][col], game[0][col]= pack4(game[3][col], game[2][col], game[1][col], game[0][col])

    draw_game(game)


# ---- 5. Placement des labels dans la grille ----

for row in range(grid_size):
    for col in range(grid_size):
        labels_grid[row][col] = tk.Label(grid_frame, width=4, height=2,
            borderwidth=1, relief="ridge", font=("Helvetica", 24, "bold"))
        labels_grid[row][col].grid(row=row, column=col, padx=grid_padding, pady=grid_padding)


# --- Programme principal ---

# Initialiser l'affichage du meilleur score
update_best_score_display()

# traitement de touches à clavier et boucle 
alpha.bind('<Key>', key_pressed)

# Boucle pour dessiner la grille du jeu
draw_game(game)

# Boucle pour la fenêtre principale de Tkinter
alpha.mainloop()