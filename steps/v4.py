import random, operator, math, os
from PIL import Image, ImageDraw, ImageChops, ImageStat

def crop4(org):
    ret = []
    width, height = org.size

    leftT = 0, 0, width // 2, height // 2
    rightT = width // 2, 0, width, height // 2
    leftB = 0, height // 2, width // 2, height
    rightB = width // 2, height // 2, width, height

    ret.append(org.crop(leftT))
    ret.append(org.crop(rightT))
    ret.append(org.crop(leftB))
    ret.append(org.crop(rightB))

    return ret

def assemble4(org, tab):
    ret = Image.new('RGBA', org.size)

    width, height = org.size

    leftT = 0, 0, width // 2, height // 2
    rightT = width // 2, 0, width, height // 2
    leftB = 0, height // 2, width // 2, height
    rightB = width // 2, height // 2, width, height

    ret.paste(tab[0], leftT)
    ret.paste(tab[1], rightT)
    ret.paste(tab[2], leftB)
    ret.paste(tab[3], rightB)

    return ret

def darkPicture(N):
    ret = Image.new('RGBA', N.size, (0, 0, 0, 0))
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
def ellipse(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(-20, org.size[0] - 1)
    y = random.randint(-20, org.size[1] - 1)
    if x < 0:
        w = random.randint(1, org.size[0] + 20)
    else:
        w = random.randint(x + 1, org.size[0] + 20)
    if y < 0:
        h = random.randint(1, org.size[1] + 20)
    else:
        h = random.randint(y + 1, org.size[1] + 20)
    col = find_median_colorE(org, x, y, w, h)
    R = col[0]
    G = col[1]
    B = col[2]
    A = random.randint(0, wartosc_alphy)
    ret.ellipse(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N

def square(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(-20, org.size[0] - 1)
    y = random.randint(-20, org.size[1] - 1)
    if x < 0:
        w = random.randint(1, org.size[0] + 20)
    else:
        w = random.randint(x + 1, org.size[0] + 20)
    if y < 0:
        h = random.randint(1, org.size[1] + 20)
    else:
        h = random.randint(y + 1, org.size[1] + 20)
    col = find_median_colorS(org, x, y, w, h)
    R = col[0]
    G = col[1]
    B = col[2]
    A = random.randint(0, wartosc_alphy)
    ret.rectangle(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N

def polygon(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    tup = ()
    for i in range(0, 3):
        x = random.randint(-20, org.size[0] + 20)
        y = random.randint(-20, org.size[1] + 20)
        tup += ((x,y),)
    col = find_median_colorP(org, tup)
    R = col[0]
    G = col[1]
    B = col[2]
    A = random.randint(0, wartosc_alphy)
    ret.polygon(tup, fill=(R, G, B, A))
    N.paste(tmp, mask=tmp)
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

def score(pop, pop_size, mona):
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
        if maxFit == 0:
            kon = 100
        else:
            kon = int(mapFromTo(pop[k]['fit'], 0, maxFit, 100, 1))
        for l in range(kon):
            ret.append(pop[k])
    return ret

def crossover(pop, pool):
    ret = []
    for i in range(len(pop)):
        child = {}
        parentA = random.choice(pool)
        parentB = random.choice(pool)
        child['pic'] = Add(parentA['pic'], parentB['pic'])
        ret.append(child)
    return ret

def dump_best(pop, it, strx):
    if not os.path.exists(disk + "/" + folder):
        os.mkdir(disk + "/" + folder)
    if not os.path.exists(disk + "/" + folder + "/" + strx):
        os.mkdir(disk + "/" + folder + "/" + strx)
    best = pop[0]
    for i in range(len(pop)):
        if pop[i]['fit'] < best['fit']:
            best = pop[i]
    best['pic'].save(disk + "/" + folder + "/" + str(strx) + "/" + str(strx) + "-" + str(it) + ".png")
    return best['pic']

def printPop(pop, it, strx):
    ret = ""
    ret += "Populacja " + str(strx) + " - " + str(it) + " (" + str(len(pop)) + ") : "
    pop = sorted(pop, key=lambda x: (x['fit']))
    for _ in range(len(pop)):
       ret += " " + str(pop[_]['fit'])
    print(ret, file=open(out, "a"))
    print(ret)

def run(mona, strx):
    populacja = []
    dark = darkPicture(mona)
    fit = distance2(mona, dark)

    if not os.path.exists(disk + "/" + folder):
        os.mkdir(disk + "/" + folder)
    if not os.path.exists(out):
        open(out, 'w').close()

    # Tworzenie N osobnikow losowych
    for i in range(ilosc_w_populacji):
        populacja.append({'pic': dark, 'fit': fit})

    # Życie
    for p in range(ilosc_petli):
        # Mutacja
        populacja = mutate(populacja, ilosc_w_populacji, wspolczynnik_mutacji, mona)
        # Ocena( 0 - 100 )
        populacja = score(populacja, ilosc_w_populacji, mona)
        # Zrzucanie najlepszego w populacji
        bst = dump_best(populacja, p, strx)
        printPop(populacja, p, strx)
        # Tworzenie poli rozrodczej do krzyżowania
        pola_rozrodcza = matingpool(populacja, ilosc_w_populacji)
        # Krzyzowanie i nowa populacja
        populacja = crossover(populacja, pola_rozrodcza)

    return bst
'''
Główna pętla programu
'''

# read image as RGB and add alpha (transparency)
ideal = Image.open("MonaLisa.png").convert("RGBA")
m = crop4(ideal)

# Sterowanie
ilosc_w_populacji = 100
ilosc_petli = 40000
wspolczynnik_mutacji = 0.1
wartosc_alphy = 126
folder = "INZ7v4"
disk = "D:/INZ2"

if not os.path.exists(disk ):
    os.mkdir(disk)

out = disk + "/" + folder + "/out.txt"

a = []
for i in range(1, 5):
    a.append(run(m[i-1], 'm' + str(i)))

ass = assemble4(ideal, a)
ass.save(disk + "/" + folder + "/output.bmp")

bss = Image.open(disk + "/INZ6v4/output.png").convert("RGBA")

print("Nowa wersja algorytmu: %s" % distance2(ideal, ass))
print("Stara wersja algorytmu: %s" % distance2(ideal, bss))