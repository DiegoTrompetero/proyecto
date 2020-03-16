import random
rutados =  "c:/Users/diego/OneDrive/Documentos/Proyecto_Algoritmo_Diego/Listatop.txt"


columnas = ("a","b","c","d","e","f","g","h","i","j")
filas = (1,2,3,4,5,6,7,8,9,10)

def escribirBaseDeDatos(listaDeTop):
    archivo = open( rutados , "w")
    print("Escritura Iniciada")
    for vehiculo in listaDeTop:
        vehiculostr = str(vehiculo[0]) +"," + str(vehiculo[1]) + "," + str(vehiculo[2]) +"," + str(vehiculo[3])
        archivo.write(vehiculostr )
    archivo.close() 
    print("Escritura finalizada")
    return True

def LeerTop (ListadeTop):
    archivo = open (rutados, "r")
    for linea in archivo.readlines():
        lista = linea.split(",")
        ListadeTop.append(lista)
        print (linea)
    return True

def ImpresionTop (Lista):
    archivo = open (rutados, "r")
    for linea in archivo.readlines():
        print (linea)

def impresion (matriz):
    for z in matriz:
        print (z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8],z[9],z[10])

def pedirNumeroEnteroValidado(messages = "Ingrese un numero Entero"):
    num = input(messages)
    while not validarEntero(num):
        print("Error valor ingresado incompatible")
        num = input(messages)
    return int(num)

def validarEntero(num):
    isValid = False
    try:
        int(num)
        isValid = True
    except ValueError:
        isValid = False
    return isValid

def relleno_de_matriz (matriz):
    columnas = ("a","b","c","d","e","f","g","h","i","j")
    Cordenadaspc = {
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
    diccflotas = {1:4,2:1,3:1}
    
    while diccflotas [1] != 0 or diccflotas[2] != 0 or diccflotas[3] !=0 :
        cantidad = random.randint(1,3)
        Direccion = random.randint(0,1)
        if cantidad == 1:
            if diccflotas [cantidad] !=0:
                Golum = random.choice (["a","b","c","d","e","f","g","h","i","j"])
                filex = random.randint(1,10)
                if Cordenadaspc [filex][Golum] == 1:
                    Cordenadaspc [filex][Golum] == 0
                    matriz [filex][columnas.index(Golum)+1]= 1
                    diccflotas [1] += -1
                    if Golum == "a" and  filex == 1:
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0

                    elif Golum == "a" and filex == 10:
                        Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0

                    elif Golum == "a":
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                        Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0

                    elif Golum == "j" and filex ==1:
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                    elif Golum == "j" and filex == 10:
                        Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0

                    elif Golum == "j":
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0

                    elif  filex == 1:
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0

                    elif filex == 10: 
                        Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0

                    else:
                        Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
        if cantidad ==2:
            if diccflotas [cantidad] !=0:
                if Direccion == 0: 
                    Golum = random.choice (["a","b","c","d","e","f","g","h","i"])
                    filex = random.randint(1,10)

                    if  Cordenadaspc [filex][columnas[columnas.index(Golum)]] != 0 and Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] != 0:
                        Cordenadaspc [filex][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                        matriz [filex][columnas.index(Golum)+1] = 2 
                        matriz [filex][columnas.index(Golum)+2] = 2
                        diccflotas [2] += -1

                        if Golum == "a" and  filex == 1:
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+2]] = 0

                        elif Golum == "a" and  filex == 10:
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+2]] = 0

                        elif Golum == "i" and filex == 1: 
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0

                        elif Golum == "i" and  filex == 10:
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0

                        elif Golum == "a": 
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0

                        elif Golum == "i":
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0

                        elif filex ==1:
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0

                        elif filex == 10:
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0



                        else:
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+2]] = 0

                if Direccion == 1:
                    Golum = random.choice (["a","b","c","d","e","f","g","h","i","j"])
                    filex = random.randint(1,9)
                        
                    if Cordenadaspc [filex][columnas[columnas.index(Golum)]] != 0 and Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] != 0:
                        Cordenadaspc [filex][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                        matriz [filex][columnas.index(Golum)+1] = 2 
                        matriz [filex+1][columnas.index(Golum)+1] = 2
                        diccflotas [2] += -1

                        if Golum == "a" and  filex == 1:
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0

                        elif Golum == "a" and  filex == 9:
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0

                        elif Golum == "j" and filex == 1: 
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0

                        elif Golum == "j" and  filex == 9:
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0

                        elif Golum == "a":
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0

                        elif Golum == "j":
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0           
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0

                        elif filex == 1:
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0           
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                        
                        elif filex == 9:
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0           
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                        
                        else: 
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0           
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)]] = 0


                        
        if cantidad == 3:
            if diccflotas [cantidad] !=0:
                if Direccion == 0: 
                    Golum = random.choice (["a","b","c","d","e","f","g","h"])
                    filex = random.randint(1,10)
                    if Cordenadaspc [filex][columnas[columnas.index(Golum)]] != 0 and Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] != 0 and Cordenadaspc [filex][columnas[columnas.index(Golum)+2]]:
                        Cordenadaspc [filex][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                        Cordenadaspc [filex][columnas[columnas.index(Golum)+2]] = 0
                        matriz [filex][columnas.index(Golum)+1] = 3 
                        matriz [filex][columnas.index(Golum)+2] = 3
                        matriz [filex][columnas.index(Golum)+3] = 3 
                        
                        diccflotas [3] += -1
                        if Golum == "a" and  filex == 1:
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+3]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+2]] = 0


                        elif Golum == "a" and  filex == 10:
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+3]] = 0

                        elif Golum == "h" and filex == 1: 
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+2]] = 0

                        elif Golum == "h" and  filex == 10:
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+2]] = 0

                        elif Golum == "a": 
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+3]] = 0


                        elif Golum == "h":
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0

                        elif filex ==1:
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+3]] = 0


                        elif filex == 10:
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+3]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+2]] = 0

                        else:
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)+2]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+3]] = 0

                if Direccion == 1: 
                    Golum = random.choice (["a","b","c","d","e","f","g","h","i","j"])
                    filex = random.randint(1,8)
                    if Cordenadaspc [filex][columnas[columnas.index(Golum)]] != 0 and Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] != 0 and Cordenadaspc [filex+2][columnas[columnas.index(Golum)]]:
                        Cordenadaspc [filex][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
                        matriz [filex][columnas.index(Golum)+1] = 3
                        matriz [filex+1][columnas.index(Golum)+1] = 3
                        matriz [filex+2][columnas.index(Golum)+1] = 3 
                        
                        diccflotas [3] += -1   
                        if Golum == "a" and  filex == 1:
                            Cordenadaspc [filex+3][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)+1]] = 0

                        elif Golum == "a" and  filex == 8:
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)+1]] = 0

                        elif Golum == "j" and filex == 1: 
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+3][columnas[columnas.index(Golum)]] = 0

                        elif Golum == "j" and  filex == 8:
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)-1]] = 0

                        elif Golum == "a":
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+3][columnas[columnas.index(Golum)]] = 0

                        elif Golum == "j":
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+3][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0           
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)-1]] = 0

                        elif filex == 1:
                            Cordenadaspc [filex+3][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0           
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)+1]] = 0
                        
                        elif filex == 8:
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0           
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)+1]] = 0

                        else: 
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)-1]] = 0           
                            Cordenadaspc [filex][columnas[columnas.index(Golum)-1]] = 0
                            Cordenadaspc [filex+1][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex-1][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+3][columnas[columnas.index(Golum)]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)+1]] = 0
                            Cordenadaspc [filex+2][columnas[columnas.index(Golum)-1]] = 0

lista_top = []

LeerTop(lista_top)

class Flota ():
    __init__(self,posiones)
    self.posiciones= posiciones


usuario = 0
while usuario == 0:
    Usernameactivo = Username
    Datosdeljugador = {"Usuario": Usernameactivo , "Puntuacion maxima": Base_de_Jugadores[Username]["Puntuacion maxima"]}
    juego = 0
    while juego == 0:
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

        relleno_de_matriz (matriz_pc)
        impresion(matriz_pc)

        
        diccionario_cordd= {
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

        disparos = 0
        puntacion = 0
        disparosrep= 0
        diccfloat = 9
        Final= False
        while Final == False :

            columna = str(input("Ingrese la columna a,b,c,d,e,f,g,h: "))
            while columna.lower() not in columnas:
                    print ("Coloque los valores pedidos")
                    columna = str(input("Ingrese la columna a,b,c,d,e,f,g,h: "))
        
            fila = pedirNumeroEnteroValidado("Ingrese el numero de fila del 1 al 10: ")
        
            while fila not in filas: 
                print ("Coloque los valores pedidos")
                fila = pedirNumeroEnteroValidado("Ingrese el numero de fila del 1 al 10: ")

        
            if diccionario_cordd[fila][columna] == 0:
                print ("Esa cordenada ya fue colocada, intente con otra")
                disparosrep += 1
            
            elif diccionario_cordd[fila][columna] == 1:
                disparos +=1 
                diccionario_cordd[fila][columna] = 0
               

                if matriz_pc[fila][columnas.index(columna)+ 1] !=0:
                    puntacion += 10
                    diccfloat += -1
                    print("Bien")
                    matriz_usuario[fila][columnas.index(columna)+ 1] = "F"
                    matriz_pc[fila][columnas.index(columna)+ 1] = "F"
                    impresion(matriz_usuario)
                    

                elif matriz_pc[fila][columnas.index(columna)+ 1] ==0:
                    puntacion += -2
                    print("Fallaste")
                    matriz_usuario[fila][columnas.index(columna)+ 1] = "X"
                    impresion(matriz_usuario)

                if diccfloat == 0:
                    Final = True

                

                
        if disparos ==9:
            print("¿Eres un Robot? lo que acabas de hacer es poco probable ....")
        
        print("Usuario: {}".format(Usernameactivo))
        print ("Disparos realizados: ", disparos)
        print ("Puntos obtuvidos: {} ptos ".format(puntacion))
        print("Disparos repetidos: ", disparosrep )
        if disparos < 45:
            print("Exelente Estrategia")
        elif disparos >= 45 and disparos <= 70:
            print ("Buena Estrategia; pero hay que mejorar")
        elif disparos > 70:
            print ("Considerese perdedor, tiene que mejorar notablemente")
        
        Nuevo = [Usernameactivo, str(puntacion), str(disparos), "\n" ]
        if puntacion > Datosdeljugador["Puntuacion maxima"]:
            Datosdeljugador["Puntuacion maxima"] = Puntuacion
        
        for x in range(1,11):
            if Nuevo[1] > lista_top [x][1]:
                lista_top.insert(x,Nuevo)
                lista_top.pop()
                ImpresionTop(lista_top)

        continuar = pedirNumeroEnteroValidado("Ingrese 0 si quiere jugar de nuevo o 1 si quieres salir")
        while continuar !=0 and continuar !=1 :
            print("Ingrese los valores desados")
            continuar = pedirNumeroEnteroValidado("Ingrese 0 si quiere jugar de nuevo o 1 si quieres salir")
        if continuar ==0:
            juego = 0
        elif continuar == 1:
            juego = 1
            usuario = 1
    
        
        


