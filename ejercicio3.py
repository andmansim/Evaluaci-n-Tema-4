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
        
        