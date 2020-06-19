"""
24- bucle for
es una estrcutura iterativa que se va a repetir x cantidad de veces
for variable in elemento iterable
    bloque de instrucciones
un elemento interable puede ser una lista, un rango , diccionario,etc

"""
contador = 0
resultado = 0

for contador in range(0, 10):
    print(f"Voy por el {contador}")

    resultado += contador
print(f"El resultado es: {resultado}")
print("-----------------------------")

#EJMEPLO DE TABLAS DE MULTIPLICAR

a = int(input("\nDe que numero quieres la tabla?: "))

if a<=1:
    a = 1
print(f"Tabla de del numero {a} , solo numeros positivos")
    
for b in range(1,11):
    print(f"{a} x {b} = {a * b}")
else:
    print("FIN")