import os

def printFile(tab, out):
    f = open(out, 'a')
    ret = ""
    ret += "Ala ma kota"
    for _ in range(len(tab)):
        ret += " " + str(tab[_])
    f.write(ret + "\n")
    print(ret)

out = 'test.txt'
tab = [1, 2, 3, 4, 5]

if os.path.exists(out):
    os.remove(out)

for i in range(5, 10):
    tab.append(i)
    printFile(tab, out)