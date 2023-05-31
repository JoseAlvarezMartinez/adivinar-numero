from random import *
numero_secreto = randint(0, 100)
intentos = 0
nombre_usuario = input("¿Como te llamas? ")

print(f"Bueno,{nombre_usuario},he pensado un numero entre el 1 y 100, \n tienes solo ocho intentos para adivinar cual crees que es el numero")

while intentos != 8:
        try:
            numero_usuario = int(input("¿Cual es tu numero?"))
            intentos += 1
            if numero_usuario not in range(1, 101):
                print("El numero no se encuentra dentro de los valores establecidos")
                intentos -= 1
            elif numero_usuario > numero_secreto:
                print("El numero es mas bajo")
            elif numero_usuario < numero_secreto:
                print("El numero es mas alto")
            else:
                print(
                    f"Felicitaciones {nombre_usuario}! Has adivinado en {intentos} intentos.")
                break ;
        except ValueError:
             print("Error: Debe ingresar un número entero. Inténtelo nuevamente.")
if numero_usuario != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")

