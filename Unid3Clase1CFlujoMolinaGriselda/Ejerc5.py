# UNIDAD 3 CLASE 1 EJERCIO 5 CONTROL DE FLUJO. MOLINA GRISELDA

name = input("¿Cómo te llamas? ")
gender = input("¿Cómo te definís (H o M)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)


name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)