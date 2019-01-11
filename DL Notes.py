# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 13:08:45 2019

@author: mypc
"""

# 11/2
# output layer

## 활성화함수
### -회귀(regression) : 항등함수(identify function)
### -분류(classification) : softmax function
### -분류문제에서 출력층의 node수는 분류하고 싶은 클래스 수로 설정하면 된다.
    
## softmax function
### -출력값으로 확률벡터로 나온다.
    
# TensorFlow
 
## 구글이 오픈소스로 공개한 머신러닝(machine learning)라이브러리
## 다차원의 행렬계산(tensor), 대규모 숫자계산 작업을 수행한다.
## 딥러닝을 비롯한 여러 머신러닝에 사용되는 라이브러리
## (딥러닝 : input과 output 사이에 은닉층이 존재하는 것)
## C++로 만들어진 라이브러리
## CPU, GPU 모드로 동작
## Python 지원한다.
  
#################################
# Anaconda Prompt
# pip install --upgrade tensorflow
#################################
  
import tensorflow as tf
tf.__version__
# Python 3.6까지 가능

tensor = tf.constant("tensorflow")  # TensorFlow의 변수
print(tensor)
tensor = "tensorflow"              # Python의 변수

sess = tf.Session()     # .Session() : 세션시작 
                        # 클라이언트 프로그램이 텐서플로 런타임 시스템과 통신하기 위해서는 세션이 생성되어야 한다.   
sess.run(tensor)
sess.close()

sess.run(tensor) # 닫힌 세션 => 실행 안 됨! 

a = tf.constant(1234)
b = tf.constant(5678)

add_op = a+b
add_op

# tf.Session() => sess.fun() => sess.close()
sess = tf.Session()
sess.run(add_op)
sess.run([a,b,add_op]) # 리스트 형태로 표현 
sess.close()

a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

x1 = a+b*c
x2 = (a+b)*c

sess = tf.Session()
z1 = sess.run(x1) # 연산 결과를 변수에 저장 => 세션이 닫혀도 꺼내 쓸 수 있음! 
z2 = sess.run(x2)
sess.close()

a = tf.constant(120, name="a")  # 상수
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")
v = tf.Variable(0, name="v")    # 변수
v
x1= a+b+c
assign_op = tf.assign(v,x1) # tf.assign(<변수>,<할당값>) : 변수에 값을 할당한다.
v   # 같은 텐서를 참조한다. <- <tf.Variable 'v_4:0' shape=() dtype=int32_ref>

sess = tf.Session()
sess.run(assign_op)
sess.run(v) # 변수에 값 할당 됐음! 
sess.run(x1)
sess.close()

a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")
v = tf.Variable(0, name="v")
v
x1= a+b+c
v = x1
v   # Variable이 아닌 Tensor! <- <tf.Tensor 'add_12:0' shape=() dtype=int32>

sess = tf.Session()
sess.run(v) # =390
sess.run(x1)
sess.close()

x = tf.Variable([[1,2,3],[4,5,6]])
y = tf.Variable([[1,2],[3,4],[5,6]])
z = tf.Variable(0)
z = tf.matmul(x,y)  # tf.matmul(,) : 행렬의 곱

sess = tf.Session()
sess.run(z) # FailedPreconditionError
# 상수는 그 즉시 메모리를 할당한다.
# 변수는 초기화를 시켜주지 않으면 안된다.
sess.run(tf.global_variables_initializer()) # tf.global_variables_initializer() : 변수를 초기화한다.
sess.run(z)
sess.close()

p1 = tf.placeholder("int32")    # placeholder는 초기화시키지 않아도 된다.
p2 = tf.placeholder("int32")
y = tf.add(p1,p2)

sess = tf.Session()
sess.run(y, feed_dict={p1:10,p2:20}) # 두 변수(p1,p2)에 각각의 값을 할당! 
sess.close()

# 함수             설명
#--------------------------------------
# tf.add         덧셈
# tf.subtract    뺄셈
# tf.multiply    곱셈
# tf.div         나눗셈의 몫, 소숫점
# tf.truediv     나눗셈의 몫, 소숫점
# tf.mod         나눗셈의 나머지
# tf.abs         절대값
# tf.negative    음수
# tf.sign        부호(음수 -1, 양수 1, 0)
# tf.reciprocal  역수(3은 1/3)
# tf.square      제곱
# tf.round       반올림
# tf.sqrt        제곱근
# tf.pow         거듭제곱
# tf.exp         지수갑
# tf.log         로그값
# tf.maximum     최대값
# tf.minimum     최소값
# tf.cos         코사인
# tf.sin         사인

x = tf.Variable(0)
y = tf.assign(x,1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(x))  # =0
    print(sess.run(y))  # =1
    print(sess.run(x))  # =1 <- y가 실행된 이후의 결과! 

# 텐서 자료 구조

## 텐서는 텐서플로의 기본 자료 구조
## 텐서는 다차원배열, 리스트로 저장
## 텐서는 학습데이터가 저장되는 다차원배열
  
## 1차원 텐서(tensor)
import numpy as np
import tensorflow as tf

arr_1 = np.array([1.5,1,5.0,10])
arr_1
arr_1[0]
arr_1.ndim
arr_1.shape
arr_1.dtype

arr_tf = tf.convert_to_tensor(arr_1,dtype=tf.float64) # numpy 배열을 tensor로 변환! 
with tf.Session() as sess:
    print(sess.run(arr_tf))
    print(sess.run(arr_tf[0]))

arr_tf.shape # arr_1.shape
arr_tf.dtype # arr_1.dtype

arr_tf.ndim # AttributeError <- shape, dtype은 numpy에서랑 똑같이 쓸 수 있는데 ndim은 못쓴다.

## 2차원 텐서
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2 = np.array([[1,1,1],[2,2,2],[3,3,3]])
type(arr_1)
type(arr_2)

tm1 = tf.constant(arr_1) # 이런 식으로도 tensor로 변환할 수 있음! 
tm2 = tf.constant(arr_2)

tm_product = tf.matmul(tm1,tm2)
tm_add = tf.add(tm1,tm2)
with tf.Session() as sess:
    print(sess.run(tm_product)) # 행렬곱 시행 
    print(sess.run(tm_add))

## 3차원 텐서
arr_3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr_3.ndim
arr_3.shape     # (plane,row,column)

tm_3 = tf.constant(arr_3)
with tf.Session() as sess:
    print(sess.run(tm_3))
    
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = tf.matmul(x,y)
with tf.Session() as sess:
    print(sess.run(z,feed_dict={x:[[3.,3.],[3.,3.]],y:[[5.,5.],[5.,5.]]})) # x와 y에 각각의 값을 할당! 

x = tf.placeholder(tf.float32,shape=(2,2)) # shape를 미리 지정! 
y = tf.placeholder(tf.float32,shape=(2,2))
z = tf.matmul(x,y)
with tf.Session() as sess:
    print(sess.run(z,feed_dict={x:[[3.,3.],[3.,3.]],y:[[5.,5.],[5.,5.]]}))



x = tf.constant([[1.0,2.0,3.0]])
print(x.get_shape()) # 1x3
w = tf.constant([[2.0],[2.0],[2.0]])
print(w.get_shape()) # 3x1
y = tf.matmul(x,w)

sess = tf.Session()
print(sess.run(x))
print(sess.run(w))
print(sess.run(y)) # 행렬곱 시행(scalar(1x1) 값!)

# Variable을 이용
x = tf.Variable([[1.0,2.0,3.0]])
w = tf.Variable([[2.0],[2.0],[2.0]])
y = tf.matmul(x,w)
init_op = tf.global_variables_initializer() 
with tf.Session() as sess:
    sess.run(init_op) # Variable은 항상 초기화해야!  
    print(sess.run(y))





# 11/5
# Feed Forward(순전파)
'''

   입력 -> 출력
         |
        bias
    y = w * x + b
  
   예제1
    w = 2 b = 1
    x   y 
    -----
    0   1
    1   3
    2   5
    
   예제2
    목표 : 입력 1 -> 출력 4
    y = w * 1 + b = 4
    
    1.weight값을 수정하면서 찾는다.
    b = 1
    w   y
    -------
    1   2
    2   3
    2.5 3.5
    3   4
    => y = 3 * 1 + 1 = 4
    
    2.bias값을 수정하면서 찾는다.
    w = 2
    b   y
    -------
    1   2 * 1 + 1 = 3
    1.5 2 * 1 + 1.5 = 3.5
    2   2 * 1 + 2 = 4
    => y = 2 * 1 + 1 = 4

  ㅇf = wx + b
    g = wx
    f = g + b
    
    g = wx
    ∂g/∂w = x
    ∂g/∂x = w
    
    f = g + b
    ∂f/∂g = 1
    ∂f/∂b = 1

    ∂f/∂w = ∂f/∂g * ∂g/∂w = ∂g/∂w (by Chain Rule)
    ∂f/∂x = ∂f/∂g * ∂g/∂x
'''
# Backpropagation(역전파)

## gradient descentdent method(경사하강법)
### ∂E/∂w (E : 오차)
### w수정 = w - α * ∂E/∂w (α : Learning Rate)

## cost function
### - 신경망 학습에서 학습데이터에 대한 오차를 측정하는 척도
    
## 평균제곱오차(mean squared error, MSE) <- 예측치(yhat)와 실제값(y)의 차이 
### - 오차 = 1/2 * ∑(ytarget - y)²

import numpy as np
t = np.array([0,0,0,0,1,0,0,0,0,0])
y = np.array([0.1,0.03,0.05,0.2,0.9,0.0,0.1,0.2,0.12,0.03])

sum((t-y)**2)/2 # MSE

def mse(t,y):
    return 0.5*np.sum((t-y)**2)

print("오차는",mse(t,y))

## Linear Regression
'''  
    -예제
     입력(x) 출력(y)
     ----------------
     1       2
     2       4
     3       6
     4       8
     5       10
     6       12
     7을 입력하면 출력값은?
     y = w * x + b
     w = 2, b = 0
     14
    
    (퍼셉트론은 weight(w),bias(b)를 정해줘야했는데 신경망은 w와 b를 자동으로 맞춰준다!!!)
'''

import tensorflow as tf
x_data = [1,2,3,4,5,6]    
y_data = [2,4,6,8,10,12]

# inputs, outputs <- tf.placeholder()
# weights, bias <- tf.Variable()
# costs(MSE) <- tf.reduce_mean()
# 경사하강법 <- tf.train.GradientDescentOptimizer(learning_rate) <- ~.minimize(cost)
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

## w,b 난수설정
w = tf.Variable(tf.random_normal([1],seed=0),name="weight")
b = tf.Variable(tf.random_normal([1],seed=0),name="bias")

hypothesis = w*x+b

cost = tf.reduce_mean(tf.square(hypothesis - y))    # MSE = 1/n
## ∑(ytarget - y)²
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)  # 미분(경사하강도를 통해 최소오차 추적)
train = optimizer.minimize(cost) # 학습

## 세션 
sess = tf.Session()
sess.run(tf.global_variables_initializer()) # 변수 초기화 

for step in range(2001):
    cost_v,w_v,b_v,_ = sess.run([cost,w,b,train],feed_dict={x:x_data,y:y_data})
    if step % 20 == 0:
        print(step,cost_v,w_v,b_v)
        
print(sess.run(hypothesis,feed_dict={x:7})) # yhat 

# 평균제곱근오차(root mean squared error, RMSE)를 이용
'''  
    -예제
     기울기 = 4.3, 절편 = 64
     공부시간    점수
     ----------------
     2           71
     4           83
     6           91
     8           97
'''
ab = [4.3,64] # [slope,y-intercept]
data = [[2,71],[4,83],[6,91],[8,97]] # [x,y]

x = [i[0] for i in data]
y = [i[1] for i in data]

def predict(x):
    return ab[0] * x + ab[1] # yhat 

predict(2)

# RMSE(Root Mean Squared Error) : 평균제곱근오차
def rmse(p,a):
    return np.sqrt(((p-a)**2).mean())

def rmse_val(predict_result,y):
    return rmse(np.array(predict_result), np.array(y)) # yhat과 y의 RMSE 계산 

predict_result = []
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부시간(x) : %.f, 실제점수(y) : %.f, 예측점수(yhat) : %.f" %(x[i],y[i],predict(x[i])))
    
print("오차 : ", rmse_val(predict_result,y)) # RMSE 

# 선형회귀(Linear Regression)
## -임의의 직선을 그어 이에 대한 평균제곱근오차(RMSE)를 구하고 이값을 "가장 작게" 만들어 주는 기울기와 절편을 찾아가는 과정

## RMSE
data = [[2,71],[4,83],[6,91],[8,97]]
np.shape(data)

x_data = [ i[0] for i in data]
y_data = [ i[1] for i in data]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1], seed=0),name="weight")
b = tf.Variable(tf.random_normal([1], seed=0),name="bais")

hypothesis = w*x +b
rmse = tf.sqrt(tf.reduce_mean(tf.square(hypothesis-y))) # cf. MSE <- tf.reduce_mean(tf.square(hypothesis - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)    # leanring_rate 잘못조절하면 결과가 안나올수도 있다.
train = optimizer.minimize(rmse)

## 세션 
sess = tf.Session()
sess.run(tf.global_variables_initializer()) # 초기화 
for step in range(2001):
    rmse_val,w_val,b_val,_ = sess.run([rmse,w,b,train],feed_dict={x:x_data,y:y_data})
    if step % 1000 == 0:
        print(step, rmse_val, w_val, b_val)

print(sess.run(hypothesis, feed_dict={x:7}))

# MSE
x_data = [2,4,6,8]    
y_data = [71,83,91,97]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1],seed=0),name="weight")
b = tf.Variable(tf.random_normal([1],seed=0),name="bias")

hypothesis = w*x+b

cost = tf.reduce_mean(tf.square(hypothesis - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer()) # 초기화 
for step in range(2001):
    cost_v,w_v,b_v,_ = sess.run([cost,w,b,train],feed_dict=
{x:x_data,y:y_data})
    if step % 20 == 0:
        print(step,cost_v,w_v,b_v)
        
print(sess.run(hypothesis,feed_dict={x:7}))

'''
[문제]linear regression 학습을 통해서 입력값에 대한 예측값을 출
력하세요.
    x1  x2  x3  y
    ---------------
    73  80  75  152
    93  88  93  185
    89  91  90  180
    96  98  100  196
    73  66  70  142
'''
# 답1       
data = [[73,80,75,152],[93,88,93,185],[89,91,90,180],[96,98,100,196],[73,66,70,142]]

x1_data = [i[0] for i in data]
x2_data = [i[1] for i in data]
x3_data = [i[2] for i in data]
y_data = [i[3] for i in data]

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w1 = tf.Variable(tf.random_normal([1], seed=0),name="weight1")
w2 = tf.Variable(tf.random_normal([1], seed=0),name="weight2")
w3 = tf.Variable(tf.random_normal([1], seed=0),name="weight3")
b = tf.Variable(tf.random_normal([1], seed=0),name="bais")

hypothesis = w1*x1 + w2*x2 + w3*x3 +b # 3개의 독립변수 
cost = tf.reduce_mean(tf.square(hypothesis-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)   # NaN으로 나오면 학습률을 줄여줘야
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val,w1_val,w2_val,w3_val,b_val,_ = sess.run([cost,w1,w2,w3,b,train],feed_dict={x1:x1_data,x2:x2_data,x3:x3_data,y:y_data})
    if step % 10000 == 0:
        print(step, cost_val, w1_val, w2_val, w3_val, b_val)
        
print("당신의 점수는",sess.run(hypothesis,feed_dict={x1:100,x2:70,x3:60}))

# 답2:
## 행렬의 곱으로 풀이1 개선
x_data = [[73,80,75],[93,88,93],[89,91,90],[96,98,100],[73,66,70]]
y_data = [[152],[185],[180],[196],[142]]

x = tf.placeholder(tf.float32,shape=[None,3])   # n행3열
y = tf.placeholder(tf.float32,shape=[None,1])   # n행1열
w = tf.Variable(tf.random_normal([3,1],seed=0),name='weight')  
 # [3,1] : 3은 x의 열값이 들어오는 값, 1은 y로 나가는 값 
b = tf.Variable(tf.random_normal([1], seed=0),name="bais")     
 # [1] : 1은 y로 나가는 값

hypothesis = tf.matmul(x,w) + b
cost = tf.reduce_mean(tf.square(hypothesis-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)   # NaN으로 나오면 학습률을 줄여줘야
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val,w_val,b_val,_ = sess.run([cost,w,b,train],feed_dict={x:x_data,y:y_data})
    if step % 10000 == 0:
        print(step, cost_val, w_val, b_val)
        
print("당신의 점수는",sess.run(hypothesis,feed_dict={x:[[100,70,60]]}))

# ex.csv파일을 불러오는 방법
import tensorflow as tf
import numpy as np
xy = np.loadtxt("c:/data/ex.csv",delimiter=",",dtype=np.float32)

x_data = xy[:,0:-1]
y_data = xy[:,[-1]]
x_data.shape
y_data.shape # 5행1열
# y_data = xy[:,-1] : 1행 5열
x = tf.placeholder(tf.float32,shape=[None,3])
y = tf.placeholder(tf.float32,shape=[None,1])
w = tf.Variable(tf.random_normal([3,1],seed=0),name='weight')
b = tf.Variable(tf.random_normal([1], seed=0),name="bais")

hypothesis = tf.matmul(x,w) + b
cost = tf.reduce_mean(tf.square(hypothesis-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val,hy_val,_ = sess.run([cost,hypothesis,train],feed_dict={x:x_data,y:y_data})
    if step % 10000 == 0:
        print(step, cost_val, hy_val)
        
print("당신의 점수는",sess.run(hypothesis,feed_dict={x:[[100,70,60]]}))


    
    

# 11/6

# binary classification
import tensorflow as tf
x_data=[[1,2],[2,3],[3,1],[4,3],[5,3],[6,2]] # 공부시간,게임시간
y_data= [[0],[0],[0],[1],[1],[1]] # 합격여부(분류값/1이 합격)

x = tf.placeholder(tf.float32,shape=[None,2]) # 입력변수
y = tf.placeholder(tf.float32,shape=[None,1])

w = tf.Variable(tf.random_normal([2,1]),name='weight') # weight값
b = tf.Variable(tf.random_normal([1]),name='bias') # bias값

hypothesis = tf.matmul(x,w) + b

# cost function
# y = 1  이면   -y * log(h(x))
# y = 0  이면   -(1-y) * log(1-h(x))
cost = -tf.reduce_mean(y* tf.log(hypothesis) + (1-y) * tf.log(1-hypothesis))

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)
"""
if hypothesis > 0.5 then:
    True(1.0)
else:
    False(0.0)
"""
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict,y),dtype=tf.float32))
accuracy

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        cost_val,_=sess.run([cost,train],feed_dict={x:x_data,y:y_data})
        if step % 200 == 0:
            print(step,cost_val)
        h,c,a=sess.run([hypothesis,predict,accuracy],feed_dict={x:x_data,y:y_data})
        print("\nhypothesis : ",h)


# [문제] xor을 logistic regression classifier를 이용해서 프로그램을 생성하세요.

x1        x2        y
---------------------
0         0         0
0         1         1
1         0         1
1         1         0

import tensorflow as tf
import numpy as np
x_data=[[0,0],[0,1],[1,0],[1,1]]
y_data= [[0],[1],[1],[0]]
x_data=np.array(x_data,dtype=np.float32)
y_data=np.array(y_data,dtype=np.float32)
x = tf.placeholder(tf.float32,[None,2])
y = tf.placeholder(tf.float32,[None,1])

# input layer
w1=tf.Variable(tf.random_normal([2,5],seed=0),name='weight1')
b1=tf.Variable(tf.random_normal([5]),name='bias1')
layer1 = tf.sigmoid(tf.matmul(x,w1)+b1)
# 중요! xor을 logistic regression classifier를 이용해서 프로그램을 생성하기 위해서는 히든층이 총 3개 필요함
# hidden layer2
w2=tf.Variable(tf.random_normal([5,4],seed=0),name='weight2')
b2=tf.Variable(tf.random_normal([4]),name='bias2')
layer2= tf. sigmoid(tf.matmul(layer1,w2)+b2)

# hidden layer3
w3=tf.Variable(tf.random_normal([4,4],seed=0),name='weight3')
b3=tf.Variable(tf.random_normal([4]),name='bias3')
layer3= tf. sigmoid(tf.matmul(layer2,w3)+b3)

# output layer
w4=tf.Variable(tf.random_normal([4,1],seed=0),name='weight4')
b4=tf.Variable(tf.random_normal([1]),name='bias4')

hypothesis = tf.sigmoid(tf.matmul(layer3,w4)+b4)
cost = -tf.reduce_mean(y*tf.log(hypothesis)+(1-y)*tf.log(1-hypothesis)) # corss entyopy cost function
train = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(10001):
    sess.run(train,feed_dict={x:x_data,y:y_data})
    if step % 1000 ==0:
        print(step,sess.run(cost,feed_dict={x:x_data,y:y_data}),sess.run([w1,w2]))
        h = sess.run(hypothesis,feed_dict={x:x_data,y:y_data})
        print(h)

a= sess.run(hypothesis,feed_dict={x:[[0,0],[0,1],[1,0],[1,1]]})
print(sess.run(tf.cast(a>0.5,dtype=tf.int32)))

# multi classification(softmax clssifier)
xy=np.loadtxt("c:/data/11.06trainset.txt",delimiter=",",dtype=np.float32)
x_data=xy[:,0:-1]
y_data=xy[:,[-1]]

x=tf.placeholder(tf.float32,[None,3])
y=tf.placeholder(tf.int32,[None,1]) # one hot encoding은 0아니면 1이므로 int로 형을 해줘야함

y_one_hot=tf.one_hot(y,3)
y_one_hot=tf.reshape(y_one_hot,[-1,3])
y_one_hot

w=tf.Variable(tf.random_normal([3,3]),name='weight')
b=tf.Variable(tf.random_normal([3]),name='bias')
logits=tf.matmul(x,w)+b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_one_hot))
cost
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)
prediction = tf.argmax(hypothesis,1) # 숫자 1은 데이터가 1차원배열이기 때문에 1로 한 것 기본값은 0임
correct_prediction = tf.equal(prediction,tf.argmax(y_one_hot,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
accuracy
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(train,feed_dict={x:x_data,y:y_data})
    if step % 100 == 0:
        loss,acc = sess.run([cost,accuracy],feed_dict={x:x_data,y:y_data})
        print("Step: ",step,"Loss: ",loss,"Accuracy: ",acc)
a = sess.run(hypothesis,feed_dict={x:[[1,2,1]]})
print(sess.run(tf.argmax(a,1)))

b = sess.run(hypothesis,feed_dict={x:[[1,7,7]]})
print(sess.run(tf.argmax(b,1)))

c = sess.run(hypothesis,feed_dict={x:[[1,4,5]]})
print(sess.run(tf.argmax(c,1)))

'''
a1 = tf.Variable([0.1,0,3,0.5])
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(tf.argmax(a1)))#가장 큰값의 index번호를 리턴해줌
print(sess.run(tf.argmin(a1)))#가장 작은값의 index번호를 리턴해줌
sess.close()
'''





# 11/7

# [문제] zoo data set을 이용해서 분류프로그램을 만드세요.
import tensorflow as tf
import numpy as np
zoo=np.loadtxt("c:/data/zoo.txt",delimiter=',',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17),dtype=np.float32,encoding='utf-8',skiprows=20)
x_data=zoo[:,0:-1]
y_data=zoo[:,[-1]]
y_data=y_data-1
y_data
# 1 : 포유류, 2 : 조류, 3 : 파충류, 4 : 어류, 5 : 양서류, 6 : 곤충/거미류, 7 : 무척추동물
# 0 : 포유류, 1 : 조류, 2 : 파충류, 3 : 어류, 4 : 양서류, 5 : 곤충/거미류, 6 : 무척추동물
print(x_data.shape,y_data.shape)
x=tf.placeholder(tf.float32,[None,16])
y=tf.placeholder(tf.int32,[None,1])

y_one_hot = tf.one_hot(y,7)
y_one_hot = tf.reshape(y_one_hot,[-1,7])

w = tf.Variable(tf.random_normal([16,7],seed=0),name="weight")
b = tf.Variable(tf.random_normal([7],seed=0),name="bias")

logits = tf.matmul(x,w)+b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_one_hot))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)

prediction = tf.argmax(hypothesis,1)
correct_prediction = tf.equal(prediction,tf.argmax(y_one_hot,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

sess=tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(optimizer,feed_dict={x:x_data,y:y_data})
    if step % 100 ==0:
        loss, acc = sess.run([cost,accuracy],feed_dict={x:x_data,y:y_data})
        print("Step : {:5}\tLoss:{:.3f}\tAcc:{:,.2%}".format(step,loss,acc))
        
pred = sess.run(prediction,feed_dict={x:x_data})
for p,y in zip(pred,y_data.flatten()):
    print("[{}] prediction : {} True Y:{}".format(p==int(y),p,int(y)))
    
worm,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,7
wren,0,1,1,0,1,0,0,0,1,1,0,0,2,1,0,0,2


zoo_hypothesis = sess.run(hypothesis,feed_dict={x:[[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]]})
print(zoo_hypothesis,sess.run(tf.argmax(zoo_hypothesis,1)))
zoo_hypothesis = sess.run(hypothesis,feed_dict={x:[[0,1,1,0,1,0,0,0,1,1,0,0,2,1,0,0]]})
print(zoo_hypothesis,sess.run(tf.argmax(zoo_hypothesis,1)))
#-----------------------------여기까지가 문제-------------------------------------------
a = np.arange(12)
a
b = a.reshape(3,4)
b = a.reshape(3,-1)
b

a.reshape(2,2,-1)
a.flatten()

# [문제206] bmi.csv 내용을 신경망을 이용해서 분류해 보세요.

# BMI
# BMI = 몸무게 / (키(m)*키(m))
# 18.5 이상 25미만이면 표준
# label : thin(저체중), normal(정상), fat(비만)
import tensorflow as tf
import numpy as np
bmi = pd.read_csv('c:/data/bmi.csv',delimiter=',')
bmi = np.array(bmi)

x_data = bmi[:,0:-1]
y_data = bmi[:,[-1]]
x0_mean = np.mean(x_data[:,[0]]); x0_std = np.std(x_data[:,[0]])
x1_mean = np.mean(x_data[:,[1]]); x1_std = np.std(x_data[:,[1]])
x_data[:,[0]] = (x_data[:,[0]] - x0_mean) / x0_std
x_data[:,[1]] = (x_data[:,[1]] - x1_mean) / x1_std

y_data[y_data=='thin'] = 0
y_data[y_data=='normal'] = 1
y_data[y_data=='fat'] = 2
# 0: thin, 1: normal, 2:fat 으로 변환
print(x_data.shape,y_data.shape)

nb_classes = 3

x = tf.placeholder(tf.float32,[None,2])
y = tf.placeholder(tf.int32,[None,1])

y_one_hot = tf.one_hot(y,nb_classes)
y_one_hot = tf.reshape(y_one_hot,[-1,nb_classes])

w = tf.Variable(tf.random_normal([2,nb_classes],seed=0),name="weight")
b = tf.Variable(tf.random_normal([nb_classes],seed=0),name="bias")
logits = tf.matmul(x,w) +b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_one_hot))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.2).minimize(cost)

prediction = tf.argmax(hypothesis,1)    
correct_prediction = tf.equal(prediction,tf.argmax(y_one_hot,1))    
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))    

sess = tf.Session()    
sess.run(tf.global_variables_initializer())    
for step in range(20001):
    sess.run(optimizer,feed_dict={x:x_data,y:y_data})
    if step % 100 == 0:
        loss,acc = sess.run([cost,accuracy],feed_dict={x:x_data,y:y_data})
        print("Step : {:5}\tLoss : {:.3f}\tAcc : {:.2%}".format(step,loss,acc))

pred = sess.run(prediction, feed_dict={x:x_data})
for p,y in zip(pred,y_data.flatten()):
    print("[{}] Prediction : {} True Y : {}".format(p==int(y),p,int(y)))

mbi_hypothesis = sess.run(hypothesis, feed_dict={x:[[(145-x0_mean)/x0_std,(60-x1_mean)/x1_std]]})
print(mbi_hypothesis, sess.run(tf.argmax(mbi_hypothesis,1)))


    


# 11/8

# https://www.tensorflow.org/tutorials/images/deep_cnn?hl=ko #tensorflow cnn에 대한 설명 링크
# https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/g3doc/tutorials/mnist/beginners/ #tensorflow mnist설명

# 합성곱:convolution
## 곱을 하다보니 이미지가 진해짐
## 필터크기를 기준으로 옮겨가면서 하나의 활성곱을 만드는 것


# CNN(Convolution Neural Network ,합성곱 신경망)
## -convolution층과 pooling층을  포함하는 신경망

# 기존신경망과 CNN의 차이
## -기존방법 : affine -> Relu
## -CNN : Conv -> Relu -> Pooling 

# 합성곱 계층
## -feature map을 만들고 그 feature map을 선명하게 해주는 층
# 합성곱 연산
## -이미지 3차원(세로, 가로, 색상) data의 형상을 유지하면서 연산하는 작업
'''
1 2 3 0       2 0 1     15 16
0 1 2 3   Θ   0 1 2     6  15
3 0 1 2       1 0 2
2 3 0 1       

입력         필터        feature map
(4,4)       (3,3)       (2,2)

(입력 - 필터) / stride + 1 = feature map
(stride : 지정된 간격으로 필터를 순회하는 간격)
(4-3)/1+1 = 2
'''
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
sess = tf.InteractiveSession() # 대화형
image = np.array([[[1],[2],[3]],
                  [[4],[5],[6]],
                  [[7],[8],[9]]],dtype=np.float32)
print(image.shape) # (3, 3, 1)
image = np.array([[[[1],[2],[3]],
                  [[4],[5],[6]],
                  [[7],[8],[9]]]],dtype=np.float32)
print(image.shape) # (1, 3, 3, 1) : (이미지 n개,행(높이),열(너비),색)
plt.imshow(image.reshape(3,3),cmap="Greys")

weight = tf.constant([[[[1.]],[[1.]]],
                      [[[1.]],[[1.]]]])
print(weight.shape) # (2, 2, 1, 1) : (행,열,색,필터수)

conv2d=tf.nn.conv2d(image,weight,strides=[1,1,1,1],padding="VALID") # tf.nn.conv2d(이미지데이터,weight값,)합성곱 매소드
conv2d_img=conv2d.eval()
conv2d_img
print(conv2d_img.shape) # (1, 2, 2, 1)

conv2d_img=np.swapaxes(conv2d_img,0,3)
conv2d_img.shape
for i, one_img in enumerate(conv2d_img):
    print(one_img.reshape(2,2))
    plt.subplot(1,2,i+1),plt.imshow(one_img.reshape(2,2),cmap="Greys")
conv2d=tf.nn.conv2d(image,weight,strides=[1,1,1,1],padding="SAME") # tf.nn.conv2d(이미지데이터,weight값,)합성곱 매소드
conv2d_img=conv2d.eval()
conv2d_img
print(conv2d_img.shape) # (1, 2, 2, 1)

conv2d_img=np.swapaxes(conv2d_img,0,3)
conv2d_img.shape
for i, one_img in enumerate(conv2d_img):
    print(one_img.reshape(3,3))
    plt.subplot(1,2,i+1),plt.imshow(one_img.reshape(3,3),cmap="Greys")
a=np.arange(15).reshape(3,5)
a.T
np.transpose(a)
np.swapaxes(a,0,1) # 축을 바꾸는 것
'''
array([[ 0,  5, 10],
       [ 1,  6, 11],
       [ 2,  7, 12],
       [ 3,  8, 13],
       [ 4,  9, 14]])
'''
np.dot(a.T,a) # np.dot은 numpy안에 있는 행렬곱을 하는 매소드
np.dot(np.transpose(a),a)
np.dot(np.swapaxes(a,0,1),a)

b=np.arange(24).reshape(2,3,4)
b.shape # (2, 3, 4)
b.T
'''
array([[[ 0, 12],
        [ 4, 16],
        [ 8, 20]],

       [[ 1, 13],
        [ 5, 17],
        [ 9, 21]],

       [[ 2, 14],
        [ 6, 18],
        [10, 22]],

       [[ 3, 15],
        [ 7, 19],
        [11, 23]]])
'''
b.T.shape # (4, 3, 2)
np.transpose(b)
"""
array([[[ 0, 12],
        [ 4, 16],
        [ 8, 20]],

       [[ 1, 13],
        [ 5, 17],
        [ 9, 21]],

       [[ 2, 14],
        [ 6, 18],
        [10, 22]],

       [[ 3, 15],
        [ 7, 19],
        [11, 23]]])
"""
np.swapaxes(b,0,2)
"""
array([[[ 0, 12],
        [ 4, 16],
        [ 8, 20]],

       [[ 1, 13],
        [ 5, 17],
        [ 9, 21]],

       [[ 2, 14],
        [ 6, 18],
        [10, 22]],

       [[ 3, 15],
        [ 7, 19],
        [11, 23]]])
"""
# Relu와 sigmoid가 무엇인가

image=np.array([[[[4],[3]],
                 [[2],[1]]]],dtype=np.float32)
pool = tf.nn.max_pool(image,ksize=[1,2,2,1],strides=[1,1,1,1],padding="VALID") # 특징되는 것을 subset하는작업이 필요한데 이때 큰값을 이용해야하므로 max_pool하는 것
-------------------
# 공유폴더에 올려주심
import tensorflow as tf
import random
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(777)  # reproducibility

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# more information about the mnist dataset
# img = mnist.train.images[0].reshape(28,28)
# plt.imshow(img,cmap="gray")
# hyper parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

# input place holders
X = tf.placeholder(tf.float32, [None, 784])
X_img = tf.reshape(X, [-1, 28, 28, 1])   # img 28x28x1 (black/white) 세로(높이)x가로(너비)
Y = tf.placeholder(tf.float32, [None, 10])

# L1 ImgIn shape=(?, 28, 28, 1) (n개 , 28,28, 색은1)
W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01)) #필터크기(3,3,색, 필터수)

#    Conv     -> (?, 28, 28, 32)
#    Pool     -> (?, 14, 14, 32)
L1 = tf.nn.conv2d(X_img, W1, strides=[1, 1, 1, 1], padding='SAME')
L1 = tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')
'''
Tensor("Conv2D:0", shape=(?, 28, 28, 32), dtype=float32)
Tensor("Relu:0", shape=(?, 28, 28, 32), dtype=float32)
Tensor("MaxPool:0", shape=(?, 14, 14, 32), dtype=float32)
'''

# L2 ImgIn shape=(?, 14, 14, 32)
W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01)) # 3,3,32,64(필터수,이미지수)
#    Conv      ->(?, 14, 14, 64)
#    Pool      ->(?, 7, 7, 64)
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')
L2_flat = tf.reshape(L2, [-1, 7 * 7 * 64])
'''
Tensor("Conv2D_1:0", shape=(?, 14, 14, 64), dtype=float32)
Tensor("Relu_1:0", shape=(?, 14, 14, 64), dtype=float32)
Tensor("MaxPool_1:0", shape=(?, 7, 7, 64), dtype=float32)
Tensor("Reshape_1:0", shape=(?, 3136), dtype=float32)
'''
# fully connected layer
# Final FC 7x7x64 inputs -> 10 outputs
W3 = tf.get_variable("W3", shape=[7 * 7 * 64, 10], initializer=tf.contrib.layers.xavier_initializer())
b = tf.Variable(tf.random_normal([10]))
logits = tf.matmul(L2_flat, W3) + b

# define cost/loss & optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# initialize
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# train my model
print('Learning started. It takes sometime.')
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        feed_dict = {X: batch_xs, Y: batch_ys}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning Finished!')

# Test model and check accuracy
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy:', sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))

# Get one and predict
r = random.randint(0, mnist.test.num_examples - 1)
print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
print("Prediction: ", sess.run(tf.argmax(logits, 1), feed_dict={X: mnist.test.images[r:r + 1]}))

plt.imshow(mnist.test.images[r:r + 1].reshape(28, 28), cmap='Greys', interpolation='nearest')
plt.show()

# [문제]0부터 143까지의 원소로 이루어진 12 x 12 행렬을 만들고 4 x 4 필터(단위행렬)를 이용해서 합성곱을 수행하세요. 단 스트라이드는 1입니다.
# 답1
image=np.arange(0,144).reshape(12,12)
filter=np.eye(4,4)

result = []
for i in range(len(image)-3):
    for k in range(len(image)-3):
        result.append(np.sum(image[i:i+4,k:k+4]*filter))
result = np.array(result).reshape(9,9)
print(result)

# --문제의 답은 여기까지
# 패딩(padding) : 합성곱 연산을 수행하기 전에 입력 데이터 주변을 특정값으로 채워 늘리는 것을 말한다.
## 이유?
### 패딩을 하지 않을 경우 데이터의 공간 크기는 합성곱 계층을 지날때마다 작아지게 되므로 가장 자리 정보들이 사라지게 되는 문제가 발생하기 때문에 패딩을 사용한다.

a=np.arange(16).reshape(4,4)
a_pad=np.pad(a,pad_width=1,mode="constant",constant_values=0)
a_pad
[(top,bottom),(left,right)]

np.pad(a,pad_width=[(1,1),(1,1)],mode="constant",constant_values=0)#pad_width=[(top,bottom),(left,right)]
np.pad(a,pad_width=[(0,1),(0,1)],mode="constant",constant_values=0)

# [문제] 0부터 15까지 원소로 이루어진 4 x 4 행렬을 만들고 0부터 8까지의 원소로 이루어진 3 x 3 필터를 이용해서 합성곱하는데,
# 제로패딩을 출력결과를 4 x 4 로 출력하세요.(단 스트라이드는 1로 수행)
a = np.arange(16).reshape(4,4)
a_pad = np.pad(a,pad_width=1,mode='constant',constant_values=0)
filter = np.arange(9).reshape(3,3)

result = []
for r in range(len(a_pad)-2):
    for c in range(len(a_pad)-2):
        result.append(np.sum(a_pad[r:r+3,c:c+3]*filter))

result = np.array(result).reshape(4,4)
print(result)
# -----------------------

## 입력(H,W), 필터크기(FH,FW), 출력크기(OH,OW)
## 스트라이드 : S, 패딩 : P
'''
          H + 2P -FH
OH = -------------------------- + 1
               S
       (OH-1) * S - H +FH
P = ---------------------------
               2
((4-1)*1 -4+3)/2 = 1
'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=Image.open("c:\\data\\b2b.jpg")
plt.imshow(img)
img_pixel = np.array(img) # 이미지의 픽셀값을 뽑아내는 방법
img_pixel

def rgb_gray(image):
    r, g, b = image[:,:,0],  image[:,:,1], image[:,:,2] # 픽셀에서 빨강, 초록, 파랑색 값만 뽑아내는 것
    gray = 0.2989*r + 0.5870*g + 0.1140*b
    return gray

plt.imshow(rgb_gray(img_pixel),cmap='gray') 
img_pixel_gray = rgb_gray(img_pixel)
plt.imsave("c:\\data\\b2b_gray.jpg",img_pixel_gray) # 이미지 저장하는 것, 실제 픽셀작업한거와 저장본은 달라짐

def convolusion(image,filter,stride,bias):
    col = int((len(image[0])-len(filter[0]))/stride+1)
    row = int((len(image)-len(filter))/stride+1)
    filter_col = len(filter[0])
    filter_row = len(filter)
    convolusion_list=[]
    for i in range(row):
        for j in range(col):
            convolusion_list.append(np.sum(image[i:i + filter_row,j:j+filter_col]*filter))
    return np.array(convolusion_list).reshape(row,col)
filter = np.array([[[255,255,255],[0,0,0],[255,255,255]],
                   [[0,0,0],[0,0,0],[0,0,0]],
                   [[255,255,255],[0,0,0],[255,255,255]]]) # filter모양도 rgb가 들어갈 수 있도록 만든 것

filter_gray = rgb_gray(filter)
plt.imshow(filter_gray,cmap='gray')

result=convolusion(img_pixel_gray,filter_gray,stride=1,bias=0)
plt.imshow(result,cmap="gray")
plt.imsave("c:\\data\\b2b_result.jpg",result,cmap="gray")





# 11/9

"""
bric 실제 이미지 데이터를 활용한 cnn 링크
http://www.birc.co.kr/2018/02/26/%EC%8B%A4%EC%A0%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-cnn-%EB%AA%A8%EB%8D%B8-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0/
"""

# 풀링계층

## conv -> pooling -> fully connected(pooling/reshape해서 쫙 펼치는 것)
## convolusion : 이미지의 특징을 추출하는 계층(하나의 이미지로 여러개의 다른 feature map을 생성)
## pooling 계층
### -출력값에서 일부분만 취하는 기능
### -합성곱을 하다보면 이렇게 저렇게 망쳐 놓은 그림들을 각각 부분에서 대표들을 뽑아 사이즈가 작은 이미지를 만드는 것이다
### -마치 사진을 축소하면 해상도가 좋아지는 듯한 효과와 비슷하다.

## pooling의 종류3가지
### -최대풀링 : 합성곱 데이터에서 가장 큰 값을 대표값으로 선정
### -평균풀링 : 합성곱 데이터에서 모든 값의 평균을 대표값으로 선정
### -확률적 풀링 : 합성곱 데이터에서 임의 확률로 한계 설정
'''
21  8  8  12    21  12
12 19  9   7    18  10
 8 10  4   3
18 12  9  10
'''
import tensorflow as tf
import numpy as np
a = np.array([[21,8,8,12],
              [12,19,9,7],
              [8,10,4,3],
              [18,12,9,10]])

max_pooling(a)
def max_pooling(array):
    res = []
    a = array.flatten()
    for i in range(0,12,2):     # i=0,2,4,6,8,10
        if i == 4 or i == 6:
            continue
        temp = np.array([a[i:i+2],a[i+4:i+6]])
        res.append(np.max(temp))
    res = np.array(res).reshape(2,2)
    return res
max_pooling(a)
"""
array([[21, 12],
       [18, 10]])
"""





# 11/12
# http://www.vision.caltech.edu/Image_Datasets/Caltech101/
# 101_ObjectCategories.tar.gz (131Mbytes) C드라이브에 저장한 후 압축풀기

# 테스트셋 트레이닝셋 만들기
from PIL import Image
import os,glob
import numpy as np
from sklearn.model_selection import train_test_split

caltech_dir = "c:/101_ObjectCategories"
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)

image_w = 64
image_h = 64
pixels = image_w * image_h * 3

X = []
Y = []
for idx, cat in enumerate(categories):
    label = [0 for i in range(nb_classes)]
    label[idx] = 1
    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w,image_h))
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
        if i % 10 == 0:
            print(i,"\n",data)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = train_test_split(X,Y)
xy = (X_train,X_test,y_train,y_test)
np.save("c:/101_ObjectCategories/5obj.npy",xy)
print(len(Y))

# 학습시키기
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np

categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_class = len(categories)

image_w = 64
image_h = 64

X_train, X_test, y_train, y_test = np.load("c:/101_ObjectCategories/5obj.npy")

X_train = X_train.astype("float")/255   # RGB 최대치가 255
X_test = X_test.astype("float")/255

X_train.shape

model = Sequential()
model.add(Convolution2D(32,3,3,border_mode="same",input_shape=X_train.shape[1:]))
#border_mode="same" : padding이랑 같은 역할
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))    # Dropout : 뉴런에서 다음뉴런에 전달할 때 없어도될만한 라인 가지치기(25% 가지치기)

# 은닉층
model.add(Convolution2D(64,3,3,border_mode="same"))
model.add(Activation('relu'))
model.add(Convolution2D(64,3,3))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

# flatten
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_class))
model.add(Activation('softmax'))    # 최종적으로는 확률갑으로 표현해주는것이 좋다.
model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
model.fit(X_train,y_train,batch_size=32,nb_epoch=50)
# nb_epoch 만큰 돌아간다.

score = model.evaluate(X_test,y_test)
print('loss =',score[0])
print('accuracy =',score[1])

# 모델을 파일로 저장
from keras.models import load_model

model.save("c:/101_ObjectCategories/5obj-model.h5")

model_1 = load_model("c:/101_ObjectCategories/5obj-model.h5")

# 학습된 이미지 분류
import sys,os
from PIL import Image
import numpy as np

image_size = 64
categories = ["chair","camera","butterfly","elephant","flamingo"]

X = []
files = glob.glob("c:/101_ObjectCategories/elephant/image_0001.jpg")
for i, f in enumerate(files):
    img = Image.open(f)
    img = img.convert("RGB")
    img = img.resize((image_size,image_size))
    data = np.asarray(img)
    X.append(data)

X = np.array(X)
np.argmax(model.predict(X))

# 학습하지 않은 이미지로 분류
import sys,os
from PIL import Image
import numpy as np

image_size = 64
categories = ["chair","camera","butterfly","elephant","flamingo"]

X = []
files = glob.glob("F:/학원/5.머신러닝/sample/*.jpg")
for i, f in enumerate(files):
    img = Image.open(f)
    img = img.convert("RGB")
    img = img.resize((image_size,image_size))
    data = np.asarray(img)
    X.append(data)

X = np.array(X)
np.argmax(model.predict(X)[0])
np.argmax(model.predict(X)[1])
# 학습시켜서 다시 돌려보자

html = ""
pre = model.predict(X)
for i, p in enumerate(pre):
    y = p.argmax()
    print("입력:", files[i])
    print("분류 이름:", categories[y])
    html += """
        <h3>입력:{0}</h3>
        <div>
          <p><img src="{1}" width=300></p>
          <p>분류 이름:{2}</p>
         </div>
    """.format(os.path.basename(files[i]),files[i], categories[y])
# 리포트 저장하기 --- (※5)
html = "<html><body style='text-align:center;'>" + \
    "<style> p { margin:0; padding:0; } </style>" + \
    html + "</body></html>"
with open("c:/101_ObjectCategories/result.html", "w") as f:
    f.write(html)
 
# 학습되지 않는 이미지들 저장
pre = model.predict(X_test)
for i,v in enumerate(pre):
    pre_ans = v.argmax()
    ans = y_test[i].argmax()
    dat = X_test[i]
    if ans == pre_ans: continue
    print("[NG]", categories[pre_ans], "!=", categories[ans])
    print(v)
    fname = "c:/101_ObjectCategories/error/" + str(i) + "-" + categories[pre_ans] + \
        "-ne-" + categories[ans] + ".png"
    dat *= 256
    img = Image.fromarray(np.uint8(dat))
    img.save(fname)
score = model.evaluate(X_test, y_test)

print('loss=', score[0])
print('accuracy=', score[1])





# 11/14

# SVM(Support Vector Machines)
## -기계학습 분야 중 하나로 패턴 인식, 자료분석을 위한 지도학습 모델이다.
## -지도학습은 미리 답을 주고 학습을 시킨다.
## -비지도학습은 답을 주지 않고 학습을 시킨다.
## -분류와 회귀분석을 위해 사용된다.
## -두 카테고리 중 어느 하나에 속한 데이터의 집합이 주어졌을 때 새로운 데이터는 어느 카테고리에 속할지 판단하는 기준으로 가장 큰 폭을 가진 경계를 찾는 알고리즘
## -선형분류 뿐 아니라 비선형 분류도 가능하다.
## -모델을 만들 때 고려해야할 parameter가 많지 않다.
## -적은 양의 데이터로 모델을 만들 수 있다.
## -딥러닝이 이전에는 분류 모형중에서 기술적으로 가장 진보된 모형으로 평가되었다

import pandas as pd
from sklearn.svm import LinearSVC
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

iris=pd.read_csv("c:/data/iris.csv")
iris_data= iris[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
iris_label= iris['Name']
train_data,test_data,train_label,test_label= train_test_split(iris_data,iris_label,test_size = 0.2)
iris_model=svm.SVC(kernel = 'linear')
irs_model=LinearSVC() # iris_model=svm.SVC(kernel = 'linear')이거와 같은 것 각각 LinearSVC와 svm에 있는 매소드
iris_model.fit(train_data,train_label)
iris_pred=iris_model.predict(test_data)
ac_score = metrics.accuracy_score(test_label,iris_pred)
print("정답률 :",ac_score)

iris_model.predict([[6.0,2.9,4.5,1.5]]) # array(['Iris-versicolor'], dtype=object)
iris_model.predict([[6.0,2.9,4.5,1.5]])[0] # 'Iris-versicolor' /붓꽃의 종류만 보고자하면 0번 인덱스
iris_model.predict([[3.0,1.9,2.5,0.5]]) # array(['Iris-versicolor'], dtype=object)
iris_model.predict([[3.0,1.9,2.5,0.5]])[0] # 'Iris-versicolor'

# bmi로 하기
df=pd.read_csv("c:/data/bmi.csv")
df
label=df["label"]
w=df["weight"]/100
h=df["height"]/200
wh=pd.concat([w,h],axis=1)

train_data, test_data, train_label, test_label = train_test_split(wh, label, test_size=0.2)
bmi_model=svm.SVC(kernel = 'linear')
bmi_model=svm.SVC(kernel = 'RBF')
bmi_model=LinearSVC()
bmi_model.fit(train_data,train_label)
bmi_pred=bmi_model.predict(test_data)
ac_score=metrics.accuracy_score(test_label,bmi_pred)
print("정답률:",ac_score)

bmi_model.predict([[71/100,178/200]]) # array(['normal'], dtype=object)
bmi_model.predict([[71/100,178/200]])[0] # 'normal'
bmi_model.predict([[51/100,155/200]]) # array(['normal'], dtype=object)
bmi_model.predict([[51/100,155/200]])[0] # 'normal'

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("c:/data/bmi.csv",index_col=2) # 어떤 컬럼을 인덱스로 만들것인가를 묻는 것
df

fig=plt.figure()
ax=fig.add_subplot(1,1,1) # (1,1,1)의 의미는 축을 만든 것
def scatter(lbl, color):
    b=df.loc[lbl]
    ax.scatter(b['weight'],b['height'],c=color, label=lbl)

scatter("fat","red")
scatter("normal","black")
scatter("thin","green")
ax.legend(loc=1)
plt.savefig("c:/data/bmi_scatter.jpg")

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
# %matplotlib inline
csv = pd.read_csv('c:/data/iris.csv')
X =  csv[["SepalLength","SepalWidth"]]
y = csv["Name"]
X = np.array(X) # np.array안에는 숫자값만 넣어야 하므로 일단 name값을 제외한 값들을 x값에 넣어둔 것
bclass = {"Iris-setosa": 0, "Iris-virginica": 1, "Iris-versicolor":2} # 붓꽃의 종류별로 각각 0과 1과 2로 조건제어문 하지 않고 딕셔너리로 만든 후 변경
y = y.apply(lambda x : bclass[x]) # 딕셔너리로 변경된 것을 이용하 람다에 넣어서 조건제어문 사용하지 않는 것
y = np.array(y)



def plotSVC(title):
    x_min, x_max = X[:, 0].min()- 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min()- 1, X[:, 1].max() + 1
    h = (x_max / x_min)/100
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    np.arange(y_min, y_max, h))
    plt.subplot(1, 1, 1)
    Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.title(title)
    plt.show()

# Linear(선형) : 분류시 이상치에 대한 표현이 잘 되지 않는다는 문제점이 있음
# rbf(비선형): 유클리드 거리계산을 통해 선형에서 표현되지 않았던 굴곡을 표현해줌
kernels = ['linear', 'rbf']
for kernel in kernels:
    svc = svm.SVC(kernel=kernel).fit(X, y)
    plotSVC('kernel=' + str(kernel))

# 데이터 포인트 사이의 거리는 가우시안 커널에 의해 계산된다
# gamma는 가우시안 커널의 폭을 제어하는 매개변수 

gammas = [0.1, 1, 10, 100] # 비선형에 가중치값을 조절하여 폭을 조절한 수 있게 하는 것이 감마/ 감마 값에 따라서 분류가 달라지는 것/감마값을 너무 높게 주게 되면 overfitting 될 수 있음
for gamma in gammas:
   svc = svm.SVC(kernel='rbf', gamma=gamma).fit(X, y)
   plotSVC('gamma=' + str(gamma))
   
# kmeans, svm은 비지도 학습 





# 11/16
   
# TF-IDF(Term Frequency - Inverse Document Frequency)
## TF(단어 빈도)는 특정한 단어가 문서내에 얼마나 자주 등장하는지를 나타내는 값이다.
## 이 값이 높을수록 문서에서 중요하다고 생각할 수 있다.
## 하지만 하나의 문서에서 많이 나오지 않고 다른 문서에서 자주 등장하면 단어의 중요도는 낮아진다.
## DF(문서 빈도) 이값을 역수를 하면 IDF(역문서빈도)
## TF-IDF는 TF와 IDF를 곱한 값으로 점수가 높은 단어일수록 다른 문서에는 많지 않고 해당 문서에서 자주 등장하는 단어의미이다.

# 문서1 : if you think you can
# 문서2 : or you think you can not you are right

# TF-IDF 계산 단계
## 1.각 문서에 대한 각 단어의 빈도를 계산
## 2.IDF계산
## 3.TF-IDF계산
'''
문서1
단어    단어수
if        1
you       2
think     1
can       1

문서2
단어    단어수
or        1
you       3
think     1
can       1
not       1
are       1
right     1

문서1 단어수 : 5
문서2 단어수 : 9

단계 1)
            어떤 문서에서 단어t가 나오는 횟수
TF(t) =    --------------------------------
            그 문서에서 있는 단어의 총 수
TF('think',문서1) = 1/5 = 0.2
TF('think',문서2) = 1/9 ≒ 0.111

단계 2)
           
IDF(t) =  log10(문서의 총수/ 단어 t가 들어간 문서의 수)
'''
import numpy as np

'''
IDF('think',문서1)=np.log10(2/2)=0

단계 3)
TF * IDF 계산
TFIDF('think',문서1) = 0.2 * 0 = 0
TFIDF('think',문서2) = 0.11 * 0 = 0

tf('right',문서1) = 0/5 =  0
tf('right',문서2) = 1/9 ≒ 0.111

idf('right',문서) = np.log10(2/1) ≒ 0.301

tfidf('right',문서1) = 0 * 0.301 = 0
tfidf('right',문서2) = 0.11 * 0.301 = 0.03311
'''
# word2vec(word to vector)
# -구글의 토마스미콜로프(Tomas Mikolov) 이끄는 팀이 개발
# -2계층 신경망(two layer neural network)을 사용해 개발
# -텍스트에서 벡터 집합을 생성한다.
from konlpy.tag import Komoran
tagger = Komoran()
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests
import lxml.html
import codecs
fp = codecs.open('c:/data/미술관옆동물원.txt','r')
soup = BeautifulSoup(fp,"html.parser")
body = soup.select_one("body")
text = body.getText()
articles = []
articles = text.split('\n')
len(articles)
fp.close()

from sklearn.feature_extraction.text import TfidfVectorizer

# TfidfVectorizer
## Tf-IDF방정식으로 단어의 가중치를 조정한 BOW 벡터를 만든다.

# BOW(Bag Of Words)
## 문서를 숫자 벡터로 변환하는 가장 기본적인 방법

corpus = ['This is the first document', 'This document is the second document','And this is the third one', 'Is this the first document']
v= TfidfVectorizer()
x= v.fit_transform(corpus) # term-document matrix 생성
print(v.get_feature_names())
# '['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']' 단어들을 알파벳 순서대로 인덱스를 만든 것
x.shape # Out[47]: (4, 9) /4는 matrix로 만든 문장의 수, 9는 분석해야할 단어의 수
print(x)
'''
  (0, 8)        0.38408524091481483 #0은 첫번째 문서의 this라는 단어는 인덱싱 되어있는 단어들 중 8번째에 있는 것임을 표현
  (0, 3)        0.38408524091481483
  (0, 6)        0.38408524091481483
  (0, 2)        0.5802858236844359
  (0, 1)        0.46979138557992045
  (1, 8)        0.281088674033753
  (1, 3)        0.281088674033753
  (1, 6)        0.281088674033753
  (1, 1)        0.6876235979836938
  (1, 5)        0.5386476208856763
  (2, 8)        0.267103787642168
  (2, 3)        0.267103787642168
  (2, 6)        0.267103787642168
  (2, 0)        0.511848512707169
  (2, 7)        0.511848512707169
  (2, 4)        0.511848512707169
  (3, 8)        0.38408524091481483
  (3, 3)        0.38408524091481483
  (3, 6)        0.38408524091481483
  (3, 2)        0.5802858236844359
  (3, 1)        0.46979138557992045
  '''
# 왼쪽(0,8)은 0은 첫번째 문서의 this라는 단어는 인덱싱 되어있는 단어들 중 8번째에 있는 것임을 표현/ 오른쪽 값은 tf*idf값임
print(v.vocabulary_.get('first'))#인덱스 번호를 return해줌
print(v.vocabulary_.get('document'))

# CountVectorizer 
from sklearn.feature_extraction.text import CountVectorizer 
## -문서를 토큰(단어) 리스트로 변환한다.
## -각 문서에서 토큰의 출현빈도를 센다.
## -각 문서를 BOW 인코딩 벡터로 변환한다.

c=CountVectorizer()
c.fit(corpus) # 카운트 벡터라이저 했던 단어가 보임
c.vocabulary_
'''
{'this': 8,
 'is': 3,
 'the': 6,
 'first': 2,
 'document': 1,
 'second': 5,
 'and': 0,
 'third': 7,
 'one': 4}
'''
c.transform(['This is the second document']).toarray() # array([[0, 1, 0, 1, 0, 1, 1, 0, 1]], dtype=int64)
# c.vocabulary_결과에 단어가 있으면 0,없으면 1로 표현해주는 것 

c.transform(corpus).toarray()
"""
array([[0, 1, 1, 1, 0, 0, 1, 0, 1],
       [0, 2, 0, 1, 0, 1, 1, 0, 1],
       [1, 0, 0, 1, 1, 0, 1, 1, 1],
       [0, 1, 1, 1, 0, 0, 1, 0, 1]], dtype=int64)
"""

# 2글자 이상인 명사만 추출
def get_noun(text):
    nouns = tagger.nouns(text)
    return [n for n in nouns if len(n) > 1]

count=0
articles_1=[]
for i in articles:
    if len(i)==0:
        print(count)
        continue
    articles_1.append(i)
cv = TfidfVectorizer(tokenizer = get_noun,max_features=100) # 2글자 이상인 단어 중 특징이 될만한 단어 maximum 100개만 출력하는 것
tdm=cv.fit_transform(articles_1)

import numpy as np
import operator
words = cv.get_feature_names()
count_map = tdm.sum(axis=0)
count_map.shape
count = np.squeeze(np.array(count_map))
count.shape
word_count = list(zip(words,count))
word_count
word_count = sorted(word_count,key=operator.itemgetter(1),reverse=True) # 카운트 수가 높은 순으로 sorted한것

hot_key = list(dict(word_count[:50]).keys())

from matplotlib import pyplot
from wordcloud import WordCloud
wc = WordCloud(font_path="c:\\Windows\\Fonts\\malgun.ttf",background_color = 'white', width = 400, height = 300)
cloud = wc.fit_words(dict(word_count))
pyplot.figure(figsize=(12,9))
pyplot.imshow(cloud)
pyplot.show()



# 강사님이 주신 코드
from konlpy.tag import Komoran
tagger = Komoran()  # 형태소 분석기
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests
import lxml.html
import codecs


articles = []
fp = codecs.open("c:/data/미술관옆동물원.txt", "r")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText()
articles = text.split("\n")
len(articles)
fp.close()



from sklearn.feature_extraction.text import TfidfVectorizer

def get_noun(text):
    nouns = tagger.nouns(text)
    return [n for n in nouns if len(n) > 1] 


cv = TfidfVectorizer(tokenizer=get_noun, max_features=100)
tdm = cv.fit_transform(articles)
print(cv.get_feature_names())
print(tdm.toarray())
print(tdm) 


import numpy as np
import operator
words = cv.get_feature_names()

count_mat = tdm.sum(axis=0)
count_mat.shape
count = np.squeeze(np.asarray(count_mat))
count.shape
word_count = list(zip(words, count))
word_count = sorted(word_count, key=operator.itemgetter(1), reverse=True)
word_count

hot_key = list(dict(word_count[:50]).keys())
hot_key


%matplotlib inline
from matplotlib import pyplot
from wordcloud import WordCloud
wc = WordCloud(font_path='C:\\Windows\\Fonts\\NGULIM.ttf', background_color='white', width=400, height=300)
cloud = wc.fit_words(dict(word_count))
pyplot.figure(figsize=(12, 9))
pyplot.imshow(cloud)
pyplot.axis("off")
pyplot.show()

import codecs
from konlpy.tag import Twitter
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

def sigmoid(x):
    return 1 / (1 + math.e ** -x)


twitter = Twitter()
results = []
lines = articles
words_all = []

for line in lines:
    # 형태소 분석하기
    malist = twitter.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 명사/동사/부사만 걸러내기 
        if word[1] in ['Noun','Verb','Adjective']:
            r.append(word[0])
            words_all.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    # print(rl)

''' 
pip install gensim
''' 

from gensim.models import word2vec
yang_file = 'c:/data/yang.model'
with open(yang_file, 'w', encoding='utf-8') as fp2:
    fp2.write("\n".join(results))
    
fp2.close() 

data = word2vec.LineSentence(yang_file)
model = word2vec.Word2Vec(data,size=200, window=10, hs=1, min_count=2, sg=1) 
# size = 200차원벡터
# window = 주변단어는 앞뒤로 10개
# min_count = 출연비도는 2개 미만은 제외
# hs = 1이면 softmax를 트레이닝할 때 사용/ 0이면 0이 아닌 음수로 샘플링됨.
# sg = 0이면 분석방법론은 CBOW/1이면 분석방법론은 Skip_Gram 
# CBOW(Continuous Bag of Word) : 주변 단어들을 가지고 중심에 있는 단어를 맞추는 방식
# Skip-Gram : 중심에 있는 단어로 주변 단어를 예측하는 방법

model.save("c:/data/yang_w2v.model") # model저장하는 방법


model.most_similar(positive=["춘희"]) # positive는 유사한것/negative는 유사하지 않은 것
model.most_similar(positive=["철수"])
model.most_similar(positive=["미술관"])
model["결혼"]
model["사람"]
model.most_similar(positive=["미술관","여자"] , negative=["여자"])

model.similarity('춘희','철수') # 두 단어끼리의 관련성 정도를 리턴해줌
model.similarity('춘희','인공')





# Problem Set 

[문제199] 보험데이터를 이용해서 보험료에 가장 영향을 주는 독립변수가 무엇인지 확인하세요.

##R에서##

insurance <- read.csv("c:/data/insurance.csv")

lmresult <- lm(charges ~ age+sex+bmi+children+smoker+region, data = insurance)
lmresult

summary(lmresult)

정답 : 
  
insurance <- read.csv("c:/data/insurance.csv",header=T)
str(insurance)
cor(insurance[c("age","bmi","children","charges")])
#age - charges 가 가장 큰 연관관계가 있다.

install.packages("psych")
library(psych)
pairs.panels(insurance[c("age","bmi","children","charges")])

ins_model <- lm(charges ~ ., data = insurance)
ins_model

insurance$bmi30 <- ifelse(insurance$bmi >= 30,1,0)
ins_model2 <- lm(charges ~ age+children+bmi+sex+smoker+bmi30*smoker+region,data=insurance)
ins_model2

##Python에서##

import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("c:/data/insurance.csv")

df.head()

cols = ['charges','age','bmi','children']

dummy_sex = pd.get_dummies(df['sex'],prefix='sex')
dummy_smoker = pd.get_dummies(df['smoker'],prefix='smoker')
dummy_region = pd.get_dummies(df['region'],prefix='region')

data = df[cols].join(dummy_sex['sex_male'])
data = data.join(dummy_smoker['smoker_yes'])
data = data.join(dummy_region.ix[:,1:])
data.head()

data.isnull().sum()

from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(data.ix[:,1:],data['charges'])
reg.intercept_
reg.coef_

stats.linregress(data.ix[:,1:],data['charges'])

정답 : 

import pandas as pd

df = pd.read_csv("c:/data/insurance.csv")
df.head()

dummy_sex = pd.get_dummies(df['sex'],prefix='sex')
dummy_smoker = pd.get_dummies(df['smoker'],prefix='smoker')
dummy_region = pd.get_dummies(df['region'],prefix='region')
col = ['age','bmi','children','charges']
data = dummy_smoker.join(dummy_sex)
data = data.join(df[col])
data

import statsmodels.formula.api as smf
lm = smf.ols(formula="charges ~ age+smoker_yes+sex_male+bmi+children",data=data).fit()
print(lm.params)

-------------------------------------------------------------------------------

[문제200] tensorflow 상수를 이용해서 아래와 같이 결과를 출력하는 프로그램을 만드세요.
a + b = 6
a * b = 8

import tensorflow as tf

a = tf.constant(2)
b = tf.constant(4)
c = a + b
d = a * b

with tf.Session() as sess:
    print('a + b = {}'.format(sess.run(c)))
    print('a * b = {}'.format(sess.run(d)))

[문제201] tensorflow 상수를 이용해서 아래와 같이 결과를 출력하는 프로그램을 만드세요.
단 두 변수의 입력값을 실행시에 넣도록하는 변수를 이용하세요.
Add : 6
Mulitply : 8

a = tf.placeholder(tf.int32)    #placeholder는 초기화시키지 않아도 된다.
b = tf.placeholder(tf.int32)
add = tf.add(a,b)
mul = tf.multiply(a,b)

with tf.Session() as sess:
    print('Add : %d'%sess.run(add, feed_dict={a:2,b:4}))
    print('Multiply : %d'%sess.run(mul, feed_dict={a:2,b:4}))

-------------------------------------------------------------------------------

[문제202]
x변수는 1행3열 모양의 1,2,3
w변수는 3행1열 모양의 2,2,2
y변수는 x와 w를 행렬의 곱을 이용한 결과를 수행하는 프로그램을 작성하세요.

x = tf.placeholder(tf.float32,shape=(1,3))
w = tf.placeholder(tf.float32,shape=(3,1))
z = tf.matmul(x,w)
with tf.Session() as sess:
    print(sess.run(z,feed_dict={x:[[1,2,3]],w:[[2],[2],[2]]}))
    
정답:

#상수를 이용
x = tf.constant([[1.0,2.0,3.0]])
print(x.get_shape())
w = tf.constant([[2.0],[2.0],[2.0]])
print(w.get_shape())
y = tf.matmul(x,w)

sess = tf.Session()
print(sess.run(x))
print(sess.run(w))
print(sess.run(y))


#변수를 이용
x = tf.Variable([[1.0,2.0,3.0]])
w = tf.Variable([[2.0],[2.0],[2.0]])
y = tf.matmul(x,w)
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(y))
-------------------------------------------------------------------------------
1105
[문제203] linear regression 학습을 통해서 입력값에 대한 예측값을 출력하세요.
 x1  x2  x3  y
 ---------------
 73  80  75  152
 93  88  93  185
 89  91  90  180
 96  98  100  196
 73  66  70  142
    
 풀이1 : 
        
data = [[73,80,75,152],[93,88,93,185],[89,91,90,180],[96,98,100,196],[73,66,70,142]]

x1_data = [i[0] for i in data]
x2_data = [i[1] for i in data]
x3_data = [i[2] for i in data]
y_data = [i[3] for i in data]

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w1 = tf.Variable(tf.random_normal([1], seed=0),name="weight1")
w2 = tf.Variable(tf.random_normal([1], seed=0),name="weight2")
w3 = tf.Variable(tf.random_normal([1], seed=0),name="weight3")
b = tf.Variable(tf.random_normal([1], seed=0),name="bais")

hypothesis = w1*x1 + w2*x2 + w3*x3 +b
cost = tf.reduce_mean(tf.square(hypothesis-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)   #NaN으로 나오면 학습률을 줄여줘야
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val,w1_val,w2_val,w3_val,b_val,_ = sess.run([cost,w1,w2,w3,b,train],feed_dict={x1:x1_data,x2:x2_data,x3:x3_data,y:y_data})
    if step % 10000 == 0:
        print(step, cost_val, w1_val, w2_val, w3_val, b_val)
        
print("당신의 점수는",sess.run(hypothesis,feed_dict={x1:100,x2:70,x3:60}))

풀이2 :

#행렬의 곱으로 풀이1 개선
x_data = [[73,80,75],[93,88,93],[89,91,90],[96,98,100],[73,66,70]]
y_data = [[152],[185],[180],[196],[142]]

x = tf.placeholder(tf.float32,shape=[None,3])   #n행3열
y = tf.placeholder(tf.float32,shape=[None,1])   #n행1열
w = tf.Variable(tf.random_normal([3,1],seed=0),name='weight')   #[3,1] : 3은 x의 열값이 들어오는 값, 1은 y로 나가는 값 
b = tf.Variable(tf.random_normal([1], seed=0),name="bais")      #[1] : 1은 y로 나가는 값

hypothesis = tf.matmul(x,w) + b
cost = tf.reduce_mean(tf.square(hypothesis-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)   #NaN으로 나오면 학습률을 줄여줘야
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val,w_val,b_val,_ = sess.run([cost,w,b,train],feed_dict={x:x_data,y:y_data})
    if step % 10000 == 0:
        print(step, cost_val, w_val, b_val)
        
print("당신의 점수는",sess.run(hypothesis,feed_dict={x:[[100,70,60]]}))

#ex.csv파일을 불러오는 방법
import tensorflow as tf
import numpy as np

xy = np.loadtxt("c:/data/ex.csv",delimiter=",",dtype=np.float32)

x_data = xy[:,0:-1]
y_data = xy[:,[-1]]
x_data.shape
y_data.shape #5행1열
#y_data = xy[:,-1] : 1행 5열
x = tf.placeholder(tf.float32,shape=[None,3])
y = tf.placeholder(tf.float32,shape=[None,1])
w = tf.Variable(tf.random_normal([3,1],seed=0),name='weight')
b = tf.Variable(tf.random_normal([1], seed=0),name="bais")

hypothesis = tf.matmul(x,w) + b
cost = tf.reduce_mean(tf.square(hypothesis-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val,hy_val,_ = sess.run([cost,hypothesis,train],feed_dict={x:x_data,y:y_data})
    if step % 10000 == 0:
        print(step, cost_val, hy_val)
        
print("당신의 점수는",sess.run(hypothesis,feed_dict={x:[[100,70,60]]}))

-------------------------------------------------------------------------------
1106
[문제204] xor를 logistic regression classifier를 이용해서 프로그램을 생성하세요.

0 0 0
0 1 1 
1 0 1
1 1 0

import tensorflow as tf
import numpy as np

x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[0]]
x_data = np.array(x_data,dtype=np.float32)
y_data = np.array(y_data,dtype=np.float32)

x = tf.placeholder(tf.float32,[None,2])
y = tf.placeholder(tf.float32,[None,1])

w1 = tf.Variable(tf.random_normal([2,2],seed=0),name='weight1')
b1 = tf.Variable(tf.random_normal([2],seed=0),name='bias1')
layer1 = tf.sigmoid(tf.matmul(x,w1) + b1)

w2 = tf.Variable(tf.random_normal([2,1],seed=0),name='weight2')
b2 = tf.Variable(tf.random_normal([1],seed=0),name='bias2')
hypothesis = tf.sigmoid(tf.matmul(layer1,w2) + b2)

cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1-y) * tf.log(1-hypothesis))   #cross entropy cost function
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
    
for step in range(10001):
    sess.run([cost,train],feed_dict={x:x_data,y:y_data})
    if step % 100 == 0:
        print(step,sess.run(cost,feed_dict={x:x_data,y:y_data}),sess.run([w1,w2]))
        h = sess.run(hypothesis,feed_dict={x:x_data,y:y_data})
        print(h)

a = sess.run(hypothesis,feed_dict={x:[[0,0],[0,1],[1,0],[1,1]]})
print(sess.run(tf.cast(a>0.5,dtype=tf.int32)))

#은닉층을 하나 더 넣어보자

import tensorflow as tf
import numpy as np

x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[0]]
x_data = np.array(x_data,dtype=np.float32)
y_data = np.array(y_data,dtype=np.float32)

x = tf.placeholder(tf.float32,[None,2])
y = tf.placeholder(tf.float32,[None,1])

#input
w1 = tf.Variable(tf.random_normal([2,5],seed=0),name='weight1')
b1 = tf.Variable(tf.random_normal([5],seed=0),name='bias1')
layer1 = tf.sigmoid(tf.matmul(x,w1) + b1)
#hidden layer2
w2 = tf.Variable(tf.random_normal([5,4],seed=0),name='weight2')
b2 = tf.Variable(tf.random_normal([4],seed=0),name='bias2')
layer2 = tf.sigmoid(tf.matmul(layer1,w2) + b2)
#hidden layer3
w3 = tf.Variable(tf.random_normal([4,4],seed=0),name='weight3')
b3 = tf.Variable(tf.random_normal([4],seed=0),name='bias3')
layer3 = tf.sigmoid(tf.matmul(layer2,w3) + b3)

#output layer
w4 = tf.Variable(tf.random_normal([4,1],seed=0),name='weight4')
b4 = tf.Variable(tf.random_normal([1],seed=0),name='bias4')
hypothesis = tf.sigmoid(tf.matmul(layer3,w4) + b4)

cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1-y) * tf.log(1-hypothesis))   #cross entropy cost function
train = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
    
for step in range(10001):
    sess.run([cost,train],feed_dict={x:x_data,y:y_data})
    if step % 100 == 0:
        print(step,sess.run(cost,feed_dict={x:x_data,y:y_data}),sess.run([w1,w2]))
        h = sess.run(hypothesis,feed_dict={x:x_data,y:y_data})
        print(h)

a = sess.run(hypothesis,feed_dict={x:[[0,0],[0,1],[1,0],[1,1]]})
print(sess.run(tf.cast(a>0.5,dtype=tf.int32)))

-------------------------------------------------------------------------------
1107
[문제205] zoo data set을 이용해서 분류프로그램을 만드세요.

import tensorflow as tf
import numpy as np

xy = np.loadtxt("c:/data/zoo_data.txt",delimiter=",",usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17),dtype=np.float32)
#usecols : 사용할 열을 지정해준다.(여기서는 첫번째 열(1.animal name)은 필요없다.)

x_data = xy[:,0:-1]
y_data = xy[:,[-1]]
y_data = y_data - 1
#18.type이 1번부터 7번까지 되어있어 0번부터 6번까지로 맞춰준다.
#0 : 포유류, 1 : 조류, 2 : 파충류, 3 : 어류, 4 : 양서류, 5 : 곤충/거미류, 6 : 무척추동물

print(x_data.shape,y_data.shape)
nb_classes = 7
x = tf.placeholder(tf.float32,[None,16])
y = tf.placeholder(tf.int32,[None,1])

y_one_hot = tf.one_hot(y,nb_classes)    #one_hot encoding : N개의 단어를 각각 N차원의 벡터로 표현
y_one_hot = tf.reshape(y_one_hot,[-1,nb_classes])
#3차원에서 2차원으로 바꿔준다.

w = tf.Variable(tf.random_normal([16,nb_classes],seed=0),name="weight")
b = tf.Variable(tf.random_normal([nb_classes],seed=0),name="bias")

logits = tf.matmul(x,w) + b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_one_hot))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)

prediction = tf.argmax(hypothesis,1)
correct_prediction = tf.equal(prediction,tf.argmax(y_one_hot,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(optimizer,feed_dict={x:x_data,y:y_data})
    if step % 100 == 0:
        loss,acc = sess.run([cost,accuracy],feed_dict={x:x_data,y:y_data})
        print("Step:{:5}\tLoss:{:.3f}\tAcc:{:.2%}".format(step,loss,acc))
#:5 : 다섯자리숫자 오른쪽정렬
#:.3f : 소숫점 이하 세자리
#:.2% : 소숫점 이하 두자리, %

pred = sess.run(prediction,feed_dict={x:x_data})
for p,y in zip(pred,y_data.flatten()):
    print("[{}] Prediction : {} True Y: {}".format(p==int(y),p,int(y)))
    
#worm,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,7
#wren,0,1,1,0,1,0,0,0,1,1,0,0,2,1,0,0,2 
zoo_hypothesis = sess.run(hypothesis,feed_dict={x:[[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]]})
print(zoo_hypothesis,sess.run(tf.argmax(zoo_hypothesis,1)))
zoo_hypothesis = sess.run(hypothesis,feed_dict={x:[[0,1,1,0,1,0,0,0,1,1,0,0,2,1,0,0]]})
print(zoo_hypothesis,sess.run(tf.argmax(zoo_hypothesis,1)))

'''
a = np.arange(12)
a
b = a.reshape(3,4)
b = a.reshape(3,-1)

a.reshape(2,2,-1)
a.reshape(2,-1,2)

a.flatten()
'''

-------------------------------------------------------------------------------

[문제206] bmi.csv 내용을 신경망을 이용해서 분류해 보세요.

#BMI
# BMI = 몸무게 / (키(m)*키(m))
# 18.5 이상 25미만이면 표준
#label : thin(저체중), normal(정상), fat(비만)

import pandas as pd

bmi = pd.read_csv('c:/data/bmi.csv',delimiter=',')
bmi = np.array(bmi)

x_data = bmi[:,0:-1]
y_data = bmi[:,[-1]]
x0_mean = np.mean(x_data[:,[0]]); x0_std = np.std(x_data[:,[0]])
x1_mean = np.mean(x_data[:,[1]]); x1_std = np.std(x_data[:,[1]])
x_data[:,[0]] = (x_data[:,[0]] - x0_mean) / x0_std
x_data[:,[1]] = (x_data[:,[1]] - x1_mean) / x1_std

y_data[y_data=='thin'] = 0
y_data[y_data=='normal'] = 1
y_data[y_data=='fat'] = 2
# 0: thin, 1: normal, 2:fat 으로 변환
print(x_data.shape,y_data.shape)

nb_classes = 3

x = tf.placeholder(tf.float32,[None,2])
y = tf.placeholder(tf.int32,[None,1])

y_one_hot = tf.one_hot(y,nb_classes)
y_one_hot = tf.reshape(y_one_hot,[-1,nb_classes])

w = tf.Variable(tf.random_normal([2,nb_classes],seed=0),name="weight")
b = tf.Variable(tf.random_normal([nb_classes],seed=0),name="bias")
logits = tf.matmul(x,w) +b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_one_hot))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)

prediction = tf.argmax(hypothesis,1)    
correct_prediction = tf.equal(prediction,tf.argmax(y_one_hot,1))    
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))    

sess = tf.Session()    
sess.run(tf.global_variables_initializer())    
for step in range(2001):
    sess.run(optimizer,feed_dict={x:x_data,y:y_data})
    if step % 100 == 0:
        loss,acc = sess.run([cost,accuracy],feed_dict={x:x_data,y:y_data})
        print("Step : {:5}\tLoss : {:.3f}\tAcc : {:.2%}".format(step,loss,acc))

pred = sess.run(prediction, feed_dict={x:x_data})
for p,y in zip(pred,y_data.flatten()):
    print("[{}] Prediction : {} True Y : {}".format(p==int(y),p,int(y)))

mbi_hypothesis = sess.run(hypothesis, feed_dict={x:[[(<키>-x0_mean)/x0_std,(<몸무>-x1_mean)/x1_std]]})
print(mbi_hypothesis, sess.run(tf.argmax(mbi_hypothesis,1)))
 
-------------------------------------------------------------------------------
1108
[문제207] 0부터 143까지의 원소로 이루어진 12x12행렬을 만들고 4x4필터(단위행렬)를 이용해서 합성곱을 수행하세요. 단 스트라이드는 1입니다.

image=np.arange(0,144,dtype=np.float32).reshape(1,12,12,1)
plt.imshow(image.reshape(12,12),cmap=Greys)
print(image.shape)

weight = np.eye(4,4,dtype=np.float32).reshape(4,4,1,1)
print(weight.shape)

conv2d = tf.nn.conv2d(image,weight,strides=[1,1,1,1],padding='VALID')
conv2d_img = conv2d.eval()
conv2d_img
print(conv2d_img.shape)
#(1, 9, 9, 1)

conv2d_img=np.swapaxes(conv2d_img,0,3)
conv2d_img.shape

정답 :

a = np.arange(144).reshape(12,12)
filter = np.eye(4,4)

result = []
for r in range(len(a)-3):
    for c in range(len(a)-3):
        result.append(np.sum(a[rr+4,cc+4]*filter))
        
result = np.array(result).reshape(9,9)
print(result)

-------------------------------------------------------------------------------

[문제208] 0부터 15까지 원소로 이루어진 4x4행렬을 만들고 0부터 8까지의 원소로 이루어진 3x3필터를 이용해서 합성곱하는데 제로패딩을 이용해서 출력결과를 4x4로 출력하세요.
(단, 스트라이드는 1로 수행)

a = np.arange(16).reshape(4,4)
a_pad = np.pad(a,pad_width=1,mode='constant',constant_values=0)
filter = np.arange(9).reshape(3,3)

result = []
for r in range(len(a_pad)-2):
    for c in range(len(a_pad)-2):
        result.append(np.sum(a_pad[r:r+3,c:c+3]*filter))

result = np.array(result).reshape(4,4)
print(result)

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
