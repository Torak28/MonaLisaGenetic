import random, operator, math, os
from PIL import Image, ImageDraw, ImageChops, ImageStat

def crop64(org):
    ret4 = crop4(org)

    ret16 = crop4(ret4[0])
    ret16.extend(crop4(ret4[1]))
    ret16.extend(crop4(ret4[2]))
    ret16.extend(crop4(ret4[3]))

    ret64 = crop4(ret16[0])
    ret64.extend(crop4(ret16[1]))
    ret64.extend(crop4(ret16[2]))
    ret64.extend(crop4(ret16[3]))
    ret64.extend(crop4(ret16[4]))
    ret64.extend(crop4(ret16[5]))
    ret64.extend(crop4(ret16[6]))
    ret64.extend(crop4(ret16[7]))
    ret64.extend(crop4(ret16[8]))
    ret64.extend(crop4(ret16[9]))
    ret64.extend(crop4(ret16[10]))
    ret64.extend(crop4(ret16[11]))
    ret64.extend(crop4(ret16[12]))
    ret64.extend(crop4(ret16[13]))
    ret64.extend(crop4(ret16[14]))
    ret64.extend(crop4(ret16[15]))

    return ret64

def crop16(org):
    ret4 = crop4(org)
    ret16 = crop4(ret4[0])
    ret16.extend(crop4(ret4[1]))
    ret16.extend(crop4(ret4[2]))
    ret16.extend(crop4(ret4[3]))

    return ret16

def assemble64(org, tab):
    org1 = crop4(org)

    pic = []

    pic.append(assemble16(org1[0], [tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7], tab[8], tab[9], tab[10], tab[11], tab[12], tab[13], tab[14], tab[15]]))
    pic.append(assemble16(org1[1], [tab[16], tab[17], tab[18], tab[19], tab[20], tab[21], tab[22], tab[23], tab[24], tab[25], tab[26], tab[27], tab[28], tab[29], tab[30], tab[31]]))
    pic.append(assemble16(org1[2], [tab[32], tab[33], tab[34], tab[35], tab[36], tab[37], tab[38], tab[39], tab[40], tab[41], tab[42], tab[43], tab[44], tab[45], tab[46], tab[47]]))
    pic.append(assemble16(org1[3], [tab[48], tab[49], tab[50], tab[51], tab[52], tab[53], tab[54], tab[55], tab[56], tab[57], tab[58], tab[59], tab[60], tab[61], tab[62], tab[63]]))

    ret = assemble4(org, pic)

    return ret


def assemble16(org, tab):
    org1 = crop4(org)

    pic = []

    pic.append(assemble4(org1[0], [tab[0], tab[1], tab[2], tab[3]]))
    pic.append(assemble4(org1[1], [tab[4], tab[5], tab[6], tab[7]]))
    pic.append(assemble4(org1[2], [tab[8], tab[9], tab[10], tab[11]]))
    pic.append(assemble4(org1[3], [tab[12], tab[13], tab[14], tab[15]]))

    ret = assemble4(org, pic)

    return ret

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
    ret1 = Image.new('RGBA', org.size)
    ret2 = Image.new('RGBA', org.size)
    ret3 = Image.new('RGBA', org.size)
    ret4 = Image.new('RGBA', org.size)

    width, height = org.size

    leftT = 0, 0, width // 2, height // 2
    rightT = width // 2, 0, width, height // 2
    leftB = 0, height // 2, width // 2, height
    rightB = width // 2, height // 2, width, height

    ret1.paste(tab[0], leftT)
    ret2.paste(tab[1], rightT)
    ret3.paste(tab[2], leftB)
    ret4.paste(tab[3], rightB)

    ret = Image.alpha_composite(ret1, ret2)
    ret = Image.alpha_composite(ret, ret3)
    ret = Image.alpha_composite(ret, ret4)

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
    N = Image.alpha_composite(N, tmp)
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
    #nowosc
    N = Image.alpha_composite(N, tmp)
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
    N = Image.alpha_composite(N, tmp)
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

    bst = 0

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
m = crop64(ideal)

# Sterowanie
ilosc_w_populacji = 20
ilosc_petli = 20
wspolczynnik_mutacji = 0.1
wartosc_alphy = 126
folder = "INZ9v6"
disk = "D:/INZ2"

if not os.path.exists(disk ):
    os.mkdir(disk)

out = disk + "/" + folder + "/out.txt"

a = []
for i in range(1, 65):
    a.append(run(m[i-1], 'm' + str(i)))

ass = assemble64(ideal, a)
ass.save(disk + "/" + folder + "/output.bmp")

bss = Image.open(disk + "/INZ6v4/output.png").convert("RGBA")

print("Nowa wersja algorytmu: %s" % distance2(ideal, ass))
print("Stara wersja algorytmu: %s" % distance2(ideal, bss))