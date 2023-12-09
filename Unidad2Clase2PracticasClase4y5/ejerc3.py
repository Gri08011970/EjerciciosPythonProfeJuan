#ejercicio número 3 de Prácticas de las clases 4y5. Molina Griselda

a = int(input("Ingresa un número:"))
b = int(input("Ingresa otro número:"))
c = int

if a==b:
    print("Ingresa dos números diferentes:")

#cambio de valores para asegurarnos que la variable c, siempre sea mayor a la variable a.

else:
    if a > b:
        c = b
        b = a
        a = c


    while a <= b:
        if a % 2 == 0:
            print("El número ",a," es par")
        else:
         print("El número ",a," es impar")  
        a = a + 1 