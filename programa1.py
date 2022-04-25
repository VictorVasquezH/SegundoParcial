##Elabore un programa desde python se enciendan suecuencialmente todos los leds de manera ascendente y desencente
import pyfirmata
import time 
board = pyfirmata.Arduino('COM3')
  

def ascendete():
    while True:
        board.digital[6].write(0)
        board.digital[6].write(1)
        time.sleep(.5)
        board.digital[7].write(1)
        time.sleep(.5)
        board.digital[8].write(1)
        time.sleep(.5)
        board.digital[9].write(1)
        time.sleep(.5)
        board.digital[10].write(1)
        time.sleep(.5)
        board.digital[11].write(1)
        time.sleep(.5)
        board.digital[6].write(0)
        board.digital[7].write(0)
        board.digital[8].write(0)
        board.digital[9].write(0)
        board.digital[10].write(0)
        board.digital[11].write(0)

def descendete():
    while True: 
        board.digital[11].write(0)
        board.digital[11].write(1)
        time.sleep(.5)
        board.digital[10].write(1)
        time.sleep(.5)
        board.digital[9].write(1)
        time.sleep(.5)
        board.digital[8].write(1)
        time.sleep(.5)
        board.digital[7].write(1)
        time.sleep(.5)
        board.digital[6].write(1)
        time.sleep(.5)
        board.digital[11].write(0)
        board.digital[10].write(0)
        board.digital[9].write(0)
        board.digital[8].write(0)
        board.digital[7].write(0)
        board.digital[6].write(0)


def led():
        print("------------------------")
        print("  SELECCION UNA OPCION  ")
        print("                        ")
        print("  1. Forma Ascendente   ")
        print("  2. Forma Descendente  ")
        print("                        ")
        print("------------------------")

        opcion = input("Ingrese el numero de la opcion que decea ejecutar: ")
        if opcion == "1":
                ascendete()

        if opcion == "2":
                descendete()


if __name__ == "__main__":
    led()


