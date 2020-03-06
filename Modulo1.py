class Usuario ():
    def __init__ (self,Username,Nombres,Apellidos,Edad,Genero,Puntuacion_Max):
        self.Username = Username
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Edad = Edad
        self.Genero = Genero
        self.Puntuacion_Max = Puntuacion_Max


Base_de_Jugadores = {}


print ("Bienvenido a Batalla naval")

Username = str(input('''Ingrese su nombre de usuario:
(debe ser menor a 30 carcateres y no debe contener espacios)
'''))

if Username not in Base_de_Jugadores:
    while len(Username) >= 30:
        Username = str(input('''Ingrese su nombre de usuario:
        (debe ser menor a 30 carcateres y no debe contener espacios)
        '''))

    Verificacion = False
    while Verificacion == False:
        Espacio = False
        for x in Username:
            if x == " ":
                Esapacio = True

        if Espacio:
            Username = str(input('''Ingrese su nombre de usuario:
            (debe ser menor a 30 carcateres y no debe contener espacios)
            '''))

        elif Espacio == False:
            Verificacion == True

    Nombres = input ("Ingrese sus Nombres")
    Apellidos = input ("Ingrese sus apellidos")
    Nombre_completo = str(Nombres) + " " + str(Apellidos)
    Genero = str(input("Ingrese H para hombreo M para Mujer"))
    
    if Genero.lower() == "h":
        Genero = "Hombre"

    elif Genero.lower( )== "m":
        Genero = "Mujer"

    elif Genero.lower( ) != "m" and Genero.lower() != "h":
        
