import helper as helpers
from ejercicio1 import *
import ejercicio2 as e2
import ejercicio3 as e3

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Ejercicio1: Árbol de Huffman")
        print("[2] ")
        print("[3]  ")
        print("[4]  ")
        print("[5]  ")
        print("[6]  ")
        print("========================")
        
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Encriptamos y desencriptamos...\n")
            datos = {'A': 0.2, 'F': 0.17, '1': 0.13, '3': 0.21, '0': 0.05 , 'M': 0.09, 'T': 0.15}
            #ordenamos en función de los valores
            datos0 = sorted(datos.items(), key= lambda x: x[1])
            datos1 =[]
            #los pasamos a lista
            for j in datos0:
                datos1.append(j[1])

            datos2 = datos1.copy()#Hacemos copia pq luego eliminamos para añadir
            #Creamos los elementos del árbol
            lista_arbol = []
            sumar_elem(lista_arbol, datos1)

            #Creo raiz
            arbol = nodoArbol(lista_arbol[len(lista_arbol)-1])
            #Añado elementos al árbol
            h = len(lista_arbol) - 1
            while h > 1:
                arbol.insertar_nodo(lista_arbol[h],lista_arbol[h-1],lista_arbol[h-2])
                h = h - 3

            #Asociamos 0, 1
            dic = {}
            arbol.ceros_unos(datos2, dic)
            dat_lista = list(datos.items()) #Es un diccionario con las frecuencias de los datos y sus 1 y 0 correspondientes

            #Asociamos los números a las letras
            dicc = {} #El diccionario ya con los datos y sus 1, 0
            for i in dic.keys():
                for j in dat_lista:
                    if i in j:
                        dicc[j[0]] = dic[i]

            #Encriptar un mensaje
            usuario = input('Introduce un mensaje a encriptar con los siguientes caracteres: A, F, 1, 0, M, T, F, 3: ')
            encrip = []
            mensajes(usuario, encrip, dicc, False)
            print('Mensaje encriptado: ' + str(encrip))

            #Desencriptar un mensaje
            desencrip = []
            mensajes(encrip, desencrip, dicc, True)
            print('Mensaje desencriptado: ' + str(desencrip))
                            
        if opcion == '2':
            print("...\n")
            
        
        if opcion == '3':
            print("...\n")
            # Comprobación de DNI válido
           
        
        if opcion == '4':
            print("...\n")
           
                
        if opcion == '5':
            print("...\n")
            
            
        if opcion == '6':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")