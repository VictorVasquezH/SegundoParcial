##Elabore un programa que encienda la mitad de los leds, durante 1 segundo y la mitad de leds durante 2 segundos
import pyfirmata
import time 
board = pyfirmata.Arduino('COM3')

while True:
    #Primera Mitad:
    board.digital[6].write(1)
    board.digital[7].write(1)
    board.digital[8].write(1)
    time.sleep(1)
    board.digital[6].write(0)
    board.digital[7].write(0)
    board.digital[8].write(0)

    #Segunda Mitad
    board.digital[9].write(1)
    board.digital[10].write(1)
    board.digital[11].write(1)
    time.sleep(2)
    board.digital[9].write(0)
    board.digital[10].write(0)
    board.digital[11].write(0)
