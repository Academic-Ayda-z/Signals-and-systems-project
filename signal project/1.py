import cmath
import matplotlib.pyplot as plt

N = 22
yImg=[]
yReal=[]
y = []
x=[]

def X(k):
    return (3/4) ** k


Y = [X(i) for i in range(N)]


def ak(N, X, k):
    Sum = 0
    for n in range(N):
        Sum += cmath.exp(-k * cmath.pi * 2 / N * n * 1j) * complex(X(n))
    return Sum / N


def xn(N, ak, n):
    Sum = 0
    global y,yImg, yReal
    for k in range(N):
        Sum += cmath.exp(k * cmath.pi * 2 / N * n * 1j) * complex(ak(N, X, k))
    y.append(Sum)
    yImg.append(Sum.imag)
    yReal.append(Sum.real)


for i in range(N):
    x.append(i)
    xn(N, ak, i)

# plotting the line 1 points
fig=plt.figure()
# naming the x axis
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4=fig.add_subplot(224)


plt1.plot(x, y, color='r')
plt1.set_title(' "fourie series"  $y =0.75^x $')

plt2.plot(x, yImg, color='b')
plt2.set_title('Imaginary')

plt3.plot(x, yReal, color='g')
plt3.set_title('Real')

plt4.plot(x, Y, color='black')
plt4.set_title('$y=0.75^x$')

fig.subplots_adjust(hspace=.5, wspace=0.5)

# function to show the plot
plt.show()
