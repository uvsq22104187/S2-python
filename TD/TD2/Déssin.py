import tkinter as tk

def disque():
    canvas.create_oval((50,50), (150,150), fill="blue", width=5)

def carré():
    canvas.create_rectangle((200,50), (300,150), fill="red", width=5)

def croix():
    canvas.create_rectangle((200,200), (230,300), fill="green")
    canvas.create_rectangle((165,235), (265,265), fill="green")

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Dessin")

bt = tk.Button(racine, text="choisir une couleur", font = ("helvetica", "10")) # création du widget
bt.grid(row=0, column=1) # positionnement du widget

bt = tk.Button(racine, text="Cercle", font = ("helvetica", "10"), command = disque) # création du widget
bt.grid(row=1, column=0) # positionnement du widget

bt = tk.Button(racine, text="Carré", font = ("helvetica", "10"), command = carré) # création du widget
bt.grid(row=2, column=0) # positionnement du widget

bt = tk.Button(racine, text="Croix", font = ("helvetica", "10"), command = croix) # création du widget
bt.grid(row=3, column=0) # positionnement du widget

canvas = tk.Canvas(racine, bg="black", height=500, width=500, relief = "groove" , borderwidth = 10)
canvas.grid(row=1, column=1, rowspan= 3)


racine.mainloop() # Lancement de la boucle principale