from prioridad import*
class NodoCola(object):
    info, sig = None, None

class Cola(object):
    def __init__(self):
        #Creamos una cola vacia
        self.frente, self.final = None, None
        self.tamanio = 0
        
    def arribo(cola, dato):
        #Arriba el dato al final de la cola
        nodo = NodoCola() #creamos una variable tipo nodo
        nodo.info = dato #el dato del nodo
        if cola.frente is None:
            cola.frente = nodo #Si la cola esta vacia, se añade como el primer elemento
        else:
            cola.final.sig = nodo #Si la cola no esta vacía, se pone en el ultimo hueco vacio aka el final
        cola.final = nodo
        cola.tamanio += 1

    def atencion(cola):
        #Atiende el elemento al principio de la cola y lo devuelve
        dato = cola.frente.info #accedemos a la info y la guardamos en una variable auxiliar
        cola.frente = cola.frente.sig #suplantamos el principio de la cola por el valor siguiente, como si quitaramos en primer elemento
        if cola.frente is None:
            cola.final = None #Si no quedan mas elementos en el frente, no hay final
        cola.tamanio -= 1
        return dato
    
    def cola_vacia(cola):
        #Devuelve true si la cola esta vacia
        return cola.frente is None
    
    def en_frente(cola):
        #Devuelve el valor almacenado en el frente de la cola
        return cola.frente.info
    
    def tamanio(cola):
        #Devuelve el tamaño de la cola
        return cola.tamanio
    
    def mover_al_final(cola):
        #Mueve el elemento almacenado al principio de la cola al final
        dato = Cola.atencion(cola)
        Cola.arribo(cola, dato)
        return dato

    def barrido(cola):
        #Muestra el contenido de una cola sin perder datos
        i = 0
        while i < cola.tamanio(cola):
            dato = cola.mover_al_final(cola)
            print(dato)
            i += 1
