# continuación del ejercicio 4 de la unidad 3 de la clase 1.
#números ordenados de menor a mayor . Molina Griselda

print("Ingrese el primer número:")
número1 = int(input())
print("Ingrese el segundo número:")
número2 = int(input())
print("Ingrese el tercer número:")
número3 = int(input())

if(número1<número2<número3):
    print("",número1," - ", número2," - ",número3)
elif(número2<número1 and número1<número3):
     print("",número2," - ", número1," - ",número3)
elif(número3<número1 and número1<número2):
     print("",número3," - ", número1," - ",número2) 
elif(número3<número2 and número2<número1):
     print("",número3," - ", número2," - ",número1)   
elif(número1<número3 and número3<número2):
     print("",número1," - ", número3," - ",número2)    
elif(número2<número3 and número3<número1):
     print("",número2," - ", número3," - ",número1)  
else :
     print("ingresaste números iguales")                          