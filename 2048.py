# Auteur : Ruben ten Cate
# Version : 2.0
# Date : 03.03.2026
# Jeu 2048 en Python avec Tkinter

#Librairies
import tkinter as tk
import os

# ---- 1. Configuration de la fenêtre principale tkinter ----

alpha = tk.Tk() # La fenêtre principale s'appelle alpha et non root 
alpha.title("Jeu 2048 - Ruben ten Cate") # Titre de la fenêtre principale
tk.background = "#252528" # Couleur de fond de la fenêtre principale
alpha.configure(bg=tk.background)
alpha.resizable(False, False) # Empêche la redimension de la fenêtre principale

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
    [0, 0, 0, 2],
]

game_middle = [
    [2,   0,   32,   8],
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

# Grille Graphique (labels Tkinter)
labels_grid = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None]]

# Choix du tableau à afficher

#game = game_start      # début du jeu
game = game_middle      # milieu du jeu
#game = game_advanced   # fin du jeu


# ---- 3. Création d'un dictionnaire de couleur pour les blocs du jeu ----
colors = {
    0: "white", # Couleur de fond pour les cases vides
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
    counter = 0
    if c == 0:
        c, d = d, 0
        counter +=1
        print(counter)
    if b == 0:
        b, c, d = c, d, 0
        counter +=1
    if a == 0:
        a, b, c, d = b, c, d, 0
        counter +=1
    
    if a == b:
        a, b, c, d = 2*a, c, d, 0
        counter +=1

    if b == c:
        b, c, d = 2*b, d, 0
        counter +=1
    
    if c == d:
        c, d = 2*c, 0
        counter +=1
    print(counter)    
    return a, b, c, d,counter
"""
print(pack4(0, 2, 4, 4))
print (pack4(2, 4, 4, 0))
print (pack4(2, 2, 2, 2))
print (pack4(0,0,0,2))
"""
# 4.4 Fonction pour traiter les touches du clavier et faire bouger les blocs du jeu

def key_pressed(event):
    touche = event.keysym
    if (touche == "Right" or touche == "d" or touche == "D"):
        droite()
    if (touche == "Left" or touche == "a" or touche == "A"):
        gauche()
    if (touche == "Up" or touche == "w" or touche == "W"):
        haut()
    if (touche == "Down" or touche == "s" or touche == "S"):
        bas()
    if (touche == "Q" or touche == "q"):
        alpha.quit()

def droite():
    moves = 0
    for row in range(grid_size):
        game[row][3], game[row][2], game[row][1], game[row][0], counter = pack4(game[row][3], game[row][2], game[row][1], game[row][0])
        moves += counter
    draw_game(game)
    print(f"Vous avez pressé la touche droite. Compteur: {moves}")

def gauche():
    moves = 0
    for row in range(grid_size):
        game[row][0], game[row][1], game[row][2], game[row][3], counter = pack4(game[row][0], game[row][1], game[row][2], game[row][3])
        moves += counter
    draw_game(game)
    print(f"Vous avez pressé la touche gauche. Compteur: {moves}")

def haut():
    moves = 0
    for col in range(grid_size):
        game[0][col], game[1][col], game[2][col], game[3][col], counter  = pack4(game[0][col], game[1][col], game[2][col], game[3][col])
        moves += counter
    draw_game(game)
    print(f"Vous avez pressé la touche haut. Compteur: {moves}")

def bas(): 
    moves = 0
    for col in range(grid_size):
        game[3][col], game[2][col], game[1][col], game[0][col], counter= pack4(game[3][col], game[2][col], game[1][col], game[0][col])
        moves += counter
    draw_game(game)
    print(f"Vous avez pressé la touche bas. Compteur: {moves}")

# 4.5 Fonction pour ajouter une nouvelle tuile (2 ou 4) à une position aléatoire de la grille après chaque mouvement (à implémenter dans le sprint 3...)

# ---- 5. Placement des labels dans la grille ----

for row in range(grid_size):
    for col in range(grid_size):
        labels_grid[row][col] = tk.Label(grid_frame, width=4, height=2,
            borderwidth=1, relief="ridge", font=("Helvetica", 24, "bold"))
        labels_grid[row][col].grid(row=row, column=col, padx=grid_padding, pady=grid_padding)




# --- Programme principal ---

# traitement de touches à clavier et boucle 
alpha.bind('<Key>', key_pressed)

# Boucle pour dessiner la grille du jeu
draw_game(game)

# Boucle pour la fenêtre principale de Tkinter
alpha.mainloop()