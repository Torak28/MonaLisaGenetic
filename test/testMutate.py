import matplotlib.pyplot as plt

a = [79,53,33,18,12]

plt.plot([1,4,16,64,256], a, 'r-')
plt.axis([1, 260, 10, 100])
plt.title("Wartość funckji oceny w kolejnych trybach podziału")
plt.xlabel("Tryb podziału obrazu")
plt.ylabel("Wartość funkcji oceny")
plt.grid(True)
plt.show()