# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:24:13 2018

@author: mypc
"""

# 1. KNN
import pandas as pd
dataset=pd.read_csv("C:/data/iris.csv")
dataset.head()
x=dataset.drop('Name',axis=1)
y=dataset['Name']
x
y ### 목표변수/label값

# 독립변수와 종속변수 분리
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
x_train
y_test
y_train

# 의사결정트리 
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test) ### 학습이 잘 됬는가를 확인하는 것
y_pred

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

classifier.predict([[5.1,3.5,1.4,0.2]])[0] ### Testing 

classifier.score(x_train, y_train)
classifier.score(x_test, y_test)



# 2. KMeans 
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv("C:\data\iris.csv")
iris.head() 

plt.scatter(iris.SepalLength, iris.SepalWidth, s=40)
plt.title('Sepal')
plt.scatter(iris.PetalLength, iris.PetalWidth, s=40)
plt.title('Petal') ### 더 촘촘하게 잘 모여 있고, linear로 분류 가능 

model = KMeans(n_clusters=3) ### k값
model.fit(iris.iloc[:,0:4]) ### fit() <- 학습 
model.labels_

colormap = np.array(['red','blue','black'])
plt.scatter(iris.PetalLength, iris.PetalWidth, c=colormap[model.labels_], s=40)
plt.title("K Mean Classification")

model



# 3. Linear Regression 
# sklearn 이용 
from scipy import stats 
score = pd.read_csv("C://data/score.txt")
slope, intercept, r_value, p_value, std_err = stats.linregress(score.iloc[:,2], score['성적'])

p_value < 0.05
## IQ와 성적에는 상관관계가 있다! -> reject H0

from sklearn import linear_model ### 선형회귀모형을 만듬 
reg = linear_model.LinearRegression() ### 인스턴스화 
reg.fit(score.iloc[:,2:6], score['성적']) ### fitting 
print('절편 : \n',reg.intercept_)
print('기울기 : \n',reg.coef_)
