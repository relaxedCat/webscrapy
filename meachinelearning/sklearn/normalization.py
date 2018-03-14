from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
#数据正规化
a = np.arange(9,dtype=np.float64).reshape(3,3)
print(a)
print(preprocessing.scale(a))

X,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,random_state=22,n_clusters_per_class=1,scale=100)
#可视化数据
plt.scatter(X[:,0],X[:,1],c = y)
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = SVC()
clf.fit(X_train,y_train)
#正规化之前
print(clf.score(X_test,y_test))
X = preprocessing.scale(X)
plt.scatter(X[:,0],X[:,1],c = y)
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf.fit(X_train,y_train)
#正规化之后
print(clf.score(X_test,y_test))