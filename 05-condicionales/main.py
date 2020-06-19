#18- Condicionales 
#Es una estructura de control que permite controlar el flujo del programa
#Si un dato cumple una condicion se ejecutaran una serie de instruciones , sino se cumple se ejecutan otras
"""
Si se_cumple_esta_condicion:
    Ejecutr un grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

#Ejemplo 1
print("####EJEMPLO 1####")
color = input("Adivina mi color favorito: ")
if color == "rojo":
    print("Correcto")
else:
    print("Incorrecto")

#19- Operadores de comparacion

== , igual
!= , diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que  

print("\n####EJEMPLO 2####")
year = int(input("¿En que año estamos?"))
if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")


print("\n####EJEMPLO 3####")
nombre = input("Ingresa tu nombre: ")
continente = input("Ingrese su continente: ")
edad = int(input("Ingresa tu edad: "))
mayoria_edad = 18j
jubilacion = 65
continente1 = "America"
continente2 = "Europa"
continente3 = "Asia"
continente4 = "Africa"

if edad >=18 and continente == continente1 and edad <= jubilacion:
    print(f"{nombre} es americano,mayor de {edad} años de edad y no es jubilado.")
elif edad <=18 and continente == continente1:
        print(f"{nombre} es americano, menor de {edad} años de edad.")

##21 - elif

dia = int(input("Ingrese el numero del dia de la semana: "))
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

#22- Operadores logicos
#And y
#Or o
#Negacion !
#not No
"""
#Ejemplo 6 operador or

pais = "Colombia"
if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

#Ejemplo 7 operador not

pais = "Colombia"
if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais}  no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")

#Operador !=
pais = "USA"
if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais}  no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")