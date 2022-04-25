##Desarrollar un programa que permita controlar el prototipo en tiempo real desde Python al circuito con los leds.   (en consola) 
import pyfirmata
import time 
board = pyfirmata.Arduino('COM3')



def encender():
    board.digital[6].write(1)
    board.digital[7].write(1)
    board.digital[8].write(1)
    board.digital[9].write(1)
    board.digital[10].write(1)
    board.digital[11].write(1)
    print("LED 1 : Encendida")
    print("LED 2 : Encendida")
    print("LED 3 : Encendida")
    print("LED 4 : Encendida")
    print("LED 5 : Encendida")
    print("LED 6 : Encendida")

def apagada():
    board.digital[6].write(0)
    board.digital[7].write(0)
    board.digital[8].write(0)
    board.digital[9].write(0)
    board.digital[10].write(0)
    board.digital[11].write(0)
    print("LED 1 : Apagada")
    print("LED 2 : Apagada")
    print("LED 3 : Apagada")
    print("LED 4 : Apagada")
    print("LED 5 : Apagada")
    print("LED 6 : Apagada")





def run():
    print("------------------------")
    print("  SELECCION UNA OPCION  ")
    print("                        ")
    print("  1. Encender led       ")
    print("  2. Apagar led         ")
    print("                        ")
    print("------------------------")
    opcion = input("Ingrese el numero de la opcion que decea ejecutar: ")
    if opcion == "1":
        encender()
    if opcion == "2":
        apagada()
    while True:
        run()

if __name__ == "__main__":
    run()


















