import matplotlib.pyplot as plt
import numpy as np

gruplar =["A","B","C"]
veriler =[15,45,30]
plt.figure(figsize=(12,4))
plt.subplot(131)
plt.bar(gruplar,veriler)
plt.title("Üst Başlık")
plt.subplot(132)
plt.scatter(gruplar,veriler)
plt.title("Üst Başlık")
plt.suptitle(133)
plt.plot(gruplar,veriler)
plt.suptitle("Kategoriler")
plt.show()
