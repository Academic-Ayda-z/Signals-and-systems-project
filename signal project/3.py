import math

import numpy as np
from matplotlib import pyplot as plt
from numpy.distutils.from_template import conv


def X(n):
    B = 10
    if -B / 2 < n < B / 2:
        return 1
    return 0


def H(n):
    if n >= 0:
        return math.exp(-n)
    return 0


def y(n, t,H,X):
    summ = 0
    for k in list(np.arange(-t,t,1)):
        summ += H(k) * X(n-k)
    return summ

t=15
result=[]
x=[]
for i in np.arange(-t,t,1):
    x.append(i)
    result.append(y(i,t,H,X))

plt.plot(x, result,label="y(n)")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()

