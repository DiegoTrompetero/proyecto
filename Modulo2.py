columnas = ("a","b","c","d","e","f","g","h","i","j")
filas = (1,2,3,4,5,6,7,8,9,10)
def impresion (matriz):
    for z in matriz:
        print (z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8],z[9],z[10])

matriz_usuario = [
[" " ],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[]
]

z= 1
for y in range(1,11):
    matriz_usuario[y].append( z )
    z += 1

w=1
for y in columnas:
    matriz_usuario[0].insert(w,y)
    w +=1

for y in range (1,11):
    while len(matriz_usuario[y]) <= 10:
        matriz_usuario[y].append("O")

impresion(matriz_usuario)

matriz_pc= [
[" " ],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[]
]

z= 1
for y in range(1,11):
    matriz_pc[y].append( z )
    z += 1

w=1
for y in columnas:
    matriz_pc[0].insert(w,y)
    w +=1

for y in range (1,11):
    while len(matriz_pc[y]) <= 10:
        matriz_pc[y].append(0)

impresion(matriz_pc)

class Flota ():
    __init__(self,posiones)
juego = 0
while juego = 0:
    diccionario_cordd: {
    1:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    2:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    3:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    4:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    5:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    6:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    7:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    8:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    9:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1},
    10:{"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1}
    }

    puntacion = 0


