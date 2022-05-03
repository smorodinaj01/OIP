import numpy as np
from matplotlib import pyplot as plt


#Метод для построения зависимости напряжения от времени, с настройками цвета и формы линии, 
# размера и цвета маркеров, частоты отображений маркеров и легендой

 
with open ("Settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]


volt = np.loadtxt("Data.txt", dtype = int)
volt = volt/256 * 3.3
fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
 

with open ("Settings.txt", "r") as settings:
    dT = float(settings.readline())

tmp = np.arange(0, len(volt)*dT, dT)

xmax = np.argmax(tmp)*dT
qmax = volt.argmax()


str1 = "Время зарядки =" + str(qmax*dT) + "s" 
str2 = "Время разрядки =" + (str((len(volt)-qmax)*dT)) + "s"

# Название графика и оси
ax.set_title("График зарядки и разрядки конденсатора.", fontsize = 17, wrap=True) 
ax.set_xlabel("Время t, с", fontsize = 15)
ax.set_ylabel("Напряжение V, В", fontsize = 15)


ax.plot(tmp, volt, color = 'b', label = "V(t)", marker = 'x', markevery = 20)  # Цвет синий
ax.minorticks_on()


ax.grid(which = 'major', color = 'g', linewidth = 0.5)
ax.grid(which = 'minor', color = 'g', linestyle = '--')


ax.legend()
ax.set(xlim=(0, xmax + 4), ylim=(0, 3.3))

# В версии graph 1:
# plt.text(0.3*len(tmp)*dT, 2, str1)
# plt.text(0.3*len(tmp)*dT, 1.5, str2)

plt.text(0.7*len(tmp)*dT, 2.0, str1)
plt.text(0.7*len(tmp)*dT, 1.7, str2)

fig.savefig("graph.svg")