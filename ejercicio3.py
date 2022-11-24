'''
Ejercicio 3

Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, 
para lo cual se deben tener en cuenta las siguientes actividades:
a.         de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las 
naturales) y tipo (natural o arquitectónica);
b.         cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la 
distancia que las separa;
c.         hallar el árbol de expansión mínimo de cada tipo de las maravillas;
d.         determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
e.         determinar si algún país tiene más de una maravilla del mismo tipo;
f.         deberá utilizar un grafo no dirigido.
'''

class Adyacente(object):
    def __init__(self, info, distancia):
        self.info = info
        self.sig = None
        self.distancia = distancia
        self.visitado = False

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


class Grafo(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
        
    def insertar(grafo, dato):
        #nodo = nodoVertice(dato)
        if grafo.inicio is None:
            grafo.inicio = dato
        else:
            aux_grafo = grafo.inicio
            grafo.inicio = dato
            grafo.inicio.sig = aux_grafo
            grafo.tamanio +=1
    
    def mostrar(self):
        vertice = self.inicio
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado= True
                print(vertice.info)
                vertice = vertice.sig 

'''def colocar_adyacencia(vertice, maravillas, dist, n):
    while vertice is not None:
        vertice2 = vertice.sig
        if not vertice.visitado:
            vertice.visitado = True
            while vertice2 is not None:
                if not isinstance(vertice2.info, dict):
                    vertice2 = vertice2.info
                if vertice.info['tipo'] == vertice2.info['tipo']:
                    distancia(vertice, vertice2, dist)
                    print(vertice.info, vertice.adyacentes.info.info, vertice.adyacentes.distancia) 
                vertice2 = vertice2.sig 
            ''if n < 6:
                n = n + 1
                vertice = maravillas[n]''
            
            
colocar_adyacencia(vertice, maravillas, dist, n)            
'''
def rest_visitado(grafo):
    vertice = grafo.inicio
    while vertice is not None:
        vertice.visitado = False
        vertice = vertice.sig

def distancia(v1, v2, lista):
    for i in range(len(lista)):
        if v1.info['nombre'] in lista[i] and v2.info['nombre'] in lista[i]:
            v1.insertar_adyacente(v2, dist[i][2])

def ajust_vertice2(vertice, vertice2, dist):
    if vertice2 is not None:
        if not isinstance(vertice2.info, dict):
            vertice2 = vertice2.info
        if vertice.info['tipo'] == vertice2.info['tipo']:
            distancia(vertice, vertice2, dist)
        ajust_vertice2(vertice, vertice2.sig, dist)
        
def colocar_adyacencia(vertice, maravillas, dist, n):
    if vertice is not None:
        vertice2 = vertice.sig
        if not vertice.visitado:
            vertice.visitado = True
            ajust_vertice2(vertice, vertice2, dist)
            if n < 6:
                n = n + 1
                colocar_adyacencia(maravillas[n], maravillas, dist, n)
                   
maravillas=[{'nombre': 'Gran Muralla China', 'pais': 'China', 'tipo': 'ARQ'}, {'nombre': 'Coliseo de Roma' , 'pais': 'Italia' , 'tipo': 'ARQ'}, 
            {'nombre': 'Ciudad de Petra', 'pais': 'Jordania ' , 'tipo': 'ARQ'}, {'nombre': 'Bahía de Ha Long', 'pais': 'Vietnam' , 'tipo': 'NAT'}, 
            {'nombre': 'Isla Jeju', 'pais': 'Corea Sur' , 'tipo': 'NAT'}, {'nombre': 'Machu Picchu', 'pais': 'Peru' , 'tipo': 'ARQ'}, 
            {'nombre': 'Taj Mahal', 'pais': 'India', 'tipo':'ARQ'}]

dist = [['Gran Muralla China', 'Coliseo de Roma', 7565], ['Gran Muralla China', 'Ciudad de Petra', 6217], 
        ['Gran Muralla China', 'Machu Picchu', 17038], ['Gran Muralla China', 'Taj Mahal', 7510], 
        ['Coliseo de Roma','Ciudad de Petra', 3673], ['Coliseo de Roma','Machu Picchu', 10478], 
        ['Coliseo de Roma','Taj Mahal', 6571], ['Ciudad de Petra','Taj Mahal', 4396], 
        ['Ciudad de Petra', 'Machu Picchu',  12547], ['Machu Picchu', 'Taj Mahal', 16941], ['Bahía de Ha Long', 'Isla Jeju', 2362 ]]
#creamos vértices
m1 = nodoVertice(maravillas[0])
m2 = nodoVertice(maravillas[1])
m3 = nodoVertice(maravillas[2])
m4 = nodoVertice(maravillas[3])
m5 = nodoVertice(maravillas[4])
m6 = nodoVertice(maravillas[5])
m7= nodoVertice(maravillas[6])

grafo = Grafo()
grafo.insertar(m1)
grafo.insertar(m2)
grafo.insertar(m3)
grafo.insertar(m4)
grafo.insertar(m5)
grafo.insertar(m6)
grafo.insertar(m7)



grafo.mostrar()
rest_visitado(grafo)
maravillas = [m1, m2, m3, m4, m5, m6, m7]
vertice = grafo.inicio
n = 0

colocar_adyacencia(vertice, maravillas, dist, n)            
