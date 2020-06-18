#9-Variables
#Una variable es una contenedor de informacion que dentro guardara un dato, se pueden
#crear muchas variables y que cada una tenga un dato dinstinto 

#Creamos variables y les asignamos un valor
texto1 = "Master en python"
texto2 = "hola mundo"
#Imprime
print(texto1)
print(texto2)
#sustituimos los valores de las variables ya creadas
texto1 = "Hola Python"
texo2 = "Mundo Python"

print("--------------------------------------")

#10-La concatenacion
#Es el poder unir dos variables os string
nombre = "Jose"      #string
apellido = "Brown"   #string
web = "josebrown.com" #string

# Concatenamos 3 strings con el signo de mas 
print(nombre + " " + apellido + " " + web )

# Concatenamos con f, permite incrustar dentro del texto , cualquier variable, usamos print(f"{variable}") 
print(f"{nombre} {apellido} {web}")

#Utilizando la funcion format , print("{}{}".format(variable1, variable2))
print("Hola me llamo {} {} mi web es {}".format(nombre,apellido,web))

#pasando unas variables como parametro a la funcion print
#no es concatenacion como tal , la funcion print toma las variables y las concatena ella misma.
print(nombre, apellido, web)



