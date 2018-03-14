from sklearn.model_selection import validation_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits.data
y = digits.target

param_range = np.logspace(-6,-2.3,5)
train_loss,test_loss = validation_curve(SVC(),X,y,param_range=param_range,param_name='gamma',cv=10,scoring='accuracy')
train_loss_mean = np.mean(train_loss,axis=1)
test_loss_mean = np.mean(test_loss,axis=1)

plt.plot(param_range,train_loss_mean,'o-',label='training',color = 'red')
plt.plot(param_range,test_loss_mean,'o-',label='testing',color = 'green')
plt.xlabel('gamma')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()