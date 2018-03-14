from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

bost_data = datasets.load_boston()
bost_x = bost_data.data
bost_y = bost_data.target
model = LinearRegression()
train_x,test_x,train_y,test_y = train_test_split(bost_x,bost_y,test_size=0.3)
model.fit(train_x,train_y)
print(model.predict(bost_x[:4,:]))
print(bost_y[:4])
#斜率
print(model.coef_)
#截距
print(model.intercept_)
#获取之前定义的参数
print(model.get_params())
#R^2打分输出精度
print(model.score(test_x,test_y))
x,y = datasets.make_regression(n_samples=1000,n_features=1,n_targets=1,noise=10)
plt.scatter(x,y)
plt.show()