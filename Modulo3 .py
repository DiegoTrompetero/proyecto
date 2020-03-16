rutatres = "c:/Users/diego/OneDrive/Documentos/Proyecto_Algoritmo_Diego/Estadisticas.txt"
def leerestadisticas (lista):
    archivo = open (rutatres, "r")
    for lineas in archivo.readlines():
        lita=lineas.split(",")
        lista.append(lita)
    print("Estadisticas leidas")
    return True

def Escribirestadisticas (lista2):
    archivo = open(rutatres, "w")
    print("Escritura Iniciada")
    for freedom in lista2:
        freestr = str(freedom[0]) + ","+ str(freedom[1])
        archivo.write(freestr)
    archivo.close()
    print("Escritura finalizada")
    return True

Lista_Estadisticas = []
leerestadisticas(Lista_Estadisticas)
print(Lista_Estadisticas)

puntos_hombre= int(Lista_Estadisticas[0][0])
partidas_hombres = int(Lista_Estadisticas[1][0])
puntos_mujeres = int(Lista_Estadisticas [2][0])
partidas_mujeres = int(Lista_Estadisticas[3][0])
PJ518 = int(Lista_Estadisticas[4][0])
PJ1945 = int(Lista_Estadisticas[5][0])
PJ4660 = int(Lista_Estadisticas[6][0])
PJ61100 = int (Lista_Estadisticas[7][0])
Partidas_Jugadas = int (Lista_Estadisticas[8][0])
Tiros_hechos = int (Lista_Estadisticas [9][0])

promedio_hombres = puntos_hombre / partidas_hombres
promediomujeres = puntos_mujeres / partidas_mujeres
promedio_tiros = Tiros_hechos / Partidas_Jugadas
print ("Partidas Jugadas: ", Partidas_Jugadas)
print ("Tiros hechos: ", Tiros_hechos)
print ("Tiros promedios por partida: ", promedio_tiros)
print ("Puntos hechos por hombres: ", puntos_hombre)
print ("Partidas jugadas por hombres",partidas_hombres)
print ("Puntuacion promedia hombres por partido: ", promedio_hombres)
print ("Puntos hechos por mujeres: ", puntos_mujeres)
print ("Partidas jugadas por mujeres: ", partidas_mujeres)
print ("Puntuacion promedia mujeres por partido: ", promediomujeres)
print ('''Partidas jugadas por intervalos de edad:
        Entre 5 a 18 años: {}
        Entre 19 a 45 años: {}
        Entre 46 a 60 años: {}
        Entre 61 a 100 años: {}
        '''.format(PJ518,PJ1945,PJ4660,PJ61100))

Listaderangos = [PJ518,PJ1945,PJ4660,PJ61100]
maximo = 0
for x in Listaderangos:
    if x > maximo:
        maximo = x

if maximo == PJ518:
    print ("Rango de edad que juega mas: 5 a 18 años")

elif maximo ==PJ1945:
    print ("Rango de edad que juega mas: 19 a 45 años")

elif maximo == PJ4660:
    print ("Rango de edad que juega mas: 46 a 60 años")

elif maximo == PJ61100:
    print("Rango de edad que juega mas: 61 a 100 años")



print ( Lista_Estadisticas)

Escribirestadisticas (Lista_Estadisticas)