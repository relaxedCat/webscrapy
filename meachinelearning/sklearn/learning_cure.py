from sklearn.model_selection import learning_curve #学习曲线
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits.data
y = digits.target

train_size,train_loss,test_loss = learning_curve(SVC(gamma=0.001),X,y,cv=10,scoring='accuracy',train_sizes=[0.1,0.25,0.5,0.75,1])
train_loss_mean = np.mean(train_loss,axis=1)
test_loss_mean = np.mean(test_loss,axis=1)
print(train_size)
print('=========train loss============')
print(train_loss_mean)
print('=========test loss============')
print(test_loss_mean)

plt.plot(train_size,train_loss_mean,'o-',color = 'red',label = 'training')
plt.plot(train_size,test_loss_mean,'o-',color = 'green',label = 'testing')
plt.xlabel('train sizes')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()