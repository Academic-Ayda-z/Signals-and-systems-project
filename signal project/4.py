import math
from scipy.fftpack import ifft
from scipy.fftpack import fft
import numpy as np
from matplotlib import pyplot as plt


all_t = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
def h(t):
    return math.exp(abs(t)*-2)

def H():
#    return 2 / (1 + w ** 2)
    return fft([h(i) for i in all_t])


def xs(t):
    return math.cos(t / 10)


def xn(t):
    return 3 / 10 * math.cos(10 * t)


def xTotal():
    total = []
    for num in all_t:
        total.append(xn(num) + xs(num))
    return total

def xt():
    total=xTotal()
    plt.plot(all_t, total)
    plt.xlabel('t - axis')
    plt.ylabel('y - axis')
    plt.title('B')
    plt.show()



yW = []


def Hjw():
    yW=H()
    plt.plot(all_t, yW)
    plt.xlabel('W - axis')
    plt.ylabel('H(jW) - axis')
    plt.title('A')
    plt.show()

def yt():
    XW = fft(xTotal())
    HW = H()
    YW = []
    for i in range(len(HW)):
        YW.append(XW[i]*HW[i])

    y = ifft(YW)
    yt=[]
    for i in y:
        yt.append(abs(i))
    return yt
def y_():
    y=yt()
    plt.plot(all_t,y)
    plt.xlabel('t - axis')
    plt.ylabel('y - axis')
    plt.title('C')
    plt.show()


Hjw()
xt()
y_()
plt.plot(all_t, yt())
plt.plot(all_t,xTotal())
plt.xlabel('t - axis')
plt.ylabel('xTotal vs y(t)')
plt.title('D')
plt.legend()
plt.show()
