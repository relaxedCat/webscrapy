import numpy as np
import matplotlib.pyplot as plt

'''
# x = np.linspace(0,10,1000)
# y = np.sin(x) + 1
# z = np.cos(x**2) + 1
#
# plt.figure(figsize = (8,4))
# plt.plot(x,y,label = '$\sin x+1$',color = 'red',linewidth = '2')
#
# plt.plot(x,z,'b--',label = '$\cos x^2 + 1$')
# plt.xlabel('时间线')
# plt.ylabel('Volt')
# plt.title('the first picture')
# plt.ylim(0,2.2)
#
# plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示问题
# plt.rcParams['axes.unicode_minus'] = False #解决保存图片时负号的显示问题
# plt.legend()
# plt.show()
'''

# x = np.linspace(-1,1)
# y = 2 * x + 1
# plt.figure()
# plt.plot(x,y,label='esfsfsefesf',color = 'red')
# plt.xlabel('x value')
# plt.ylabel('y value')
# plt.show()

x1 = np.linspace(-3,3)
y1 = 2 * x1 + 1
y2 = x1 **2

plt.figure(num=3,figsize=(8,5))
plt.plot(x1,y1,color='red',linewidth=2.0,linestyle='--',label='red line')
plt.plot(x1,y2,label='blue line')
#设定x范围
plt.xlim(-1,2)
#设定y范围
plt.ylim(-2,3)
plt.xlabel('x的值')
plt.ylabel('y的值')
plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False #解决保存图片时负号的显示问题
#设定x刻度
x_ticks = np.linspace(-1,2,5)
plt.xticks(x_ticks)
#设定y刻度
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])
#移动坐标轴
ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
#显示图例：根据label，默认显示在左上角，upper right：右上角
plt.legend(loc='best')
plt.show()

#散点图
def plotscatter():
    n = 1024
    X = np.random.normal(0,1,n)
    Y = np.random.normal(0,1,n)
    #color value
    T = np.arctan2(Y,X)
    plt.scatter(X,Y,s=75,c=T,alpha=0.5)
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    #忽视x,y轴
    plt.xticks(())
    plt.yticks(())
    plt.show()
#柱状图
def plotbar():
    n = 12
    X = np.arange(n)
    print(X)
    Y = np.arange(12)
    print(Y)
    plt.bar(X,Y,facecolor='#ff9999', edgecolor='white')
    for x,y in zip(X,Y):
        plt.text(x,y,'%0.2f'%y,ha='center', va='bottom')
    plt.show()
if __name__ == '__main__':
    # plotscatter()
    plotbar()