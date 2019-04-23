
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
import matplotlib as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
# x=np.arange('2018-01-01','2019-01-01',dtype='datetime64[M]')
x=np.arange(1,13,1)
print(x)
y=[17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
y1=[-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]
def func(x,a,b,c):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """

    return a*x*x+b*x+c
def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, a, b, c)
popt, pcov = curve_fit(func, x, y)
a=-0.2
b=-0.11
c=339/24
x1=np.arange(1,13, 1)
y1vals=func(x1,a,b,c)
pl.plot(x,y,"*",label="Maximum temperature")
plot2=pl.plot(x1, y1vals, 'r',label='Fitting function')
pl.plot(x,y1,"*",label="Minimum temperature")
pl.plot(x,y)
pl.plot(x,y1)
pl.xlabel('x axis')
pl.ylabel('y axis')
pl.show()
pl.savefig('p2.png')