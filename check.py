import numpy as np
import random as rnd
import math
A_LENGTH = 81
B_LENGTH = 81
H_HEIGHT = 75

def calc(x, y, z):
    if ((x - 40) * (x - 40) + (y - 40) * (y - 40) <= (40 * (75 - z) / 75) * (40 * (75 - z) / 75)):
        return True
    else : return False

outx = []
outy = []
outz = []
for i in range(-11, 91, 1):
    for j in range(-31, 91, 1):
        tk = 0
        for k in range(H_HEIGHT):
            if calc(i, j, k) == True:
                if k > tk:
                    tk = k
            else:
                break
        if tk == 0 and ((i - 40) * (i - 40) + (j - 40) * (j - 40) < 2500): tk = -10
        if tk == 0 and i > 30 and i < 50 and j < 40: tk = -10
        outx.append(i)
        outy.append(j)
        outz.append(tk)
        #if i % 500 == 0 and j % 500 == 0 : print (i, j)
print (len(outx))
np.savetxt("testx.txt", outx)
np.savetxt("testy.txt", outy)
np.savetxt("testz.txt", outz)