#11-Tipos de datos
#Tipo de dato que se le asgina a una variable
#entero, flotante, booleano

#None, tipo de dato que indica que la variable no tiene nada
perro = None
print(perro)
#Mostrar el tipo de dato, la funcion type se le da un dato , y dira el tipo de dato
print(type(perro))
print("-----------------------------")

#dato cadena, se le conoce como string, un conjunto de caracteres
cadena = "Hola me llamo Jose"
print(cadena)
print(type(cadena))
print("-----------------------------")

#dato entero ,es un numero entero int
entero  = 99
print(entero)
print(type(entero))
print("-----------------------------")

#dato flotante , es un numero decimal float
flotante = 25.5
print(flotante)
print(type(flotante))
print("-----------------------------")

#dato booleano, dato que indica si una variable es True or False , usa tipo CamelCase
booleano1 = True
booleano2 = False
print(f"{booleano1} , {booleano2}")
print(type(booleano1))
print(type(booleano2))
print("-----------------------------")

#tipo de dato lista o array, arreglo, es una coleccion de datos o variables. usa "[a,b,c]"
lista = [10,20,30,40]
print(lista)
print(type(lista))
print("-----------------------------")

#lista de datos variados
lista_string = [44, "treinta", 49, "uno"]
print(lista_string)
print(type(lista_string))
print("-----------------------------")
#tupla, es una lista de datos que no cambian y usa "(a,b,c)"
tupla = ("master", "en", "python")
print(tupla)
print(type(tupla))
print("-----------------------------")

#diccionario , es un tipo de array asociativo , o un documento formato JSON, que permite tener una clave y un valor
#{"clave": "valor" , "clave2": "valor2"}
diccionario = {
    "nombre": "Jose",
    "apellido": "Brown",
    "pagina_web": "josebrown.com"
}
print(diccionario)
print(type(diccionario))
print("-----------------------------")

#dato rango, defino la funcion range, imprime un rango definido. range(numero)
rango = range(9)
print(rango)
print(type(rango))
print("-----------------------------")

#dato set, es parecido a una tupla, son valores asignados, no son tipo clave-valor
#frozenset ,  es parecido a un set , péro con datos congelados, osea , que no se pueden cambiar
#dato byte, b"string"
dato_byte = b"hola"
print(dato_byte)
print(type(dato_byte))
print("-----------------------------")
 
#12- Convertir de un tipo de dato a otro
 #Nos dara error , por que estamos concatenando un string con int, usamos str(), para convertir a un string
texto = "Hola"
numero = str(10)
print(texto +" " + numero)
#Se puede forzar un tipo de dato , para que cambie a otro. str(), float(), int().




