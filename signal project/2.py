import matplotlib.pyplot as plt
import numpy as np


def sinc(i):
    return np.sin((i * 6 + 7) * np.pi) / ((i * 6 + 7) * np.pi)


def sinc2(i):
    return np.sin((i) * np.pi) / ((i) * np.pi)


x = np.arange(-2 * np.pi, 2 * (np.pi), 0.01)
y = sinc(x)
y2 = sinc2(x)

# plotting the points
plt.plot(x, y, label="sinc(6t+7)")
plt.plot(x, y2, label="sinc(t)")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('sinc(t) vs sinc(6t+7)')
plt.legend()
plt.show()
