import numpy as np
def calc(x, y, z):
    if ((x - 40) * (x - 40) + (y - 40) * (y - 40) <= (40 * (75 - z) / 75) * (40 * (75 - z) / 75)):
        return True
    else : return False

outx = []
outy = []
outz = []
for i in range(80):
    for j in range(80):
        tk = 0
        for k in range(75):
            if calc(i, j, k) == True:
                if k > tk:
                    tk = k
            else:
                break
        outx.append(i)
        outy.append(j)
        outz.append(tk)
np.savetxt("testx.txt", outx)
np.savetxt("testy.txt", outy)
np.savetxt("testz.txt", outz)

