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
        print("[1] csv")
        print("[2] ")
        print("[3]  ")
        print("[4]  ")
        print("[5]  ")
        print("[6]  ")
        print("========================")
        
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Vamos a ver csv...\n")
            #Solo he llamado al fichero helpers para q nos lo limpie y organice los datos
            lista_dicc = helpers.leer('csvs/Pokemon.csv')     
            helpers.comas(lista_dicc)
            helpers.limpiar(lista_dicc)
            helpers.camb_nombre(lista_dicc, 'Attack', 'Ataque') #se le pasa la lista, el nombre viejo y el nuevo
            helpers.bonito(lista_dicc)
                            
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