'''
Ejercicio 3

Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
a.         de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica);
b.         cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa;
c.         hallar el árbol de expansión mínimo de cada tipo de las maravillas;
d.         determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
e.         determinar si algún país tiene más de una maravilla del mismo tipo;
f.         deberá utilizar un grafo no dirigido.
'''
from cola import *
class nodoArista(object):
    '''Clase nodo vértice'''
    def __init__(self, info, destino):
        '''
        Crea un nodo arista con la información cargada
        '''
        self.info = info
        self.destino = destino
        self.sig = None
    
class nodoVertice(object):
    '''
    Clase nodo vértice
    '''
    def __init__(self, info):
        '''
        Crea un nodo vértice con la información cargada
        '''
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo(object):
    '''
    Clase grafo implementación lista de listas de adyacencia
    '''
    def __init__(self, dirigido = True):
        '''
        Crea un gráfo vacío
        '''
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0
        
class Arista(object):
    '''
    Clase lista de aristas implenentación sobre lista
    '''
    def __init__(self):
        '''
        Crea una lista de aristas vacía
        '''
        self.inicio = None
        self.tamanio = 0
        
    def insertar_vertice(grafo, dato):
        '''
        Insertar un vértice grafo
        '''
        nodo = nodoVertice(dato)
        if grafo.inicio is None or grafo.inicio.info > nodo.info:
            nodo.sig = grafo.inicio
            grafo.inicio = nodo
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while act is not None and act.info < nodo.info:
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        grafo.tamanio += 1
    
    def insertar_arista(grafo, dato, origen, destino):
        '''
        Inserta una arista desde el vértice origen al destino
        '''
        Arista.agregar_arista(origen.adyacentes, dato, destino.info)
        if not grafo.dirigido:
            Arista.agregar_arista(destino.adyacentes, dato, origen.info)
    
    def agregar_arista(origen, dato, destino):
        '''
        Agregar la arista desde el vértice origen al destino
        '''
        nodo = nodoArista(dato, destino)   
        if origen.inicio is None or origen.inicio.destinio > destino:
            nodo.sig = origen.inicio
            origen.inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.sig
            while act is not None and act.destino < nodo.destino:
                ant = act
                act = act.sig
            nodo.sig= act
            ant.sig = nodo
        origen.tamanio += 1
    
    def eliminar_vertice(grafo, clave):
        '''
        Elimina un vértice del grafo y lo devuelve si lo encuentra
        '''
        x = None
        if grafo.inicio.info == clave:
            x = grafo.inicio.info
            grafo.inicio = grafo.inicio.sig
            grafo.tamanio -= 1
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while act is not None and act.info != clave :
                ant = act
                act = act.sig
            
            if act is not None:
                x = act.sig
                ant.sig = act.sig 
                grafo.tamanio -=1
        if x is not None:
            aux = grafo.inicio
            while aux is not None:
                if aux.adyacentes.inicio is not None:
                    Arista.eliminar_arista(aux.adyacentes, clave)
                aux = aux.sig
        
        return x
    
    def buscar_vertice(grafo, buscado):
        '''
        Devuelve la dirección del elemento buscado
        '''
        aux = grafo.inicio
        while aux is not None and aux.info != buscado:
            aux = aux.sig
        return aux

    
    def buscar_arista(vertice, buscado):
        '''
        Devuelve la dirección del elemento buscado
        '''
        aux = vertice.adyacentes.inicio
        while aux is not None and aux.destino != buscado:
            aux = aux.sig
        return aux
    
    def tamanio(grafo):
        '''
        Devuelve el número de vértices en el grafo
        '''
        return grafo.tamanio
    
    def grafo_vacio(grafo):
        '''
        Devuelve True si el grafo está vacío
        '''
        return grafo.inicio is None
    
    
    def eliminar_arista(vertice, destino):
        '''
        Elimina una arista del vértice y lo devuelve si lo encuentra
        '''
        x = None
        if vertice.inicio.destino == destino:
            x = vertice.inicio.info
            vertice.inicio = vertice.inicio.sig
            vertice.tamanio -= 1
        
        else:
            ant = vertice.inicio
            act = vertice.inicio.sig
            while act is not None and act.destino != destino:
                ant = act
                act = act.sig
            if act is not None:
                x = act.info
                ant.sig = act.sig
                vertice.tamanio -= 1
        return x
    
    def existe_paso(grafo, origen, destino):
        '''
        Barrido en profundidad del grafo
        '''
        resultado = False
        if not origen.visitado:
            origen.visitado = True
            vadyacentes = origen.adyacentes.inicio
            while vadyacentes is not None and not resultado:
                adyacente = Arista.buscar_vertice(grafo, vadyacentes.destino)
                if adyacente.info == destino.info:
                    return True
                elif not adyacente.visitado:
                    resultado = Arista.existe_paso(grafo, adyacente, destino)
                vadyacentes = vadyacentes.sig
                
        return resultado
    
    def adyacentes(vertice):
        '''
        Muestra los adyacentes del vértice
        '''
        aux = vertice.adyacentes.inicio
        while aux is not None:
            print(aux.destino, aux.info)
            aux = aux.sig 
    
    def es_adyacente(vertice, destino):
        '''
        Determina si el destino es adyacente directo
        '''
        resultado = False
        aux = vertice.adyacentes.inicio 
        while aux is not None and not resultado:
            if aux.destino == resultado:
                resultado = True
            aux= aux.sig 
        return resultado
    
    def marcar_no_visitado(grafo):
        '''
        Marca todos los vértices del grafo como no visitados
        '''
        aux = grafo.inicio
        while aux is not None:
            aux.visitado = False
            aux = aux.sig 
    
    def barrido_profundidad(grafo, vertice):
        '''
        Barrido en profundidad del grafo
        '''
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado = True
                print(vertice.info)
                adyacentes = vertice.adyacentes.inicio 
                while adyacentes is not None:
                    adyacente = Arista.buscar_vertice(grafo, adyacentes.destino)
                    if not adyacente.visitado:
                        Arista.barrido_profundidad(grafo, adyacente)
                    adyacentes = adyacentes.sig 
            vertice = vertice.sig 
            
    def barrido_amplitud(grafo, vertice):
        '''
        Barrido en amplitud del grafo
        '''
        cola = Cola()
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado = True 
                Cola.arribo(cola, vertice)
                while not Cola.cola_vacia(cola):
                    nodo = Cola.atencion(cola)
                    print(nodo.info)
                    adyacentes = nodo.adyacentes.inicio
                    while adyacentes is not None:
                        adyacente = Arista.buscar_vertice(grafo, adyacentes.destino)
                        if not adyacente.visitado: 
                            adyacente.visitado = True 
                            Cola.arribo(cola, adyacente)
                        adyacentes = adyacentes.sig
                        
            vertice = vertice.sig
    