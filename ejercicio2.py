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

    def por_nivel(raiz, lista):
        '''
        Realiza el barrido postorden del árbol
        '''
        pendientes = Cola()
        Cola.arribo(pendientes, raiz)
        while not Cola.cola_vacia(pendientes):
            nodo = Cola.atencion(pendientes)
            lista.append(nodo.info)
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
        nodoArbol.insertar_nodo(arboles,pokemon[i], parametro)
        
def contar(lista, lista1):
    listas=[]
    for i in range(len(lista1)):
        
        a =lista.count(lista1[i])
        listas.append(lista1[i])
        listas.append(a)
    return listas
