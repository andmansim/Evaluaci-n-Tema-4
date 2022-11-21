'''
Ejercicio 2
Se tiene un archivo con los Pokémons de las 8 generaciones cargados de manera desordenada (890 en total) 
de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/ tipos,
para el cual debemos construir tres árboles para acceder de manera eficiente a los datos almacenados en el archivo, 
contemplando lo siguiente:

a.         los índices de cada uno de los árboles deben ser nombre, número y tipo;
b.         mostrar todos los datos de un Pokémon a partir de su número y nombre para este último, la 
búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres 
comiencen o contengan dichos caracteres;
c.         mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
d.         realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel 
por nombre;
e.         mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
f.         mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.
'''
from helper import *
from cola import *


class nodoArbol(object):
    def __init__(self, info):
        self.izq= None
        self.der = None
        self.info = info
    
    def eliminar_nodo(raiz, clave):
        '''
        Elimina el elemento del árbol y lo devuelve si lo encuentra
        
        '''
        x = None
        if raiz is not None:
            if clave < raiz.info:
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif clave > raiz.info:
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if raiz.izq is None:
                    raiz = raiz.der
                elif raiz.der is None:
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x

    def insertar_nodo(raiz, dato, param):
        '''
        Insertamos el nodo en el árbol
        '''
        if raiz is None:
            raiz = nodoArbol(dato)                        
        elif dato[param] < raiz.info[param]:
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato, param)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato, param)
        return raiz

    def arbolvacio(raiz):
        '''
        Devuelve True si el árbol está vacío
        '''
        return raiz is None

    def remplazar (raiz):
        '''
        Determina el nodo que remplazará al que se elimina
        '''
        aux = None
        if raiz.der is None:
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux

    def por_nivel(raiz):
        '''
        Realiza el barrido postorden del árbol
        '''
        pendientes = Cola()
        Cola.arribo(pendientes, raiz)
        while not Cola.cola_vacia(pendientes):
            nodo = Cola.atencion(pendientes)
            print(nodo.info)
            if nodo.izq is not None:
                Cola.arribo(pendientes, nodo.izq)
            if nodo.der is not None:
                Cola.arribo(pendientes, nodo.der)

    def buscar(raiz, clave, param):
        '''
        Devuelve la dirección del nodo buscado
        '''
        pos = None
        if raiz is not None:
            if raiz.info[param] == clave:
                pos = raiz
            elif clave < raiz.info[param]:
                pos = nodoArbol.buscar(raiz.izq, clave, param)
            else:
                pos = nodoArbol.buscar(raiz.der, clave, param)
        return pos
    
    '''def buscar1(raiz, clave, param):
      
        pos = None
        if raiz is not None:
            if clave in raiz.info[param].lower():
                pos = raiz
            elif clave < raiz.info[param].lower():
                pos = nodoArbol.buscar1(raiz.izq, clave, param)
            else:
                pos = nodoArbol.buscar1(raiz.der, clave, param)
        
        return pos'''
        
    def inorden(raiz, lista):
        '''
        Hace el barrido inorden del árbol
        '''
        if raiz is not None:
            nodoArbol.inorden(raiz.izq, lista)
            lista.append(raiz.info)
            nodoArbol.inorden(raiz.der, lista)
    
    def inorden1(raiz, lista):
        '''
        Hace el barrido inorden del árbol
        '''
        if raiz is not None:
            nodoArbol.inorden1(raiz.izq, lista)
            lista.append(raiz.info['tipo1'])
            nodoArbol.inorden1(raiz.der, lista)


    def preorden(raiz):
        '''
        Realiza el barrido preorden del árbol
        '''
        if raiz is not None:
            print(raiz.info)    
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)

    def preorden1(raiz, lista, letra, param):
        '''
        Para buscar por nombres
        '''
        if raiz is not None:
            if letra in raiz.info[param].lower():
                lista.append(raiz.info[param])    
            nodoArbol.preorden1(raiz.izq, lista, letra, param)
            nodoArbol.preorden1(raiz.der, lista,letra, param)
    
    def preorden2(raiz, lista, tipo, param, param1):
        '''
        Para buscar el nombre según el tipo
        '''
        if raiz is not None:
            if tipo == raiz.info[param].lower():
                lista.append(raiz.info[param1])    
            nodoArbol.preorden2(raiz.izq, lista, tipo, param, param1)
            nodoArbol.preorden2(raiz.der, lista,tipo, param, param1)
    
    def postorden(raiz):
        '''
        Realiza el barrido postorden del árbol
        '''
        if raiz is not None:
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)
            
    def postorden1(raiz, lista, tipo, param, param1):
        '''
        Ver pokemon débiles a un tipo
        '''
        if raiz is not None:
            nodoArbol.postorden1(raiz.der, lista, tipo, param, param1)
            if tipo >= raiz.info[param]:
                lista.append(raiz.info[param1])
            nodoArbol.postorden1(raiz.izq, lista, tipo, param, param1)

def crear_arbol(arboles, n, parametro, pokemon):
    for i in range(1, n):
        arboles.insertar_nodo(pokemon[i], parametro)
        


#main     
pok1 = inicio_csv()
#Árbol por nombre
arbol = nodoArbol(pok1[0])
crear_arbol(arbol, 890, 'nombre', pok1)
#Árbol por id
arbol1 = nodoArbol(pok1[0])
crear_arbol(arbol1, 890, 'id_p', pok1)
#Árbol por tipo1
arbol2 = nodoArbol(pok1[0])
crear_arbol(arbol2, 890, 'tipo1', pok1)

#busco por id_p
print('Buscamos datos:')
num = int(input('Introduce id del pokemon a buscar:'))
busco = arbol1.buscar(num, 'id_p')
print(busco.info)
#busco por nombre
lista = []
let = input('Introduce el nombre del pokemon a buscar: ')
arbol.preorden1(lista, let, 'nombre')
if lista == []:
    print('No se ha encontrado ningún resultado')
print(lista)

#nombres pokemon de tipo agua, fuego, planta y eléctrico
nom_agua= []
arbol2.preorden2(nom_agua, 'water', 'tipo1', 'nombre')
print('\n')
print('Pokemons tipo agua:')
print(nom_agua)

nom_fuego=[]
arbol2.preorden2(nom_fuego, 'fire', 'tipo1', 'nombre')
print('\n')
print('Pokemons tipo fuego:')
print(nom_fuego)

nom_planta=[]
arbol2.preorden2(nom_planta, 'grass', 'tipo1', 'nombre')
print('\n')
print('Pokemons tipo planta:')
print(nom_planta)

nom_electro=[]
arbol2.preorden2(nom_electro, 'electric', 'tipo1', 'nombre')
print('\n')
print('Pokemons tipo eléctrico:')
print(nom_electro)

#Lista ordenada por id
or_id=[]
arbol1.inorden(or_id)
print('\n')
print('Lista ordenada por id:')
print(or_id[:3])

#lista ordenada por nombre
or_nom=[]
arbol.inorden(or_nom)
print('\n')
print('Lista ordenada por nombre:')
print(or_nom[:3])

print('\n')
a = [arbol.por_nivel()]
print('Lista2 ordenada por nombre:')
print(a[:3]) #Mirar

#Jolteo(electrico), Lycanroc(roca) y Tyrantrum(roca, dragon)

elec = []
arbol2.postorden1(elec, 0.5, 'against_electric', 'nombre')
print('\n')
print('Lista de pokemons débiles contra el electro')
print(elec)

roca = []
arbol2.postorden1(roca, 0.5, 'against_rock', 'nombre')
print('\n')
print('Lista de pokemons débiles contra la roca')
print(roca)

drag = []
arbol2.postorden1(drag, 0.5, 'against_dragon', 'nombre')
print('\n')
print('Lista de pokemons débiles contra el tipo dragón')
print(drag)

#Lista de tipo de pokemons únicos
l= []
arbol2.inorden(l)
l_unic=[]
for i in set(l):
    l_unic.append(i)
print(l_unic)
