##Elaborar un programa que cuando aumente la intensidad de la corriente a través de un potenciomentro, logre que la velocidad de los leds (del inciso 1) fluya más rapido y al disminuir la intensidad de la corriente del potenciomentro fluya más lento. 
import pyfirmata
import time 
board = pyfirmata.Arduino('COM3')

itera = pyfirmata.util.Iterator(board)
itera.start()

analog_input = board.get_pin('a:0:i')

def ascendente():
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.01
        board.digital[6].write(1)
        time.sleep(delay)
        board.digital[7].write(1)
        time.sleep(delay)
        board.digital[8].write(1)
        time.sleep(delay)
        board.digital[9].write(1)
        time.sleep(delay)
        board.digital[10].write(1)
        time.sleep(delay)
        board.digital[11].write(1)
        time.sleep(delay)
        board.digital[6].write(0)
        board.digital[7].write(0)
        board.digital[8].write(0)
        board.digital[9].write(0)
        board.digital[10].write(0)
        board.digital[11].write(0)
    else:
        time.sleep(0.1)

def descendente():
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.01
        board.digital[11].write(1)
        time.sleep(delay)
        board.digital[10].write(1)
        time.sleep(delay)
        board.digital[9].write(1)
        time.sleep(delay)
        board.digital[8].write(1)
        time.sleep(delay)
        board.digital[7].write(1)
        time.sleep(delay)
        board.digital[6].write(1)
        time.sleep(delay)
        board.digital[11].write(0)
        board.digital[10].write(0)
        board.digital[9].write(0)
        board.digital[8].write(0)
        board.digital[7].write(0)
        board.digital[6].write(0)
    else:
        time.sleep(0.1)

def menu():
    print("------------------------")
    print("  SELECCION UNA OPCION  ")
    print("                        ")
    print("  1. Forma Ascendente   ")
    print("  2. Forma Descendente  ")
    print("                        ")
    print("------------------------")

    opcion = input("Ingrese el numero de la opcion que decea ejecutar: ")
    if opcion == '1':
        while True:
            ascendente()
    elif opcion == '2':
        while True:
            descendente()
while True:
    menu()