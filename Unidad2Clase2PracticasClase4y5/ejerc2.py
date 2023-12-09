#ejercicio número 2 de Prácticas de las clases 4y5. Molina Griselda

número = int(input("Ingrese un número entero mayor que cero: "))


múltiplos = []

# Verificar si el número es múltiplo de 2, 3, 4, 5, 6, 7, 8 o 9 y agregarlos a la lista
for divisor in range(2, 9):
    if número % divisor == 0:
        múltiplos.append(divisor)

# Si se encontraron múltiplos, mostrar la lista ordenada de mayor a menor
if múltiplos:
    múltiplos.sort(reverse=True)
    print("Los divisores encontrados son:", múltiplos)
else:
    print("No se encontraron divisores exactos")
