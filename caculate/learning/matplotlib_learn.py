import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x) + 1
z = np.cos(x**2) + 1

plt.figure(figsize = (8,4))
plt.plot(x,y,label = '$\sin x+1$',color = 'red',linewidth = '2')

plt.plot(x,z,'b--',label = '$\cos x^2 + 1$')
plt.xlabel('时间线')
plt.ylabel('Volt')
plt.title('the first picture')
plt.ylim(0,2.2)

plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False #解决保存图片时负号的显示问题
plt.legend()
plt.show()