import math

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad

T = 8
n = 10

def sinc(x):
    if x == 0:
        return 1
    return math.sin(x * math.pi) / (x * math.pi)

def ak(x):
    global T
    t1 = 4
    d = t1 / T
    return d * sinc(x * d)


def XX(x):
    if abs(x)%8<=2 or abs(x)%8>=6:
        return 1
    return 0



def a(n):
    return 2 / T * quad(lambda x,n:XX(x)*np.cos(2 * math.pi/T * x * n), -4, 4, args=(n))[0]


def x(t):
    global T
    summ = 0.5
    for k in range(1, n + 1):
        summ += a(k) * np.cos(2 * k * t * math.pi / T)  # *cmath.exp(1j*k*t*2*cmath.pi/T)
    return summ



y_result2 = []
x_result = np.arange(-12, 12, 0.01)
y_result=x(x_result)
for i in x_result:
    y_result2.append(XX(i))

plt.plot(x_result, y_result, label="")
plt.plot(x_result, y_result2,label="")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
# plt.title('')
plt.legend()
plt.show()
