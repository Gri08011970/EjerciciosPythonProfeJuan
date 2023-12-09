# UNIDAD 3 CLASE 1 EJERCIO 9 CONTROL DE FLUJO. MOLINA GRISELDA.

numero = int(input("Ingrese un número entero: "))

# Mostrar un triángulo con el patrón de números
for i in range(1, numero + 1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()
