#ejercicio número 4 de Prácticas de las clases 4y5. Molina Griselda

print("Ingrese números enteros. Ingrese 0 para terminar.")

numeros = []

while True:
    numero = int(input("Ingrese un número entero (o 0 para terminar): "))
    if numero == 0:
        break
    numeros.append(numero)

# Verificar si se ingresaron números
if numeros:
    # Encontrar el número mayor y el menor
    numero_mayor = max(numeros)
    numero_menor = min(numeros)

    
    print(f"El número mayor es: {numero_mayor}")
    print(f"El número menor es: {numero_menor}")
else:
    print("No se ingresaron números.")


