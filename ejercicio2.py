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
    
    def buscar1(raiz, clave, param, lista):
        
        print(lista)
        for i in range(2):
            pos = None
            if raiz is not None:
                if clave in raiz.info[param].lower():
                    pos = raiz
                elif clave < raiz.info[param].lower():
                    pos = nodoArbol.buscar1(raiz.izq, clave, param, lista)
                else:
                    pos = nodoArbol.buscar1(raiz.der, clave, param, lista)
            lista.append(pos.info)
        return lista
           
    def inorden(raiz):
        '''
        Hace el barrido inorden del árbol
        '''
        if raiz is not None:
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)

    def preorden(raiz):
        '''
        Realiza el barrido preorden del árbol
        '''
        if raiz is not None:
            print(raiz.info)    
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)

    def postorden(raiz):
        '''
        Realiza el barrido postorden del árbol
        '''
        if raiz is not None:
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)

def crear_arbol(arboles, n, parametro, pokemon):
    for i in range(1, n):
        arboles.insertar_nodo(pokemon[i], parametro)
        

a = 'Bul a'
if 'bul' in a.lower():
    print(a.lower())
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
busco = arbol1.buscar(7, 'id_p')
print(busco.info)
#busco por nombre
busco1 = arbol.buscar1('iv', 'nombre', [])
print(busco1.info)