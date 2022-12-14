import helper as helpers
import ejercicio1 as e1
import ejercicio2 as e2
import ejercicio3 as e3

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Ejercicio1: Árbol de Huffman")
        print("[2] Ejercicio2: Pokemons")
        print("[3] Ejercicio3: Grafos ")
        print("[4] Salir del menu ")
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
            e1.sumar_elem(lista_arbol, datos1)

            #Creo raiz
            arbol = e1.nodoArbol(lista_arbol[len(lista_arbol)-1])
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
            e1.mensajes(usuario, encrip, dicc, False)
            print('Mensaje encriptado: ' + str(encrip))

            #Desencriptar un mensaje
            desencrip = []
            e1.mensajes(encrip, desencrip, dicc, True)
            print('Mensaje desencriptado: ' + str(desencrip))
                            
        if opcion == '2':
            print("Información de los pokemons...\n")
            pok1 = helpers.inicio_csv()
            #Árbol por nombre
            arbol = e2.nodoArbol(pok1[0])
            e2.crear_arbol(arbol, 890, 'nombre', pok1)
            #Árbol por id
            arbol1 = e2.nodoArbol(pok1[0])
            e2.crear_arbol(arbol1, 890, 'id_p', pok1)
            #Árbol por tipo1
            arbol2 = e2.nodoArbol(pok1[0])
            e2.crear_arbol(arbol2, 890, 'tipo1', pok1)

            #busco por id_p
            print('-----------Buscamos datos:------------------')
            num = int(input('Introduce id del pokemon a buscar:'))
            busco = arbol1.buscar(num, 'id_p')
            print(busco.info)
            #busco por nombre
            lista = []
            let = input('Introduce el nombre del pokemon a buscar: ')
            arbol.preorden1(lista, let, 'nombre')
            if lista == []:
                print('No se ha encontrado ningún resultado')
            print(lista)

            #nombres pokemon de tipo agua, fuego, planta y eléctrico
            print('\n')
            print('------------------Tipos de pokemons--------------------')
            nom_agua= []
            arbol2.preorden2(nom_agua, 'water', 'tipo1', 'nombre')
            print('\n')
            print('Pokemons tipo agua:')
            print(nom_agua)

            nom_fuego=[]
            arbol2.preorden2(nom_fuego, 'fire', 'tipo1', 'nombre')
            print('\n')
            print('Pokemons tipo fuego:')
            print(nom_fuego)

            nom_planta=[]
            arbol2.preorden2(nom_planta, 'grass', 'tipo1', 'nombre')
            print('\n')
            print('Pokemons tipo planta:')
            print(nom_planta)

            nom_electro=[]
            arbol2.preorden2(nom_electro, 'electric', 'tipo1', 'nombre')
            print('\n')
            print('Pokemons tipo eléctrico:')
            print(nom_electro)

            #Lista ordenada por id
            print('\n')
            print('----------------Listas ordenadas-----------------')
            or_id=[]
            arbol1.inorden(or_id)
            print('\n')
            print('Lista ordenada por id:')
            print(or_id[:3]) #Solo son 3 ejemplos

            #lista ordenada por nombre
            or_nom=[]
            arbol.inorden(or_nom)
            print('\n')
            print('Lista ordenada por nombre:')
            print(or_nom[:3]) #Solo son 3 ejemplos

            print('\n')
            nom_por_nivel=[]
            arbol.por_nivel(nom_por_nivel)
            print('Lista2 ordenada por nombre:')
            print(nom_por_nivel[:3]) #Solo son 3 ejemplos

            #Jolteo(electrico), Lycanroc(roca) y Tyrantrum(roca, dragon)
            elec = []
            arbol2.postorden1(elec, 0.5, 'against_electric', 'nombre')
            print('\n')
            print('Lista de pokemons débiles contra el electro')
            print(elec)

            roca = []
            arbol2.postorden1(roca, 0.5, 'against_rock', 'nombre')
            print('\n')
            print('Lista de pokemons débiles contra la roca')
            print(roca)

            drag = []
            arbol2.postorden1(drag, 0.5, 'against_dragon', 'nombre')
            print('\n')
            print('Lista de pokemons débiles contra el tipo dragón')
            print(drag)

            #Lista de tipo de pokemons únicos
            l= []
            arbol2.inorden1(l)
            l_unic=[]
            for i in set(l):
                l_unic.append(i)
            print('\n')
            print('Tipos pokemon:')
            l_rep= e2.contar(l, l_unic)
            print(l_rep)
            
        
        if opcion == '3':
            print("Grafos...\n")
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
            m1 = e3.nodoVertice(maravillas[0])
            m2 = e3.nodoVertice(maravillas[1])
            m3 = e3.nodoVertice(maravillas[2])
            m4 = e3.nodoVertice(maravillas[3])
            m5 = e3.nodoVertice(maravillas[4])
            m6 = e3.nodoVertice(maravillas[5])
            m7= e3.nodoVertice(maravillas[6])

            grafo = e3.Grafo()
            grafo.insertar(m1)
            grafo.insertar(m2)
            grafo.insertar(m3)
            grafo.insertar(m4)
            grafo.insertar(m5)
            grafo.insertar(m6)
            grafo.insertar(m7)


            print('vertices iniciales ---------------------------')
            grafo.mostrar()
            e3.rest_visitado(grafo)
            maravillas = [m1, m2, m3, m4, m5, m6, m7]
            vertice = grafo.inicio
            n = 0
            print('\nGrafo completo-----------------------------')
            e3.colocar_adyacencia(vertice, maravillas, dist, n) 
                    
                
            
        if opcion == '4':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")