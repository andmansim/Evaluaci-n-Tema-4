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

class nodo:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo= tipo

class nodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = None
    
    def insertar_adyacente(self, info, distancia):
        nodo = Adyacente(info, distancia)
        if self.adyacentes is None:
            self.adyacentes = nodo
        else:
            aux_adyacente = self.adyacentes
            self.adyacentes = nodo
            self.sig = aux_adyacente

class Adyacente(object):
    def __init__(self, info, distancia):
        self.info = info
        self.sig = None
        distancia = distancia

class grafo(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
        
    def insertar (self, dato ):
        nodo = nodoVertice(dato)
        if self.inicio is None:
            self.iicio = nodo
        else:
            aux_grafo = self.inicio
            self.inicio = nodo
            self.inicio.sig = aux_grafo
            self.tamanio +=1
    
    def mostrar(self):
        vertice = self.inicio
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado= True
                print(vertice.info)
                vertice = vertice.sig
        
maravillas=[{'nombre': 'Gran Muralla China', 'pais': 'China', 'tipo': 'ARQ'}, 
            {'nombre': 'Coliseo de Roma' , 'pais': 'Italia' , 'tipo': 'ARQ'}, 
            {'nombre': 'Ciudad de Petra', 'pais': 'Jordania ' , 'tipo': 'ARQ'}, 
            {'nombre': 'Bahía de Ha Long', 'pais': 'Vietnam' , 'tipo': 'NAT'}, 
            {'nombre': 'Isla Jeju', 'pais': 'Corea Sur' , 'tipo': 'NAT'}, 
            {'nombre': 'Machu Picchu', 'pais': 'Peru' , 'tipo': 'ARQ'}, 
            {'nombre': 'Taj Mahal', 'pais': 'India', 'tipo':'ARQ'}]
#creamos vértices
m1 = nodoVertice(maravillas[0])
m2 = nodoVertice(maravillas[1])
m3 = nodoVertice(maravillas[2])
m4 = nodoVertice(maravillas[3])
m5 = nodoVertice(maravillas[4])
m6 = nodoVertice(maravillas[5])
m7= nodoVertice(maravillas[6])


