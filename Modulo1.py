ruta = "c:/Users/diego/OneDrive/Documentos/Proyecto_Algoritmo_Diego/Basededatos.txt"
import ast

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

        Verificacion = False
        while Verificacion == False:
            Espacio = False
            for x in Username:
                if x == " ":
                    Espacio = True
            if Espacio == True:
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
            Edad = pedirNumeroEnteroValidado("Ingrese su edad: ")
            Puntuacion_Max = Base_de_Jugadores[Username]["Puntuacion maxima: "]
            Base_de_Jugadores[Username] = Usuario(Username, Nombres,Apellidos, Edad, Base_de_Jugadores[Username]["Genero"],Puntuacion_Max).ordenar()
            actualizaBD (Base_de_Jugadores)
        

elif Username in Base_de_Jugadores : 
    deseo = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere cambiar tus datos de usuario: ")

    while deseo != 0 and deseo !=1:
        print("Ingrese lo deseado")
        deseo = pedirNumeroEnteroValidado("Ingrese 0 si quiere ingresar al juego o 1 si quiere cambiar tus datos de usuario: ")

    if deseo ==1:
        Nombres = input ("Ingrese sus Nombres: ")
        Apellidos = input ("Ingrese sus apellidos: ")
        Edad = pedirNumeroEnteroValidado("Ingrese su edad: ")
        Puntuacion_Max = Base_de_Jugadores[Username]["Puntuacion maxima"]

        Base_de_Jugadores[Username] = Usuario(Username, Nombres,Apellidos, Edad, Base_de_Jugadores[Username]["Genero"],Puntuacion_Max).ordenar()
        actualizaBD (Base_de_Jugadores)

if deseo == 0 and quieres == 0:
  pass  