import random, operator, math, numpy, os
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
    ret = Image.new('RGBA', org.size)

    width, height = org.size

    leftT = 0, 0, width // 2, height // 2
    rightT = width // 2, 0, width, height // 2
    leftB = 0, height // 2, width // 2, height
    rightB = width // 2, height // 2, width, height

    ret.paste(tab[0], leftT, mask=tab[0])
    ret.paste(tab[1], rightT, mask=tab[1])
    ret.paste(tab[2], leftB, mask=tab[2])
    ret.paste(tab[3], rightB, mask=tab[3])

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
        w = random.randint(0, org.size[0] + 20)
    else:
        w = random.randint(x + 1, org.size[0] + 20)
    if y < 0:
        h = random.randint(y + 1, org.size[1] + 20)
    else:
        h = random.randint(y + 1, org.size[1] + 20)
    col = find_median_colorE(org, x, y, w, h)
    R = col[0]
    G = col[1]
    B = col[2]
    A = random.randint(0, 255)
    ret.ellipse(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N

def square(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(-20, org.size[0] - 1)
    y = random.randint(-20, org.size[1] - 1)
    if x < 0:
        w = random.randint(0, org.size[0] + 20)
    else:
        w = random.randint(x + 1, org.size[0] + 20)
    if y < 0:
        h = random.randint(y + 1, org.size[1] + 20)
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

m1 = m[0]
m2 = m[1]
m3 = m[2]
m4 = m[3]
m5 = m[4]
m6 = m[5]
m7 = m[6]
m8 = m[7]
m9 = m[8]
m10 = m[9]
m11 = m[10]
m12 = m[11]
m13 = m[12]
m14 = m[13]
m15 = m[14]
m16 = m[15]
m17 = m[16]
m18 = m[17]
m19 = m[18]
m20 = m[19]
m21 = m[20]
m22 = m[21]
m23 = m[22]
m24 = m[23]
m25 = m[24]
m26 = m[25]
m27 = m[26]
m28 = m[27]
m29 = m[28]
m30 = m[29]
m31 = m[30]
m32 = m[31]
m33 = m[32]
m34 = m[33]
m35 = m[34]
m36 = m[35]
m37 = m[36]
m38 = m[37]
m39 = m[38]
m40 = m[39]
m41 = m[40]
m42 = m[41]
m43 = m[42]
m44 = m[43]
m45 = m[44]
m46 = m[45]
m47 = m[46]
m48 = m[47]
m49 = m[48]
m50 = m[49]
m51 = m[50]
m52 = m[51]
m53 = m[52]
m54 = m[53]
m55 = m[54]
m56 = m[55]
m57 = m[56]
m58 = m[57]
m59 = m[58]
m60 = m[59]
m61 = m[60]
m62 = m[61]
m63 = m[62]
m64 = m[63]



# Sterowanie
ilosc_w_populacji = 100
ilosc_petli = 10000
wspolczynnik_mutacji = 0.1
wartosc_alphy = 126
folder = "INZ9v6"
disk = "E:/INZ"

if not os.path.exists(disk ):
    os.mkdir(disk)

out = disk + "/" + folder + "/out.txt"

a1 = run(m1, "m1")
a2 = run(m2, "m2")
a3 = run(m3, "m3")
a4 = run(m4, "m4")
a5 = run(m5, "m5")
a6 = run(m6, "m6")
a7 = run(m7, "m7")
a8 = run(m8, "m8")
a9 = run(m9, "m9")
a10 = run(m10, "m10")
a11 = run(m11, "m11")
a12 = run(m12, "m12")
a13 = run(m13, "m13")
a14 = run(m14, "m14")
a15 = run(m15, "m15")
a16 = run(m16, "m16")
a17 = run(m17, "m17")
a18 = run(m18, "m18")
a19 = run(m19, "m19")
a20 = run(m20, "m20")
a21 = run(m21, "m21")
a22 = run(m22, "m22")
a23 = run(m23, "m23")
a24 = run(m24, "m24")
a25 = run(m25, "m25")
a26 = run(m26, "m26")
a27 = run(m27, "m27")
a28 = run(m28, "m28")
a29 = run(m29, "m29")
a30 = run(m30, "m30")
a31 = run(m31, "m31")
a32 = run(m32, "m32")
a33 = run(m33, "m33")
a34 = run(m34, "m34")
a35 = run(m35, "m35")
a36 = run(m36, "m36")
a37 = run(m37, "m37")
a38 = run(m38, "m38")
a39 = run(m39, "m39")
a40 = run(m40, "m40")
a41 = run(m41, "m41")
a42 = run(m42, "m42")
a43 = run(m43, "m43")
a44 = run(m44, "m44")
a45 = run(m45, "m45")
a46 = run(m46, "m46")
a47 = run(m47, "m47")
a48 = run(m48, "m48")
a49 = run(m49, "m49")
a50 = run(m50, "m50")
a51 = run(m51, "m51")
a52 = run(m52, "m52")
a53 = run(m53, "m53")
a54 = run(m54, "m54")
a55 = run(m55, "m55")
a56 = run(m56, "m56")
a57 = run(m57, "m57")
a58 = run(m58, "m58")
a59 = run(m59, "m59")
a60 = run(m60, "m60")
a61 = run(m61, "m61")
a62 = run(m62, "m62")
a63 = run(m63, "m63")
a64 = run(m64, "m64")

ass = assemble64(ideal, [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, a48, a49, a50, a51, a52, a53, a54, a55, a56, a57, a58, a59, a60, a61, a62, a63, a64])
ass.save(disk + "/" + folder + "/output.png")

bss = Image.open(disk + "/INZ6v4/output.png").convert("RGBA")

print("Nowa wersja algorytmu: %s" % distance2(ideal, ass))
print("Stara wersja algorytmu: %s" % distance2(ideal, bss))