# def structure_grid():
#     for row in range(grid_size):
#         for col in range(grid_size):
#             print("0", end=" ")
#         print()

# Fonction de la grille avec des frames pour chaque cellule

from cProfile import label
import tkinter as tk

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


root = tk.Tk()
root.title("Exemple Label")
root.geometry("300x100")

#2. Créer le label
def label_use(row, col):
    label = tk.Label(root,
                    text= "2",
                    font= ("Helvetica", 24, "bold"),
                    fg= text_colors[2], # Utilisation de la couleur pour le texte du label
                    bg= colors[2], # Utilisation de la couleur pour le fond du label
                    width=4, #largeur caractères max
                    height=2, #hauteur en nombre de lignes
                    padx=5, #espacement horizontal
                    pady=5, #espacement vertical   
                    borderwidth=2,
                    relief="groove")
    label.grid(row=row, column=col)

for row in range(4):
    for col in range(4):
        label_use(row, col)
    

# 3. Afficher le label

# 4. Lancer la boucle principale
root.mainloop()

# print (4)

# for row in range(4):
#     for col in range(4):
#         print(0, end="")
#     print()
    
# Label tkinter


# For est une boucle qui permet de répéter une action un certain nombre de fois.
# je dis, pour i dan la page de 0, 1, 2, 3 for in in range (4)
# Et ensuite, pour j dans la plage de 0, 1, 2, 3

