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
y # target variable/label

# seperate independent and dependent variable 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
x_train
y_test
y_train

# Decision Tree 
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test) # to confirm how well learning is operated
y_pred

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

classifier.predict([[5.1,3.5,1.4,0.2]])[0] # Testing 

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
plt.title('Petal') # more dense, easier to express as a line 

model = KMeans(n_clusters=3) # k value
model.fit(iris.iloc[:,0:4]) # fit() <- learning  
model.labels_

colormap = np.array(['red','blue','black'])
plt.scatter(iris.PetalLength, iris.PetalWidth, c=colormap[model.labels_], s=40)
plt.title("K Mean Classification")

model



# 3. Linear Regression 
# Use sklearn 
from scipy import stats 
score = pd.read_csv("C://data/score.txt")
slope, intercept, r_value, p_value, std_err = stats.linregress(score.iloc[:,2], score['성적'])

p_value < 0.05
## There are a certain correlation between IQ and grade! -> reject H0

from sklearn import linear_model # create linear regression model
reg = linear_model.LinearRegression() # make it an instance variable 
reg.fit(score.iloc[:,2:6], score['성적']) # fitting 
print('절편 : \n',reg.intercept_)
print('기울기 : \n',reg.coef_)
