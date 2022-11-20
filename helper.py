import os
import platform 
import pandas as pd
def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

pok = pd.read_csv('pokedex.csv')
