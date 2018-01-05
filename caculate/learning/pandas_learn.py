import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series([1,2,3],index=['a','b','c'])
d = pd.DataFrame([[1,2,3],[4,5,6],],columns=['a','b','c'])
d2 = pd.DataFrame(s)

print(d.head())
print(d.describe())
# pd.read_excel('../websrapy/resource/csv/xiuxiu.xls')
# d3 = pd.read_csv('../../webscrapy/resource/csv/xiuxiu.csv',encoding = 'utf-8')
# print(d3)

catering_sale = '../data/catering_sale.xls'
data = pd.read_excel(catering_sale,index_col=u'日期')
print(data.describe())
print(len(data))

plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False #解决保存图片时负号的显示问题
p = data.boxplot(return_type='dict') #画箱线图
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.08, y[i]))
plt.show()
