import numpy
import math
import time
from PIL import Image

def randomElem():
    ret = numpy.empty([1], int)
    ret = numpy.delete(ret, 0)
    ret = numpy.append(ret, [numpy.random.randint(256, size=4)])
    return ret

def randomPictur(N):
   ret = numpy.empty_like(N)
   for i in range(ret.shape[0]):
       for j in range(ret. shape[1]):
           ret[i][j] = randomElem()
   return ret

def darkPicture(N):
    ret = numpy.zeros_like(N)
    return ret

# distance between 2 oints in 3D space
# |P_1\, P_2| = \sqrt{(x_2- x_1)^2 + (y_2 -y_1)^2 + (z_2- z_1)^2}
def distance(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            ret += int(math.sqrt(pow(int(N[i][j][0]) - int(org[i][j][0]),2) + pow(int(N[i][j][1]) - int(org[i][j][1]),2) + pow(int(N[i][j][2]) - int(org[i][j][2]),2)))
    return ret

# suma różnic kwadratów
def distance2(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            a = int(org[i][j][0]) + int(org[i][j][1]) + int(org[i][j][2])
            b = int(N[i][j][0]) + int(N[i][j][1]) + int(N[i][j][2])
            ret += (a - b) * (a - b)
    return ret

def distance3(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            deltaR = org[i][j][0] - N[i][j][0]
            deltaG = org[i][j][1] - N[i][j][1]
            deltaB = org[i][j][2] - N[i][j][2]

            pFit = deltaR * deltaR + deltaG * deltaG + deltaB * deltaB
            ret += pFit
    return ret

def distance4(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            if org[i][j][0] != N[i][j][0] or org[i][j][1] != N[i][j][1] or org[i][j][2] != N[i][j][2]:
                ret +=1
    return ret

# Mutacja
def square(org, N):
    tmp = darkPicture(N)
    x = numpy.random.randint(org.shape[0])
    y = numpy.random.randint(org.shape[1])
    w = numpy.random.random_integers(x + 1,org.shape[0])
    h = numpy.random.random_integers(y + 1, org.shape[1])
    R = org[x][y][0]
    G = org[x][y][1]
    B = org[x][y][2]
    # eksperymentalne wydanie
    A = numpy.random.randint(126)
    for i in range(N.shape[0]):
        if i >= x and i <= w:
            for j in range(N.shape[1]):
                if j >=y and j <= h:
                    tmp[i][j][0] = R
                    tmp[i][j][1] = G
                    tmp[i][j][2] = B
                    tmp[i][j][3] = A
    ret = Image.alpha_composite(Image.fromarray(N,"RGBA"),Image.fromarray(tmp,"RGBA"))
    return numpy.asarray(ret, dtype='uint8')

# Krzyżowanie
def Add(P1, P2):
    ret = Image.alpha_composite(Image.fromarray(P1, "RGBA"), Image.fromarray(P2, "RGBA"))
    return numpy.asarray(ret, dtype='uint8')

def mapFromTo(x,a,b,c,d):
   ret = (x - a) /(b - a) * (d - c) + c
   return ret

def matingpool(pop, pop_size):
    pop = sorted(pop, key=lambda x:(x['fit']))
    maxFit = pop[-1]['fit']
    ret = []
    for k in range(pop_size):
        # Rzutowanie ilosci elementow z aktalnego fita na zakres 100 do 0
        # Dzięki temu mainting pool zawiera więcej dobrych osobników
        kon = int(mapFromTo(pop[k]['fit'], 0, maxFit, 100, 1))
        for l in range(kon):
            ret.append(pop[k])
    return ret

def mutate(pop, pop_size, pop_it, org):
    for i in range(pop_size):
        if numpy.random.random() < pop_it:
            pop[i]['tab'] = square(org, pop[i]['tab'])
    return pop

def score(pop, pop_size):
    for i in range(pop_size):
        pop[i]['fit'] = distance2(tab, pop[i]['tab'])
    return pop

def crossover(pop, pool):
    ret = []
    for i in range(len(pop)):
        child = {}
        parentA = numpy.random.choice(pool)
        parentB = numpy.random.choice(pool)
        child['tab'] = Add(parentA['tab'], parentB['tab'])
        ret.append(child)
    return ret

def dump_best(pop, it):
    best = pop[0]
    for i in range(len(pop)):
        if pop[i]['fit'] < best['fit']:
            best = pop[i]
    newIm = Image.fromarray(best['tab'], "RGBA")
    newIm.save("E:/INZ/" + str(it) + ".png")

def printPop(pop, it):
    print("Populacja " + str(it) + " (" + str(len(pop)) + ") : ", end="")
    pop = sorted(pop, key=lambda x: (x['fit']))
    for _ in range(len(pop)):
        print(pop[_]['fit'], end=" ")
    print("")

'''
Główna pętla programu
'''

# read image as RGB and add alpha (transparency)
im = Image.open("MonaLisa.png").convert("RGBA")
tab = numpy.asarray(im, dtype='uint8')

# Sterowanie
ilosc_w_populacji = 100
ilosc_petli = 10000
wspolczynnik_mutacji = 0.1

populacja = []

dark = darkPicture(tab)
fit = distance2(tab, dark)


# Tworzenie N osobnikow losowych
for i in range(ilosc_w_populacji):
    populacja.append({'tab' : dark, 'fit' : fit})

# Życie
for p in range(ilosc_petli):
    # Mutacja
    populacja = mutate(populacja, ilosc_w_populacji, wspolczynnik_mutacji, tab)
    # Ocena( 0 - 100 )
    populacja = score(populacja, ilosc_w_populacji)
    # Zrzucanie najlepszego w populacji
    dump_best(populacja, p)
    printPop(populacja, p)
    # Tworzenie poli rozrodczej do krzyżowania
    pola_rozrodcza = matingpool(populacja, ilosc_w_populacji)
    # Krzyzowanie i nowa populacja
    populacja = crossover(populacja, pola_rozrodcza)

    # Alpha przy mutacji na 126 jest jak co
