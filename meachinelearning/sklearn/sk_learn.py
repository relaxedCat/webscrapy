from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
#属性
iris_x = iris.data
#标签
iris_y = iris.target
#训练集和测试集分开，测试集占用30%
x_train,x_test,y_train,y_test = train_test_split(iris_x,iris_y,test_size=0.3)
print(y_train)

#建立模型-训练-预测
knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
print(knn.predict(x_test))
print(y_test)
