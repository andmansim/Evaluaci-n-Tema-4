class Prioridad(object):
    def __init__(self):
        self.cola = []
    
    def __str__(self): # NO LO TERMINO DE ENTENDER
        '''
        Recorremos la cola y nos une los elementos con un espacio
        '''
        return ' '.join([str(i) for i in self.cola])
    
    def vacia(self):
        return len(self.cola) == 0
    
    def insertar(self, datos):
        self.cola.append(datos)
    
    def eliminar(self):
        '''
        Primero establecemos q el valor max es 0, luego recorremos la cola. 
        Si ese valor es mayor q el máximo entonces ese se combierte e el nuevo máximo. Después lo elimina.
        
        '''
        try:
            max = 0
            for i in range(len(self.cola)):
                if self.cola[i] > self.cola[max]: #Mira 12 > 0 --> Sí, entonces max = 12, 1 > 12 --> No, max = 12, etc.
                    max = i
            valor = self.cola[max] #Nos guarda el valor max
            del self.cola[max] #Elimina el máximo de la cola
            return valor
        except IndexError:
            print()
            exit()