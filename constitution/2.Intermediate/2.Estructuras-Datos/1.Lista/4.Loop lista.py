#Loop lista

lista = [1,2,3,4,5]

for numero in lista:
    print(numero)

for numero in enumerate(lista):
    print(numero)

for index, numero in enumerate(lista):
    print(index, numero)
