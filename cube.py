from matplotlib import pyplot as plt
import numpy as np
import random as rnd

SAND_R = 0.00135 * 4
A_LENGTH = 51
B_LENGTH = 51
H_HEIGHT = 51
DECREASE_RATE = 0.899
EXPEND_RATE = 0.988
TOTAL = 0.
WAVE_HEIGHT = 9
RAIN_PER_ROUND = 500
AFFECT_RATIO = 0.8
ACCUMULATE_LIMITATION = 625

model = np.ndarray([A_LENGTH, B_LENGTH, H_HEIGHT], bool)

func_x0 = 0.8
func_w = 4
func_a = 40
BASE_F3 = 64 * (0.33 * 3.1415 * 10 * SAND_R * SAND_R * (3 * 2.713 * SAND_R * 0.5 + 2 * SAND_R * 0.353 - 2 * SAND_R) + 1.414 * 3.1415 * SAND_R) * 1.713 / 3
BASE_F = 64 * 0.33 * 3.1415 * 10 * SAND_R * SAND_R * (3 * 2 * SAND_R * 0.5 + 2 * SAND_R * 0.353 - 2 * SAND_R) + 1.414 * 3.1415 * SAND_R

'''
Todo 利用三维线性规划剔除形状
'''
print (BASE_F3)

def legal(i, j, k):
    if i >= 0 and i < A_LENGTH:
        if j >= 0 and j < B_LENGTH:
            if k >= 0 and k < H_HEIGHT:
                if model[i, j, k] == False:
                    return True
    return False

def getForce(i, j, k, ftype):
    ret = 0.
    if ftype == False:
        if legal(i + 1, j, k):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j + 1, k):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j + 1, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i, j + 1, k):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i, j + 1, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i, j, k + 1):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j, k):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j + 1, k):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j + 1, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j, k - 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j + 1, k - 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i, j, k - 1):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j, k - 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j + 1, k - 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
    else :
        if legal(i + 1, j, k):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j - 1, k):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j - 1, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i, j - 1, k):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i, j - 1, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i, j, k + 1):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j, k):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j - 1, k):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j - 1, k + 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j, k - 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i + 1, j - 1, k - 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i, j, k - 1):
            ret = ret + BASE_F * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j, k - 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
        if legal(i - 1, j - 1, k - 1):
            ret = ret + BASE_F3 * (500. + (float)(H_HEIGHT - k)) / 500.
    return ret

rainAffected = 0
def recheck():
    counter = 0.
    global rainAffected
    header = np.ndarray([A_LENGTH, H_HEIGHT], int)
    deleter = np.ndarray([A_LENGTH, B_LENGTH], int)
    for i in range(A_LENGTH):
        for k in range(H_HEIGHT):
            for j in range(B_LENGTH):
                deleter[i, j] = 0
                if model[i, j, k] == False:
                    header[i, k] = j
                    break
    for i in range(A_LENGTH):
        for j in range(B_LENGTH):
            for k in range(H_HEIGHT):
                if getForce(i, j, k, 0) < 2.33691 * (B_LENGTH - j) / B_LENGTH + 0.8 * round(pow(EXPEND_RATE, header[i, k]), 3) + 0.0005 * rainAffected * pow(EXPEND_RATE, H_HEIGHT - k):
                    #print (getForce(i, j, k, 0))
                    if legal(i, j, k) and k <= WAVE_HEIGHT + 5:
                            model[i, j, k] = True
                            deleter[i, j] = deleter[i, j] + 1
                else :
                    #if j == 49 or i == 0 or i == 49 or modelcpy[i, j + 1, k] == True or modelcpy[i + 1, j, k] == True or modelcpy[i - 1, j, k] == True:
                    if legal(i, j, k) and getForce(i, j, k, 1) < 2.33691 * round(pow(DECREASE_RATE, j - header[i, k] + 1), 3):
                        model[i, j, k] = True
                        deleter[i, j] = deleter[i, j] + 1
    for i in range(RAIN_PER_ROUND):
        x = rnd.randint(0, A_LENGTH - 1)
        y = rnd.randint(0, B_LENGTH - 1)
        for z in range(H_HEIGHT):
            if model[x, y, z] == True and z > 0:
                rainforce = 0.004 / 0.1 + rnd.uniform(-0.02, 0.02)
                rainAffected = rainAffected + 1
                if legal(x, y, z - 1) and (getForce(x, y, z - 1, 0)) / 24 < rainforce:
                    print ("affected!!!")
                    model[x, y, z - 1] = True
    for i in range(A_LENGTH):
        for j in range(B_LENGTH):
            kcounter = 0
            for k in range(H_HEIGHT):
                if model[i, j, k] == False:   
                    counter = counter + 1
                    kcounter = kcounter + 1
            for k in range(H_HEIGHT):
                if k < kcounter:
                    model[i, j, k] = False
                else :
                    model[i, j, k] = True
    print (counter / TOTAL)
    return counter

for i in range(A_LENGTH):
    for j in range(B_LENGTH):
        for k in range(H_HEIGHT):
            TOTAL = TOTAL + 1

ratio = recheck() / TOTAL
i = 1
ploty = [1, ratio]
plotx = [0, i]
while ratio > 0.7:
    i = i + 1
    ratio = recheck() / TOTAL
    plotx.append(i)
    ploty.append(ratio)
outx = []
outy = []
outz = []
for i in range(A_LENGTH):
    for j in range(B_LENGTH):
        tk = 0
        for k in range(H_HEIGHT):
            if model[i, j, k] == False:
                if k > tk:
                    tk = k
            else:
                break
        outx.append(i)
        outy.append(j)
        outz.append(tk)
print (len(plotx))
np.savetxt("cbx.txt", outx)
np.savetxt("cby.txt", outy)
np.savetxt("cbz.txt", outz)
plt.figure()
plt.plot(plotx, ploty)
plt.show()
# 18

# 12 times