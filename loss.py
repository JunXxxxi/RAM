import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.font_manager import FontProperties
import csv


def readcsv(files):
    csvfile = open(files,'r')
    plots = csv.reader(csvfile, delimiter=',')
    x = []
    y = []
    for row in plots:
        y.append(float(row[2]))
        x.append(float(row[1]))
    return x,y


mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'

plt.figure()
x2, y2 = readcsv("run_train-tag-loss_1_restaurant.csv")
plt.plot(x2,y2, color='red',label='train')

# x,y=readcsv("logs/run_1619000034_r0.005_b32_l0.001_train-tag-loss_1.csv")
# plt.plot(x, y, 'red',label='train')

plt.xticks(fontsize=30)
plt.yticks(fontsize=30)

plt.ylim(0,2)
plt.xlim(0,1800)
plt.xlabel('Steps',fontsize=40)
plt.ylabel('Loss',fontsize=40)
plt.legend(fontsize=16)
plt.show()
