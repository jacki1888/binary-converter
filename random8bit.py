from random import *

def random8Bit():
    binArray = []
    for i in range(8):
        bit = randint(0,1)
        binArray.append(bit)
    binConv = [128,63,32,16,8,4,2,1]
    binFinal = 0
    for i in range(8):
        if binArray[i] == 1:
            binFinal = binFinal + binConv[i]
    print(binFinal)

