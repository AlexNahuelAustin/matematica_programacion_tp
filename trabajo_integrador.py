#menu para convertir de 1.binario a decimal o 2.decimal a binario o 3.salir del menu
while True:
    opcion = input("ingrese una opcion:\n 1.para conversor a binario\n 2.para el conversor a decimal.\n 3.salir \n ")
    if opcion == "1":
        print("pasaje de decimal a binario")
        numero = input("ingrese un numero del 0 al 14: ")
        try:
            numero = int(numero)
            if 0 <= numero <= 14:
                binario_convertido = bin(numero)[2:]
                print(f"el {numero} en binario es: {binario_convertido}")
            else:
                print("Por favor, ingrese un número entre 0 y 14: ")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    elif opcion == "2":
        print("conversor de binario a decimal")
        binario = input("ingrese un numero binario: ")
        try:
            decimal_convertido = int(binario, 2)
            if 0 <= decimal_convertido <= 14:
                print(f"El binario {binario} en decimal es: {decimal_convertido}")
            else:
                print("El número binario ingresado representa un valor fuera del rango 0-14.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número binario válido (solo 0s y 1s).")
    elif opcion == "3":
        print("saliendo")
        break
    else:
        print("Opción inválida. Por favor, ingrese 1, 2 o 3.")




# conversor de binario a decimal(de 0 al 9, sino salta error e ingrese nuevamente el numero)






#conversor de decimal a binario (de 0 al 9, sino salta error e ingrese nuevamente el numero)






#juego de adivinar el numero y salte cuanto intentos tuvo o q sean con intentos prestablecido (si se acaban qur salga el numero secreto)


#Sistema conversor esta funcionando