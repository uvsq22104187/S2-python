import tkinter as tk
import random

def exchange_positions(widget1, widget2):
    global selected_button
    # récupère les informations de placement des widgets
    pos1 = widget1.grid_info()
    pos2 = widget2.grid_info()
    
    # échange les positions des widgets
    widget1.grid(row=pos2['row'], column=pos2['column'])
    widget2.grid(row=pos1['row'], column=pos1['column'])
    
    # réinitialise la sélection de bouton
    selected_button = None

root = tk.Tk()

# Créer 16 boutons et les placer aléatoirement
buttons = [tk.Button(root, text="{}".format(i+1), bg = "brown", anchor = "center", height = 1 , width = 3 ,
                       font = ("helvetica", "35")) for i in range(15)]
random.shuffle(buttons)
for i, button in enumerate(buttons):
    button.grid(row=i // 4, column=i % 4)


# Placer le 16ème bouton à la position (3,3)
button16 = tk.Button(root, text="", bg = "white", anchor = "center", height = 1 , width = 3 ,
                       font = ("helvetica", "35"))
button16.grid(row=3, column=3)

# Définir une fonction de clic pour les boutons
def button_click(widget):
    global selected_button
    
    if selected_button is None:
        # Si aucun bouton n'a été sélectionné auparavant
        selected_button = widget
    else:
        # Si un bouton a déjà été sélectionné
        exchange_positions(selected_button, widget)
    
# Configurer la commande de clic pour chaque bouton
for button in buttons + [button16]:
    button.config(command=lambda b=button: button_click(b))

selected_button = None

root.mainloop()