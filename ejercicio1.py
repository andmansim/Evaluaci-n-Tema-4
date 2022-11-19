'''
 crear un árbol de Huffman a partir de la siguiente tabla:

Símbolo Frecuencia

A 0.2
F 0.17
1 0.13
3 0.21
0 0.05
M 0.09
T 0.15

b.         desarrollar las funcionas para comprimir y descomprimir un mensaje.
'''


from cola import*

class nodoArbol(object):
    def __init__(self, info):
        self.izq= None
        self.der = None
        self.info = info # le pasamos la información inicial del árbol, ¿raíz?
        
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
    
    def insertar_nodo(raiz, dato):
        '''
        Insertamos el nodo en el árbol
        '''
        
        if raiz is None:
             raiz = nodoArbol(dato)                        
        elif dato < raiz.info:
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
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
    
    def buscar(raiz, clave):
        '''
        Devuelve la dirección del nodo buscado
        '''
        pos = None
        if raiz is not None:
            if raiz.info == clave:
                pos = raiz
            elif clave < raiz.info:
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos
                
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


datos = {'A': 0.2, 'F': 0.17, '1': 0.13, '3': 0.21, '0': 0.05 , 'M': 0.09, 'T': 0.15}
datos1 = sorted(datos.items(), key= lambda x: x[1])

print(datos1)
lista_arbol = []
for i in range(len(datos1)):
    lista = []
    lista1= []
    suma = datos1[0][1] + datos1[1][1]
    print(suma, datos1[0][1], datos1[1][1])
    lista1.append(datos1[0][0])
    lista1.append(datos1[1][0])
    lista.append(lista1)
    lista.append(suma)
    print(lista)
    datos1.remove(datos1[0])
    datos1.remove(datos1[0])
    datos1.append(lista)
    print(datos1)
