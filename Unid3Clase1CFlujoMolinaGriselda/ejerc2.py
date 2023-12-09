# UNIDAD 3 CLASE 1 EJERCIO 2 CONTROL DE FLUJO. MOLINA GRISELDA
segundos = int(input("Escriba la cantidad de minutos a convertir:"))

días = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos = segundos // 60
segundos = segundos % 60
print("Días: {} - Horas: {} - Minutos: {} - Segundos: {}".format(días, horas, minutos, segundos))