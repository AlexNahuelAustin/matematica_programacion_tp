#Menu para convertir de 1.decimal a binario o 2.binario a decimal o 3 Juego 4 Salir
import random
# Creamos la función contador_binario que muestra los números del 0 al 15 y sus respectivos num binarios
def contador_binario():
    
    import time

    print("Estos son los numeros Binarios del 0 al 15")
    time.sleep(2)

    for i in range(0,16):   
        num = i
        time.sleep(0.5)
        binario = "0"

        while num >= 2:
            binario += str(num % 2)
            num = num // 2

        binario += str(num)

        print(f"{i} = {binario[::-1]}")


while True: # Se crea el Menu de opciones (While al entrar al True solo toma verdadero)
    print("Ingrese una opción:")
    print("1. Conversor decimal a binario")
    print("2. Conversor binario a decimal")
    print("3. Juego de adivinar el número")
    print("4. Contador binario")
    print("5. Salir")
    opcion = input("Ingrese su numero ")
    
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
        print("\nJuego: Adivina el número entre 1 y 100")
        numero_correcto =random.randint(1, 100)
        while True:
            try:
                numero_usuario = int(input("Adivina el número: "))
                if numero_usuario == numero_correcto:
                    print("¡Has adivinado el número!")
                    break
                elif numero_usuario < numero_correcto:
                    print("Intenta con un número mayor.")
                else:
                    print("Intenta con un número menor.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
    elif opcion == "4": # Agregamos la función de contador binario
        contador_binario()



    elif opcion == "5": # Tercera Opcion del menu
        print("saliendo")
        break
    else:
        print("Opción inválida. Por favor, ingrese 1, 2, 3, 4 o 5.")
        continue
    
    print("\n¿Querés empezar de nuevo?")
    print("1. Sí")
    print("2. No")
    repetir = input("Elegí una opción: ")

    if repetir != "1":
        print("¡Hasta luego!")
        break

#Probando el repositorio

#Juego de adivinar el numero y salte cuanto intentos tuvo o q sean con intentos preestablecido (si se acaban, tiene que salir el numero secreto)


#Sistema conversor esta funcionando


