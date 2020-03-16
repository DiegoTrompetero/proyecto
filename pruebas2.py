import ast
diccionario = {}
ruta = "c:/Users/diego/OneDrive/Documentos/Proyecto_Algoritmo_Diego/Basededatos.txt"
archivo = open(ruta, "r")
jdic = archivo.read()
diccionario = ast.literal_eval(jdic)

archivo.close()

print (diccionario)


