
#ejercicio número 3bis de Prácticas de las clases 4y5. Molina Griselda

numInicial = int(input("Ingrese el primer número entero: "))
numFinal = int(input("Ingrese el segundo número entero: "))

# Inicializar el contador de números pares
InicioNumPares = 0

# Iterar desde el número inicial hasta el número final (incluyendo ambos extremos)
for numero in range(numInicial, numFinal + 1):
    if numero % 2 == 0:  
        InicioNumPares += 1  


print(f"La cantidad de números pares entre {numInicial} y {numFinal} es: {InicioNumPares}")
