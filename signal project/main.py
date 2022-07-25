import cmath
import math
import numpy as np
from matplotlib import pyplot as plt
from numpy.distutils.from_template import conv
T=8
n=10

def sinc(x):
    if x==0:
        return 1
    return math.sin(x*math.pi)/(x*math.pi)

def ak(x):
    global T
    t1=4
    d=2*t1/T
    return d*sinc(x*d)

def x(t):
    summ=0
    for k in range(-10,10):
       summ=ak(k)*cmath.exp(1j*k*t*2*cmath.pi/T)#cos(2*math.pi/T *t)
    return summ

print(x(7.5))
def XX(t):
    if -2<=t%8<=2:
        return 1
    return 0

x_result=[]
y_result=[]
y_result2=[]
for i in range(0,n+1):
    x_result.append(i)
    y_result.append(x(i))
    y_result2.append(XX(i))

plt.plot(x_result, y_result,label="")
#plt.plot(x_result, y_result2,label="")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
#plt.title('')
plt.legend()
plt.show()