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
    
    def insertar_nodo(raiz, dato, dato1,dato2):
        '''
        Insertamos el nodo en el árbol
        '''
       
        if raiz is None:
            raiz = nodoArbol(dato1)                        
        elif dato1 < raiz.info:
            if dato == 1.0 :
                busco = raiz
                raiz.der = nodoArbol.insertar_nodo(busco.der, dato, dato1,dato2)
                raiz.izq = nodoArbol.insertar_nodo(busco.izq, dato, dato2,dato1)
            else:    
                busco = arbol.buscar(dato)
                busco.izq = nodoArbol.insertar_nodo(busco.izq, dato, dato2,dato1)
                busco.der = nodoArbol.insertar_nodo(busco.der, dato, dato1,dato2)
        else:
            if raiz.info == 1.0 :
                busco = raiz
                raiz.der = nodoArbol.insertar_nodo(busco.der, dato, dato1, dato2)
                raiz.izq = nodoArbol.insertar_nodo(busco.izq, dato, dato2,dato1)
            else:
                busco = arbol.buscar(dato)
                raiz.der = nodoArbol.insertar_nodo(busco.der, dato, dato1,dato2)
                raiz.izq = nodoArbol.insertar_nodo(busco.izq, dato, dato2,dato1)
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
    
    def buscar(raiz, clave):
        '''
        Devuelve la dirección del nodo buscado
        '''
        pos = None
        if raiz is not None:
            if raiz.info == clave:
                pos = raiz
            else:
                if raiz.izq is not None and raiz.der is not None:
                    pos = nodoArbol.buscar(raiz.izq, clave)
                    if pos is None:
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
    
    def preorden1(raiz, lista):
        '''
        Realiza el barrido preorden del árbol
        '''
        if raiz is not None:
            lista.append(raiz.info)    
            nodoArbol.preorden1(raiz.izq, lista)
            nodoArbol.preorden1(raiz.der, lista)
    
    def postorden(raiz):
        '''
        Realiza el barrido postorden del árbol
        '''
        if raiz is not None:
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)


datos = {'A': 0.2, 'F': 0.17, '1': 0.13, '3': 0.21, '0': 0.05 , 'M': 0.09, 'T': 0.15}
datos0 = sorted(datos.items(), key= lambda x: x[1])
datos1 =[]

    
for j in datos0:
    datos1.append(j[1])
print(datos1)
d = datos1.copy()
lista_arbol = []
for i in range(len(datos1)-1):
    lista = []
    lista1= []
    suma = round(datos1[0] + datos1[1], 2)
    lista_arbol.append(datos1[0])
    lista_arbol.append(datos1[1])
    lista_arbol.append(suma)
    print(lista_arbol)
    '''lista1.append((datos1[0][0], datos1[0][1]))
    lista1.append((datos1[1][0], datos1[1][1]))'''
    #lista.append(lista1)
    #lista.append(suma)
    datos1.remove(datos1[0])
    datos1.remove(datos1[0])
    datos1.append(suma)
    datos1 = sorted(datos1)
    print(datos1)
arbol = nodoArbol(datos1[0])
#lista_arbol = sorted(lista_arbol, reverse = True)
print(lista_arbol)
h = len(lista_arbol) - 1
while h > 1:
    #busco = arbol.buscar(lista_arbol[h])
    #print(busco.info, busco.der, busco.izq )
    arbol.insertar_nodo(lista_arbol[h],lista_arbol[h-1],lista_arbol[h-2])
    
    h = h - 3
pre = []
arbol.preorden1(pre)
l =[]    
arbol.por_nivel(l)
cero_uno = []
for i in range(len(l)):
    if  i % 2 == 0:
        cero_uno.append(1)
    elif i% 2 != 0:
        cero_uno.append(0)

dicc= dict(zip(l, cero_uno))
del(dicc[l[0]])
print(pre)
print(dicc)
c =list(reversed(d))
print(c)

dic={}
for i in dicc:
    a = [i, i+1]
    del (i)
    print(dicc)
