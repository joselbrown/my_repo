# el uso del guion , dentro de una variable, es incorrecto
#perro-negro = "animal"
perro_negro = "hola"
print(perro_negro)
print("-----------------------------")

# las dobles comillas, comillas simples
mi_texto = '"master"'
mi_texto2 = "en \"python\" " # la diagonal escapa a el siguiente caracter, escapa de la funcionalidad de la comilla
texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)
print("-----------------------------")

#uso de valores especiales , el salto de linea
texto_unido = mi_texto + "\n " + mi_texto2
print(texto_unido)
print("-----------------------------")

#uso de valores especiales, la tabulacion 
texto_unido = mi_texto + "\t " + mi_texto2
print(texto_unido)
print("-----------------------------")

#uso de valores especiales, el borrado de variables antecedentes
texto_unido = mi_texto + "\r " + mi_texto2
print(texto_unido)
print("-----------------------------")
