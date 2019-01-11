# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:05:45 2018

@author: Cavin
"""
# A program to predict the NHL matches using the Poisson Distribution and Skellam Distribution 

# Sources
## https://www.hockey-reference.com/leagues/NHL_2019_games.html
## https://github.com/dashee87/blogScripts/blob/master/Jupyter/2017-06-04-predicting-football-results-with-statistical-modelling.ipynb

# 1. Poisson Distribution 
## Package 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from scipy.stats import poisson, skellam

## Dataset 
ice = pd.read_csv("C:/data/hockey.csv")
display(ice)
ice.columns
ice = ice[['Home','Visitor','G.1','G']]
ice = ice.rename(columns={'G.1': 'Home Goals', 'G': 'Away Goals'})

ice.mean()

## using Skellam statistics 
### probability of draw between home and away team
skellam.pmf(0, ice.mean()[0], ice.mean()[1])
### probability of home team winning by one goal
skellam.pmf(1, ice.mean()[0], ice.mean()[1])
### probability of home team winning by two goals
skellam.pmf(2, ice.mean()[0], ice.mean()[1])
### probability of home team losing by one goal
skellam.pmf(-1, ice.mean()[0], ice.mean()[1])

## importing the tools required for the Poisson regression model
import statsmodels.api as sm
import statsmodels.formula.api as smf

ice.head()
ice_h = ice[['Home','Visitor','Home Goals']]
ice_h.columns = ['team','opponent','goals']
ice_h['field'] = 'home'
ice_a = ice[['Visitor','Home','Away Goals']]
ice_a.columns = ['team','opponent','goals']
ice_a['field'] = 'away'
ice_data = pd.concat([ice_h, ice_a])

poisson0 = smf.glm(formula="goals ~ field + team + opponent", data=ice_data).fit()
poisson0.summary()

## simulation 
ice.mean()
home_avg = poisson0.predict(pd.DataFrame(data={'team': 'Vancouver Canucks', 'opponent': 'Pittsburgh Penguins','field':'home'},index=[0]))
away_avg = poisson0.predict(pd.DataFrame(data={'team': 'Pittsburgh Penguins', 'opponent': 'Vancouver Canucks','field':'away'},index=[0]))
team_pred = [[poisson.pmf(i, team_avg) for i in range(0, 6)] for team_avg in [home_avg, away_avg]]
van_pit = np.outer(np.array(team_pred[0]), np.array(team_pred[1]))
print(van_pit)

### probability of Vancouver winning by one goal
skellam.pmf(1, home_avg[0], away_avg[0])
### probability of Vancouver winning by two goals
skellam.pmf(2, home_avg[0], away_avg[0])
### probability of Vancouver losing by one goal
skellam.pmf(-1, home_avg[0], away_avg[0])

### Vancouver win
np.sum(np.tril(van_pit, -1))
### draw
np.sum(np.diag(van_pit))
### Pittsburgh win
np.sum(np.triu(van_pit, 1))

## Visualisation
## 1. construct Poisson  for each mean goals value
poisson_pred = np.column_stack([[poisson.pmf(i, ice.mean()[j]) for i in range(8)] for j in range(2)])

### plot histogram of actual goals
plt.hist(ice[['Home Goals', 'Away Goals']].values, range(9), alpha=0.7, label=['Home', 'Away'],normed=True, color=["skyblue", "orange"])

### add lines for the Poisson distributions
pois1, = plt.plot([i-0.5 for i in range(1,9)], poisson_pred[:,0], linestyle='-', marker='o',label="Home", color = 'darkblue')
pois2, = plt.plot([i-0.5 for i in range(1,9)], poisson_pred[:,1], linestyle='-', marker='o',label="Away", color = 'yellow')

leg=plt.legend(loc='upper right', fontsize=13, ncol=2)
leg.set_title("Poisson           Actual        ", prop = {'size':'14', 'weight':'bold'})

plt.xticks([i-0.5 for i in range(1,9)],[i for i in range(9)])
plt.xlabel("Goals",size=13)
plt.title("Average Number of Goals",size=14,fontweight='bold')
plt.ylim([-0.004, 0.4])
plt.tight_layout()
plt.show()

## 2. Skellam 
skellam_pred = [skellam.pmf(i,  ice.mean()[0],  ice.mean()[1]) for i in range(-7,9,2)]

plt.hist(ice[['Home Goals']].values - ice[['Away Goals']].values, range(-7,9,2), alpha=0.7, label='Actual',normed=True, color = 'skyblue')
plt.plot([i+0.5 for i in range(-7,9,2)], skellam_pred, linestyle='-', marker='o',label="Skellam", color = 'darkblue')
plt.legend(loc='upper right', fontsize=13)
plt.xticks([i+0.5 for i in range(-7,9,2)],[i for i in range(-7,9,2)])
plt.xlabel("Home Goals - Away Goals",size=13)
plt.title("Difference in Goals",size=14,fontweight='bold')
plt.ylim([-0.004, 0.20])
plt.tight_layout()
plt.show() 

## 3. Vancouver and Pittsburgh 
fig,(ax1,ax2) = plt.subplots(2, 1)

van_home = ice[ice['Home']=='Vancouver Canucks'][['Home Goals']].apply(pd.value_counts,normalize=True)
van_home_pois = [poisson.pmf(i,np.sum(np.multiply(van_home.values.T,van_home.index.T),axis=1)[0]) for i in range(8)]
pit_home = ice[ice['Home']=='Pittsburgh Penguins'][['Home Goals']].apply(pd.value_counts,normalize=True)
pit_home_pois = [poisson.pmf(i,np.sum(np.multiply(pit_home.values.T,pit_home.index.T),axis=1)[0]) for i in range(8)]

van_away = ice[ice['Visitor']=='Vancouver Canucks'][['Away Goals']].apply(pd.value_counts,normalize=True)
van_away_pois = [poisson.pmf(i,np.sum(np.multiply(van_away.values.T,van_away.index.T),axis=1)[0]) for i in range(8)]
pit_away = ice[ice['Visitor']=='Pittsburgh Penguins'][['Away Goals']].apply(pd.value_counts,normalize=True)
pit_away_pois = [poisson.pmf(i,np.sum(np.multiply(pit_away.values.T,pit_away.index.T),axis=1)[0]) for i in range(8)]

ax1.bar(van_home.index-0.4,van_home.values,width=,color="#034694",label="Vancouver")
ax1.bar(pit_home.index,pit_home.values,width=0.4,color="#EB172B",label="Pittsburgh")
pois1, = ax1.plot([i for i in range(8)], van_home_pois, linestyle='-', marker='o',label="Vancouver", color = "#0a7bff")
pois1, = ax1.plot([i for i in range(8)], pit_home_pois, linestyle='-', marker='o',label="Pittsburgh", color = "#ff7c89")

leg=ax1.legend(loc='upper right', fontsize=12, ncol=2)
leg.set_title("Poisson                 Actual                ", prop = {'size':'14', 'weight':'bold'})
ax1.set_xlim([-0.5,7.5])
ax1.set_ylim([-0.01,0.65])
ax1.set_xticklabels([])
### mimicing the facet plots in ggplot2 with a bit of a hack
ax1.text(7.65, 0.585, '                Home                ', rotation=-90,
        bbox={'facecolor':'#ffbcf6', 'alpha':0.5, 'pad':5})
ax2.text(7.65, 0.585, '                Away                ', rotation=-90,
        bbox={'facecolor':'#ffbcf6', 'alpha':0.5, 'pad':5})

ax2.bar(van_away.index-0.4,van_away.values,width=0.4,color="#034694",label="Vancouver")
ax2.bar(pit_away.index,pit_away.values,width=0.4,color="#EB172B",label="Pittsburgh")
pois1, = ax2.plot([i for i in range(8)], van_away_pois,
                  linestyle='-', marker='o',label="Chelsea", color = "#0a7bff")
pois1, = ax2.plot([i for i in range(8)], pit_away_pois,
                  linestyle='-', marker='o',label="Pittsburgh", color = "#ff7c89")
ax2.set_xlim([-0.5,7.5])
ax2.set_ylim([-0.01,0.65])
ax1.set_title("Number of Goals per Match",size=14,fontweight='bold')
ax2.set_xlabel("Goals per Match",size=13)
ax2.text(-1.15, 0.9, 'Proportion of Matches', rotation=90, size=13)
plt.tight_layout()
plt.show()



# 2. KNN-Classification 
## https://www.statista.com/statistics/675382/average-nhl-salary-by-team/
## http://www.espn.com/nhl/attendance
## https://theathletic.com/210035/2018/01/12/sizing-up-the-nhl-2017-18-nhl-teams-by-age-height-and-weight/
## https://www.nhlnumbers.com/team-salaries

## https://blog.goodaudience.com/predicting-fifa-world-cup-2018-using-machine-learning-dc07ad8dd576 
'''
name: team name
gf: goals for
sf: shots for
pn: 
pim: 
ga: goals against
sa: shots against
ppg: power play goals
ppo: power play occurrence
esg: even strength goals 
eso: even strength occurence 
field: home/away
salary: average salary of players 
attendence
age: average age of players 
height	
weight	
result: win/lose <- dependent variable 
'''
import pandas as pd
import numpy as np

data = pd.read_csv("C:\data\icehockey.csv")
data.head()

'''
## Chi-Square Statistics to remove insignificant variables 
def chi_square(x):
    a = np.array(data[x])
    b = np.array(data['result'])
    c = pd.crosstab(a,b, rownames=[x], colnames=['result'])

    from scipy.stats import chi2_contingency
    from scipy.stats import chi2
    stat, p, dof, expected = chi2_contingency(c)
    ### interpret test-statistic
    prob = 0.95
    critical = chi2.ppf(prob, dof)
    if abs(stat) >= critical:
        print(p)
        print('Dependent (reject H0)')
    else:
        print(p)
        print('Independent (fail to reject H0)')

chi_square('GF/G')
chi_square('GA/G')
chi_square('SF/G') ### remove this! (p>a)
chi_square('SA/G') ### remove this! (p>a)
chi_square('PCT')
chi_square('PKT') ### remove this! (p>a)
'''

## tree
### feature_cols = ['pclass','gender','age','embarked_Q','embarked_S'] ### 종속변수에 유의하게 영향을 줄 듯한 독립변수들만 따로 모아놓음 
x = data.drop(['name','result'], axis=1) 
x.head()
y = data['result']

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='gini', max_depth=3)
model2 = DecisionTreeClassifier(criterion='entropy', max_depth=3)
model2.fit(x,y)

pd.DataFrame({'feature':x.columns, 'importance':model2.feature_importances_}) ### 모델.feature_importances_: 각 변수의 유의 수준(Gini Index)을 알 수 있음!!!  

###################################################################################

## visualisation (미완성)
import pydotplus
import graphviz
from sklearn.tree import export_graphviz
from IPython.display import Image

## 붓꽃 case 
import pandas as pd
dataset=pd.read_csv("C:/data/iris.csv")
dataset.head()
x=dataset.drop('Name',axis=1)
y=dataset['Name']
x
y ### 목표변수(label)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
x_train
y_test
y_train

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
### classifier=DecisionTreeClassifier(criterion='entropy', max_depth=2) ### entropy 사용 // max_depth: 가지가 너무 많으면 복잡하니까 가지 수 조절! 
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test) ### 학습이 잘 됬는가를 확인하는 것
y_pred

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

classifier.predict([[5.1,3.5,1.4,0.2]])[0] ### Testing Data 

classifier.score(x_train, y_train)
classifier.score(x_test, y_test)

dot_data = export_graphviz(classifier, out_file = None, ### classifier: 모델
                           feature_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'], ### feature_names: 모델 안에 사용한 변수들 표현(리스트 형식)
                           class_names = ['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], ### class_names: 꽃의 종류(category) 적음 
                           filled=True, rounded=True, special_characters=True) ### 그래프의 모양 
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png()) 



import pandas as pd
titanic = pd.read_csv("C:/data/titanic.csv") ### 타이타닉 생존자 분석 
titanic
titanic.columns ### 독립 변수들 중에 필요 없는 것 제외시키고, 문자형은 숫자형으로 바꿔줘야 함(one hot encoding) <- 독립 변수들을 학습시키기 위해서는, 숫자형으로 만들어야 계산 가능!
titanic.head()

## one hot encoding 
titanic['gender'] = titanic.gender.map({'female':0, 'male':1}) ### dictionary를 통해 컬럼 내의 필드값 변경 
titanic.isnull() ### Null값 체크 
titanic.isnull().any() ### 각각의 컬럼을 합산해서 필드값이 Null인 거 체크 -> 변수 내에 NaN이 하나라도 있으면 True 
titanic.isnull().sum() ### 각 변수에 True가 몇 개인 지 합산 
titanic.isnull().sum()['age'] ### age 변수에 해당되는 값만 리턴 
titanic.isnull().sum().sum() ### 데이터 전체의 NaN 개수 계산 <- pandas의 기능! 

titanic[titanic.isnull()['age']] ### age 변수에 NaN이 들어 있는 튜플들만 리턴 -> 버리고 싶으면 dropna() 쓰면 됨! 
titanic['age'].median() ### NaN에 해당되는 튜플들이 많으면 보편적으로 평균이나 중앙값을 집어넣음! 
titanic['age'].fillna(titanic['age'].median(), inplace=True) ### fillna()를 이용해서 NaN에 median값 적용 // inplace=True <- 바로 적용시키는 거! 
titanic.head() ### embarked: 탑승항구 <- C(Cherbourg), Q(Queenstown), S(Southampton) <- 이 세 값들이 각각의, 종속변수에 영향을 줄 수 있는, 독립변수가 되어야 함! => "더미변수"!!! 
set(titanic['embarked']) ### 이 세 개를 각각의 독립변수화 => 이들이 개별적으로 종속변수에 영향 미칠 수 있는지 파악 -> Dummy Variables 

embarked_dummies = pd.get_dummies(titanic['embarked'], prefix='embarked') ### get_dummies(): 자동으로 더미 변수가 만들어짐!!! 
embarked_dummies.drop(embarked_dummies.columns[0], axis=1, inplace=True) ### 변수명.columns[0]: 해당 컬럼 검색 
titanic = pd.concat([titanic, embarked_dummies], axis=1) ### cbind 

titanic.columns
feature_cols = ['pclass','gender','age','embarked_Q','embarked_S'] ### 종속변수에 유의하게 영향을 줄 듯한 독립변수들만 따로 모아놓음 
titanic[feature_cols] ### 해당 컬럼들만 뽑아냄 
x = titanic[feature_cols]
x.head()
y = titanic['survived']

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='gini', max_depth=3)
model2 = DecisionTreeClassifier(criterion='entropy', max_depth=3)
model.fit(x,y)

pd.DataFrame({'feature':feature_cols, 'importance':model.feature_importances_}) ### 모델.feature_importances_: 각 변수의 유의 수준(Gini Index)을 알 수 있음!!! -> gender가 가장 큰 영향 

import pydotplus
import graphviz
from sklearn.tree import export_graphviz
from IPython.display import Image
dot_data = export_graphviz(model, out_file = None, 
                           feature_names = ['pclass', 'gender', 'age', 'embarked_Q', 'embarked_S'], ### feature_names: 모델 안에 사용한 변수들 표현(리스트 형식)
                           class_names = ['1','0'], ### class_names: 꽃의 종류(category) 적음 
                           filled=True, rounded=True, special_characters=True) ### 그래프의 모양 
graph = pydotplus.graph_from_dot_data(dot_data) 
Image(graph.create_png()) 

## 회귀분석 (미완성) 
import statsmodels.api as sm

def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results
reg_m(data['result'], data['GF/G']).summary()

###################################################################################

## Prediction 
data.columns
van = [3.00, 25.0, 8, 19, 3.22, 32.2, 0, 1, 5, 9, 1, 3.24,	17.99,	27.5,	72.9,	199]
pit = [3.71, 30.0, 3, 6, 3.43, 36.0, 0, 3, 1, 6, 0, 3.38,	18.59,	27.7,	72.7,	200]

train = data.drop(['name','result'], axis=1)
label = data['result']

from sklearn.neighbors import KNeighborsClassifier as knn
clf = knn(n_neighbors = 9)
clf.fit(train, label)
clf.predict(np.array([van]))[0]
clf.predict(np.array([pit]))[0]
