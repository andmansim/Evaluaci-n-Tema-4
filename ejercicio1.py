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
                busco = nodoArbol.buscar(raiz, dato)
                busco.izq = nodoArbol.insertar_nodo(busco.izq, dato, dato2,dato1)
                busco.der = nodoArbol.insertar_nodo(busco.der, dato, dato1,dato2)
        else:
            if raiz.info == 1.0 :
                busco = raiz
                raiz.der = nodoArbol.insertar_nodo(busco.der, dato, dato1, dato2)
                raiz.izq = nodoArbol.insertar_nodo(busco.izq, dato, dato2,dato1)
            else:
                busco = nodoArbol.buscar(raiz, dato)
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

    def recorrer_ar(raiz, dato, lista, encontrado):
        
        if raiz is not None:
            if raiz.der == None and raiz.izq == None: #Estoy en una hoja
                if raiz.info == dato:
                    encontrado = True
            else:
                if encontrado != True:
                    lista.append(0)
                    encontrado = nodoArbol.recorrer_ar(raiz.izq, dato, lista, encontrado)
                    if encontrado != True:
                        lista.pop()
                if encontrado!= True:
                    lista.append(1)
                    encontrado = nodoArbol.recorrer_ar(raiz.der, dato, lista, encontrado)
                    if encontrado != True:
                        lista.pop()
                    
        return encontrado

    def ceros_unos(raiz, datos, dic):
        for i in datos:
            cero_uno = []
            nodoArbol.recorrer_ar(raiz, i, cero_uno, False)
            dic[i] = cero_uno
                
def sumar_elem(lista, datos):
    for i in range(len(datos)-1):
        
        suma = round(datos[0] + datos[1], 2)
        lista.append(datos[0])
        lista.append(datos[1])
        lista.append(suma)
        datos.remove(datos[0])
        datos.remove(datos[0])
        datos.append(suma)
        datos = sorted(datos)
        
def mensajes(datos, lista, diccionario, control):
    for i in datos:
        for j in diccionario.keys():
            if control:
                if i == diccionario[j]:
                    lista.append(j)
            else:
                if i in j:
                    lista.append(diccionario[j])
                    
