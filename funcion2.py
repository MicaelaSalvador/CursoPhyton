def validar(a,b):
    if a==b:
        return True
    else:
         return False
        
# a=5
# b=4
# validar_dato=validar(a,b)
# print(validar_dato)
lista=[1,2,3,4,5]
print("Ingrese un numero por teclado")
b=int(input())
for numero in lista :
   if validar(numero,b) :
    print("El numero b esta en la lista")
    break
else:
    print("El numero b no esta en la lista")

    