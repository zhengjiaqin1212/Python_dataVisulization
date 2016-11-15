#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import  MultipleLocator,FuncFormatter

figure = plt.figure(figsize=(18,8));
axe = figure.add_subplot(1,1,1,axisbg='#BCD2EE');
figure.patch.set_color('white');
figure.set_alpha(0.5);
axe.set_alpha(0.50);
y_2016 = [10,100,200,240,300,359,450,500,521,574,619,669,721,769,807,841,873,900,930,955,979,1000,1028,1063,1111,1148,1207];
x_2016 = [1,7,16,40,65,87,96,150,250,425,480,540,600,660,720,780,840,900,960,1020,1080,1140,1200,1260,1320,1380,1440];

for index in range(len(y_2016)):
    plt.annotate(str(y_2016[index]),xy=(x_2016[index],y_2016[index]),xytext=(x_2016[index]-1,y_2016[index]+10))
axe.plot(x_2016,y_2016,'ro-',label="money")
# axe.scatter(x_2016,y_2016,color="#EE4000");
plt.legend(loc='best')
plt.xlabel("Time(s)")
plt.ylabel("sum of business transactions");
plt.title("double 11 in 2016")
plt.ylim(0,1300)
plt.xlim(0,60*24);
axe.xaxis.set_major_locator( MultipleLocator(60));
axe.xaxis.set_minor_locator( MultipleLocator(10) )
def xlabel(x,pos):
    num = int(x/60);
    label = str(num)+":00";
    return label;
axe.xaxis.set_major_formatter( FuncFormatter( xlabel ))
plt.show();