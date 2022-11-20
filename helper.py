import os
import platform 
import csv

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
def leer():
    '''
    Leemos el csv y lo almacenamos en una lista de diccionarios
    '''
    lista = []
    with open('pokedex.csv', newline="\n") as fichero:
            reader = csv.DictReader(fichero, delimiter=",") #lo pasa a diccionario
            for linea in reader:
                lista.append(linea) 
    
    return lista

def inicio_csv():
    lista = leer()
    lista1 = []
    for i in lista:
        dicc= {}
        dicc['id_p'] = i['pokedex_number']
        dicc['nombre'] = i['name']
        dicc['tipo1'] = i['type_1']
        dicc['tipo2'] = i['type2']
        dicc['against_fire'] = i['against_fire']
        dicc['against_water'] = i['against_water']
        dicc['against_electric'] = i['against_electric']
        dicc['against_grass'] = i['against_grass']
        dicc['against_ice'] = i['against_ice']
        dicc['against_fight'] = i['against_fight']
        dicc['against_poison'] = i['against_poison']
        dicc['against_ground'] = i['against_ground']
        dicc['against_flying'] = i['against_flying']
        dicc['against_psychic'] = i['against_psychic']
        dicc['against_bug'] = i['against_bug']
        dicc['against_rock'] = i['against_rock']
        dicc['against_ghost'] = i['against_ghost']
        dicc['against_dragon'] = i['against_dragon']
        dicc['against_dark'] = i['against_dark']
        dicc['against_steel'] = i['against_steel']
        dicc['against_fairy'] = i['against_fairy']

        lista1.append(dicc)
    return lista1
    
