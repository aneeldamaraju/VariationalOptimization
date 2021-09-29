

import numpy as np
from matplotlib import pyplot as plt


def make_quadratic(F):
    a = F[0]
    minX = F[1]
    X = np.linspace(0,10,500)
    b = -2*a*minX
    c = a*minX**2
    print(c)
    Y = a*np.square(X) + b*X + c

    return X,Y

f1x = (2,1)
f2x = (2,5)
g1x = (3,4)
g2x = (4,5)

x1, f1 = make_quadratic(f1x)
x2, f2 = make_quadratic(f2x)

plt.subplot(1,2,1)

plt.plot(x1,f1)
plt.plot(x2,f2)
# plt.plot(x1,f1+f2)

f1min = np.min(f1)
f2min = np.min(f2)

x1min = x1[np.argmin(f1)]
x2min = x2[np.argmin(f2)]

plt.scatter(x1min,f1min)
plt.scatter(x2min,f2min)

plt.subplot(1,2,2)


x1, g1 = make_quadratic(g1x)
x2, g2 = make_quadratic(g2x)

plt.plot(x1,g1)
plt.plot(x2,g2)
# plt.plot(x1,np.abs(g1-g2))


g1min = g1[np.argmin(f1)]
g2min = g2[np.argmin(f2)]

x1min = x1[np.argmin(f1)]
x2min = x2[np.argmin(f2)]

plt.scatter(x1min,g1min)
plt.scatter(x2min,g2min)


plt.show()



E = np.square(f1[np.argmin(f1)])+np.square(f2[np.argmin(f2)])\
    +np.square(g1[np.argmin(f1)]-g2[np.argmin(f2)])

gbar = .5*(g1min+g2min)

# Next, make mesh grid and plot over it find min exhaustively.
plt.figure()

