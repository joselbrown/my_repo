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
"""

print("\n####EJEMPLO 3####")
nombre = input("Ingresa tu nombre: ")
continente = input("Ingrese su continente: ")
edad = int(input("Ingresa tu edad: "))
mayoria_edad = 18
jubilacion = 65
continente1 = "America"
continente2 = "Europa"
ontinente3 = "Asia"


if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad, tiene {edad}")
    if continente == continente1 :
        print("Usted es Americano")
    else:
        print(f"{nombre} no es Americano")
else:
    print(f"{nombre} no es mayor de edad , no tiene {mayoria_edad}")


