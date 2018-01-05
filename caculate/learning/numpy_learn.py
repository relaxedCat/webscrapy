import numpy as np
from scipy.optimize import fsolve
from scipy import integrate
a = np.array([2,0,1,5])

print(a)
print(a.min())
print(a.max())
print(a[:3])
a.sort()
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b*b)

print('=========================我是分隔符========================')

def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 -1,x1**2 - x2 -2]

result = fsolve(f,[1,1])
print(result)
print('=========================我是分隔符========================')

def g(x):
    return (1 - x**2) ** 0.5
pi_2,err = integrate.quad(g,-1,1)
print(pi_2 * 2)
