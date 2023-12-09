# números ordenados de menor a mayor  usando listas y sus métodos.

lista = [17,7,19]

#  imprime la lista NO ordenada
print("Lista desordenada: ",lista)

# Ordena la lista
lista.sort()

# imprime  la lista ordenada
print("Lista Ordenada: ", lista)


numeros_ordenados = sorted([8,1,70])

print("ordenados en orden ascendente: ", numeros_ordenados)

numeros_ordenados = sorted([14,9,71], reverse=True)

print("Ordenados en orden descendente: ", numeros_ordenados)