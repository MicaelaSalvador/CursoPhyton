def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

print("Introduzca un numero:\n")
numero1 = int(input())
print("Introduzca otro  numero:\n")
numero2 = int(input())

while True:
    print("Menu")
    print("Elija la opcion para operar :\n 1.Multiplicar\n 2.Dividir \n 3.Sumar\n 4.Restar\n 5.Apagar la calculadora")
    opcion=input()
    
    if opcion == "1":
      resMultiplicar=  multiplicar(numero1,numero2)
      print(resMultiplicar)
      break
    elif opcion =="2":
        resDividir=dividir(numero1,numero2)
        print(resDividir)
        break
        
    elif opcion =="3":
        resSumar=sumar(numero1,numero2)
        print(resSumar)
        break
        
    elif opcion =="4":
        resRestar = restar(numero1,numero2)
        print(resRestar)
        break
    elif opcion =="5" :
        print("Saliendo de la calculadora")
        break
    else:
        print("Opcion Incorrecta")