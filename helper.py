import os
import platform 
import pandas as pd
def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

pok = pd.read_csv('pokedex.csv', names=['pokedex_number', 'name', 'type_1', 'type_2', 'against_normal',
       'against_fire', 'against_water', 'against_electric', 'against_grass',
       'against_ice', 'against_fight', 'against_poison', 'against_ground',
       'against_flying', 'against_psychic', 'against_bug', 'against_rock',
       'against_ghost', 'against_dragon', 'against_dark', 'against_steel',
       'against_fairy'])
print(pok.columns)
pok = pok.rename(columns={'pokedex_number': 'id_p', 'name': 'nombre', 'type_1': 'tipo1', 'type_2': 'tipo2' })
print(pok.columns)
