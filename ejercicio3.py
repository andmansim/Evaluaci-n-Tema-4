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
        