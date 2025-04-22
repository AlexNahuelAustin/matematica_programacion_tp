#menu para convertir de 1.binario a decimal o 2.decimal a binario o 3.salir del menu
while True: # Se crea el Menu de opciones (While al entrar al True solo toma verdadero)
    opcion = input("ingrese una opcion:\n 1.para conversor a binario\n 2.para el conversor a decimal.\n 3.Juego \n 4.salir")
    if opcion == "1": # Primera opcion del menu
        print("pasaje de decimal a binario")
        numero = input("ingrese un numero del 0 al 14: ")
        try: # Variables que controla errores de manera controlada
            numero = int(numero)
            if 0 <= numero <= 14:
                binario_convertido = bin(numero)[2:] # Corte de cadena [2:] para solo quedarse con los dijitos binarios
                print(f"el {numero} en binario es: {binario_convertido}")
            else:
                print("Por favor, ingrese un número entre 0 y 14: ")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    elif opcion == "2": # Segunda Opcion del Menu
        print("conversor de binario a decimal")
        binario = input("ingrese un numero binario: ")
        try: # Variables que controla errores de manera controlada
            decimal_convertido = int(binario, 2)
            if 0 <= decimal_convertido <= 14:
                print(f"El binario {binario} en decimal es: {decimal_convertido}")
            else:
                print("El número binario ingresado representa un valor fuera del rango 0-14.")
        except ValueError: # Variable que bloquea el try (Captura y manejana el error)
            print("Entrada inválida. Por favor, ingrese un número binario válido (solo 0s y 1s).")
    elif opcion == "3": # Tercera Opcion del menu
        print("saliendo")
        break
    else:
        print("Opción inválida. Por favor, ingrese 1, 2, 3 o 4.")
    



#juego de adivinar el numero y salte cuanto intentos tuvo o q sean con intentos prestablecido (si se acaban qur salga el numero secreto)


#Sistema conversor esta funcionando