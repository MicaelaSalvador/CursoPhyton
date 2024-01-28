while True:
    print("Escribe una opcion:\n 1.Comparar dos numeros: \n 2. Introduzca un numero impar: \n 3.Terminar el programa")
    opcion =input()
    if opcion == "1":
        print("\nIntroduzca un numero\n")
        a=int(input())
        print("\nIntroduzca otro numero\n")
        b=int(input())
        if a == b :
            print("\nLos numeros son iguales\n")
        elif a > b :
            print("\n A es mayor que B \n")
        else :
            print("\n A es menor que B \n")
    elif opcion =="2":
        print("\n Introduzca un numero \n")
        a=int(input())
        while a %2 == 0 :
            print("\n Numero Par, introduzca otro numero \n")
            a=int(input())
            print("a es impar")
    elif opcion =="3":
        break
    else:
        print("Opcion incorrecta")
        
      
        