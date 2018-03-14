from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score #K折交叉验证模块

#加载iris数据
iris_data = load_iris()
X = iris_data.data
y = iris_data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
print(knn.score(X_test,y_test))

#使用K折交叉验证模块
scores = cross_val_score(knn,X,y,cv=5,scoring='accuracy')
#打印5次预测的准确率
print(scores)
#5次准去率的均值
print(scores.mean())

'''
准确率accuracy用来判断classification模型的好坏
'''

#建立测试数据集
k_range = range(1,31)
k_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
    k_scores.append(scores.mean())

#可视化数据
plt.plot(k_range,k_scores)
plt.xlabel('Value of k for Knn')
plt.ylabel('cross_validation accuracy')
plt.show()

'''
平均方差mean square error用来判断回归Regression的好坏
'''
k_range = range(1, 31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    loss = -cross_val_score(knn, X, y, cv=10, scoring='neg_mean_squared_error')
    k_scores.append(loss.mean())

plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated MSE')
plt.show()