import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

class quadratic:

    def __init__(self,F):
        a = F[0]
        minX = F[1]

        self.a = F[0]

        self.b = -2*a*minX
        self.c = a*minX**2
        # X = np.linspace(0,10,500)
        # Y = a*np.square(X) + b*X + c

    def apply(self,X):
        self.E  = np.log(1+self.a * np.square(X) + self.b * X + self.c)
        self.minE = np.min(self.E)
        self.minimumX = X[np.unravel_index(np.argmin(self.E,axis=None), self.E.shape)]
        self.X = X
        return self.E

    def evaluate(self):
        pass

##
# f1x = (2,1)
# f2x = (2,5)
# g1x = (3,4)
# g2x = (4,5)
#
# x1, f1 = make_quadratic(f1x)
# x2, f2 = make_quadratic(f2x)
#
# plt.subplot(1,2,1)
#
# plt.plot(x1,f1)
# plt.plot(x2,f2)
# # plt.plot(x1,f1+f2)
#
# f1min = np.min(f1)
# f2min = np.min(f2)
#
# x1min = x1[np.argmin(f1)]
# x2min = x2[np.argmin(f2)]
#
# plt.scatter(x1min,f1min)
# plt.scatter(x2min,f2min)
#
# plt.subplot(1,2,2)
#
#
# x1, g1 = make_quadratic(g1x)
# x2, g2 = make_quadratic(g2x)
#
# plt.plot(x1,g1)
# plt.plot(x2,g2)
# # plt.plot(x1,np.abs(g1-g2))
#
#
# g1min = g1[np.argmin(f1)]
# g2min = g2[np.argmin(f2)]
#
# x1min = x1[np.argmin(f1)]
# x2min = x2[np.argmin(f2)]
#
# plt.scatter(x1min,g1min)
# plt.scatter(x2min,g2min)
#
#
# plt.show()
#
#
#
# E = np.square(f1[np.argmin(f1)])+np.square(f2[np.argmin(f2)])\
#     +np.square(g1[np.argmin(f1)]-g2[np.argmin(f2)])
#
# gbar = .5*(g1min+g2min)
# ##
# Next, make mesh grid and plot over it find min exhaustively.


X1, X2 = np.meshgrid(np.linspace(2,7,10*10),np.linspace(2,7,10*10))

#Dfine arbitarty energy functgioms (quadratics)
f1x = quadratic((2,4))
f2x = quadratic((2,6))
g1x = quadratic((3,2.5))
g2x = quadratic((4,5))

#Solve for energies at various points on meshgrid
f1E = f1x.apply(X1)
g1E = g1x.apply(X1)

f2E = f2x.apply(X2)
g2E = g2x.apply(X2)

ET = f2E+f1E+np.square(g1E-g2E)

##PLotting Code
# plt.figure(); ax = sns.heatmap(f1E,yticklabels = X1[0,:]); ax.set_yticks(np.linspace(0,1,20)*ax.get_ylim()[0]); plt.title('Energy F1');plt.show()
# plt.figure(); sns.heatmap(f2E);plt.title('Energy F2');plt.show()

plt.figure(); sns.heatmap(f2E**2+f1E**2);plt.title('Energy Total');plt.show()

# plt.figure(); sns.heatmap(g1E); plt.title('Energy G1');plt.show()
# plt.figure(); sns.heatmap(g2E);plt.title('Energy G2');plt.show()

plt.figure(); sns.heatmap(np.square(g1E-g2E));plt.title(' Square of (G1-G2)');plt.show()

plt.figure(); sns.heatmap(f2E+f1E+np.square(g1E-g2E));plt.title('Total Energy function');plt.show()

ET = f2E+f1E+np.square(g1E-g2E)
X1minIDX,X2minIDX =np.unravel_index(np.argmin(ET,axis=None), ET.shape)
X1min = X1[X1minIDX,X1minIDX]
X2min = X2[X2minIDX,X2minIDX]
##
print('Algorithm Start')
## Algorithm
#X1min = 3.6363636363636362
#X2min = 2.4242424242424243

# use single row for convenience
x1 = X1[0,:]
x2 = X2[:,0]

f1Ea = f1E[0,:]
f2Ea = f2E[:,0]

g1Ea = g1E[0,:]
g2Ea = g2E[:,0]

idx1 =np.argmin(f1Ea)
idx2 = np.argmin(f2Ea)

x1hat = x1[idx1]
x2hat = x2[idx2]

gbar = (g1Ea[idx1]-g2Ea[idx2])/2



for iter in range(100):
    opt1 = np.square(f1Ea) + np.square(g1Ea - gbar)
    idx1 = np.argmin(opt1)
    opt2 = np.square(f2Ea) + np.square(g2Ea - gbar)
    idx2 = np.argmin(opt2)

    gbar = (g1Ea[idx1] - g2Ea[idx2]) ** 2
    # print(ET[idx1, idx2])
    # print("x1 guess", x1[idx1])
    # print("x2 guess", x2[idx2])

X1minIDX,X2minIDX =np.unravel_index(np.argmin(ET,axis=None), ET.shape)
X1min = X1[X1minIDX,X1minIDX]
X2min = X2[X2minIDX,X2minIDX]

print('Optimal min Log Energy = ', np.log(np.min(ET,axis=None)))
print('Optimal X1', X1min)
print('Optimal X2', X2min)



print('Min Log energy found', np.log(ET[idx1,idx2]))
print("x1 guess", x1[idx1])
print("x2 guess", x2[idx2])

print('ok')

