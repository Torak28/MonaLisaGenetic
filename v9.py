from CythonLib import MonaGen

imgs = ["BFF", "J",  "Stanczyk", "UK2", "MonaLisa.png"]
for _ in range(len(imgs)):
    print(imgs[_] + " start!")
    MonaGen.run(imgs[_] + ".png", 1, 20, 20, 0.1, 126, "E:\\", "INZ2\\" + imgs[_] + "\\1", "INZ2\\" + imgs[_] + "\\1\\out.txt")
    print("1 done")
    MonaGen.run(imgs[_] + ".png", 4, 20, 20, 0.1, 126, "E:\\", "INZ2\\" + imgs[_] + "\\4", "INZ2\\" + imgs[_] + "\\4\\out.txt")
    print("4 done")
    MonaGen.run(imgs[_] + ".png", 16, 20, 20, 0.1, 126, "E:\\", "INZ2\\" + imgs[_] + "\\16", "INZ2\\" + imgs[_] + "\\16\\out.txt")
    print("16 done")
    MonaGen.run(imgs[_] + ".png", 64, 20, 20, 0.1, 126, "E:\\", "INZ2\\" + imgs[_] + "\\64", "INZ2\\" + imgs[_] + "\\64\\out.txt")
    print("64 done")
    MonaGen.run(imgs[_] + ".png", 256, 20, 20, 0.1, 126, "E:\\", "INZ2\\" + imgs[_] + "\\256", "INZ2\\" + imgs[_] + "\\256\\out.txt")
    print("256 done")
    print(imgs[_] + " done!")