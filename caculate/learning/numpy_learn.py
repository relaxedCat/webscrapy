import numpy as np
from scipy.optimize import fsolve
from scipy import integrate
a = np.array([2,0,1,5])

print(a)
print(a.min())
print(a.max())
print(a[:2])
a.sort()
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b*b)
print(b)
print(b.ndim) #维度
print(b.shape) #行数和列数
print(b.size) #元素的个数
c = np.linspace(1,2,30,dtype=np.float32)#返回无一个一个等差数列
print(c)
print(c.shape)
d = c[:,np.newaxis]#列上加一個維度
print(d)
print(d.shape)
print(c[np.newaxis,:])
print(c[np.newaxis,:].shape)#行上加个维度
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
print('=========================我是分隔符========================')
a_1 = np.array([[1,1],[0,1]],dtype=int)
b_1 = np.arange(4).reshape(2,2)
c_1 = np.dot(a_1,b_1)
c_2 = a_1.dot(b_1)
c_3 = a_1 * b_1
print(c_1)
print(c_2)
print(c_3)
e = np.random.random((2,4))
print(e)
print(np.sum(e))
print(np.max(e))
print(np.min(e))
print('=========================我是分隔符========================')
f = np.arange(0,12).reshape(3,4)
print(f)
#均值
print(np.mean(f))
print(np.average(f))
print(f.mean())
#中位数
print(np.median(f))
#累加函数
print(np.cumsum(f))
#累差函数
print(np.diff(f))
print(np.nonzero(f))
#转置
print(np.transpose(f))
print(f.T)
print(f.T.flatten())
for item in f.flat:
    print(item)
#合并
A = np.array([1,2,3])[:,np.newaxis]
B = np.array([1,2,3])[:,np.newaxis]
print(np.vstack((A,B)))
print(A.shape,np.vstack((A,B)).shape)
C = np.concatenate((A,B,A),axis=0)
print(C)
D = np.concatenate((A,B,B,A),axis=1)
print(D)
E = np.arange(12).reshape(3,4)
print(E)
print(np.split(E,2,axis=1))
print(np.split(E,3,axis=0))
print(np.array_split(E,3,axis=1))