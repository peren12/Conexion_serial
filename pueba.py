import serial
import time
try:
    LaunchPad = serial.Serial('COM10', 57600)
    alll=""
    bande = 0
    while (bande != 1):
        lista = []
        i = 0
        while i < 7:
            d = LaunchPad.read()
            lista.append(d)
            i = i + 1
        print lista
        if lista != ['0','1','0','1','0','1','0']:
            alll=alll + ''.join(lista)
        else:
            bande = 1
        #time.sleep(0.2)
    LaunchPad.close()
    print alll   

except:
    print '\nfailure\n'

