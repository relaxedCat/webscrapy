from sklearn import svm
from sklearn import datasets
import pickle
from sklearn.externals import joblib
clf = svm.SVC()
iris = datasets.load_iris()
X,y = iris.data,iris.target
print(X.size)
print(X.shape)
clf.fit(X,y)

#1、使用pickle保存
with open('./save/clf.pickle','wb') as f:
    pickle.dump(clf,f)
with open('./save/clf.pickle','rb') as f:
    clf2 = pickle.load(f)
    print(clf2.predict(X[0:1]))

#2、使用joblib保存
joblib.dump(clf,'./save/clf.pkl')
clf3 = joblib.load('./save/clf.pkl')
print(clf3.predict(X[0:1]))


