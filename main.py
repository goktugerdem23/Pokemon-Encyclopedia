import tkinter.font
from tkinter import *
import requests
from tkinter import PhotoImage
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name" : pokemon_data["name"],
            "height" : pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities" :  [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types" : [type_data["type"]["name"] for type_data in pokemon_data["types"]]
        }
        return pokemon_info

    else:
        return None


def run_pokemon_info():


    pokemon_name = input_entry.get()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:

        info_text = f"Name: {pokemon_info['name']}\n" \
                    f"Height: {pokemon_info['height']}\n" \
                    f"Weight: {pokemon_info['weight']}\n" \
                    f"Abilities: {', '.join(pokemon_info['abilities'])}\n" \
                    f"Types: {', '.join(pokemon_info['types'])}"
        result_label.config(text=info_text,fg="blue")
    else:
        result_label.config(text="The pokemon you are looking does not exist, or maybe it hasn't been caught yet!",fg="red")



window = Tk()
window.minsize(600,700)
window.title("Pokemon Finder")

image = PhotoImage(file="images.png")
image_label = Label(window,image=image)
image_label.pack()

title_font = tkinter.font.Font(family="Helvetica",size=12,weight="bold",)
title_label = Label(text="Welcome to pokemon encyclopedia!",font=title_font,fg="green")
title_label.pack()

input_label = Label(text="Enter pokemon name for information: ")
input_label.pack()

input_entry = Entry()
input_entry.pack()

enter_button = Button(text="Enter",command=run_pokemon_info)
enter_button.pack()

result_label = Label(window,text="",font=("Helvetica", 10),justify=LEFT)
result_label.pack(pady=10)

window.mainloop()