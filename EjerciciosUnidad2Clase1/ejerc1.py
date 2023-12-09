#ejercicio 1 Unidad 2 Clase 1. Griselda Molina

nota1 = float(input("ingrese la primera nota (entre 1 y 10):"))
nota2 = float(input("ingrese la segunda nota (entre 1 y 10):"))
nota3 = float(input("ingrese la tercer nota (entre 1 y 10):"))

promedio = (nota1 + nota2 + nota3)/3

if promedio > 6 and promedio <= 10:
   print("¡Felicitaciones! Promocionaste la materia.")
elif promedio >= 4 and promedio <=6:
    print("Alumno en condición de rendir final.")
elif promedio >= 1 and promedio <= 3:
        print("Alumno RECURSA la materia.")
else:
            print("Ingrese una calificación válida.")