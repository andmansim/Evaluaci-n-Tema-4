'''
Ejercicio 2
Se tiene un archivo con los Pokémons de las 8 generaciones cargados de manera desordenada (890 en total) 
de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/ tipos,
para el cual debemos construir tres árboles para acceder de manera eficiente a los datos almacenados en el archivo, 
contemplando lo siguiente:

a.         los índices de cada uno de los árboles deben ser nombre, número y tipo;
b.         mostrar todos los datos de un Pokémon a partir de su número y nombre para este último, la 
búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres 
comiencen o contengan dichos caracteres;
c.         mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
d.         realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel 
por nombre;
e.         mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
f.         mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.
'''
from helper import *
pok1 = inicio_csv()
print(pok1.columns)