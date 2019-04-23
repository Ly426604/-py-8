"""
name:Liu guiping
date:2019.04.23
function:数据拟合
"""
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
params = dict(
fname = R"C:\Users\HUAWEI\Desktop\python\巨磁1.csv",#打开文件巨磁3.csv
delimiter = ',',
usecols = (0,1,2,3,4),

unpack = True
)
x,y1,y2,y3,y4= np.loadtxt(**params)

def func(x,a,b):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """

    return a*x+b
def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y1 - func(x, a1, b1)
popt, pcov = curve_fit(func, x, y1)
def residuals(p, y2, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y2 - func(x, a2, b2)
popt, pcov = curve_fit(func, x, y2)
def residuals(p, y3, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y3 - func(x, a3, b3)
popt, pcov = curve_fit(func, x, y3)
def residuals(p, y4, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y4 - func(x, a4, b4)
popt, pcov = curve_fit(func, x, y4)
a1=0.0126
b1=25.5
x1=np.arange(-300, 300, 1)
y1vals=func(x1,a1,b1)
a2=0.012166667
b2=25.2
x1=np.arange(-300, 300, 1)
y2vals=func(x1,a2,b2)
a3=0.015166667
b3=150.9
x1=np.arange(-300, 300, 1)
y3vals=func(x1,a3,b3)
a4=0.015333333
b4=150.8
x1=np.arange(-300, 300, 1)
y4vals=func(x1,a4,b4)		
plt.plot(x,y1)
plot1=plt.plot(x, y1, '*',label='Real Data')
plt.plot(x,y2)
plot1=plt.plot(x, y2, 'x',label='Real Data')
plt.plot(x,y3)
plot1=plt.plot(x, y3, '.',label='Real Data')
plt.plot(x,y4)
plot1=plt.plot(x, y4, '*',label='Real Data')
plot2=plt.plot(x1, y1vals, 'r',label='Fitting1 function')
plot2=plt.plot(x1, y2vals, 'b',label='Fitting2 function')
plot2=plt.plot(x1, y3vals, 'r',label='Fitting3 function')
plot2=plt.plot(x1, y4vals, 'y',label='Fitting4 function')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')
plt.show()
plt.savefig('p2.png')