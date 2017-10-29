import random
import numpy
import operator, math
from PIL import Image, ImageDraw, ImageChops, ImageStat

def darkPicture(N):
    ret = Image.new('RGBA', N.size, (0, 0, 0, 255))
    return ret

def reduce(function, iterable, initializer=None):
    "Funkcja z Pythona 2.7"
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

def distance2(org, N):
    "Calculate the root-mean-square difference between two images"\
    "http://effbot.org/zone/pil-comparing-images.htm"

    h = ImageChops.difference(org, N).histogram()

    # calculate rms
    ret =  math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(org.size[0]) * org.size[1]))

    return ret

def find_median_colorS(N, x, y, w, h):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    ret.rectangle(((x, y), (w, h)), outline= 1, fill=1)
    median = ImageStat.Stat(N, mask=tmp).median
    return median

def find_median_colorP(N, tup):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    ret.polygon(tup, outline= 1, fill=1)
    median = ImageStat.Stat(N, mask=tmp).median
    return median

def find_median_colorE(N, x, y, w, h):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    ret.ellipse(((x, y), (w, h)), outline= 1, fill=1)
    median = ImageStat.Stat(N, mask=tmp).median
    return median

# Mutacja
def square(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(0, org.size[0] - 1)
    y = random.randint(0, org.size[1] - 1)
    w = random.randint(x + 1, org.size[0])
    h = random.randint(y + 1, org.size[1])
    col = find_median_colorS(org, x, y, w, h)
    R = col[0]
    G = col[1]
    B = col[2]
    # eksperymentalne wydanie
    A = random.randint(0, wartosc_alphy)
    ret.rectangle(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N

def polygon(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    tup = ()
    for i in range(0, 3):
        x = random.randint(0, org.size[0] - 1)
        y = random.randint(0, org.size[1] - 1)
        tup += ((x,y),)
    col = find_median_colorP(org, tup)
    R = col[0]
    G = col[1]
    B = col[2]
    # eksperymentalne wydanie
    A = random.randint(0, wartosc_alphy)
    ret.polygon(tup, fill=(R, G, B, A))
    N.paste(tmp, mask=tmp)
    return N

def ellipse(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(0, org.size[0] - 1)
    y = random.randint(0, org.size[1] - 1)
    w = random.randint(x + 1, org.size[0])
    h = random.randint(y + 1, org.size[1])
    col = find_median_colorE(org, x, y, w, h)
    R = col[0]
    G = col[1]
    B = col[2]
    # eksperymentalne wydanie
    A = random.randint(0, wartosc_alphy)
    ret.ellipse(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N

# Krzyżowanie
def Add(P1, P2):
    ret = Image.alpha_composite(P1, P2)
    return ret

def mapFromTo(x,a,b,c,d):
   ret = (x - a) /(b - a) * (d - c) + c
   return ret

def mutate(pop, pop_size, pop_it, org):
    for i in range(pop_size):
        if random.random() < pop_it:
            figure = random.random()
            if figure < 0.3:
                pop[i]['pic'] = square(org, pop[i]['pic'])
            elif figure > 0.3 and figure < 0.6:
                pop[i]['pic'] = polygon(org, pop[i]['pic'])
            else:
                pop[i]['pic'] = ellipse(org, pop[i]['pic'])
    return pop

def score(pop, pop_size):
    for i in range(pop_size):
        pop[i]['fit'] = distance2(mona, pop[i]['pic'])
    return pop

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

def crossover(pop, pool):
    ret = []
    for i in range(len(pop)):
        child = {}
        parentA = numpy.random.choice(pool)
        parentB = numpy.random.choice(pool)
        child['pic'] = Add(parentA['pic'], parentB['pic'])
        ret.append(child)
    return ret

def dump_best(pop, it):
    best = pop[0]
    for i in range(len(pop)):
        if pop[i]['fit'] < best['fit']:
            best = pop[i]
    best['pic'].save("E:/INZ5v3/" + str(it) + ".png")

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
mona = Image.open("MonaLisa.png").convert("RGBA")

# Sterowanie
ilosc_w_populacji = 100
ilosc_petli = 10000
wspolczynnik_mutacji = 0.1
wartosc_alphy = 126

populacja = []

dark = darkPicture(mona)
fit = distance2(mona, dark)


# Tworzenie N osobnikow losowych
for i in range(ilosc_w_populacji):
    populacja.append({'pic' : dark, 'fit' : fit})

# Życie
for p in range(ilosc_petli):
    # Mutacja
    populacja = mutate(populacja, ilosc_w_populacji, wspolczynnik_mutacji, mona)
    # Ocena( 0 - 100 )
    populacja = score(populacja, ilosc_w_populacji)
    # Zrzucanie najlepszego w populacji
    dump_best(populacja, p)
    printPop(populacja, p)
    # Tworzenie poli rozrodczej do krzyżowania
    pola_rozrodcza = matingpool(populacja, ilosc_w_populacji)
    # Krzyzowanie i nowa populacja
    populacja = crossover(populacja, pola_rozrodcza)