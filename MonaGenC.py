from CythonLib import MonaGen

# MonaGen.init()

tab = [1, 4, 16, 64, 256]
imgs = [23, 24, 25]

for i in range(len(imgs)):
    for j in range(len(tab)):
        MonaGen.run("C:/Users/Torak28/Desktop/Inzynierka/Official/Obrazy/" + str(imgs[i]) + ".png", tab[j], 20, 1000, 0.1, 126, "E:\\", "Wyniki2\\" + str(imgs[i]) + "\\" + str(tab[j]), "Wyniki2\\" + str(imgs[i]) + "\\" + str(tab[j]) + "\\o.txt")