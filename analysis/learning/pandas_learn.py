import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
s = pd.Series([1,2,3],index=['a','b','c'])
d = pd.DataFrame([[1,2,3],[4,5,6],],columns=['a','b','c'])
d2 = pd.DataFrame(s)

print(d.head())
print(d.describe())
# pd.read_excel('../websrapy/resource/csv/xiuxiu.xls')
# d3 = pd.read_csv('../../webscrapy/resource/csv/xiuxiu.csv',encoding = 'utf-8')
# print(d3)

# catering_sale = '../data/catering_sale.xls'
# data = pd.read_excel(catering_sale,index_col=u'日期')
# print(data.describe())
# print(len(data))
#
# plt.figure()
# plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示问题
# plt.rcParams['axes.unicode_minus'] = False #解决保存图片时负号的显示问题
# p = data.boxplot(return_type='dict') #画箱线图
# x = p['fliers'][0].get_xdata()
# y = p['fliers'][0].get_ydata()
# y.sort()
# for i in range(len(x)):
#     if i > 0:
#         plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]), y[i]))
#     else:
#         plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.08, y[i]))
# plt.show()
print('====================我是分隔符=================')

s = pd.Series([1,3,6,np.nan,44,1])
print(s)

dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
print(df['b'])

df1 = pd.DataFrame(np.arange(0,12,1,dtype=np.int).reshape(3,4))
print(df1)

df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20180131'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3] * 4,dtype='int32'),
                    'E':pd.Categorical(['test','train','test','train']),
                    'F':'foo'})
print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)

print('===============我是分隔符2==============')
dates = pd.date_range('20130101', periods=6)
df3 = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print('===============选取数据==============')
print(df3)
print(df3.A)
print(df3[0:3])
print(df3['20130101':'20130103'])
print(df3.loc['20130103'])
print(df3.loc[:,['A','B']])
print('========位置选取法=============')
print(df3.iloc[3:1])
#行index3、4和列index 1、2
print(df3.iloc[3:5,1:3])
#行1、3、5 列1、2
df3['F'] = np.nan
df3['E'] = pd.Series([1,2,3,4,5,6,],index=pd.date_range('20130101',periods=6))
print(df3)

print(df3.iloc[[1,3,5],1:3])
#混合模式:前3行，AC两列
print(df3.ix[:3,['A','C']])
#条件筛选
print(df3[df3.A > 8])
df3.iloc[2,2] = 111
df3.loc['20130102','B'] = 2222
df3.B[df3.A > 4] = 0
print('====================缺失值处理===================')
datass = pd.date_range('20180101',periods=6)
df4 = pd.DataFrame(np.arange(24).reshape((6,4)),index=datass,columns=['A','B','C','D'])
df4.iloc[0,1] = np.nan
df4.iloc[1,2] = np.nan
print(df4)
print(df4.dropna(axis=0,how='any'))#0:对行操作，1：对列操作；any:只要存在NaN就drop掉，'all'：必须是全部NaN才drop掉
print(df4.fillna(value=0)) #对所有的NaN的值进行替换为0
print(df4.isnull()) #判断是否有缺失值
print(np.any(df4.isnull()) == True) # 检测是否有缺失值，若存在即返回

print('=======================合并操作=========================')
df5 = pd.DataFrame(np.ones((3,4)) * 0,columns=['a','b','c','d'])
df6 = pd.DataFrame(np.ones((3,4)) * 1,columns=['a','b','c','d'])
df7 = pd.DataFrame(np.ones((3,4)) * 2,columns=['a','b','c','d'])
res = pd.concat([df5,df6,df7],axis=0,ignore_index=True)
res1 = pd.concat([df5,df6,df7],axis=1)
print(res)
print(res1)
df8 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df9 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])
res3 = pd.concat([df8,df9],axis=0,join='outer')
print(res3)

df10 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res4 = df10.append([s1],ignore_index=True)
print(res4)

# data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# print(type(data))
# #累加
# data = data.cumsum()
# data.plot()
# plt.show()

dataframe = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list('ABCD')
)
# dataframe = dataframe.cumsum()
# dataframe.plot()
# plt.show()
ax = dataframe.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
dataframe.plot.scatter(x='B',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()