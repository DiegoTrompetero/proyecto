class Usuario ():
    def __init__ (self,Username,Nombres,Apellidos,Edad,Genero,Puntuacion_Max):
        self.Username = Username
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Edad = Edad
        self.Genero = Genero
        self.Puntuacion_Max = Puntuacion_Max

    def ordenar ():
        diccdejugador = {
            "Nombres": self.Nombres
            "Apellidos": self.apellidos
            "edad": self.edad
            "Genero": self.Genero
            "Puntuacion maxima": Puntuacion_Max
        }

def validarEntero(num):
    isValid = False
    try:
        int(num)
        isValid = True
    except ValueError:
        isValid = False
    return isValid


Base_de_Jugadores = {}
diccionario_top= {}


print ("Bienvenido a Batalla naval")

Username = str(input('''Ingrese su nombre de usuario:
(debe ser menor a 30 caracteres y no debe contener espacios)
'''))

if Username not in Base_de_Jugadores:
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
                    Esapacio = True

            if Espacio:
                Username = str(input('''Ingrese su nombre de usuario:
                (debe ser menor a 30 caracteres y no debe contener espacios)
                '''))

            elif Espacio == False:
                Verificacion == True

        Nombres = input ("Ingrese sus Nombres")
        Apellidos = input ("Ingrese sus apellidos")
        Edad = validarEntero("Ingrese su edad")
        Nombre_completo = str(Nombres) + " " + str(Apellidos)
        Genero = str(input("Ingrese H para hombreo M para Mujer"))
        while Genero.lower( ) != "m" and Genero.lower() != "h":
            print("ingrese los datos pedidos")
        if Genero.lower() == "h":
            Genero = "Hombre"

        elif Genero.lower( )== "m":
            Genero = "Mujer"
        
        Puntuacion_Max = 0
        print("Datos del nuevo usuario:")
        print("Nombre de usuario:", Username)
        print("Nombre completo: ", Nombre_completo)
        print("Genero: ", Genero)
        print("Edad: ",Edad
        Base_de_jugadores[Username] = Usuario(Username, Nombres,Apellidos, Edad, Genero,Puntuacion_Max)

else:
    deseo = validarEntero("Ingrese 0 si quiere ingresar al juego o 1 si quiere cambiar tus datos de usuario")
    while deseo != 0 and deseo !=1:
        print("Ingrese lo deseado")
        deseo = validarEntero("Ingrese 0 si quiere ingresar al juego o 1 si quiere cambiar tus datos de usuario")

    if deseo ==1:

        Base_de_jugadores[Username] = Usuario(Username, Nombres,Apellidos, Edad, Genero,Puntuacion_Max)

    




   
        
