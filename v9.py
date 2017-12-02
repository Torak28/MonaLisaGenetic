import random, operator, math, os, time, queue
from PIL import Image, ImageDraw, ImageChops, ImageStat
from threading import Thread

def crop256(org):
    ret64 = crop64(org)

    ret256 = crop4(ret64[0])
    for _ in range(1, 64):
        ret256.extend((crop4(ret64[_])))

    return ret256


def crop64(org):
    ret16 = crop16(org)

    ret64 = crop4(ret16[0])
    for _ in range(1, 16):
        ret64.extend(crop4(ret16[_]))

    return ret64


def crop16(org):
    ret4 = crop4(org)
    ret16 = crop4(ret4[0])
    ret16.extend(crop4(ret4[1]))
    ret16.extend(crop4(ret4[2]))
    ret16.extend(crop4(ret4[3]))

    return ret16


def assemble256(org, tab):
    org1 = crop4(org)

    pic = []

    pic.append(assemble64(org1[0], tab[:64]))
    pic.append(assemble64(org1[0], tab[64:128]))
    pic.append(assemble64(org1[0], tab[128:192]))
    pic.append(assemble64(org1[0], tab[192:256]))

    ret = assemble4(org, pic)

    return ret


def assemble64(org, tab):
    org1 = crop4(org)

    pic = []

    pic.append(assemble16(org1[0], tab[:16]))
    pic.append(assemble16(org1[1], tab[16:32]))
    pic.append(assemble16(org1[2], tab[32:48]))
    pic.append(assemble16(org1[3], tab[48:64]))

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
    "Calculate the root-mean-square difference between two images" \
    "http://effbot.org/zone/pil-comparing-images.htm"

    h = ImageChops.difference(org, N).histogram()

    # calculate rms
    ret = math.sqrt(reduce(operator.add,
                           map(lambda h, i: h * (i ** 2), h, range(256))
                           ) / (float(org.size[0]) * org.size[1]))

    return ret


def find_median_colorS(N, x, y, w, h):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    ret.rectangle(((x, y), (w, h)), outline=1, fill=1)
    median = ImageStat.Stat(N, mask=tmp).median
    return median


def find_median_colorP(N, tup):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    ret.polygon(tup, outline=1, fill=1)
    median = ImageStat.Stat(N, mask=tmp).median
    return median


def find_median_colorE(N, x, y, w, h):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    ret.ellipse(((x, y), (w, h)), outline=1, fill=1)
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
    ret.ellipse(((x, y), (w, h)), fill=(R, G, B, A))
    N.paste(tmp, mask=tmp)
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
    ret.rectangle(((x, y), (w, h)), fill=(R, G, B, A))
    N.paste(tmp, mask=tmp)
    # nowosc
    N = Image.alpha_composite(N, tmp)
    return N


def polygon(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    tup = ()
    for i in range(0, 3):
        x = random.randint(-20, org.size[0] + 20)
        y = random.randint(-20, org.size[1] + 20)
        tup += ((x, y),)
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


def mapFromTo(x, a, b, c, d):
    ret = (x - a) / (b - a) * (d - c) + c
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
    pop = sorted(pop, key=lambda x: (x['fit']))
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
    f = open(out, 'a')
    ret = ""
    ret += "Populacja " + str(strx) + " - " + str(it) + " (" + str(len(pop)) + ") : "
    pop = sorted(pop, key=lambda x: (x['fit']))
    for _ in range(len(pop)):
        ret += " " + str(pop[_]['fit'])
    f.write(ret + "\n")
    print(ret)


def run(mona, strx, q):
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
        # printPop(populacja, p, strx)
        # Tworzenie poli rozrodczej do krzyżowania
        pola_rozrodcza = matingpool(populacja, ilosc_w_populacji)
        # Krzyzowanie i nowa populacja
        populacja = crossover(populacja, pola_rozrodcza)

    q.put(bst)

def aproximate(mona, mode):
    if not os.path.exists(disk):
        os.mkdir(disk)
    if mode == 4:
        m = crop4(ideal)
    elif mode == 16:
        m = crop16(ideal)
    elif mode == 64:
        m = crop64(ideal)
    elif mode == 256:
        m = crop256(ideal)
    else:
        m = crop256(mona)

    '''
    q = queue.Queue()

    pool = []
    for i in range(1, (mode + 1)):
        t_ = Thread(target=run(m[i - 1], 'm' + str(i), q), name="Thread" + str(i))
        pool.append(t_)

    a = []
    for thread in pool:
        thread.start()
        ret = q.get()
        a.append(ret)

    for thread in pool:
        thread.join()

    a = []
    for i in range(1, (mode + 1)):
        a.append(run(m[i - 1], 'm' + str(i)))
    '''

    q = queue.Queue()

    # Czy to wspólny dostęp do m? nope
    # Czy to wynik funkcji? nope
    # Czy użycie poola coś pomaga?

    a = m[0]
    b = m[1]
    c = m[1]
    d = m[2]

    Thread(target=run(a, 'm' + str(1), q), name="Thread" + str(1)).start()
    Thread(target=run(b, 'm' + str(2), q), name="Thread" + str(2)).start()
    Thread(target=run(c, 'm' + str(3), q), name="Thread" + str(3)).start()
    Thread(target=run(d, 'm' + str(4), q), name="Thread" + str(4)).start()

    a = []

    while q.qsize() != 0:
        a.append(q.get())

    if mode == 4:
        ass = assemble4(ideal, a)
    elif mode == 16:
        ass = assemble16(ideal, a)
    elif mode == 64:
        ass = assemble64(ideal, a)
    elif mode == 256:
        ass = assemble256(ideal, a)
    else:
        ass = assemble256(ideal, a)
    ass.show()
    ass.save(disk + "/" + folder + "/output.bmp")


'''
Główna pętla programu
'''

# read image as RGB and add alpha (transparency)
ideal = Image.open("MonaLisa.png").convert("RGBA")


# Sterowanie
ilosc_w_populacji = 20
ilosc_petli = 5000
wspolczynnik_mutacji = 0.1
wartosc_alphy = 126
folder = "test"
disk = "D:/INZ2"
out = disk + "/" + folder + "/out.txt"

s = time.time()
aproximate(ideal, 4)
print("Czas wykonania: %s" % (time.time() - s))