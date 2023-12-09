# UNIDAD 3 CLASE 1 EJERCIO 7 CONTROL DE FLUJO. MOLINA GRISELDA

from datetime import datetime


fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")

# Convertir la cadena ingresada a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Calcular la diferencia entre las fechas
diferencia = fecha_actual - fecha_nacimiento

# Calcular años, meses y días
dias_totales = diferencia.days
años = dias_totales // 365
meses = (dias_totales % 365) // 30  # Aproximadamente 30 días por mes
dias = (dias_totales % 365) % 30

# Mostrar la edad en años, meses y días
print(f"Llevas aproximadamente: {años} años, {meses} meses y {dias} días de vida.")
