import tkinter as tk
import random as rd

def echange_pos(b):

    # récupère les informations de placement des widgets
    pos1 = bouton0.grid_info()
    pos2 = b.grid_info()
    
    # échange les positions des widgets
    bouton0.grid(row=pos2['row'], column=pos2['column'])
    b.grid(row=pos1['row'], column=pos1['column'])



fen = tk.Tk()
fen.title("Jeu taquin")

pos = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]

for i in range(8):
    row, column = rd.choice(pos)
    pos.remove((row, column))  # Enlever la position choisie de la liste des positions restantes
    bouton = tk.Button(fen, bg = "dark goldenrod", text=f"{i+1}", anchor = "center", height = 3, width = 7, font = ("helvitica", "20"))
    bouton.grid(row=row, column=column)
    bouton.config(command=lambda b=bouton: echange_pos(b))

bouton0 = tk.Button(fen, bg = "olive drab", text = "0", anchor = "center", height = 3, width = 7, font = ("helvitica", "20"))
bouton0.grid(row = 2, column = 2)

fen.mainloop()