import tkinter as tk #pour importer une fenêtre
import requests  # Permet d'envoyer des requêtes HTTP en utilisant Python.


def converti():
    # Pour récupérer le taux de change actuel entre l'euro et le dollar
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    response = requests.get(url)
    data = response.json()
    exchange = data["rates"]["USD"]

    # Pour récupérer la valeur saisie par l'utilisateur et la convertir
    original = float(amount_entry.get())
    converted = original * exchange

    #  Pour afficher la valeur convertie
    result_label.config(text=f"{converted:.2f} USD")
    
    # Pour sauvegarder automatiquement l'historique de la convertion
    test = open("test.txt","a")
    test.write(f"{converted:.2f} USD\n")
    test.close()

# Pour Créer une fenêtre tkinter
windows = tk.Tk()
windows.title("Convertisseur euro/dollar")
windows.geometry('320x420')


# Pour créer un champ pour saisir la valeur à convertir
amount_entry = tk.Entry(windows)
amount_entry.pack()

# Pour créer un bouton pour lancer la conversion
converti_button = tk.Button(windows, text="Convertir", command=converti)
converti_button.pack()

# Pour créer un label pour afficher le résultat
result_label = tk.Label(windows, text="")
result_label.pack()

# Démarrer la boucle tkinter
windows.mainloop()





