# Author : Ruben ten Cate
# Version : 1.0
# Date : 2024-06-01
# 2048 Game in Python using Tkinter

import tkinter as tk
import os

# ---- 1. Configuration de la fenêtre principale tkinter ----

alpha = tk.Tk() # La fenêtre principale s'appelle alpha et non root 
alpha.title("Jeu 2048") # Titre de la fenêtre principale
tk.background = "#252528" # Couleur de fond de la fenêtre principale
alpha.configure(bg=tk.background)

## Ajout de mon icône personnalisée
icone = os.path.dirname(__file__) #.dirname(__file__) donne le chemin du dossier du script en cours
icon_path = os.path.join(icone, "assets", "letter_r.ico") #Construire le chemin complet de l'icône avec les variables ci-dessus
alpha.iconbitmap(icon_path) #Créer une icone personnalisée (fichier .ico) avec -iconbitmap comme attribut

# ---- 2. Création d'un dictionnaire de couleur pour les blocs du jeu ----
colors = {
    2: "#FFFFFF",
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



# ----- Configuration de la grille ----
block_size = 100 # Taille de chaque cellule en pixels
grid_padding = 10 # Espacement entre les cellules en pixels
grid_size = 4 # Taille de la grille (4x4)
blocks = [] # La variable blocks est une liste (vide pour l'instant)

# Dénition de Frame pour la grille du jeu

grid_frame = tk.Frame(alpha, bg="#9B9B9B", relief="groove", width=400, height=400)
grid_frame.pack(padx=0, pady=0) # Espacement entre la grille et les bords de la fenêtre


# Fonction de la grille avec des frames pour chaque cellule
def structure_grid1():
    for row in range(grid_size):
        row_blocks = []
        for col in range(grid_size):
            block_frame = tk.Frame(
                grid_frame,
                bg="#CECECE",
                width=block_size,
                height=block_size
            )
            block_frame.grid(row=row, column=col, padx=grid_padding, pady=grid_padding)
            
            row_blocks.append(block_frame)
        blocks.append(row_blocks)

#Créer la grille dans tkinter avec frame
structure_grid1()

# --- Affichage du jeu (start, middle, advanced) ---

# Le tableau du début du jeu, une liste de listes, chaque ligne représente 4 colonnes
# les lignes sont dans une liste, et les colonnes dans la liste des lignes
# Création d'un maquette de début, milieu et avancé du jeu pour voir l'affichage ensuite
game_start = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 2],
]

game_middle = [
    [2,   0,   0,   0],
    [32,  8,  0,   2],
    [256,   128, 32, 0],
    [512,   256,   16, 8],
]

game_advanced = [
    [512,   16,   0,   0],
    [32,  8,  4,   2],
    [2048,   128, 64, 256],
    [8192,   4096,   1024, 8],
]

# Choix du tableau à afficher

#game = game_start       # début du jeu
game = game_middle    # milieu du jeu
#game = game_advanced

# Fonction pour afficher le début du jeu 

def draw_game(game):
    for row in range(grid_size):
        for col in range(grid_size):
            value = game[row][col] #Va chercher les valeurs de la liste de listes

            #--utilisation de chatgpt pour trouver comment écrire la suite de cette fonction...
            frame = blocks[row][col] #varaible frame construite selon les blocs prédéfinies

            #Condition : si la valeur est nulle, mettre la couleur de l'arrière plan sur défaut.
            if value == 0: 
                frame.configure(bg="#CECECE")
            # Sinon, remplir l'arrière plan selon la couleur et afficher la valeur case selon la liste de couleur
            else:
                frame.configure(bg=colors[value])  #configurer le frame selon la liste des couleurs établies
                
                label = tk.Label(   
                    frame,
                    text=str(value), # Mettre le chiffre dans le block
                    bg=colors[value],
                    fg=text_colors[value], # Foreground, c'est la couleur du texte, selon le dictionnaire de texte_colors
                    font=("Helvetica", 30, "bold")
                )
                label.place(relx=0.5, rely=0.5, anchor="center")



# cell_frame 
#     cell_frame = tk.Frame(
#         root,
#         bg="#cdc1b4",
#         width=cell_size,
#         height=cell_size
#     )
#     cell_frame.grid(row=row, column=col, padx=grid_padding, pady=grid_padding)

# Créer un grille de 4x4 avec des 0
# def create_grid():
#     for row in range(4):
#         for col in range(4):
#             print("0", end=" ")
#         print()

#Créer un grille de 4x4 avec variable
# def structure_grid():
#     for row in range(grid_size):
#         for col in range(grid_size):
#             print("0", end=" ")
#         print()


draw_game(game)

alpha.mainloop()



#def create_grid():
    #for row in range (grid_size):