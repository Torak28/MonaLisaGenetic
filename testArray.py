import random
from PIL import Image, ImageDraw

def darkPicture(N):
    ret = Image.new('RGBA', N.size, (0, 0, 0, 255))
    return ret

# suma różnic kwadratów
def distance2(org, N):
    ret = 0
    for i in range(org.size[0]):
        for j in range(org.size[1]):
            a = sum(org.getpixel((i,j)))
            b = sum(N.getpixel((i,j)))
            ret += (a - b) * (a - b)
    return ret

# Mutacja
def square(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(0, org.size[0] - 1)
    y = random.randint(0, org.size[1] - 1)
    w = random.randint(x + 1, org.size[0])
    h = random.randint(y + 1, org.size[1])
    R = org.getpixel((x,y))[0]
    G = org.getpixel((x,y))[1]
    B = org.getpixel((x,y))[2]
    # eksperymentalne wydanie
    A = random.randint(0, 126)
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
    R = org.getpixel((x, y))[0]
    G = org.getpixel((x, y))[1]
    B = org.getpixel((x, y))[2]
    # eksperymentalne wydanie
    A = random.randint(0, 126)
    ret.polygon( tup, fill=(R, G, B, A))
    N.paste(tmp, mask=tmp)
    return N

def ellipse(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(0, org.size[0] - 1)
    y = random.randint(0, org.size[1] - 1)
    w = random.randint(x + 1, org.size[0])
    h = random.randint(y + 1, org.size[1])
    R = org.getpixel((x,y))[0]
    G = org.getpixel((x,y))[1]
    B = org.getpixel((x,y))[2]
    # eksperymentalne wydanie
    A = random.randint(0, 126)
    ret.ellipse(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N

# Krzyżowanie
def Add(P1, P2):
    ret = Image.alpha_composite(P1, P2)
    return ret

'''
    Od tego w dół trzeba ogarnąć kod
'''

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
        if random.random() < pop_it:
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
mona = Image.open("MonaLisa.png").convert("RGBA")

# Sterowanie
ilosc_w_populacji = 100
ilosc_petli = 100000
wspolczynnik_mutacji = 0.1

populacja = []

dark = darkPicture(mona)
for i in range(50):
    x1 = square(mona, dark)
    x2 = polygon(mona, dark)
    x3 = Add(x1, x2)
    x4 = ellipse(mona, dark)
    x = Add(x3, x4)
x.show()