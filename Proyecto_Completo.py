ruta = "c:/Users/diego/OneDrive/Documentos/Proyecto_Algoritmo_Diego/Basededatos.txt"
rutados =  "c:/Users/diego/OneDrive/Documentos/Proyecto_Algoritmo_Diego/Listatop.txt"
rutatres = "c:/Users/diego/OneDrive/Documentos/Proyecto_Algoritmo_Diego/Estadisticas.txt"
import ast
import random

columnas = ("a","b","c","d","e","f","g","h","i","j")
filas = (1,2,3,4,5,6,7,8,9,10)

class Usuario ():
    def __init__ (self,Username,Nombres,Apellidos,Edad,Genero,Puntuacion_Max):
        self.Username = Username
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Edad = Edad
        self.Genero = Genero
        self.Puntuacion_Max = Puntuacion_Max

    def ordenar (self):
        return{
            "Nombres": self.Nombres,
            "Apellidos": self.Apellidos,
            "edad": self.Edad,
            "Genero": self.Genero,
            "Puntuacion maxima": self.Puntuacion_Max
        }

def validarEntero(num):
    isValid = False
    try:
        int(num)
        isValid = True
    except ValueError:
        isValid = False
    return isValid

def pedirNumeroEnteroValidado(messages = "Ingrese un numero Enter0"):
    num = input(messages)
    while not validarEntero(num):
        print("Error valor ingresado incompatible")
        num = input(messages)
    return int(num)  

def rellenarBD(diccionario):
    archivo = open(ruta, "r")
    jdic = archivo.read()
    diccionario = ast.literal_eval(jdic)
    archivo.close()
    return diccionario

def actualizaBD (dic):
    archivo = open(ruta, "w")
    archivo.write (str(dic))
    archivo.close()
    print ("Base de datos actualizada")
    return

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
    return True

def ImpresionTop (Lista):
    archivo = open (rutados, "r")
    n =0
    for linea in archivo.readlines():
        print (n,".  " ,linea)
        n +=1

def impresion (matriz):
    for z in matriz:
        print (z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8],z[9],z[10])

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
                        Cordenadaspc [filex+2][columnas[columnas.index(Golum)]] = 0
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

class Flota ():
    def __init__(self,posiones): 
        self.posiones= posiones

class Buque3(Flota):
    def __init__ (self,posiones,tipo):
        Flota.__init__(self,posiones)
        self.tipo = tipo

    def catalogar (self):
        print ("Un buque de {} posiones {} pista de aterrizaje".format(self.posiones,self.tipo))

class Buque2(Flota):
    def __init__ (self,posiones,tipo):
        Flota.__init__(self,posiones)
        self.tipo = tipo

    def catalogar (self):
        print ("Un buque de {} posiones {} la capacidad de comunicarse".format(self.posiones,self.tipo))

class Submarinos (Flota):
    def __init__ (self,posiones,tipo):
        Flota.__init__(self,posiones)
        self.tipo = tipo

    def catalogar (self):
        print ("Un Submarino de {} posion {} ".format(self.posiones,self.tipo))
#Aqui Comienza el modulo 1

# /$$      /$$                 /$$           /$$                   /$$ /$$           /$$  
#| $$$    /$$$                | $$          | $$                  / $$/ $$         /$$$$  
#| $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$   /$$| $$  /$$$$$$        /$$$$$$$$$$      |_  $$  
#| $$ $$/$$ $$ /$$__  $$ /$$__  $$| $$  | $$| $$ /$$__  $$      |   $$  $$_/        | $$  
#| $$  $$$| $$| $$  \ $$| $$  | $$| $$  | $$| $$| $$  \ $$       /$$$$$$$$$$        | $$  
#| $$\  $ | $$| $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$      |_  $$  $$_/        | $$  
#| $$ \/  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$/| $$|  $$$$$$/        | $$| $$         /$$$$$$
#|__/     |__/ \______/  \_______/ \______/ |__/ \______/         |__/|__/        |______/
                                                                                         
                                                                                         
Base_de_Jugadores = {}

print ('''
  ____        _        _ _         _   _                  _ 
 |  _ \      | |      | | |       | \ | |                | |
 | |_) | __ _| |_ __ _| | | __ _  |  \| | __ ___   ____ _| |
 |  _ < / _` | __/ _` | | |/ _` | | . ` |/ _` \ \ / / _` | |
 | |_) | (_| | || (_| | | | (_| | | |\  | (_| |\ V / (_| | |
 |____/ \__,_|\__\__,_|_|_|\__,_| |_| \_|\__,_| \_/ \__,_|_|''')
                                                            
                                                            

print ("Bienvenido a Batalla naval")
print ("Producto de SamanGames G.C")

archivo = open(ruta, "r")
jdic = archivo.read()
Base_de_Jugadores = ast.literal_eval(jdic)
archivo.close()

Username = str(input('''Ingrese su nombre de usuario:
(debe ser menor a 30 caracteres y no debe contener espacios)
'''))

ingreso = 0
while ingreso == 0:
    if Username not in Base_de_Jugadores:
        pregunta = str(input("Primera vez que juegas: Si[s] NO [n]:  "))
        while pregunta.lower() != "n" and pregunta.lower() != "s":
            pregunta = str(input("Primera vez que juegas: Si[s] NO [n]"))
        if pregunta.lower() == "n":
             Username = str(input('''Ingrese su nombre de usuario:
                (debe ser menor a 30 caracteres y no debe contener espacios)
                '''))
        elif pregunta.lower() == "s":
            while len(Username) >= 30:
                Username = str(input('''Ingrese su nombre de usuario:
                (debe ser menor a 30 caracteres y no debe contener espacios)
                '''))

            while Username in Base_de_Jugadores:
                print("Ya ese nombre existe")
                Username = str(input('''Ingrese su nombre de usuario:
                (debe ser menor a 30 caracteres y no debe contener espacios)
                '''))
            
            Verificacion = False
            while Verificacion == False:
                Espacio = False
                for x in Username:
                    if x == " ":
                        Espacio = True
                if Espacio == True:
                    print("Sigue lo indicado")
                    Username = str(input('''Ingrese su nombre de usuario:
                     (debe ser menor a 30 caracteres y no debe contener espacios)
                     '''))
                elif Espacio == False:
                    Verificacion = True

            Nombres = input ("Ingrese sus Nombres: ")
            Apellidos = input ("Ingrese sus apellidos: ")
            Edad = pedirNumeroEnteroValidado( "Ingrese su edad: ")
            Nombre_completo = str(Nombres) + " " + str(Apellidos)
            Genero = str(input("Ingrese H para hombreo M para Mujer: "))
            while Genero.lower( ) != "m" and Genero.lower() != "h":
                print("ingrese los datos pedidos")
            if Genero.lower() == "h":
                Genero = "Hombre"

            elif Genero.lower( )== "m":
                Genero = "Mujer"


            print("Datos del nuevo usuario:")
            print("Nombre de usuario:", Username)
            print("Nombre completo: ", Nombre_completo)
            print("Genero: ", Genero)
            print("Edad: ",Edad)
            Base_de_Jugadores[Username] = Usuario(Username,Nombres,Apellidos, Edad, Genero , 0).ordenar()
            actualizaBD (Base_de_Jugadores)

            quieres = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere cambiar tus datos de usuario: ")
            while quieres != 0 and quieres !=1:
                print("Ingrese lo deseado")
                quieres = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere cambiar tus datos de usuario: ")

            if quieres ==1:
                Nombres = input ("Ingrese sus Nombres: ")
                Apellidos = input ("Ingrese sus apellidos: ")
                Nombre_completo = str(Nombres) + " " + str(Apellidos)
                Edad = pedirNumeroEnteroValidado("Ingrese su edad: ")
                Puntuacion_Max = Base_de_Jugadores[Username]["Puntuacion maxima: "]
                print("Datos de usuario:")
                print("Nombre de usuario:", Username)
                print("Nombre completo: ", Nombre_completo)
                print("Genero: ", Genero)
                print("Edad: ",Edad)
                Base_de_Jugadores[Username] = Usuario(Username, Nombres,Apellidos, Edad, Base_de_Jugadores[Username]["Genero"],Puntuacion_Max).ordenar()
                actualizaBD (Base_de_Jugadores)
                quieres = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere salir: ")
                while quieres != 0 and quieres !=1:
                    print("Ingrese lo deseado")
                if quieres == 0 or quieres == 1:
                    ingreso = 1
            elif quieres == 0:
                deseo = 0
                ingreso = 1

    elif Username in Base_de_Jugadores : 
        deseo = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere cambiar tus datos de usuario: ")

        while deseo != 0 and deseo !=1:
            print("Ingrese lo deseado")
            deseo = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere cambiar tus datos de usuario: ")

        if deseo ==1:
            Nombres = input ("Ingrese sus Nombres: ")
            Apellidos = input ("Ingrese sus apellidos: ")
            Nombre_completo = str(Nombres) + " " + str(Apellidos)
            Edad = pedirNumeroEnteroValidado("Ingrese su edad: ")
            Puntuacion_Max = Base_de_Jugadores[Username]["Puntuacion maxima"]
            print("Datos de usuario:")
            print("Nombre de usuario:", Username)
            print("Nombre completo: ", Nombre_completo)
            print("Genero: ", Genero)
            print("Edad: ",Edad)
            Base_de_Jugadores[Username] = Usuario(Username, Nombres,Apellidos, Edad, Base_de_Jugadores[Username]["Genero"],Puntuacion_Max).ordenar()
            actualizaBD (Base_de_Jugadores)
            deseo = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere salir: ")
            while deseo != 0 and deseo !=1:
                print("Ingrese lo deseado")
                deseo = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere salir: ")
                if deseo == 0 or deseo == 1:
                    ingreso = 1
                    
        if deseo == 0:
            ingreso= 1

 
# __       __                  __            __                    __  __     ______                           __  __     ______  
#/  \     /  |                /  |          /  |                  /  |/  |   /      \                         /  |/  |   /      \ 
#$$  \   /$$ |  ______    ____$$ | __    __ $$ |  ______         _$$ |$$ |_ /$$$$$$  |       __    __        _$$ |$$ |_ /$$$$$$  |
#$$$  \ /$$$ | /      \  /    $$ |/  |  /  |$$ | /      \       / $$  $$   |$$____$$ |      /  |  /  |      / $$  $$   |$$ ___$$ |
#$$$$  /$$$$ |/$$$$$$  |/$$$$$$$ |$$ |  $$ |$$ |/$$$$$$  |      $$$$$$$$$$/  /    $$/       $$ |  $$ |      $$$$$$$$$$/   /   $$< 
#$$ $$ $$/$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |      / $$  $$   |/$$$$$$/        $$ |  $$ |      / $$  $$   | _$$$$$  |
#$$ |$$$/ $$ |$$ \__$$ |$$ \__$$ |$$ \__$$ |$$ |$$ \__$$ |      $$$$$$$$$$/ $$ |_____       $$ \__$$ |      $$$$$$$$$$/ /  \__$$ |
#$$ | $/  $$ |$$    $$/ $$    $$ |$$    $$/ $$ |$$    $$/         $$ |$$ |  $$       |      $$    $$ |        $$ |$$ |  $$    $$/ 
#$$/      $$/  $$$$$$/   $$$$$$$/  $$$$$$/  $$/  $$$$$$/          $$/ $$/   $$$$$$$$/        $$$$$$$ |        $$/ $$/    $$$$$$/  
#                                                                                           /  \__$$ |                            
#                                                                                           $$    $$/                             
#                                                                                            $$$$$$/                              

if deseo == 0 or quieres == 0:
    lista_top = []
    LeerTop(lista_top)
    Lista_Estadisticas = []
    leerestadisticas(Lista_Estadisticas)
    sesion = 0
    while sesion == 0:
        ver = pedirNumeroEnteroValidado('''A donde desea ingresar:
         1) Entrar al juego 
         2) Ver top 10
         3) Entrar en las estadisticas
         4) Cerrar Sesion
         ''')

        while ver != 1 and ver !=2 and ver != 3 and ver != 4:
           ver = pedirNumeroEnteroValidado('''A donde desea ingresar:
             1) Entrar al juego 
             2) Ver top 10
             3) Entrar en las estadisticas
             4) Cerrar sesion
             ''')
    
        if ver == 2:
            print('''
                  _____             __  _____ 
                 |_   _|           /  ||  _  |
                   | | ___  _ __   `| || |/' |
                   | |/ _ \| '_ \   | ||  /| |
                   | | (_) | |_) | _| |\ |_/ /
                   \_/\___/| .__/  \___/\___/ 
                           | |                
                           |_|                
                ''')

            ImpresionTop(lista_top)
            pregunta = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu princilpal o 1 si quieres cerrar sesion: ")
            while pregunta != 0 and pregunta !=1:
                print("Ingresa lo indicado")
                pregunta = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu princilpal o 1 si quieres cerrar sesion: ")
            
            if pregunta == 1:
                sesion = 1


        elif ver == 1:
            #2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            usuario = 0
            while usuario == 0:
                Usernameactivo = Username
                Datosdeljugador = {"Usuario": Usernameactivo , "Puntuacion maxima": Base_de_Jugadores[Username]["Puntuacion maxima"]}
                juego = 0
                while juego == 0:
                    print("El enemigo tiene lo siguiente en el tablero:")
                    Buquetres = Buque3("tres", random.choice(["con", "sin"])).catalogar()
                    Buquedos =Buque2("dos", random.choice(["con", "sin"])).catalogar()
                    sub1 = Submarinos("una", random.choice (["sumergido", "sin sumergirse"])).catalogar() 
                    sub2 = Submarinos("una", random.choice (["sumergido", "sin sumergirse"])).catalogar()
                    sub3 = Submarinos("una", random.choice (["sumergido", "sin sumergirse"])).catalogar()
                    sub4= Submarinos("una", random.choice (["sumergido", "sin sumergirse"])).catalogar()
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


                    print('''

                     /$$$$$$$$ /$$          
                    | $$_____/|__/          
                    | $$       /$$ /$$$$$$$ 
                    | $$$$$   | $$| $$__  $$
                    | $$__/   | $$| $$  \ $$
                    | $$      | $$| $$  | $$
                    | $$      | $$| $$  | $$
                    |__/      |__/|__/  |__/

                    ''')

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
                        print("Nuevo record: de {} a {} ptos". format( Datosdeljugador["Puntuacion maxima"], puntacion))
                        Datosdeljugador["Puntuacion maxima"] = puntacion
                        Base_de_Jugadores[Username]["Puntuacion maxima"] = puntacion
                        actualizaBD(Base_de_Jugadores)
                    
                    elif Datosdeljugador["Puntuacion maxima"] == 0  :
                        Datosdeljugador["Puntuacion maxima"] = puntacion 


                    for x in range(1,11):
                        if Nuevo[1] > lista_top [x][1]:
                            print("Felicidades, entraste en el top 10 en la posicion {}".format(x))
                            lista_top.insert(x,Nuevo)
                            lista_top.pop()
                            escribirBaseDeDatos(lista_top)
                            ImpresionTop(lista_top)
                            break
                    #Agregar disparos
                    Lista_Estadisticas [9][0] = str(int(Lista_Estadisticas [9][0])+disparos)
                    #Agregar partida
                    Lista_Estadisticas[8][0] = str(int(Lista_Estadisticas[8][0])+1)
                    if Base_de_Jugadores[Username]["Genero"] == "Hombre":
                        #Partidas Hombre
                        Lista_Estadisticas[1][0] = str(int(Lista_Estadisticas[1][0])+1)
                        #Puntos Hombre
                        Lista_Estadisticas[0][0] = str(int(Lista_Estadisticas[0][0])+puntacion)
                    
                    elif Base_de_Jugadores[Username]["Genero"] == "Mujer":
                        #Partidas Mujeres
                        Lista_Estadisticas[3][0] = str(int(Lista_Estadisticas[3][0])+1)
                        #Puntos Mujeres
                        Lista_Estadisticas[2][0] = str(int(Lista_Estadisticas[2][0])+puntacion)

                    if Base_de_Jugadores[Username]["edad"] >= 5 and  Base_de_Jugadores[Username]["edad"] <= 18:
                        #Partida 5 a 18
                        Lista_Estadisticas[4][0] = str(int(Lista_Estadisticas[4][0])+1)

                    elif Base_de_Jugadores[Username]["edad"] >= 19 and Base_de_Jugadores[Username]["edad"] <= 45:
                        #Partida 19 a 45
                        Lista_Estadisticas[5][0] = str(int(Lista_Estadisticas[5][0])+1)
                        
                    elif Base_de_Jugadores[Username]["edad"] >= 46 and Base_de_Jugadores[Username]["edad"] <= 60:
                        #Partida 46 a 60
                        Lista_Estadisticas[6][0] = str(int(Lista_Estadisticas[6][0])+1)

                    elif Base_de_Jugadores[Username]["edad"] >= 61 and Base_de_Jugadores[Username]["edad"] <= 100:
                        #Partida 61 a 100
                        Lista_Estadisticas[7][0] = str(int(Lista_Estadisticas[7][0])+1)


                    Escribirestadisticas (Lista_Estadisticas)
                    continuar = pedirNumeroEnteroValidado("Ingrese 0 si quiere jugar de nuevo o 1 si quieres salir")
                    while continuar !=0 and continuar !=1 :
                        print("Ingrese los valores desados")
                        continuar = pedirNumeroEnteroValidado("Ingrese 0 si quiere jugar de nuevo o 1 si quieres salir")
                    if continuar ==0:
                        juego = 0
                    elif continuar == 1:
                        juego = 1
                        usuario = 1
            Escribirestadisticas (Lista_Estadisticas)
            cerrar = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu princilpal o 1 si quieres cerrar sesion: ")
            while cerrar != 0 and cerrar !=1:
                print("Ingresa lo indicado")
                cerrar = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu princilpal o 1 si quieres cerrar sesion: ")
            
            if cerrar == 1:
                sesion = 1
        

        elif ver ==3:
            #3333333333333333333333333333333333333333333333333333333333333333333333333333
            print('''
           
  ______     _            _ _     _   _               
 |  ____|   | |          | (_)   | | (_)              
 | |__   ___| |_ __ _  __| |_ ___| |_ _  ___ __ _ ___ 
 |  __| / __| __/ _` |/ _` | / __| __| |/ __/ _` / __|
 | |____\__ \ || (_| | (_| | \__ \ |_| | (_| (_| \__ \\
 |______|___/\__\__,_|\__,_|_|___/\__|_|\___\__,_|___/
                                                      
           ''')
           
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

            cerrar = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu princilpal o 1 si quieres cerrar sesion: ")
            while cerrar != 0 and cerrar !=1:
                print("Ingresa lo indicado")
                cerrar = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu princilpal o 1 si quieres cerrar sesion: ")
            
            if cerrar == 1:
                sesion = 1

        elif ver == 4:
            sesion =1

print('''

  /$$$$$$        /$$ /$$                    
 /$$__  $$      | $$|__/                    
| $$  \ $$  /$$$$$$$ /$$  /$$$$$$   /$$$$$$$
| $$$$$$$$ /$$__  $$| $$ /$$__  $$ /$$_____/
| $$__  $$| $$  | $$| $$| $$  \ $$|  $$$$$$ 
| $$  | $$| $$  | $$| $$| $$  | $$ \____  $$
| $$  | $$|  $$$$$$$| $$|  $$$$$$/ /$$$$$$$/
|__/  |__/ \_______/|__/ \______/ |_______/ 
                                                                               

''')            
actualizaBD(Base_de_Jugadores)
Escribirestadisticas (Lista_Estadisticas)