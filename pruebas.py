import random

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
                        Cordenadaspc [filex+1][columnas[columnas.index(Golum)]] = 0
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

columnas = ("a","b","c","d","e","f","g","h","i","j")
def impresion (matriz):
    for z in matriz:
        print (z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8],z[9],z[10])
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

relleno_de_matriz(matriz_pc)

impresion(matriz_pc)
print (matriz_pc)
