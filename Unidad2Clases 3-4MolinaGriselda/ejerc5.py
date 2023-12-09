# Función para contar las vocales en una palabra
def contar_vocales(palabra):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in palabra:
        letra_lower = letra.lower()
        if letra_lower in vocales:
            vocales[letra_lower] += 1
    return vocales

print("Ingrese palabras. Escriba 'Fin del ingreso' para terminar.")
palabras = []
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra.lower() == 'fin del ingreso':
        break
    palabras.append(palabra)

# Contar la cantidad total de letras y la cantidad de cada vocal
cantidad_total_letras = sum(len(palabra) for palabra in palabras)
vocales_totales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for palabra in palabras:
    vocales_palabra = contar_vocales(palabra)
    for vocal, cantidad in vocales_palabra.items():
        vocales_totales[vocal] += cantidad


print(f"\nCantidad total de letras ingresadas: {cantidad_total_letras}")
print("Cantidad de cada vocal:")
for vocal, cantidad in vocales_totales.items():
    print(f"{vocal}: {cantidad}")
