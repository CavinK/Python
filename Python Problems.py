# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:00:29 2018

@author: Cavin
"""

# [문제1] x,y 변수에 있는 값을 기준으로 수행한 결과 입니다. 
# x 와 y 변수에 어떤 값이 있어야 하나요.
# 또한 결과값이 나오기 위해서 어떤 계산식을 만들어야 하는지 계산식을 만들어 보세요.
'''
result_1 =  7 = x+y
result_2 =  3 = x-y
result_3 =  -3 = y-x
result_4 =  10 = x*y
result_5 =  0.4 = x/y
result_6 =  0 = y//x
result_7 =  2 = x//y
result_8 =  32 = y**x
result_9 =  7.0 = float(x+y) = y + y*x/y
result_10 =  -21 = y**y - x**y = (x+y) * (x-y)
result_11 =  50 = x**y*y
result_12 =  29 = x**y + y**y
'''
x = 5
y = 2

# [문제_2] v_str 변수에 이 문자열을 입력하세요. 
v_str = "시간은 멈추지 않습니다. 하루를 유익하게 살아야합니다."
# 1. "시간은 멈추지 않습니다." 만 출력해주세요
v_str[0:12]

# 2. "하루를 유익하게 살아야합니다." 만 출력해주세요
v_str[14:]

# 3. "살아야합니다."  만 출력해주세요
v_str[23:]

# 4. "시추니루하야"  이 글자만 출력해주세요.
v_str[::5]

# 5. "시간은 멈추지 않습니다. 하루를 유익하게" 만 출력해주세요.
v_str[:-8]

# 6. v_str 문자열을 뒤순으로 출력해 주세요.
v_str[::-1]

# [문제3] 
'''
>>> x = '파리썬'
>>> x
'파리썬'
'''
# 인덱스를 이용해서 리 -> 이로 변환하세요.
## Python은 R과는 달리 인덱싱 만으로는 글자 수정할 수 없음 
## 밑에 another solution처럼 일일이 인덱스값을 뽑아내거나, 
## 귀찮으면 문자 함수 사용! 
x = '파리썬'
x = list(x)
x
x[1] = '이'
x
x = "".join(x)
x

## Another solution 
x = x[0] + "이" + x[2]
x

# a = 'a b c d e f g' 변수에 문자열이 들어 있습니다. 다음을 수행하세요.

# [문제4] a 변수에 있는 문자의 갯수를  구하세요.
a = 'a b c d e f g'
len(a)

# [문제5] a 변수에 공백문자 갯수를 구하세요.
a.count(" ")

# [문제6] a 변수 안에 있는 공백문자를 제외한 갯수를 구하세요.
b = a.replace(" ","")
len(b)

# [문제7] a 변수에 있는 공백문자를 제거한 후 b 변수에 넣어주세요
b = a.replace(" ","")
b

# [문제8] a 변수에 있는 문자를 분리한 후 c 변수에 넣어주세요.
c = a.split(" ")
c

# [문제9] c 변수에 있는 문자를 합쳐서 자신의 변수에 다시 넣어주세요.
"".join(c)

# 아래와 같은 문자데이터가 있습니다. 
url = 'http://www.python.org'

# [문제10] http:// 제거한 후 url 변수에 넣어 주세요.
url = url.replace("http://","")
url

# [문제11] url변수에 있는 문자 데이터에 '.'을 기준으로 분리하세요.
url = url.split(".")

# [문제12] url변수에 있는 문자데이터를 www.python.org 모양으로 만드세요.
url = ".".join(url)

# [문제13] url변수에 있는 문자데이터를 대문자로 변환하세요.
url.upper()

# [문제14] url변수에 있는 문자데이터를 소문자로 변환하세요.
url.lower()

# [문제15] 반복문을 사용하지 않고  * 를 가로 100개 출력
star = "*"
star = star.center(100)
star = star.replace(" ","*")

# [문제16] 반복문을 사용하지 않고  * 를 세로 10개 출력
star = "*"
star = star.ljust(10)
star = star.replace(" ","\n*")
print(star)

# [문제17] day 변수에 20180905를 입력하세요. 화면 출력은 2018년 09월 05일 출력하세요.
day = "20180905"
day[0]
print("%s년 %s월 %s일" %(day[0:4], day[4:6], day[6:8]))

# food 변수 아래와 같이 데이터가 들어 있습니다.food변수를 생성하시고 문제를 풀어보세요.
'''
>>> food[0]
['김밥', '라면', '오뎅']
>>> food[1]
['비빔밥', '김치찌게']
>>> food[2]
['자장면', '짬뽕']
'''
# [문제18]  1번 index에 청국장 추가 하세요
food = [[],[],[]]
food[0] = ['김밥', '라면', '오뎅']
food[1] = ['비빔밥', '김치찌게']
food[2] = ['자장면', '짬뽕']
food[1].append('청국장')
food

# [문제19] 2번 index에 탕수육 추가하세요.
food[2].append('탕수육')
food

# [문제20] 0번 index에 있는 오뎅 삭제하세요.
food[0].pop()
food

# [문제21] 0번 index에 튀김, 튀김, 떡복이 한꺼번에 추가하세요
food[0].extend(['튀김', '튀김', '떡복이'])
food

# [문제22] 2번 index에 2번 위치에 유산슬 추가하세요
food[2].insert(2,'유산슬')
food

# [문제23] 튀김 갯수를 세어주세요
food[0].count('튀김')
food[1].count('튀김')
food[2].count('튀김')

# [문제24] 0번 index만 정렬해주세요
food[0].sort() ### food.sort() <- 이렇게 하면 요소 정렬이 안 됨! (중첩 리스트가 있을 때는 주의!) 
food

# [문제25] 0번 index에 마지막 데이터 삭제하세요
food[0].pop()
food

len(food) ### 중첩된 리스트를 하나로 봐서 계산! 
len(food[0]) ### 요소 번호를 써줘야 제대로 된 숫자를 파악하는 게 가능! 

# [문제26] 숫자를 입력값으로 받아서 짝수인지 홀수인지를 출력하는 프로그램을 만드세요.
num = int(input("숫자를 입력하세요: "))
if (num % 2) == 0:
   print("{}는 짝수입니다" .format(num))
else:
   print("{}는 홀수입니다" .format(num))

# [문제27] 한글, alphabet만 입력받아야 합니다. 
# 만약에 다른 문자가 들어 오면 "한글, alphabet 이외의 문자가 포함되어 있습니다." 
# 라는 문구가 출력해야 하고 아니면 입력받은 문자를 출력하세요.
alp = input("문자를 입력하세요: ")
if (alp.isalpha()) == 0:
   print("한글, alphabet 이외의 문자가 포함되어 있습니다.") ### 공백문자 있으면 False가 됨! 
else:
   print(alp)

# [문제28] 숫자를 입력값으로 받습니다. 
# 만약 숫자가 이외의 값이 들어 오면 "숫자 이외의 문자가 포함되어 있습니다." 아니면 숫자 출력하세요.
nume = input("숫자를 입력하세요: ")
if (nume.isnumeric()) == 0:
   print("숫자 이외의 문자가 포함되어 있습니다.")
else:
   print(nume)

# [문제29] 1부터 100까지 합을 구하세요 
num = 100
sum = 0
while(num > 0):
       sum += num
       num -= 1 ### 카운트 변수를 따로 설정해야 함! 
print("The sum is", sum)

# [문제30] 단을 입력값으로 받아서 구구단을 출력하세요.
num = int(input("숫자를 입력하세요: "))
for i in range(1, 10):
   print(num,'x',i,'=',num*i)

num = int(input("숫자를 입력하세요: "))
i = 1
while(i < 10):
       print(num,'x',i,'=',num*i)
       i += 1 ### 카운트 변수를 따로 설정해야 함! 
       
for i in range(1, 10):
    for num in range(1, 10):
        print(i,'x',num,'=',num*i)

# [문제30] 1부터 100까지의 3의 배수를 출력, 합을 구하세요. while문을 이용하세요.
sum3 = 0
i = 0
while i <= 100:
    i += 1
    if i % 3 != 0: 
        continue
    print(i)
    sum3 += i
print(sum3)

# [문제31] 조건이 없는 상태에서 1부터 10까지 3,5를 제외한 합을 구하세요.
# continue문, break문을 이용하세요.
sum35 = 0
i = 0
while 1:
    i += 1
    if i > 10: ### 이 부분을 while 조건문으로 넣으면 같은 결과 나옴! 
        break
    if i == 5 or i == 3:
        continue
    sum35 += i
print(sum35)

# [문제32] 리스트 변수에 18,2,3,1,4,5,7,8,9,10,11,15,16 값이 들어 있습니다. 짝수만 합을 구하세요.
a = [18,2,3,1,4,5,7,8,9,10,11,15,16]
suma = 0
i = -1
while 1:
    i += 1
    if i > len(a)-1:
        break
    if a[i] % 2 == 0:
        suma += a[i]
    else:
        continue
print(suma)

# [문제33] 구구단을 생성하세요
num = 2
i = 1
while(num < 10):
    print("-- ",num,"단"," --")
    while(i < 10):
       print(num,'x',i,'=',num*i)
       i += 1
    num += 1
    i = 0

# [문제34] 리스트 변수에 12,3,21,4,5,7,33,2,18,9,10,31,15,16 값이 들어 있습니다. 최대값을 구하세요.
numbers = [12,3,21,4,5,7,33,2,18,9,10,31,15,16]
x = 0
lar = numbers[x]
while x < len(numbers):
  if numbers[x] > lar:
    lar = numbers[x]
  x = x+1
print(lar)

# [문제35] 리스트 변수에 12,3,21,4,5,7,33,2,18,9,10,31,15,16 값이 들어 있습니다. 최소값을 구하세요.
numbers = [12,3,21,4,5,7,33,2,18,9,10,31,15,16]
x = 0
sma = numbers[x]
while x < len(numbers):
  if numbers[x] < sma:
    sma = numbers[x]
  x = x+1
print(sma)

# [문제36] 학생들의 점수가 90,55,63,78,80 점이 있습니다.
# 60점 이상이면 합격, 60점 미만이면 불합격 출력해 주세요.
stu = [90,55,63,78,80]
for i in range(0,len(stu)):
    if stu[i] >= 60:
        print("합격")
    else:
        print("불합격")

# [문제37] 1부터 100까지 합을 구하세요.(for 이용)
sum100 = 0
for i in range(1,101):
    sum100 += i
print(sum100)

# [문제38] 1부터 10까지 출력하세요. 단 4, 8은 제외(for 이용)
for i in range(1,11):
    if i == 4 or i == 8:
        continue
    print(i)

# [문제39] 화면과 같이 출력하세요.(for 이용)
'''
가로의 숫자를 입력하세요 : 5
세로의 숫자를 입력하세요 : 5
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
'''
srow = int(input("가로의 숫자를 입력하세요 : "))
scol = int(input("세로의 숫자를 입력하세요 : "))
for i in range(0, scol):
    print("★ "*srow)

# [문제40] 구구단을 출력하세요.(for 이용)
for i in range(2, 10):
    for num in range(1, 10):
        print(i,'x',num,'=',num*i)

# [문제41] 구구단을 만드세요. 
# 2단에서 9단까지만 입력하세요, [0은 구구단 전부를 출력합니다.]: 
mul = int(input("숫자를 입력하세요 : "))
if mul == 0:
    for i in range(2, 10):
        for num in range(1, 10):
            print(i,'x',num,'=',num*i)
else:
    for num in range(1, 10):
        print(mul,'x',num,'=',mul*num)

# [문제42]lst 변수에 a,b,c,d값이 있습니다. for문을 이용하여 아래화면과 같이 출력하세요.
'''
0번 a값이 있습니다.
1번 b값이 있습니다.
2번 c값이 있습니다.
3번 d값이 있습니다.
'''
lst = ['a','b','c','d']
for i in range(0,len(lst)):
    print(i,"번",lst[i],"값이 있습니다.")

# [문제43] 1부터 9까지 x 리스트 변수에 입력하세요.
# y변수는 x 변수의 값을 2곱한 값으로 입력해주세요. 
x=list(range(1,10))
y=[]
for i,name in enumerate(x):
    y.insert(i,name*2)
print(y)

## 리스트 표현식 
z = [i*2 for i in x] 
z

# [문제44] apple, banana, orange 리스트 변수에 값을 입력하시고
# 이 값들의 길이를 출력해주세요.
fruit = [ 'apple', 'banana', 'orange']
list(enumerate(fruit))
for i,name in enumerate(fruit):
    print("The length of ",name," is ",len(fruit[i]))

f = [len(fruit[i]) for i,name in enumerate(fruit)]
f

# [문제45] 변수에 아래와 같이 들어 있습니다. 아래처럼 결과를 출력하세요.
'''
lst1 = [1,2,3]
lst2 = [4,5,6]
출력결과
[4, 5, 6, 8, 10, 12, 12, 15, 18]
'''
lst1 = [1,2,3]
lst2 = [4,5,6]

y = []
for i,name in enumerate(lst2):
    for j,name2 in enumerate(lst1):
        y.insert(j,name*name2)
print(y)

for x in lst1:
    for y in lst2:
        print(x*y, end = ',') ### 세로로 나열된 리스트를 가로로 바꿔줌!! 

lst3 = []
for x in lst1:
    for y in lst2:
        lst3.append(x*y)
print(lst3)

l = [x*y for x in lst1 for y in lst2] ### for문에 있는 변수들을 표현식에 씀! 
l

# [문제46] 1부터 100까지 값 중에 짝수만 x변수에 입력해주세요 
x = []
for i in range(1,101):
    if i%2 == 0:
        x.append(i)
        
e = [i for i in range(1,101) if i%2 == 0] ### append()를 이렇게도 표현 가능! 
print(e, end=',')

# [문제47] 튜플변수에 사과, 귤, 오렌지, 배, 포도, 바나나, 자몽, 키위, 딸기, 블루베리, 망고를 입력하시고 
# 과일이름중에 세글자 이상인 과일만  fruit_lst변수에 입력해주세요.
t = ('사과', '귤', '오렌지', '배', '포도', '바나나', '자몽', '키위', '딸기', '블루베리', '망고')
t2 = [len(t[i]) for i,name in enumerate(t)]
t2
fruit_lst = [t[i] for i in range(1,11) if len(t[i]) >= 3]
fruit_lst

fruits=('사과','귤','오렌지','배','포도','바나나','자몽','키위','딸기','블루베리','망고')
fruits_lst=[]
for i in fruits:
    if len(name)>=3:
        fruits_lst.append(i)
print(fruits_lst)

# [문제48] 과일판매 현황을 dictionary 변수로 생성하세요. 과일 이름을 키로 하고 수량은 값으로 표현한후
# 과일이름만 대문자로 출력해주세요. 
sale = {'apple':100 , 'banana':300 , 'orange':300}
sale['apple']
sale_key = list(sale.keys())
sale_key[1].capitalize()
sale_lst = [sale_key[i].capitalize() for i in range(0,3)]
sale_lst

dic = {'apple':100 , 'banana':300 , 'orange':300}
for i in dic.keys():
    print(i.upper(), end=',')
for i,v in dic.items():
    print(i.upper()+':'+str(v), end=',\0') ### 변수명.items()는 2개(key, value) 리턴 -> for문 쓸 때 두 변수 사용! 

[i.upper() for i in dic.keys()]
[[i.upper(), v] for i,v in dic.items()]

# [문제49] 함수에 두개의 숫자를 입력값으로 받아서 값을 비교하는 함수를 생성하세요 
def compare(x,y):
    if x>y:
        print(x," is bigger")
    elif y>x:
        print(y," is bigger")
    else:
        print(x," is equal to ",y)
compare(5,10)

# [문제50] 두 인수값을 받아서 합한 값을 리턴해주는 sum함수를 생성하세요.
def sum(x,y):
    print(x+y)
def sum(x,y):
    return x+y
sum(1,2) ### 1,2 <- 실질매개변수 // x,y <- 형식매개변수 

def sum(*x): ### 가변인수값 ->  for문 사용! 
    sum0 = 0
    for i in x:
        sum0 += i
    print(sum0)
sum(1,2,3,4,5)

def sum(*x): 
    sum0 = 0
    for i in x:
        sum0 += i
    return sum0 
z = sum(1,2,3,4,5)
print(z)
sum(1,2,3)

# [문제51] 
cal("sum",1,2,3,4) ### 크게 보면 2개의 인수라 생각! 
cal("mul",1,2,3,4,5)
cal("SUM",1,2,3,4,5)

def cal(arg1,*x):
    sum0 = 0
    mul0 = 1
    if arg1 == "sum": ### 변수명.lower() 함수를 사용하는 방법도 생각! 
        for i in x:
            sum0 += i
        print(sum0)
    elif arg1 == "mul":
        for i in x:
            mul0 *= i
        print(mul0)
    else:
        print("The first argument must be 'sum' or 'mul' only")

def cal(arg1,*x):
    sum0 = 0
    mul0 = 1
    if arg1.lower() == "sum": 
        for i in x:
            sum0 += i
        print(sum0)
    elif arg1.lower() == "mul":
        for i in x:
            mul0 *= i
        print(mul0)
    else:
        print("The first argument must be 'sum' or 'mul' only")

# [문제52] 여러 숫자를 인수값으로 받아서 합과 평균을 출력하는 aggF함수를 생성하세요.
'''
aggF(1,2,3,4,5,6,7,8,9,10)
  
합 :  55
평균 : 5.5 
'''
def aggF(*x):
    sum0 = 0
    for i in x:
        sum0 += i
    print("합 : ",sum0)
    print("평균 : ",sum0/len(x))
aggF(1,2,3,4,5,6,7,8,9,10)

def aggF(*x):
    hap=0
    avg=0
    for i in x:
        hap+=i
        avg=hap/len(x)
    return '합: %d \n평균: %d'%(hap,avg)

z = aggF(1,2,3,4,5)
print(z)

def aggF(*x):
    hap=0
    avg=0
    for i in x:
        hap+=i
        avg=hap/len(x)
    print('합: %d' %(hap), '평균: %0.2f' %(avg)) ### %0.2f: 소수점 2자리 
    return hap, avg
add, mult = aggF(1,2,3,4,5)
print(add, mult)

# [문제53] 입력값을 누적해서 더하는 함수를 작성하세요.
'''
>>> print(add(2))
2

>>> print(add(8))
10
'''
sum0 = 0
def add(x):
    global sum0
    sum0 += x
    print(sum0)
add(2)
add(10)

sum0 = 0
def add(x):
    global sum0
    sum0 += x
    return sum0
print(add(2))
print(add(10))

# [문제54] 아래와 같이 변수에 값이 들어 있습니다. 
# exchang 함수에 x변수에 값을 넣으면 y로 변환하는 함수를 만드세요.
x = ["귀도","반","로섬"]
y = ["Guido","van", "Rossum"]

def exchang(*args):
    print(y)   
exchang(x)

def exchang(x):
    x = x[:] ### 이거 없으면, x변수의 내용도 바뀜! 
    for i in range(len(x)):
        x[i] = y[i]
    print(x)
print(x)
print(y)
exchang(x)

# [문제55]약수를 구하는 divisor 함수를 생성하세요.
'''
1이상의 숫자를 입력하세요: 100
[100, 50, 25, 20, 10, 5, 4, 2, 1]
'''
def divisor():
    n = int(input("1이상의 숫자를 입력하세요: "))
    i = 1
    list = []
    while i <= n:
        if n % i == 0:
            list.append(i)
        i = i + 1
    list.sort(reverse = True)
    return list
divisor()

## Another solution 
print("어떤 정수를 나누어 떨어지게 하는, 0이 아닌 정수이다. 음의 정수도 약수가 되지만 일반적으로 양의 약수만 다룬다")

num1 = int(input("1이상의 숫자를 입력하세요: ") )
def divisor(num1):
    for i in range(1,num1+1):
        if(num1%i == 0):
            print(i,end=" ")          
divisor(num1)

num1 = int(input("1이상의 숫자를 입력하세요: "))
def divisor(num1):
    num2 = int(num1/2) ### 편의상 반으로 나눠서 약수들을 구함 
    num3 = []
    num3.append(num1)
    while num2 >= 1:
        if num1 % num2 == 0:
            num3.append(num2)
        num2 -= 1
    return(sorted(num3)) ### return(sorted(num3,reverse=False))
print(divisor(num1))

# [문제56] 여러 값을 동일한 변수에 순차적으로 저장할수 있는 용도의 변수 타입과 부호는 ?
## list []

# [문제57] x 리스트 변수에 1, 3, 5, 7, 9 를 입력하세요
x = [1,3,5,7,9]

# [문제58] x 변수에 타입을 확인하세요.
type(x)

# [문제59] x변수에 첫번째값을 확인해주세요
x[0]

# [문제60] x변수에 제일뒤에 값을 확인해주세요
x[-1] 

# [문제61] x변수에 10를 제일 뒤에 추가해주세요.
x.append(10)

# [문제62] x변수에 있는 값들중에 10을 삭제해주세요
x.pop(-1)

# [문제63] x변수에 1번색인위치에 2를 입력하세요.
x.insert(1,2)

# [문제64] x변수에 1번색인값을 제거해주세요.
x.pop(1)

# [문제65] x 변수에 첫번째 부터  세번째까지 값을 출력해주세요.
x[0:3]   

# [문제66] x 변수에 제일뒤에서 두개 값을 출력해주세요.
x[-2:]

# [문제67] x 변수를 y변수에 대입한 후 y변수에 11을 추가한 후 x값도 확인 한 후 분석해주세요.
y = x
print(id(x), id(y))
y.append(11)
x
y
## 둘 다 바뀜! 

# [문제68] x변수를 z변수에 복사하지만 고유한 변수로 생성해주시고 z변수에 13을 추가 해주세요.
z = x[:]
print(id(x), id(z))
z.append(13)
x
z
## 원본에 영향 안 줌! 

# [문제69] 
    x = [1,2,3]
    y = [4,5,6]
#   y변수에 값을 x 변수에 넣어주세요.
x.append(y) ### 중첩 리스트 
x.extend(y) ### 두 리스트를 하나로 합침 

# [문제70] x 변수에 1번 인덱스의 값을 제거해주세요.
x.pop(1)
x

# [문제71] x변수에 1번 부터 3번 인덱스를 제거해주세요.
del x[1:4]

# [문제72] 중첩리스트를 이용할때 첫번째 항목의 첫번째 항목의 값을 추출해주세요.
x[-1][0]

# [문제73] 리스트형과 비슷하지만 요소의 값을 변경 할 수 없는 타입과 부호는 ?
## tuple ()
    
# [문제74] 키, 값을 저장하는 데이터 타입과 부호는 ?
## dictionary {}
    
# [문제75]  아래와 같은 내용을 변수에 입력해주세요. 변수이름은 dict
'''
           이름 : '홍길동'
           나이 : 30
           직업 : '파이썬개발자'
'''           
dict = {"이름":"홍길동", "나이":30, "직업":"파이썬개발자"}
  
# [문제76] dict변수 키를 출력하세요.
dict.keys()  

# [문제77] dict변수 값을 출력하세요.
dict.values()

# [문제78] dict변수의 키, 값을 출력해주세요.
dict.items()

# [문제79] dict변수의 이름만 출력해주세요.
dict["이름"]

# [문제80] dict변수의 주소 = '서울' 추가해주세요
dict["주소"] = "서울"
    
# [문제81]  dict변수의 나이값을 32 수정하세요.
dict["나이"] = 32

## factorial 공리: n * factorial(n-1) if n>=1
## factorial(n) = 1 if n=0
def fact(n):
    if n == 1 or n <= 0:
        return 1
    else:
        return n * fact(n-1) ### if문 제대로 안 써주면 무한루프! 
                             ### stack 구조 <- fact()에서 계속 숫자 뽑아 쌓아놓음 
                             ### 5 * fact(4) <- fact(4)의 값을 당장은 모름 => "5 * fact(4)"를 stack algorithm에 쌓아놓음 => 쭉 쌓아놓은 다음, fact(1)을 알게 되면, 하나씩 pop해서 쭉 계산! 
fact(5)

def fact_loop(n):
    mul1 = 1
    if n == 1 or n <= 0:
        return 1
    else:
        for i in range(n,1,-1):
            mul1 *= i
        return mul1
fact_loop(5)

## 최대공약수, 최소공배수
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm
num1 = 54
num2 = 24

# [문제83] stddev(2,3,1,7) 표준편차를 구하세요. stddev함수를 생성하세요.
'''
평균 = 관측값의 합 / 데이터수
편차 = 관측값 - 평균
편차 제곱합 = (편차**2)+(편차**2)
분산 = 편차제곱합/데이터수(자유도)
표준편차 = math.sqrt(분산)

import math
math.sqrt(분산)
'''
import math
x = [2,3,1,7]
mean = sum(x)/len(x)
var = sum(pow(i-mean,2) for i in x) / len(x)    
std = math.sqrt(var)
std

def stddev(*x):
    lstx = [i for i in x] 
    mean = sum(x)/len(x)
    var = sum(pow(i-mean,2) for i in x) / len(x)    
    std = math.sqrt(var)
    return std

stddev(2,3,1,7)

import math   
def stddev(*x):
    global hap ### 전체 합 
    hap=0
    global mean ### 전체 평균 
    mean=0
    for i in x:
        hap+=i
        mean=hap/len(x)
    global e ### 편차
    e=[x[i]-mean for i in range(0,len(x))]
    global ee ### 편차 제곱합 
    ee=0
    for i in range(0,len(x)):
        ee+=e[i]**2
    global var ### 분산 
    var=ee/(len(x)-1)
    global sd ### 표준 편차 
    sd=math.sqrt(var)
    return sd

## Another solution 
### 메소드 안에 메소드 정의 가능! 
import math
def stddev(*arg):
    def mean():
        return sum(arg)/len(arg)
    
    def variance(m):
        total = 0
        for i in arg:
            total += (i-m)**2
        return total/(len(arg)-1)
    v = variance(mean())
    return math.sqrt(v)
stddev(2,3,1,7)

## 오브젝트 단위로 만드는 방법 
### 일일히 copy & paste하지 않고, 따로 저장해놓음! 
### c:\python\stddev.py 
### import math의 math도 py 파일로 저장되어 있는 거 
### import stddev로 사용하려면, path를 걸어야 함! 
import sys
sys.path 
sys.path.append('c:\\python')

## import 모듈이름 
### 모듈이름.메소드이름() 
import stddev
dir()
stddev.stddev(2,3,1,7)
stddev.var
stddev.mean

## from 메소드 import *: 메소드만 따로 가져옴 
from stddev import * 
stddev(2,3,1,7)

# [문제84] stats 모듈에 평균, 분산, 표준편차함수를 사용할수 있는 프로그램을 생성하세요.
'''
>>> import stats
>>> stats.mean(1,2,3,4,5)
3.0
>>> stats.variance(1,2,3,4,5)
2.5
>>> stats.stddev(1,2,3,4,5)
1.5811388300841898
'''
import stats
stats.mean(1,2,3,4,5)
stats.variance(1,2,3,4,5)
stats.stddev(1,2,3,4,5)

# [문제85] 프로그램을 생성하세요.
'''
액수입력 : 362
화폐단위를 입력하세요 : 100 50 1
1원 : 12개
50원 : 1개
100원 : 3개
'''
def coin():
    num = int(input("액수입력 : "))
    cur = input("화폐단위를 입력하세요 : ")
    cur_int = [int(i) for i in cur.split(' ')]
    cur_int.sort(reverse = True)
    
    for i in range(0,len(cur_int)):
        count = num//cur_int[i]
        print(cur_int[i],"원 :",count,"개")
        num -= count * cur_int[i]
    
coin()

## Other solutions 
def coinGreedy(money, cash_type):
    cash_type.sort(reverse=True)  
    remain = money 
    res = {}  
    for cash in cash_type:
        dvmd = divmod(remain,cash)
        res[cash] = dvmd[0]
        remain = dvmd[1] 
    return res

money = int(input('액수입력 : '))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
res = coinGreedy(money,cash_type)
for k,v in res.items():
    print('{0}원 : {1}개'.format(k,v))

### sorted(): 정렬에 대한 미리보기 
### key=operator.itemgetter(0) 옵션 <- operator 모듈을 불러와야 함! 
import operator

for k,v in sorted(res.items(), key=operator.itemgetter(0)): ### key=operator.itemgetter(0): dictionary 안의 key를 기준으로 오름차순 정렬 
    print('{0}원 : {1}개'.format(k,v))

for k,v in sorted(res.items(), key=operator.itemgetter(1)): ### key=operator.itemgetter(1): dictionary 안의 value를 기준으로 오름차순 정렬 
    print('{0}원 : {1}개'.format(k,v))

for k,v in sorted(res.items(), key=operator.itemgetter(0), reverse=True): ### key를 기준으로 내림차순 
    print('{0}원 : {1}개'.format(k,v))

for k,v in sorted(res.items(), key=operator.itemgetter(1), reverse=True): ### value를 기준으로 내림차순 
    print('{0}원 : {1}개'.format(k,v))

# [문제86] 숫자를 입력값으로 받은 후 짝수인지 홀수 인지를 출력한후 그 숫자값을 기준으로
# 짝수면 짝수형식의 증가값으로 10개 출력, 홀수면 홀수형식의 증가값으로 10개 출력합니다.
# 만약에 숫자가 들어 오지 않으면 예외사항처리하세요.
'''
숫자를 입력해주세요 : 10
짝수
10
12
14
16
18
20
22
24
26
28
>>> 

숫자를 입력해주세요 : 11
홀수
11
13
15
17
19
21
23
25
27
29

숫자를 입력해주세요 : 이십
invalid literal for int() with base 10: '이십'
숫자를 입력하세요
'''
def evenodd():
    try:
        dig = int(input("숫자를 입력해주세요 : "))
        if dig%2 == 0:
            print("짝수")
            for i in range(1,10):
                dig += 2
                print(dig)
        elif dig%2 != 0:
            print("홀수")
            for i in range(1,10):
                dig += 2
                print(dig)
        else:
            raise Exception(dig) ### User가 발생시키는 exception <- 앞으로 일어날 오류가 뭔지 모르는 경우 사용! 
    except Exception as error:
        print(error)
        return evenodd() ### 재귀 호출 써서 계속 숫자 입력하게 유도! 
evenodd()

# [문제87] 오늘이 무슨 요일인지 출력해주세요 
days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
days[datetime.datetime.now().weekday()]

def weekdays():
    n = datetime.datetime.now().weekday()
    if n == 0:
        print("월요일")
    elif n == 1:
        print("화요일")
    elif n == 2:
        print("수요일")
    elif n == 3:
        print("목요일")
    elif n == 4:
        print("금요일")
    elif n == 5:
        print("토요일")
    elif n == 6:
        print("일요일")
weekdays()

# [문제88] 함수에 인수 값으로 현재 날짜, 일 수 정보를 입력 받아서 더 한 날짜 정보를 리턴하는 next_day 함수를 생성하세요. 
def next_day(x,y):
    x = datetime.datetime.strptime(x, "%Y-%m-%d")
    return datetime.datetime(int(x.strftime('%Y')),int(x.strftime('%m')),int(x.strftime('%d'))) + datetime.timedelta(days = y)
next_day("2018-09-01",100)

def next_day():
    x = datetime.datetime.strptime(input("날짜 입력하세요(yyyy-mm-dd): "), "%Y-%m-%d")
    y = int(input("일 수 입력하세요: "))
    return datetime.datetime(int(x.strftime('%Y')),int(x.strftime('%m')),int(x.strftime('%d'))) + datetime.timedelta(days = y)
next_day()

# [문제89] 아래와 같은 결과가 출력될수 있도록 프로그램을 생성하세요
''' 
1에서 천만까지 짝수합, 홀수합 구합니다
1에서 천만까지 짝수합: 24999995000000
1에서 천만까지 홀수합: 25000000000000
처리시간 : 0:00:01.950003
처리시간 millisecond(1/1000)  : 1950ms
'''
def interval():
    start = datetime.datetime.now()
    print("1에서 천만까지 짝수합, 홀수합 구합니다")
    even = 0
    odd = 0
    for i in range(1,10000000):
        if i%2==0:
            even += i
        else: 
            odd += i
    print("1에서 천만까지 짝수합: ", even)
    print("1에서 천만까지 홀수합: ", odd)
    end = datetime.datetime.now()
    delta = end - start
    print("처리시간 : ", delta)
    print("처리시간 millisecond(1/1000)  : ", int(delta.total_seconds()*1000),"ms")
interval()

## Another solution 
from datetime import datetime ### 불필요하게 모듈 이름을 계속 적을 필요 없음! 
start = datetime.now()
print('1에서 천만까지 짝수합, 홀수합 구합니다')
even_result = 0
odd_result = 0
for i in range(10000000):
    if i % 2 == 0:
        even_result += i
    else:
        odd_result += i
print('1에서 천만까지 짝수합: %d'%even_result)
print('1에서 천만까지 홀수합: %d'%odd_result)
end = datetime.now()
delta = end - start
print("처리시간 : ",delta)
delta_ms = int(delta.total_seconds() * 1000)
print("처리시간 millisecond(1/1000)  : %dms"%delta_ms)

# [문제90] last_name, salary 출력해주세요 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list) ### commission_pct의 경우, null값은 ''로 표현됨 

next(emp_csv) ### 첫 행(컬럼명)은 skip하고 다음행부터 불러들임 
for emp_list in emp_csv:
    print(emp_list[2], emp_list[7])

# [문제91] last_name, last_name 길이를 출력해주세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    print(emp_list[2], len(emp_list[2]))

# [문제92] employee_id, last_name, salary*12 달 곱한 값을 출력해주세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    print(emp_list[0], emp_list[2], int(emp_list[7])*12) ### 소수점이 붙는 경우에는 float()을 씌워줌! 

# [문제93] last_name, commission_pct를 출력하는데 commission_pct값이 ''이면 0으로 출력해주세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    if emp_list[-3] == '':
        emp_list[-3] = 0
    print(emp_list[2], emp_list[-3])

# [문제94] last_name을 대문자로, job_id를 소문자로 출력해주세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    print(emp_list[2].upper(), emp_list[-5].lower())

# [문제95] last_name을 첫글자만 추출해서 소문자로 출력해주세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    emp_join = ''.join(emp_list[2])
    print(emp_join[0].lower())

# [문제96] last_name을 두번째부터 마지막까지만 추출해서 대문자로 출력해주세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    emp_join = ''.join(emp_list[2])
    print(emp_join[1:].upper())

# [문제97] 이름을 입력하면 첫글자는 대문자, 나머지 문자는 소문자를 출력하는 initcap 함수를 이용해서 이름을 출력하세요. 
def initcap(x):
    return x.lower().replace(x.lower()[0],x.lower()[0].upper())
initcap('cavin')
initcap('CAVIN')

def initcap(x):
    return x[0].upper() + x[1:].lower()

# [문제98] 이름을 입력하면 제일 뒤에 있는 철자는 대문자, 앞의 문자는 소문자로 출력하는 tailcap 함수를 생성하세요. 
def tailcap(x):
    return x.lower().replace(x.lower()[-1],x.lower()[-1].upper())
tailcap('cavin')

def tailcap(x):
    return x[:-1].lower() + x[-1].upper()

# [문제99] 이름과 급여를 출력하는데 급여를 출력할 때에 0 대신 *를 출력하세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    print(emp_list[2], emp_list[7].replace('0','*'))

# [문제100] 이름, salary * 12 + commission_pct 결과를 출력해주세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    if emp_list[-3] == '':
        emp_list[-3] = 0
    print(emp_list[2], float(emp_list[7]) * 12 + float(emp_list[-3]))

# [문제101] 이름, 입사한 요일(한글)을 출력해주세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 

import datetime
day = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
for emp_list in emp_csv:
    print(emp_list[2], day[datetime.datetime.strptime(emp_list[5], "%Y%m%d").weekday()])

# [문제102] 이름, 입사한 날짜부터 오늘까지 총 몇 일 근무했는지 출력하세요.
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 

import datetime
for emp_list in emp_csv:
    d = datetime.date.today() - datetime.datetime.strptime(emp_list[5], "%Y%m%d").date() ### datetime.datetime.now()를 쓰면 더 편하게 만들 수 있음! 
    print(emp_list[2], d.days) ### 변수명.days <- 일 수만 뽑아냄! 

# [문제103] 오늘 부터 이번달 말일까지 몇일 남았는지 출력하세요.
calendar.monthrange(datetime.date.today().year,datetime.date.today().month)[1] - datetime.date.today().day
calendar.monthrange(datetime.date.today().year,datetime.date.today().month)

# [문제104] 사원번호가 100번 사원의 사원이름과 급여를 출력하세요.
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    if emp_list[0] == "100":
        print(emp_list[2], emp_list[7])

# [문제105] 급여가 10000 이상인 사원들의 이름과 급여를 출력하세요.
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    if int(emp_list[7]) >= 10000:
        print(emp_list[2], emp_list[7])

# [문제106] 2001-01-13일에 입사한 사원의 이름과 입사일을 출력하세요
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    if int(emp_list[5]) == 20010113:
        print(emp_list[2], emp_list[7])

# [문제107] 2002 년도에 입사한 사원들의 이름과 입사일을 출력하세요.
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 

import datetime
for emp_list in emp_csv:
    if datetime.datetime.strptime(emp_list[5], "%Y%m%d").year == 2002: ### .year로 하면 숫자로 리턴! 
        print(emp_list[2], "{}-{}-{}" .format(emp_list[5][:4],emp_list[5][4:6],emp_list[5][6:8]))

# [문제108] job이 ST_CLERK 이고 월급 3000 이상인 사원들의 이름과 job, 급여 출력하세요
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    if emp_list[-5].upper() == "ST_CLERK" and int(emp_list[-4]) >= 3000:
        print(emp_list[2], emp_list[-5], emp_list[7])

# [문제109] 급여가 2500 에서 3000 사이인 사원들의 이름과 급여를 출력하세요
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    if int(emp_list[-4]) >= 2500 and int(emp_list[-4]) <= 3000:
        print(emp_list[2], emp_list[7])

# [문제110] job AD_VP , AD_PRES 인 사원들의 이름과 월급과 직업을 출력하세요
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
cnt = 0 
for emp_list in emp_csv:
    if emp_list[-5].upper() == "AD_VP" or emp_list[-5].upper() == "AD_PRES": ### not in ["AD_VP","AD_PRES"] <- 이렇게 써도 됨 
        print(emp_list[2], emp_list[-5], emp_list[7])
        cnt += 1
print(cnt,"건이 출력되었습니다")

# [문제111] 직업이 AD_VP , AD_PRES 이 아닌 사원들의 이름과 월급과 직업을 출력하세요
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
cnt = 0
for emp_list in emp_csv:
    if emp_list[-5].upper() != "AD_VP" and emp_list[-5].upper() != "AD_PRES":
        print(emp_list[2], emp_list[-5], emp_list[7])
        cnt += 1
print(cnt,"건이 출력되었습니다")

# [문제112] 커미션이 null 인 사원의 이름, 급여, 커미션을 출력하세요.
# 전체 인원수, 커미션 null의 수, 비율도 출력하세요.
import csv
import math
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
cnt_total = 0
cnt = 0
for emp_list in emp_csv:
    cnt_total += 1
    if emp_list[-3] == "":
        print(emp_list[2], emp_list[7], emp_list[-3])
        cnt += 1
print("전체 인원 수: ",cnt_total)
print("커미션 null의 수: ",cnt)
print("비율: ", round(cnt/cnt_total*100,2), "%") ### round(): 기본으로 내장되어 있는 메소드(import math 할 필요 없음!)

# [문제113]커미션이 null 이 아닌 사원들의 이름,급여,커미션을 출력하세요.
# 전체 인원수, 커미션 null의 수, 비율도 출력하세요.
import csv
import math
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
cnt_total = 0
cnt = 0
for emp_list in emp_csv:
    cnt_total += 1
    if emp_list[-3] != "":
        print(emp_list[2], emp_list[7], emp_list[-3])
        cnt += 1
print("전체 인원 수: ",cnt_total)
print("커미션 null의 수: ",cnt)
print("비율: ", round(cnt/cnt_total*100,2), "%")

# [문제114] last_name의 첫번째 철자가 S 로 시작하는 사원들의 이름과 급여를 출력하세요.
# 전체 인원수, 커미션 null의 수, 비율도 출력하세요.
import csv
import math
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
cnt_total = 0
cnt = 0
for emp_list in emp_csv:
    cnt_total += 1
    if emp_list[2][0].upper() == "S":
        print(emp_list[2], emp_list[7])
        cnt += 1
print("전체 인원 수: ",cnt_total)
print("첫번째 철자가 S 로 시작하는 사원의 수: ",cnt)
print("비율: ", round(cnt/cnt_total*100,2), "%")

# [문제115] last_name의 두번째 철자가 i 인 사원들의 이름과 월급을 출력하세요. 
# 전체 인원수, 커미션 null의 수, 비율도 출력하세요.
import csv
import math
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
cnt_total = 0
cnt = 0
for emp_list in emp_csv:
    cnt_total += 1
    if emp_list[2][1].lower() == "i":
        print(emp_list[2], emp_list[7])
        cnt += 1
print("전체 인원 수: ",cnt_total)
print("두번째 철자가 i 인 사원의 수: ",cnt)
print("비율: ", round(cnt/cnt_total*100,2), "%")

# [문제116] 50번부서 사원들의 이름, 급여 출력하는데 이름을 오름차순으로 출력하세요. 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
lst = [emp_list[2] + " " + emp_list[7] for emp_list in emp_csv if emp_list[-1] == "50"]
lst.sort()
len(lst)

for i in range(0,len(lst)):
    print(lst[i].split(" ")[0],lst[i].split(" ")[1])

## Other solutions
import csv
def sortCheck(data):
    return (data[2])

file = open('c:/data/emp.csv','r')
emp_csv=csv.reader(file)
next(emp_csv)
emp_list = []
for i in emp_csv:
    if i[10] == '50':
        emp_list.append(i)
        
emp_list_sorted = sorted(emp_list,reverse=False,key=sortCheck)

for i in emp_list_sorted:
    print(i[2],i[-4])

### lambda 함수 사용 
import csv
file = open('c:/data/emp.csv','r')
emp_csv=csv.reader(file)
next(emp_csv)
emp_list = []
for i in emp_csv:
    if i[10] == '50':
        emp_list.append(i)
        
emp_list_sorted = sorted(emp_list,reverse=False,key= (lambda data: data[2]))

for i in emp_list_sorted:
    print(i[2],i[-4])

# [문제117] job이 ST_CLERK인 사원들의 이름과 입사일과 job을 출력하는데 가장 최근에 입사한 사원부터 출력하세요.
import csv
def sortCheck(data):
    return (data[5])

file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 

emp_list = []
for i in emp_csv:
    if i[-5].upper() == "ST_CLERK":
        emp_list.append(i)

emp_list_sorted = sorted(emp_list,reverse=True,key=sortCheck)

for i in emp_list_sorted:
    print(i[2],i[5],i[6])

### lambda 함수 사용 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 

emp_list = []
for i in emp_csv:
    if i[-5].upper() == "ST_CLERK":
        emp_list.append(i)

emp_list_sorted = sorted(emp_list,reverse=True,key=(lambda data: data[5]))

for i in emp_list_sorted:
    print(i[2],i[5],i[6])

# [문제118] 부서별 급여의 총액을 구하세요. 
## Dictionary! 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
lst = [emp_list[-1] for emp_list in emp_csv]
set(lst) ### 부서코드 
code = list(set(lst))

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
print(listsum([1,3,5,7,9]))

dic = {}
for i in code:
    import csv
    file = open("C:/data/emp.csv","r")
    csv.reader(file) 
    emp_csv = csv.reader(file)
    emp_csv 
    next(emp_csv)
    lst_code = [int(emp_list[-4]) for emp_list in emp_csv if emp_list[-1] == i]
    dic[i] = listsum(lst_code)
dic

## Another solution
import csv

file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
dept_sum={}
for emp_list in emp_csv:
    if emp_list[-1] in dept_sum:
        dept_sum[emp_list[10]] = int(dept_sum[emp_list[10]])+int(emp_list[7])
    else:
        dept_sum[emp_list[10]] = int(emp_list[7])
for k,v in dept_sum.items():
    print(k,v)

# [문제119] 부서별 급여의 총액을 구하세요. 부서별로 오름차순 정렬하세요. 
'''
10 4400
20 19000
30 24900
40 6500
50 156400
60 28800
70 10000
80 304500
90 63040
100 51608
110 20308
non 7000
'''
for key in sorted(dic.keys()):
    print("%s: %s" % (key, dic[key]))

## Another solution 
def sortCheck(x):
    try:
        return int(x[0])
    except:
        return 999
    
dept_sum_sort = sorted(dept_sum.items(), reverse = False, key = sortCheck)

for k,v in dept_sum_sort:
    if k == "":
        print('non',v)
    else:
        print(k,v)

# [문제120] 단어, 알파벳을 입력값으로 넣어서 단어 안에 알파벳 수를 출력하세요
'''
<화면예>

wordF('happy','p')
2
'''
def wordF(x,y):
    print(x.count(y))
wordF('happy','p')

# [문제121] 단어를 입력값으로 넣어서 알파벳을 출력하는데 중복되는 알파벳은 하나만 출력하세요.
'''
alphaF('happy')
['h', 'a', 'p', 'y']

alphaF('intelligence')
['i', 'n', 't', 'e', 'l', 'g', 'c']
'''
def alphaF(x):
    lst = [i for i in x]
    lst_set = list(set(lst))
    print(lst_set)
alphaF('happy')
alphaF('intelligence')

# [문제122] 단어 철자의 빈도수를 출력하세요.
'''
alphaF('intelligence')
{'i': 2, 'n': 2, 't': 1, 'e': 3, 'l': 2, 'g': 1, 'c': 1}

alphaF('happy')
{'h': 1, 'a': 1, 'p': 2, 'y': 1}
'''
def alphaF(x):
    lst = [i for i in x]
    lst_set = list(set(lst))
    dic = {}
    for i in lst_set:
        dic[i] = lst.count(i)
    print(dic)
alphaF('intelligence')
alphaF('happy')

# [문제123] 아래와 같은 모양의 표를 생성하세요. 
'''
      PYTHON   R  SQL
2014      60  90   50
2015      80  65   75
2016      70  75   85
'''
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[60,90,50],[80,65,75],[70,75,85]], ### 이 부분에 딕셔너리 집어넣어도 됨! 
               index=['2014','2015','2016'],
               columns=['PYTHON','R','SQL'])

# [문제124] 'PYTHON' 열을 선택하세요
df['PYTHON']

# [문제125] '2014' 행 정보를 출력하세요. 
## 행 뽑아낼 때는 변수명.ix[] 사용! 
df.ix[0]
df.ix['2014']
df[:-2]
df[:'2014']
df['2014':'2014']

df['2014']

# [문제126] 인덱스번호를 기준으로 1부터 2번까지 출력하세요.
df[1:3]
df.ix[1:3]
df.iloc[1:3]

# [문제127] PYTHON의 값을 기준으로 60보다 큰값을 가지고 있는 행 정보를 출력하세요.
df[df['PYTHON']>60]

# [문제128] PYTHON의 값을 기준으로 60 보다 큰값을 가지고 있는 PYTHON 정보만 출력하세요.
df[df['PYTHON']>60]['PYTHON']
df.ix[df['PYTHON']>60,'PYTHON']
df.loc[df['PYTHON']>60,'PYTHON']

# [문제129] '2015' 행값 중에 PYTHON 정보만 출력하세요
df.ix['2015','PYTHON']

# [문제130] '2015' 행값 중에 PYTHON, R 정보 출력하세요 
df.ix['2015',['PYTHON','R']]

# [문제131] 'R' 열 정보를 출력하세요.
df['R']
df.ix[:,'R']

# 변수명.at[]: DataFrame에 새로운 행 추가 
## 2013년도 PYTHON:70, SQL:90, R:85 추가한다. 
df.at['2013','PYTHON'] = 70
df.at['2013','SQL'] = 90
df.at['2013','R'] = 85

df2 = df.reindex(['2013','2014','2015','2016'])
df2

# 변수명.set_value() <- 없어질 수도 있는 속성!(deprecated) 
df.set_value('2013','PYTHON',70)
df.set_value('2013','SQL',90)
df.set_value('2013','R',85)
df

## PLSQL 열을 추가 해야한다. 
df.at['2013','PLSQL'] = 50
df.at['2014','PLSQL'] = 60
df.at['2015','PLSQL'] = 70
df.at['2016','PLSQL'] = 80

## 인덱스, 컬럼 순서 조정 
df = df.reindex(['2013','2014','2015','2016'])
df = df.reindex(columns = ['SQL','PLSQL','R','PYTHON'])

# [문제132]PYTHON 점수가 80 이상 또는 SQL 점수가 90 이상인 데이터 출력하세요.
df[(df['PYTHON']>=80) | (df['SQL']>=90)]

x = df[(df['PYTHON']>=80)]
y = df[(df['SQL']>=90)]
pd.concat([x,y],axis=0)

# [문제133] PYTHON 점수가 80 이상 이고 SQL 점수 90 이상인 데이터 출력하세요.
df[(df['PYTHON']>=80) & (df['SQL']>=90)]

# [문제134] 직업이 ST_CLERK인 사원의 LAST_NAME, SALARY, JOB_ID를 출력해주세요 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")                                                                          
emp.ix[emp["JOB_ID"]=="ST_CLERK", ["LAST_NAME","SALARY","JOB_ID"]]

# [문제134] emp.csv 파일의 데이터를 판다스를 이용해서 읽어 들인 후 급여가 10000 이상인 사원들의 이름, 급여, 입사일을 출력해주세요.
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   
emp.ix[emp["SALARY"]>=10000, ["LAST_NAME","SALARY","HIRE_DATE"]] ### ix: 행 먼저 제한(indexing)
emp.loc[emp["SALARY"]>=10000, ["LAST_NAME","SALARY","HIRE_DATE"]] ### ix는 없어질 메소드 -> loc를 이용할 것! 

# [문제135] 급여 10000 이상인 사원들의 이름과 급여, 입사일를 출력하세요. 급여를 기준으로 내림차순하세요.
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   
emp2 = emp.ix[emp["SALARY"]>=10000, ["LAST_NAME","SALARY","HIRE_DATE"]]
emp2.sort_values(by="SALARY",axis=0,ascending = False) ### by절에 여러 컬럼을 쓰고 싶은 경우 -> [] 모양으로 컬럼을 쭉 넣어주면 됨! 

# [문제136] 급여를 많이 받는 순으로 10위 까지를 구하세요. 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   
emp2 = emp[["LAST_NAME","SALARY"]]
emp2.sort_values(by='SALARY',ascending=False)
emp_rank = emp2['SALARY'].rank(ascending=False, method='dense')
df = DataFrame([emp2["LAST_NAME"],emp2["SALARY"],emp_rank], index=["LAST_NAME","SALARY","RANK"]).T
df.sort_values(by="RANK")[df["RANK"]<=10]

emp2['RANK'] = emp2['SALARY'].rank(ascending=False, method='dense')
emp2['RANK']

# [문제137] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업을 출력하세요.
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   
emp.ix[emp["JOB_ID"].isin(["AD_VP", "AD_PRES"]), ["LAST_NAME","SALARY","JOB_ID"]]

# [문제138] 직업이 AD_VP ,AD_PRES 아닌 사원들의 이름, 급여, 직업을 출력하세요.
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   
emp.ix[~emp["JOB_ID"].isin(["AD_VP", "AD_PRES"]), ["LAST_NAME","SALARY","JOB_ID"]]

# [문제139] 커미션이 null인 사원의 이름, 커미션을 출력하세요. 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   
emp.ix[emp["COMMISSION_PCT"].isnull(), ["LAST_NAME","COMMISSION_PCT"]]

# [문제140] 커미션이 null이 아닌 사원의 이름, 커미션을 출력하세요. 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   
emp.ix[emp["COMMISSION_PCT"].notnull(), ["LAST_NAME","COMMISSION_PCT"]]

# [문제141] LAST_NAME 첫글자가 S로 시작되는 사원들의 LAST_NAME을 출력하세요. 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   

def first(x):
    for i in range(0,len(x)):
        if x[i][0] == "S":
            return x
emp["LAST_NAME"][emp["LAST_NAME"].apply(first).notnull()]

emp["LAST_NAME"][emp["LAST_NAME"].apply(lambda x: x[0]=='S')]
emp.loc[emp["LAST_NAME"].apply(lambda x: x[0]=='S'), "LAST_NAME"]


## Another solution 
def first_character(w):
    if w[0] == 'S':
        return True
    return False

emp["LAST_NAME"][emp["LAST_NAME"].apply(first_character)]
emp[emp["LAST_NAME"].apply(first_character)]["LAST_NAME"]
emp.ix[emp["LAST_NAME"].apply(first_character), "LAST_NAME"]

emp.ix[emp["LAST_NAME"].apply(lambda x:x[0]) == 'S', "LAST_NAME"]
emp.ix[emp["LAST_NAME"].apply(lambda x:x.startswith('S')), "LAST_NAME"]

# [문제142] last_name g로 끝나는 사원들의 이름, 급여 출력하세요. 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")  
emp.ix[emp["LAST_NAME"].apply(lambda x:x.endswith('g')), ["LAST_NAME","SALARY"]]

# [문제143] 110번 사원의 급여보다 많이 받는 사원들의 이름, 급여를 출력하세요. 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")  
emp.ix[emp["SALARY"] > int(emp[emp["EMPLOYEE_ID"]==110]["SALARY"]), ["LAST_NAME","SALARY"]]

# [문제144] 관리자 사원의 이름, 입사일, 급여를 출력하세요. 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")
emp.loc[emp["EMPLOYEE_ID"].isin(emp["MANAGER_ID"]), ["LAST_NAME","HIRE_DATE","SALARY"]]

import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
emp_mana = [emp_list[-2] for emp_list in emp_csv]

file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
next(emp_csv) 
for emp_list in emp_csv:
    if emp_list[0] in emp_mana:
        print(emp_list[2], emp_list[5], emp_list[7])

# [문제145] 101번 사원의 관리자 이름, 입사일, 급여정보를 출력하세요.
# 1. pandas를 이용해서 해결
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")  
emp.ix[emp["EMPLOYEE_ID"] == int(emp[emp["EMPLOYEE_ID"]==101]["MANAGER_ID"]), ["EMPLOYEE_ID","LAST_NAME","HIRE_DATE","SALARY"]]

# 2. 일반적으로 csv 파일을 읽어서 해결
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
emp_mana = [emp_list[-2] for emp_list in emp_csv if emp_list[0] == '101']

file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
next(emp_csv) 
for emp_list in emp_csv:
    if emp_list[0] in emp_mana:
        print(emp_list[2], emp_list[5], emp_list[7])

# [문제146] 최고 급여, 최저 급여 출력하세요.
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp["SALARY"].max()
emp["SALARY"].min()

import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv)
emp_sal = [int(emp_list[-4]) for emp_list in emp_csv]

print(max(emp_sal))
print(min(emp_sal))

x = 0
lar = emp_sal[x]
sma = emp_sal[x]
while x < len(emp_sal):
  if emp_sal[x] > lar:
    lar = emp_sal[x]
  if emp_sal[x] < sma:
    sma = emp_sal[x]
  x = x+1
print(lar, sma)

# [문제147] 20번 부서 사원들의 급여 합을 구하세요.
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp.ix[emp["DEPARTMENT_ID"] == 20, "SALARY"].sum()

import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv)
emp_sal_20 = [int(emp_list[-4]) for emp_list in emp_csv if emp_list[-1] == '20']

sum20 = 0
for i in emp_sal_20:
    sum20 += i
print(sum20)

## CSV 파일에 컬럼 이름이 없는 경우 
import csv
emp = pd.read_csv("C:/data/emp_new.csv", 
                  names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
print(emp['sal'][emp['deptno'] == 20].sum())

# [문제148] 부서번호를 입력하면 그 부서의 급여 총액을 구하는 함수를 생성하세요.
'''
dept_sum_sal()

부서번호를 입력하세요 :  20

19000.0


dept_sum_sal()

부서번호를 입력하세요 :  30

24900.0
'''
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp.ix[emp["DEPARTMENT_ID"] == 20, "SALARY"].sum()

def dept_sum_sal():
    dept = int(input("부서번호를 입력하세요 :  "))
    
    import pandas as pd
    emp = pd.read_csv("C:/data/emp.csv") 
    print(emp.loc[emp["DEPARTMENT_ID"] == dept, "SALARY"].sum())

dept_sum_sal()

# [문제149] 직업을 물어보게하고 직업을 입력하면 해당 직업의 최고 급여를 출력되게하는데 아무것도 입력하지 않으면 계속 물어보게하는
# 프로그램을 작성하세요.
'''
job_max_sal()

직업을 입력하세요 ?  ST_CLERK
3600.0

job_max_sal()

직업을 입력하세요 ? sa_rep
11500.0

job_max_sal()

직업을 입력하세요 ? 

직업을 입력하세요 ? 

직업을 입력하세요 ? 

job_max_sal()

직업을 입력하세요 ? sales
해당 직업의 사원은 없습니다.
'''
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp.loc[emp["JOB_ID"] == "ST_CLERK", "SALARY"].max()

def job_max_sal():
    try:
        jobid = input("직업을 입력하세요 ? ")
        import pandas as pd
        emp = pd.read_csv("C:/data/emp.csv")
        emp_jid = emp["JOB_ID"]
        
        if jobid.upper() in set(emp_jid):
            emp = pd.read_csv("C:/data/emp.csv") 
            print(emp.loc[emp["JOB_ID"] == jobid.upper(), "SALARY"].max())
        elif jobid.upper() == "":
            raise Exception(jobid)
        else:
            print("해당 직업의 사원은 없습니다.")
    except Exception as error:
        print(error)
        return job_max_sal()

job_max_sal()

## Other solutions 
import pandas as pd

def job_max_sal():
    try:
        emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
        name = ''
        while name =='':
            name = input('직업을 입력하세요 ? ')
        maxsal = emp['sal'][emp['job'] == name.upper()].max()
        if pd.isnull(maxsal):
            raise Exception
        return maxsal
    except Exception as err:
        print ('해당 직업의 사원은 없습니다.')

job_max_sal()

def job_max_sal():
    try:
        import  csv
        file = open("c:\data\emp_new.csv",'r')
        emp_csv = csv.reader(file)
        name = ''
        sal = []
        while name =='':
            name = input('직업을 입력하세요 ? ')
        
        for emp_list in emp_csv:
            if emp_list[2] == name.upper():
                sal.append(int(emp_list[5]))
        maxsal = max(sal)
        if maxsal=='':
            raise Exception
        return maxsal
    except Exception as err:
        print ('해당 직업의 사원은 없습니다.')

job_max_sal()

# [문제150]부서번호,급여를 기준으로 내림차순 정렬해서 아래 화면처럼 컬럼정보를 출력하세요.
'''
     deptno  empid         name      sal
105   110.0    205      Higgins  12008.0
106   110.0    206        Gietz   8300.0
8     100.0    108    Greenberg  13208.8
9     100.0    109       Faviet   9900.0
10    100.0    110         Chen   8200.0
12    100.0    112        Urman   7800.0
11    100.0    111      Sciarra   7700.0
13    100.0    113         Popp   6900.0
'''
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp.sort_values(by=["DEPARTMENT_ID","SALARY"], axis=0, ascending=False)[["DEPARTMENT_ID","EMPLOYEE_ID","LAST_NAME","SALARY"]]

# [문제151] index 번호 0부터 50까지 부서번호, 급여를 기준으로 내림차순 정렬한 후 아래결과처럼 출력하세요.
'''
    deptno  empid         name      sal
8    100.0    108    Greenberg  13208.8
9    100.0    109       Faviet   9900.0
10   100.0    110         Chen   8200.0
12   100.0    112        Urman   7800.0
11   100.0    111      Sciarra   7700.0
13   100.0    113         Popp   6900.0
'''
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp.iloc[0:51].sort_values(by=["DEPARTMENT_ID","SALARY"], axis=0, ascending=False)[["DEPARTMENT_ID","EMPLOYEE_ID","LAST_NAME","SALARY"]]

# [문제152] 50번 부서 사원들의 정보를 급여를 기준으로 내림차순 정렬해서 해서 아래 화면처럼 컬럼정보를 출력하세요.
'''
   empid         name  deptno     sal
21    121        Fripp    50.0  8200.0
20    120        Weiss    50.0  8000.0
22    122     Kaufling    50.0  7900.0
23    123      Vollman    50.0  6500.0
24    124      Mourgos    50.0  5800.0
84    184     Sarchand    50.0  4200.0
'''
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp[emp["DEPARTMENT_ID"]==50].sort_values(by="SALARY", axis=0, ascending=False)[["DEPARTMENT_ID","EMPLOYEE_ID","LAST_NAME","SALARY"]]

# [문제153] 10,20,30,40,50번 부서 사원들의 급여의 총액을 출력하세요.
'''
<화면출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
'''
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp.loc[emp["DEPARTMENT_ID"].isin([10,20,30,40,50]), ["DEPARTMENT_ID","SALARY"]].groupby("DEPARTMENT_ID").agg({"SALARY":'sum'})

# [문제154] s 변수의 값들 중에 unique한 값만 s_unique 변수에 넣어주세요 
s = [1,2,3,4,1,2,3,4,5,1,2,3,4,5,6,'']
s_unique = [i for i in set(s)]

s_unique = []
for i in s:
    if i not in s_unique:
        s_unique.append(i)
print(s_unique)

dic = {}
for i in s_unique:
    dic[i] = s.count(i)
print(dic)

se = Series(s)
se.value_counts(sort = False, normalize = True)

# [문제155] 부서별로 급여 총액을 출력하세요.
'''
<화면 출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
60 28800.0
70 10000.0
80 304500.0
90 58000.0
100 53708.8
110 20308.0
''' 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp[["DEPARTMENT_ID","SALARY"]].groupby("DEPARTMENT_ID").agg({"SALARY":"sum"})

emp.loc[emp["DEPARTMENT_ID"] == 20, ["DEPARTMENT_ID","SALARY"]]["SALARY"].sum()

import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
dept_id = emp["DEPARTMENT_ID"]
dept_id_uni = Series(dept_id.unique())
dept_id_uni = dept_id_uni.sort_values()
### dept_id_uni = dept_id_uni.dropna()
for i in dept_id_uni:
    print(int(i), emp.loc[emp["DEPARTMENT_ID"] == i, "SALARY"].sum())

# [문제156]부서별로 급여 총액을 출력하세요.
'''
<화면 출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
60 28800.0
70 10000.0
80 304500.0
90 58000.0
100 53708.8
110 20308.0
nan 7000.0
'''
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp[["DEPARTMENT_ID","SALARY"]].groupby("DEPARTMENT_ID").agg({"SALARY":"sum"})

import pandas as pd
emp=pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
s=Series(emp['deptno'].unique())
for i in s.sort_values():
    if pd.isnull(i):
        print(i,emp.loc[emp['deptno'].isnull(),'sal'].sum())
    else:
        print(int(i),emp.loc[emp['deptno'].isnull(),'sal'].sum())

import pandas as pd
emp=pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
s=Series(emp['deptno'].unique())
for i in s.sort_values():
    if pd.isnull(i):
        print(i,emp.loc[emp['deptno'].isnull(),'sal'].sum())
    else:
        print(int(i),emp.loc[emp['deptno']==i,'sal'].sum())

# [문제157] 년도별로 입사한 인원수 결과를 출력해주세요.
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv") 
emp2 = pd.read_csv("C:/data/emp.csv") 

import datetime
emp2["HIRE_YEAR"] = ""
for i in range(0,len(emp)):
    emp2["HIRE_YEAR"][i] = datetime.datetime.strptime(str(emp["HIRE_DATE"][i]), "%Y%m%d").year

emp2[["HIRE_YEAR","EMPLOYEE_ID"]].groupby("HIRE_YEAR").count()

## Another solution 
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp.dtypes
print(emp.groupby(emp['hire_date'].str.slice(0,4))['empid'].count())
print(emp.groupby(pd.to_datetime(emp['hire_date']).dt.year)['empid'].count())
pd.to_datetime(emp['hire_date']).dt
pd.to_datetime(emp['hire_date']).dt.year
pd.to_datetime(emp['hire_date']).dt.month
pd.to_datetime(emp['hire_date']).dt.day
pd.to_datetime(emp['hire_date']).apply(lambda x: x.year)
pd.to_datetime(emp['hire_date']).apply(lambda x: x.month)

pd.to_datetime(Series('2018-09-19 11:01:30')).dt.year
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.month
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.day
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.hour
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.minute
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.second
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.quarter
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.dayofweek ### 월요일=0, 일요일=6
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.dayofyear
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.date
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.time
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.week
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.days_in_month

# [문제158] emp_new.csv 를 emp리스트 변수안에 아래 모양과 같은 딕셔너리 데이터 유형에 데이트를 입력한 후 출력하세요.
'''
{'empno': 100, 'ename': King, 'job': AD_PRES, 'mgr': '', 'hiredate': 2003-06-17, 'sal': 24000, 'comm': '', 'deptno': 90}

100 King AD_PRES  2003-06-17 24000  90
101 Kochhar AD_VP 100 2005-09-21 17000  90
102 De Haan AD_VP 100 2001-01-13 17000  90
103 Hunold IT_PROG 102 2006-01-03 9000  60
104 Ernst IT_PROG 103 2007-05-21 6000  60
'''
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

emp_list = []
for i in range(0,len(emp)):
    emp_list.append({'empno': emp['empid'][i], 
                'ename': emp['name'][i], 
                'job': emp['job'][i], 
                'mgr': emp['mgr'][i], 
                'hiredate': emp['hire_date'][i], 
                'sal': emp['sal'][i], 
                'comm': emp['comm'][i], 
                'deptno': emp['deptno'][i]})
print(emp_list)

# [문제159] emp_new.csv, dept_new.csv 파일을 읽어서 사원의 이름, 부서 이름을 출력하세요.
## join 
'''
select e.name, d.name
from emp e, dept d
where e.deptno = d.deptno; 
'''

from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("C:\data\dept_new.csv", names = ['deptno','name','man','locid'])
emp['deptno'] = emp['deptno'].fillna(0).apply(lambda x:int(x))

dept_dict = {}
for i in range(0,len(dept)):
    dept_dict[dept['deptno'][i]] = dept['name'][i] 

emp["deptname"] = ""
for i in range(0,len(emp)):
    emp["deptname"][i] = dept_dict[emp["deptno"][i]]
emp[["name","deptname"]]

## Another solution
import  csv
empfile = open("c:\data\emp_new.csv",'r')
deptfile = open("c:\data\dept_new.csv",'r')
emp_csv = csv.reader(empfile)
dept_csv = csv.reader(deptfile)

emp =[]  
dept =[]

for i in  dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'mgr':i[2],'loc':i[3]})

for j in emp_csv:
    emp.append({'empno':j[0],'ename':j[1],'job':j[2],'mgr':j[3], 'hiredate':j[4],'sal':j[5],'comm':j[6],'deptno':j[7]})

for d in dept:
   for e in emp:
        if e['deptno'] == d['deptno']:
            print ( e['ename'], d['dname'])

empfile.close()
deptfile.close()

# [문제160] 사원들의 이름, 부서 이름을 출력하면서 소속부서가 없는 사원도 출력해주세요. 마지막에는 총건수도 출력하세요. 
## outer join 
'''
select e.name, d.name
from emp e, dept d
where e.deptno = d.deptno(+);
'''

from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("C:\data\dept_new.csv", names = ['deptno','name','man','locid'])
emp['deptno'] = emp['deptno'].fillna(0).apply(lambda x:int(x))

dept_dict = {}
for i in range(0,len(dept)):
    dept_dict[dept['deptno'][i]] = dept['name'][i] 
dept_dict[0] = "No dept"

count = 0
emp["deptname"] = ""
for i in range(0,len(emp)):
    emp["deptname"][i] = dept_dict[emp["deptno"][i]]
    count += 1

print(emp[["name","deptname"]], "\n", count, "건이 출력되었습니다.")

## Another solution 
import  csv
empfile = open("c:\data\emp_new.csv",'r')
deptfile = open("c:\data\dept_new.csv",'r')
emp_csv = csv.reader(empfile)
dept_csv = csv.reader(deptfile)

emp = []  
dept =[]

for i in  dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'mgr':i[2],'loc':i[3]})

for j in emp_csv:
    emp.append({'empno':j[0],'ename':j[1],'job':j[2],'mgr':j[3], 'hiredate':j[4],'sal':j[5],'comm':j[6],'deptno':j[7]})

cn = 0
for e in emp:
    if e['deptno'] == '':
        print(e['ename'])
        cn += 1
    else:
        for d in dept:
            if e['deptno'] == d['deptno']:
               print ( e['ename'], d['dname'])
               cn += 1

print(cn)

empfile.close()
deptfile.close()

# [문제161] emp_new.csv, dept_new.csv 파일 데이터에서 50번 부서 사원의 중에 급여가 5000 이상인 사원의 이름, 부서 이름을 출력하세요.
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("C:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
empdept = pd.merge(emp,dept,on='deptno')
empdept.loc[empdept['deptno'] == 50].loc[empdept['sal'] >= 5000][['name','dname']]

# [문제162] 2002년도에 근무한 사원들의 이름, 급여, 입사일, 부서코드,부서이름을 출력하세요.
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("C:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
pd.merge(emp.loc[emp['hire_date'].str.slice(0,4)=='2002',['name','sal','hire_date','deptno']],dept[['dname','deptno']])

pd.merge(emp[['name','sal','hire_date','deptno']][pd.to_datetime(emp['hire_date']).dt.year==2002],dept[['deptno','dname']])

# [문제163] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업, 부서코드, 부서이름 을 출력하세요.
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("C:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
pd.merge(emp.loc[emp['job'].isin(["AD_VP","AD_PRES"]),['name','sal','hire_date','deptno']],dept[['dname','deptno']])

# [문제164] 부서이름별 총액 급여를 출력하세요. 
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("C:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
pd.merge(emp[['sal','deptno']], dept[['dname','deptno']], on='deptno').groupby('dname').sum()['sal']

dept = DataFrame({'dname':['관리팀','마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀','영업팀','기획팀','재무팀','회계팀']},
                  index = [10,20,30,40,50,60,70,80,90,100,110])
pd.merge(emp[['name','sal','deptno']], dept, left_on='deptno', right_index=True).groupby('dname').agg({"sal":'sum'})

# [문제165] emp_new.csv 파일  데이터에 커미션 정보를 분석하려 합니다.
# 커미션에 null값들의 수, null이 아닌값들의 수를 구하세요.

# 1. 일반적으로 csv file을 읽어서 해결
import  csv
empfile = open("c:\data\emp_new.csv",'r')
deptfile = open("c:\data\dept_new.csv",'r')
emp_csv = csv.reader(empfile)
dept_csv = csv.reader(deptfile)

cnt_null = 0
cnt_not = 0
for emp_list in emp_csv:
    if emp_list[-2] == "":
        cnt_null += 1
    else:
        cnt_not += 1
print(" null값들의 수: ", cnt_null, "\n", "null이 아닌값들의 수: ", cnt_not)

# 2. pandas를 이용해서 해결
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empno','ename','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("C:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])

a = emp.loc[emp["comm"].isnull(),"empid"].count()
b = emp.loc[emp["comm"].notnull(),"empid"].count()
print(" null값들의 수: ", a, "\n", "null이 아닌값들의 수: ", b)

# [문제166] emp_new.csv, dept_new.csv 파일 데이터를 이용해서  조인된 결과를 보려고 합니다.
# 조인 함수를 생성하세요.
'''
join(emp,'deptno','ename', dept,'deptno','dname')

join(emp,'mgr','ename', emp,'empno','ename')
'''
pd.merge(emp[['name','sal','hire_date','deptno']],dept[['dname','deptno']])

def join(arg1, arg2, *x):
    x = set(x)
    c = [i for i in x if i in list(arg1.columns)]
    d = [i for i in x if i in list(arg2.columns)]
    print(pd.merge(arg1[c], arg2[d]))
join(emp, dept, 'deptno','ename','deptno','dname')
join(emp, emp, 'mgr','ename','empno','ename')

# Another solution 
import  csv
empfile = open("c:\data\emp_new.csv",'r')
deptfile = open("c:\data\dept_new.csv",'r')
emp_csv = csv.reader(empfile)
dept_csv = csv.reader(deptfile)

emp = []  
dept =[]

for i in  dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'mgr':i[2],'loc':i[3]})

for j in emp_csv:
    emp.append({'empno':j[0],'ename':j[1],'job':j[2],'mgr':j[3], 'hiredate':j[4],'sal':j[5],'comm':j[6],'deptno':j[7]})

def join(outer_table,outer_column1,outer_column2,inner_table,inner_column1,inner_column2):
   for  o  in  outer_table:
      for  i  in  inner_table:
         if o[outer_column1] == i[inner_column1]:
             print (o[outer_column2], i[inner_column2]) 
 
join(emp,'deptno','ename', dept,'deptno','dname')

join(emp,'mgr','ename', emp,'empno','ename')

import  pandas  as  pd

emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','ename','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])

def join(outer_table,outer_column1,outer_column2,inner_table,inner_column1,inner_column2):
    print(pd.merge(outer_table[[outer_column1,outer_column2]],inner_table[[inner_column1,inner_column2]],left_on=outer_column1,right_on=inner_column1))

join(emp,'deptno','ename', dept,'deptno','dname')

join(emp,'mgr','ename', emp,'empid','ename')  

# [문제167] x변수에는 1,2,3,4,5  y변수에는 6,7,8,9,10 들어 있다. f(x,y) = x2 + y 를 구하세요.(lambda, map 함수를 이용하세요)
x = [1,2,3,4,5]
y = [6,7,8,9,10]

list(map(lambda x,y:x*2+y, x,y))

# [문제168] emp_new.csv는 pandas로 읽고  dept_new.csv는 일반 csv로 읽어 들인 후 조인을 수행하세요.
import pandas
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','ename','job','mgr_e','hire_date','sal','comm','deptno'])
emp['deptno'] = emp['deptno'].fillna(0).apply(lambda x:int(x))

import  csv
deptfile = open("c:\data\dept_new.csv",'r')
dept_csv = csv.reader(deptfile)
dept = {}
for i in  dept_csv:
    dept[int(i[0])] = i[1]
dept

emp['dname']=emp['deptno'].map(dept)
print(emp[['empid', 'deptno','dname']])

## Another solution 
from pandas import Series, DataFrame
import pandas as pd
import csv

emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

deptfile = open("c:\data\dept_new.csv",'r')
dept_csv = csv.reader(deptfile)
dept = {}

for i in dept_csv:
    if i[0] != dept:
        dept[int(i[0])] = i[1]

for k,v in dept.items():
    print(k,v)

emp['dname']=emp['deptno'].map(dept)
print(emp[['empid', 'deptno','dname']])

# [문제169] happiness 변수에 문장이 있습니다. 행복이란 단어가 몇개 나오는지 분석하시고, 위치정보도 출력해주세요.
happiness = '우리나라 「헌법」 제10조는 “모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다”라고 규정하고 있다.행복추구권은 근대 입헌민주주의의 핵심인 개인주의·자유주의를 그 사상적 기반으로 하고 있다. 행복추구권에 있어서 행복은 다의적인 개념으로, 각자의 생활조건이나 가치관에 따라 다르게 이해될 수 있으나, 최소한 인간적인 고통이 없는 상태 내지 만족감을 느낄 수 있는 행복한 상태를 의미한다.'
happiness.index('행복')
happiness.rfind('행복')
happiness['행복' in happiness]

dic = {}
for i in happiness:
    dic['행복'] = happiness.count('행복')
print(dic)

happiness.index('행복')
happiness[45:].index('행복')
happiness[72:].index('행복')
happiness[123:].index('행복')
happiness[134:].index('행복') ### 217

for i in range(0,len(happiness)-2):
    if happiness[i:i+2] == '행복':
        print(i)

lst = []
x = 0
i = 0 
for i in range(0,happiness.count('행복')):
    y = happiness[x:].find('행복')
    x += y + 1
    lst.append(x - 1)
print(lst)

# [문제170] emp1.csv, emp2.csv파일을 읽어서 부서별 총액급여를 구하세요.
from pandas import Series, DataFrame
import pandas as pd
emp1 = pd.read_csv("c:\data\emp3.csv", names = ['empno','ename','hire_date','sal','deptno'])
emp2 = pd.read_csv("c:\data\emp4.csv", names = ['empno','ename','hire_date','sal','deptno'])
emp_list = [emp1, emp2]
emp = pd.concat(emp)

emp.fillna(0).groupby('deptno').agg({'sal':'sum'})

## Another solution 
import pandas as pd
emp = pd.DataFrame()
for i in range(1,3):
    file = 'c:/python_data/emp{}.csv'.format(i) ### R의 paste() 기능! 
    temp = pd.read_csv(file, names = ['empid','name','hire_date','sal','deptno'])
    emp = emp.append(temp)
print(emp['sal'].groupby(emp['deptno']).sum())

import glob
import pandas as pd
file = 'C:/python_data/emp*.csv' ### 확장자명에 따라 로드하는 기능! <- 해당 디렉토리에 있는 모든 파일을 다 불러들이니, 새로운 폴더 만들 것! 
file_list = glob.glob(file)
print(file_list)
emp = pd.DataFrame()
for i in file_list:
    temp = pd.read_csv(i, names =  ['empid','name','hire_date','sal','deptno'])
    emp = emp.append(temp)
print(emp['sal'].groupby(emp['deptno']).sum())

# [문제171] 2016년도에 태어난 아이들의 정보가 들어 있는 year2016파일을 분석해야 합니다. 총 출생수를 출력해주세요.
from pandas import Series, DataFrame
import pandas as pd
yob = pd.read_csv("c:\data\yob2016.csv", names = ['name','gen','count'])
yob['count'].sum()

## Another solution 
import csv
import os
count=0
file = 'c:\data\yob2016.txt'
name = os.path.basename('c:\data\yob2016.txt')
name = name.split('.')[0]
with open(file,'r') as f:
    data=csv.reader(f)
    for d in data:
        count += int(d[2])
print(name,count)

import csv
import os
count=0
file = 'c:\data\yob2016.txt'
name = os.path.basename('c:\data\yob2016.txt') ### 물리적인 절대 경로 중에 해당 확장자에 해당되는 것들을 로드 
name = name.split('.')[0]
with open(file,'r') as f:
    data=f.readlines()
    for d in data:
        birth = d.split(',')[2]
        count += int(birth)
print(name,count)

import pandas as pd 
import os
file = 'c:/data/yob2016.txt'
name = os.path.basename(file)
name = name.split('.')[0]
yob = pd.read_csv('c:\data\yob2016.txt', names=['name','gender','birth'])
print(name,yob['birth'].sum())

# [문제172] 2016년도에 태어난 아이 이름 상위 10까지 보여주세요. 성별 상위 5까지 보여주세요.
from pandas import Series, DataFrame
import pandas as pd
yob = pd.read_csv("c:\data\yob2016.csv", names = ['name','gen','count'])
yob.sort_values(by='count', ascending=False).head(10)
yob.loc[yob['gen']=='M'].sort_values(by='count', ascending=False).head(5)
yob.loc[yob['gen']=='F'].sort_values(by='count', ascending=False).head(5)

import pandas as pd
yob=pd.read_csv('c:\data\yob2016.csv',names=['name','gen','cn'])
yob['rank']=yob['cn'].rank(ascending=False,method='dense')
yob[yob['rank']<=10].sort_values(by='rank')
yob['frank']=yob['cn'][yob['gen']=='F'].rank(ascending=False,method='dense')
yob['mrank']=yob['cn'][yob['gen']=='M'].rank(ascending=False,method='dense')
yob[yob['frank']<=5].sort_values(by='frank')[['name','gen','cn']]
yob[yob['mrank']<=5].sort_values(by='mrank')[['name','gen','cn']]

## Another solution 
import pandas as pd 
yob2016 = pd.read_csv('c:\data\yob2016.txt', names=['name','gender','birth'])
def top(df, n=5, column='birth'):
    return df.sort_values(by=column, ascending=False)[:n]
print(top(yob2016 , n=10))
print(yob2016.groupby('gender').apply(top))

# [문제173] emp1.csv 데이터를 이용해서 급여를 많이 받는 순으로 10위까지 구하세요.
import pandas as pd
emp1 = pd.read_csv("C:\data\emp3.csv", names = ['empno','ename','hire_date','sal','deptno'])
emp1['rank'] = emp1['sal'].rank(ascending=False, method='dense')
emp1[emp1['rank']<=10].sort_values(by='rank')

# [문제174] emp1.csv 데이터를 이용해서 부서별로 급여를 많이 받는 순으로 5위까지 구하세요.
import pandas as pd
from pandas import Series, DataFrame
edept = emp1.fillna(0).groupby('deptno').agg({'sal':'sum'})
edept['rank'] = edept['sal'].rank(ascending=False, method='dense')
edept[edept['rank']<=5].sort_values(by='rank')

emp1.loc[emp1['deptno']==20].sort_values(by=['deptno','rank'])

def dept_rank(x):
    import pandas as pd
    from pandas import Series, DataFrame
    emp1 = pd.read_csv("C:\data\emp3.csv", names = ['empno','ename','hire_date','sal','deptno'])
    emp1['deptno'] = emp1['deptno'].fillna(0).apply(lambda x:int(x))
    emp1 = emp1.loc[emp1['deptno']==x]
    emp1['rank'] = emp1['sal'].rank(ascending=False, method='dense')
    print(emp1[emp1['rank']<=5].sort_values(by='rank'))
dept_rank(80)

# [문제175] yob2016.txt 데이터를 이용해서 아기 이름 순위 10위까지 구하세요.
import pandas as pd
yob = pd.read_csv('C:\data\yob2016.csv', names=['name','gen','cn'])
yob['rank'] = yob['cn'].rank(ascending=False, method='dense')
yob[yob['rank']<=10].sort_values(by='rank')

# [문제176] yob2016.txt 데이터를 이용해서 성별 아기 이름 순위 5위까지 구하세요. 
import pandas as pd
yob = pd.read_csv('C:\data\yob2016.csv', names=['name','gen','cn'])

def yob_rank(year, gender):
    try:
        import pandas as pd
        yob = pd.read_csv('C:\data\yob{}.csv' .format(year), names=['name','gen','cn'])
        yob = yob.loc[yob['gen']==gender.upper()]
        yob['rank'] = yob['cn'].rank(ascending=False, method='dense')
        print(yob[yob['rank']<=5].sort_values(by='rank'))
        if year > 2016 or year < 2000 or gender not in ['M',"F"]:
            raise Exception
    except Exception as error:
        print(error)
        print("연도는 2000~2016년, 성별은 'M'이나 'F' 입력하세요.")
yob_rank(2016,'F')

# [문제177] 2000 ~ 2016년도 년도별 출생수
# https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data
'''
2000 3777666
2001 3741011
2002 3735651
2003 3799547
2004 3817903
2005 3841440
2006 3952231
2007 3993206
2008 3925486
2009 3814539
2010 3689517
2011 3650434
2012 3648441
2013 3634744
2014 3692930
2015 3683749
2016 3637321 
''' 
def countBirths():
    ret=[]
    for y in range(2000,2017):
        count=0
        filename='c:\yob\yob%d.txt'%y
        with open(filename,'r') as f:
            data=f.readlines()
            for d in data:
                birth = d.split(',')[2]
                count += int(birth)
            ret.append((y,count))
    return ret
result = countBirths()
for year, cn in result:
    print(year,cn)

import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
year_cn=[]
all_data = pd.DataFrame()
for y in range(2000,2017):
    filename='c:\yob\yob%d.txt'%y
    name = os.path.basename(filename)
    name = name.split('.')[0]
    df = pd.read_csv(filename, names=['name','gender','birth'])
    all_data = all_data.append(df)
    year_cn.append((name[3:],all_data['birth'].sum()))
    print(name[3:],all_data['birth'].sum())

# [문제178]  2000 ~ 2016년도 년도별 출생수 결과를 year.txt 파일에 저장하세요. 
f = open("C:/data/year.txt", "a")
for i in range(2000,2017):
    file = open("C:/data/yob{}.csv" .format(i), "r")
    data = file.read()
    f.write(data)
    print(i)
    file.close()
f.close()

## Other solutions 
import os
import glob
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

### print 
year_cn=[]
### all_data = pd.DataFrame()
for f in glob.glob("c:\python_data\yob*.txt"):
    name = os.path.basename(f)
    name = name.split('.')[0]
    df = pd.read_csv(f, names=['name','gender','birth'])
    ### all_data = all_data.append(df)
    
    year_cn.append((name[3:],df['birth'].sum()))
    print(name[3:],df['birth'].sum())

### 저장 
with open('c:\python_data\year.txt','w') as f:
    for year, birth in year_cn:
        data = '%s,%s\n'%(year,birth)
        print(data)
        f.write(data)

############################################################

import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

with open('c:/data/year_total.csv','w') as f:
    writer = csv.writer(f, delimiter=',')
    for y in range(2000,2017):
        filename='c:/data/yob%d.csv'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        writer.writerow([name[3:],df['birth'].sum()]) ### 행 단위 

# [문제179] 2010 ~ 2016  년도까지 성별 출생 현황을 year_gender_total.csv 파일로 생성해주세요.
import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

with open('c:/data/year_gender_total.csv','w') as f:
    writer = csv.writer(f, delimiter=',')
    for y in range(2000,2017):
        filename='c:/data/yob%d.csv'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        writer.writerow([name[3:],'\n', df.groupby('gender').agg({'birth':'sum'}), '\n'])

## Another solution 
with open('c:/data/year_gender_total.csv','w',encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['년도','여자','남자'])
    for y in range(2000,2017):
        filename='c:\data\yob%d.csv' %y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        gender_cn = df['birth'].groupby(df['gender']).sum()
        f_cn = gender_cn.loc['F']
        m_cn = gender_cn.loc['M']
        writer.writerow([name[3:],f_cn, m_cn])

# [문제180] 2010 ~ 2016  년도까지 성별 출생 현황을 그래프를 그리세요.
import csv
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() ### 한글 폰트를 적용! 
rc('font', family=font_name)
%matplotlib inline

with open('c:/data/year_gender_total.csv','w',encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['년도','여자','남자'])
    for y in range(2000,2017):
        filename='c:\data\yob%d.csv'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        gender_cn = df['birth'].groupby(df['gender']).sum()
        writer.writerow([name[3:],gender_cn.loc['F'],gender_cn.loc['M']])
      
df = pd.read_csv('c:/data/year_gender_total.csv')
df

df = df.set_index("년도")
df
df.plot()
df.plot(kind="bar")
df.plot(kind="barh")

plt.plot(df.ix[:,0], label="여자", color="r", linestyle="--")
plt.plot(df.ix[:,1], label="남자", color="b", linestyle=":")
plt.title("성별 출생 현황", fontsize=15)
plt.xlabel("년도",fontsize=10)
plt.ylabel("출생수",fontsize=10)
plt.legend()
plt.grid()

# [문제181] 이 주소로 접속하셔서 게시글을 출력하세요.
import urllib.request as req
url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
for i in soup.findAll('p',{'class':'con'}): 
    print(i.get_text())

for i in soup.findAll(class_ = 'con'): ### 요소검사(F12)에서 해당 부분을 클릭해서 공통된 키워드를 찾아볼 것! 
    print(i.get_text())

## Another solution 
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
result = soup.find_all('p', class_="con")
for i in result:
    print(i.get_text(strip=True))

url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(res,"html.parser")
result = soup.find_all('p', class_="con")
for i in result:
    print(i.get_text(strip=True))

# [문제182] 게시글 뿐만 아니라 게시날짜 정보도 같이 출력하시오 !
'''
2017.04.12 19:48 레이디버그 3기나오면 좋은사람 손~~
'''
import urllib.request as req
url="http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(res,'html.parser')
con=soup.findAll(class_=['con','date'])
for i in con:
    print(i.get_text(strip=True))

import urllib.request as req
url="http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(res,'html.parser')
result1 = soup.find_all('span',class_='date') ### 2개를 따로 따로 추출해서, for문에서 합침! 
result2 = soup.find_all('p',class_='con')
for i in result1:
    for j in result2:
        print(i.get_text(strip=True), j.get_text(strip=True))

## Another solution 
from bs4 import BeautifulSoup
import urllib.request as req
url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)
soup= BeautifulSoup(res, "html.parser")
a = soup.find_all('p',class_="con")
b = soup.find_all('span',class_="date") ### 날짜 정보만 들어 있는 변수 
print(b[0].get_text())
print(b[0].text)

cnt= 0
for i in a:
    print(b[cnt].text,i.get_text(strip=True))
    cnt += 1
print(cnt)

# [문제183] 게시판에 게시글 전부를 수집해주세요.
cn = 0
for page in range(0,17):
    url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=%d&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&" %page
    res = req.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(res,'html.parser')
    result1 = soup.find_all('span',class_='date')
    result2 = soup.find_all('p',class_='con')
    for i in result1:
        for j in result2:
            print(i.get_text(strip=True), j.get_text(strip=True))
    cn += 1
print("총",cn,"페이지가 출력되었습니다.")

url = ["""http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=%d
       &hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&""" %page 
       for page in range(0,17)]

## Another solution 
for i in range(1,16):
    url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=" +str(i)+ "&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    res = req.urlopen(url)
    soup= BeautifulSoup(res, "html.parser")
    a = soup.find_all('p',class_="con")
    b = soup.find_all('span',class_="date")
    cnt= 0
    content =[] ### 리스트 변수 선언 <- 각 페이지의 게시글들이 저장될 수 있게 따로 만듬! 
    for i in a:
        content.append(b[cnt].text + i.get_text(strip=True))
        cnt += 1
    for j in content:
        print(j)

# [문제184] 동아일보에서 인공지능에 기사 스크롤링 해주세요.
# 동아일보 
## 1. URL 추출해서 리스트 저장 
import urllib.request as req 
content = []
for i in range(1,100,15):
    url = "http://news.donga.com/search?p=%d&query=it&check_news=2&more=1&sorting=1&search_date=1&v1=&v2=&range=1" %i
    res = req.urlopen(url)
    soup= BeautifulSoup(res, "html.parser")
    a = soup.find_all('p',class_="tit")
    for i in a:
        content.append(i.find('a').attrs['href'])
    for j in content:
        print(j)

## 2. 각 URL의 본문 추출, 저장 
body = []
for i in content:
    res = req.urlopen(i)
    soup = BeautifulSoup(res, "html.parser")
    a = soup.find_all('div', class_='article_txt')
    for j in a:
        body.append(j.get_text())
    for k in body:
        print(k)

# "인공지능"으로 검색 
## 1. URL 추출해서 리스트 저장 
content = []
for i in range(1,500,15):
    url = "http://news.donga.com/search?p={}&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1" .format(i)
    res = req.urlopen(url)
    soup= BeautifulSoup(res, "html.parser")
    a = soup.find_all('p',class_="tit")
    for i in a:
        content.append(i.find('a').attrs['href'])
    for j in content:
        print(j)

## 2. 각 URL의 본문 추출, 저장 
body = []
for i in content:
    res = req.urlopen(i)
    soup = BeautifulSoup(res, "html.parser")
    a = soup.find_all('div', class_='article_txt')
    for j in a:
        body.append(j.get_text())
    for k in body:
        print(k)
body[0].findAll('Copyright')
for i in body:
    print(i.find('Copyright'))

## Another solution 
import urllib.request
from bs4 import BeautifulSoup
params = []
for i in range(1,20,15):
    list_url = "http://news.donga.com/search?p="+str(i)+"&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"
    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url, timeout=100).read().decode("utf-8") ### timeout: 웹 크롤링할 때 시간이 너무 오래 걸리면 자동으로 stop 시키는 거 
    soup= BeautifulSoup(res, "html.parser")
    for link in soup.findAll('p', {'class':'tit'}):
        params.append(link.find('a').get('href'))
print(params)

cn = 0
txt= []
for i in params:
    print(i)
    url = urllib.request.Request(i)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    result = soup.find_all('div',class_='article_txt')
    for i in result:
        ### print(i.text)
        txt.append(i.text)

## 데이터 정제 
txt[0]
txt[0][0:txt[0].find('Copyright')] ### 뒤에 쓸모 없는 것들 필터링 
for i in range(0,30):
    print(txt[i][0:txt[i].find('Copyright')])

# [문제185] 동아일보에서 인공지능에 기사 스크롤링 하셔서 단어의 빈도수를 체크하시고 워드클라우드를 그리세요.
## 동아일보 크롤링
from bs4 import BeautifulSoup
import urllib.request as req
params =[]
url = "http://news.donga.com/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
for i in soup.select('p.tit > a'):
    params.append(i.get('href'))

cn = 0
txt= []
donga=[]

for i in params:
    res = req.urlopen(i).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    result = soup.select('div.article_txt')

    for i in result:
       txt.append(i.get_text(strip=True))
for i in range(0,len(txt)):
    donga.append(txt[i][0:txt[i].find('Copyright')])

donga="".join(donga)

## 동아일보 분석(Kkma)
tokens_donga=kkma.nouns(donga)
ko=nltk.Text(tokens_donga)
stopword = ['.',',',')','(','의','지','에','간','것','곳','달','것임','겟습','저','제','대','분','등',
            '말','고','수','이','또','창','며','를','을','명','때','개','맘']
ko = [eachword for eachword in ko if eachword not in stopword]
ko=nltk.Text(ko)
data=ko.vocab().most_common(50)

## 동아일보 분석(twitter)
tokens_donga=twitter.nouns(donga)
ko=nltk.Text(tokens_donga)
stopword = ['.',',',')','(','의','지','에','간','것','곳','달','것임','겟습','저','제','대','분','등',
            '말','고','수','이','또','창','며','를','을','명','때','개','맘']
ko = [eachword for eachword in ko if eachword not in stopword]
ko=nltk.Text(ko)
data=ko.vocab().most_common(50)

## 워드클라우드
from wordcloud import WordCloud
wordcloud=WordCloud(font_path="c:\Windows\Fonts\malgunbd.ttf",
                    background_color='white',
                    width=1000,height=600).generate_from_frequencies(dict(data))

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")

## Another solution 
import urllib.request
from bs4 import BeautifulSoup

params = []
for i in range(1,50,15):
    list_url = "http://news.donga.com/search?p="+str(i)+"&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"

    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url, timeout=100).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    for link in soup.findAll('p', class_='tit'):
        params.append(link.find('a').get('href'))

txt= []
for i in params:
    ### print(i)
    url = urllib.request.Request(i)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    result = soup.find_all('div',{'class':'article_txt'})
      
    for i in result:
        ### print(i.text)
       txt.append(i.text)

new_text =''
for i in range(0,60):
    new_text = new_text + txt[i][0:txt[i].find('Copyright')] + '\n'
    
import nltk
from konlpy.tag import Kkma
kkma = Kkma()

tokens_ko = kkma.nouns(new_text)
tokens_ko

ko = nltk.Text(tokens_ko)
len(ko.tokens)
len(set(ko.tokens))
ko.vocab()
ko.vocab().most_common(50)

with open("c:/data/new_text.txt","w",encoding="utf-8") as file:
    for i in range(0,60):
        file.write(txt[i][0:txt[i].find('Copyright')])

with open("c:/data/new_text.txt","r",encoding="utf-8") as file:
    news = file.read()

import nltk
from konlpy.tag import Kkma
kkma = Kkma()

tokens_ko = kkma.nouns(news)
ko = nltk.Text(tokens_ko)
ko.vocab()

# [문제186] http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp
# 이미지를 다운로드하세요.
import urllib.request as req
from bs4 import BeautifulSoup
ls=[]
url= "http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp"
res=req.urlopen(url).read()
soup=BeautifulSoup(res,"html.parser")
lnk= soup.select('div.sell > div.sum > a > img')

for i in lnk:
    ls.append("http://www.skwyverns.com"+i["src"])

for p in ls:
    splitStr=p.split('/')
    name=splitStr[len(splitStr)-1]
    fullPath='c:/pitcher/'+name
    req.urlretrieve(p,fullPath)

# [문제 187] 생성자에 이름, 핸드폰번호, 메일, 주소 변수를 생성합니다. 
# print_info 메소드를 생성한 후  출력하는 Contact 클래스를 생성하세요.
# 인스턴스는 set_contact 함수를 이용해서 만드시고 이름, 핸드폰번호,메일, 주소는 입력값으로 받아서 출력하세요.
"""
이름을 입력하세요 : 홍길동

핸드폰번호를 입력하세요 : 010-1000-1004

메일을 입력하세요 : hong@aaa.com

주소를 입력하세요 : 서울시 강남구 삼성로

이름 : 홍길동 
핸드폰번호 : 010-1000-1004 
메일 : hong@aaa.com 
주소 : 서울시 강남구 삼성로
""" 

class Contact:
    def __init__(self):
        self.name = '' ### 변수 선언 
        self.phone = ''
        self.mail = ''
        self.addr = ''
    def set_contact(self):
        self.name = input("이름을 입력하세요 : ")
        self.phone = input("핸드폰번호를 입력하세요 : ")
        self.mail = input("메일을 입력하세요 : ")
        self.addr = input("주소를 입력하세요 : ")
    def print_info(self):
        print("이름 :",self.name)
        print("핸드폰번호 : "+self.phone[0:3]+'-'+self.phone[3:7]+'-'+self.phone[7:])
        print("메일 :",self.mail)
        print("주소 :",self.addr)
    def save_db(self):
        import sqlite3
        conn = sqlite3.connect("C:/data/contact5.db") 
        c = conn.cursor()
        c.execute("create table contact(fullname text, cellphone text, email text, address text)") 
        c.execute("insert into contact(fullname, cellphone, email, address) values(?,?,?,?)", (self.name, self.phone, self.mail, self.addr))
        c.execute("select * from contact")
        c.fetchone()
        conn.commit()
        c.close()
        conn.close()

per1 = Contact()
per1.set_contact()
per1.print_info()
per1.save_db()


## Another solution 
class Contact:
    def __init__(self,name, pn, email, addr):
        self.name = name
        self.pn = pn
        self.email = email
        self.addr = addr
    def print_info(self):
        print("이름 : {} ".format(self.name))
        print("핸드폰번호 : {} ".format(self.pn))
        print("메일 : {} ".format(self.email))
        print("주소 : {} ".format(self.addr))
    def set_contact():
        name = input("이름을 입력하세요 : ")
        pn = input("핸드폰번호를 입력하세요 : ")
        email = input("메일을 입력하세요 : ")
        addr = input("주소를 입력하세요 : ")
        conIns = Contact(name, pn, email, addr)
        conIns.print_info()

set_contact()

# [문제188] Contact 클래스 이용해서 입력 들어 온 값들을 c:/data/contact.db 에 저장해서 관리하세요.
class Contact:
    def __init__(self):
        self.name = '' ### 변수 선언 
        self.phone = ''
        self.mail = ''
        self.addr = ''
    def set_contact(self):
        self.name = input("이름을 입력하세요 : ")
        self.phone = input("핸드폰번호를 입력하세요 : ")
        self.mail = input("메일을 입력하세요 : ")
        self.addr = input("주소를 입력하세요 : ")
    def print_info(self):
        print("이름 :",self.name)
        print("핸드폰번호 : "+self.phone[0:3]+'-'+self.phone[3:7]+'-'+self.phone[7:])
        print("메일 :",self.mail)
        print("주소 :",self.addr)
    def save_db(self):
        import sqlite3
        conn = sqlite3.connect("C:/data/contact.db") 
        c = conn.cursor()
        c.execute("create table contact(fullname text, cellphone text, email text, address text)") 
        c.execute("insert into contact(fullname, cellphone, email, address) values(?,?,?,?)", (self.name, self.phone, self.mail, self.addr))
        conn.commit()
        c.close()
        conn.close()
    def insert_data(self):
        import sqlite3
        conn = sqlite3.connect("C:/data/contact.db") 
        c = conn.cursor()
        c.execute("insert into contact(fullname, cellphone, email, address) values(?,?,?,?)", (self.name, self.phone, self.mail, self.addr))
        conn.commit()
        c.close()
        conn.close()

per1 = Contact()
per1.set_contact()
per1.print_info()
per1.save_db()
per1.insert_data()

import sqlite3
conn = sqlite3.connect("C:/data/contact.db") 
c = conn.cursor()
c.execute("select * from contact")
c.fetchall()
c.close()
conn.close()

## Another solution 
import sqlite3

class Contact:
    def __init__(self,name, pn, email, addr):
        self.name = name
        self.pn = pn
        self.email = email
        self.addr = addr
    def print_info(self):
        print("이름 : {} ".format(self.name))
        print("핸드폰번호 : {} ".format(self.pn))
        print("메일 : {} ".format(self.email))
        print("주소 : {} ".format(self.addr))
    def input(self):
        self.conn = sqlite3.connect('c:/data/contact.db')
        self.c = self.conn.cursor()
        self.c.execute("insert into contact(name, pn, mail, addr) values(?,?,?,?)",(self.name,self.pn,self.email,self.addr))
        self.c.execute('select * from contact')
        print(self.c.fetchall()) ### fetch할 때 print() 써야 함!!! 
    def commit(self):
        self.conn.commit()
    def rollback(self):
        self.conn.rollback()
    def close(self):
        self.c.close()
        self.conn.close()
    def set_contact():
        name = input("이름을 입력하세요 : ")
        pn = input("핸드폰번호를 입력하세요 : ")
        email = input("메일을 입력하세요 : ")
        addr = input("주소를 입력하세요 : ")
        conIns = Contact(name, pn, email, addr)
        conIns.print_info()
        conIns.input()
        conIns.commit()
        conIns.close()

set_contact()

## 모듈화 
### Contact.py 파일로 만들 것! 
import sys
sys.path 
sys.path.append("C:\data") ### 경로 제외: sys.path.remove("C:\data")
from Contact import * 

# [문제189] 초기 생성자에는 이름, 주소, 급여를 입력값으로 받고 아래와 같이 출력되는 클래스를 생성하세요. 
# 인스턴스 생성될때 마다 건수를 출력해주세요.
""" 
사원수 : 1
이름 : 홍길동 , 주소 : 덴마크,  급여 : 1000

사원수 : 2
이름 : 홍아들 , 주소 : 노르웨이,  급여 : 2000
""" 
class Employee:
    count = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Employee.count += 1
    def print_info(self):
        print("사원수 : " + str(Employee.count))
        print("이름 : "+self.name+" , 주소 : "+self.addr+",  급여 : "+str(self.sal))

e1 = Employee('오주혜','독일',20000)
e1.print_info()

e2 = Employee('곽윤신','일본',10000)
e2.print_info()

## Another solution 
class Employee:
    empCn = 0
    def __init__(self, name, addr, salary):
        self.name = name
        self.addr = addr
        self.salary = salary
        Employee.empCn += 1
    def printCount(self):
        print("사원수 : %d" %Employee.empCn)
    def printEmployee(self):
        print( "이름 : {} , 주소 : {},  급여 : {}".format(self.name, self.addr, self.salary))

emp1 = Employee("홍길동","덴마크", 1000)
emp1.printCount()
emp1.printEmployee()

emp2 = Employee("홍아들","노르웨이", 2000)
emp2.printCount()
emp2.printEmployee()

# [문제190] 
"""
출력화면 
2001 01 01 남성
1999 02 02 여성 
"""
id_number1 = "010101-3234567"
id_number2 = "990202-2123456"

class SSN:
    def __init__(self, id_num):
        self.id_num = id_num
    def print_info(self):
        if self.id_num[7] == '1':
            print('19'+self.id_num[0:2]+' '+self.id_num[2:4]+' '+self.id_num[4:6]+' '+'남성')
        elif self.id_num[7] == '2':
            print('19'+self.id_num[0:2]+' '+self.id_num[2:4]+' '+self.id_num[4:6]+' '+'여성')
        elif self.id_num[7] == '3':
            print('20'+self.id_num[0:2]+' '+self.id_num[2:4]+' '+self.id_num[4:6]+' '+'남성')
        elif self.id_num[7] == '4':
            print('20'+self.id_num[0:2]+' '+self.id_num[2:4]+' '+self.id_num[4:6]+' '+'여성')
        else:
            print('Invalid Social Security Number')

s1 = SSN("010101-3234567")
s1.print_info()

s2 = SSN("990202-2123456")
s2.print_info() 

# [문제191] Person 클래스를 생성하세요. 생성자는 이름, 나이, 성별을 만드세요.
# Person 클래스 에는 printMe 메소드를 생성하셔서 이름, 나이 성별을 출력합니다.

"""
Employees클래스를 생성한후 Person상속받습니다.
생성자는 이름, 나이, 성별, 주소, 생일입니다.
단 이름, 나이, 성별은 person에서 상속받으세요.
Employees 클래스에 printMe를 재구성하셔서 주소, 생일을 출력하세요.


myPerson = Person("홍길동","10", "남")
myPerson.printMe()

myEmployee = Employee("송준기", "2", "남", "서울", "2016년 01월 01일")
myEmployee.printMe()



이름은 홍길동 ,  나이는 10살 이고, 성별은 남 입니다.
이름은 송준기 ,  나이는 2살 이고, 성별은 남 입니다.
집 주소는  서울  생일은  2016년 01월 01일 입니다. 
"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def printMe(self):
        print("이름은 {} ,  나이는 {}살 이고, 성별은 {} 입니다." .format(self.name, self.age, self.gender))
        
class Employee(Person):
    def __init__(self, name, age, gender, addr, day):
        Person.__init__(self, name, age, gender)
        self.addr = addr
        self.day = day
    def printMe(self):
        Person.printMe(self)
        print("집 주소는  {}  생일은  {} 입니다." .format(self.addr, self.day))

myPerson = Person("오주혜","23", "여")
myPerson.printMe()

myEmployee = Employee("곽윤신", "29", "남", "일본", "1989년 05월 05일")
myEmployee.printMe()

# [문제192] Add 클래스에 두수를 더하는 값을 리턴하는 add 메소드 생성
# Multiply 클래스에 두수를 곱한값을 리턴하는 multiply 메소드 생성
# Divide 클래스에 두수를 나눈값을 리턴하는 divide메소드 생성
# Calculator클래스에는 Add, Multiply, Divide 상속받고 두수를 뺀값을 리턴하는 sub 메소드 생성하세요. 

class Add:
    def add(self, x, y):
        return x+y

class Multiply:
    def multiply(self, x, y):
        return x*y

class Divide:
    def divide(self, x, y):
        if y == 0:
            return "infinity"
        return x/y

class Calculator(Add, Multiply, Divide):
    pass ### 상위 클래스의 속성들을 "전부" 상속 받음 
    def sub(self, x, y):
        return x-y

x1 = Calculator()
x1.add(1,2)
x1.divide(1,2)
x1.multiply(1,2)
x1.sub(2,1)
x1.divide(0,2)
x1.divide(2,0)

# [문제193] 양의 정수값만 입력 받아서 나누기를 수행하는 positive_divide 함수를 생성하세요.

"""
print(positive_divide())
 
분자 숫자를 입력하세요 : 10
 분모 숫자를 입력하세요 : 2
5.0

print(positive_divide()) 
 
 분자 숫자를 입력하세요 : 10
 분모 숫자를 입력하세요 : -2
오류  - 음수로 나눌수 없습니다. -2


print(positive_divide())

 분자 숫자를 입력하세요 : 10
 분모 숫자를 입력하세요 : 0
오류 -  0으로 나눌수 없습니다. division by zero
""" 

def positive_divide():
    num = int(input("분자 숫자를 입력하세요 : "))
    den = int(input("분모 숫자를 입력하세요 : ")) 
    
    try: 
        if den < 0:
            print("오류  - 음수로 나눌수 없습니다. {}" .format(den))
        else:
            return num/den
    except ZeroDivisionError as error:
        print("오류 -  0으로 나눌수 없습니다.", error)
        
positive_divide()

## Other solutions 
def  positive_divide():
    try:
      
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))
        
        if(y < 0):  
            raise ValueError
        return  x / y
    except ValueError as error:
        print('오류  - 음수로 나눌수 없습니다.', error)
    except ZeroDivisionError as error:
        print('오류 -  0으로 나눌수 없습니다.',error)

positive_divide()

def  positive_divide():
    try:   
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))        
        if(y < 0):  
            raise ValueError
        return  x / y
    except ValueError:
        print('오류  - 음수로 나눌수 없습니다.', y)
    except ZeroDivisionError as error:
        print('오류 -  0으로 나눌수 없습니다.',error)

positive_divide()

class NegativeDivisionError(Exception):
    def __init__(self, value):
        self.value = value     
def  positive_divide():
    try:
        # n = NegativeDivisionError      
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))     
        if(y < 0):  
            raise NegativeDivisionError(y)
        return  x / y
    except NegativeDivisionError as error:
        print('오류  - 음수로 나눌수 없습니다.', error)
    except ZeroDivisionError as error:
        print('오류 -  0으로 나눌수 없습니다.',error)

positive_divide()

# [문제194] 한주간동안 걸음수를 요일별로 그래프를 그리세요.
# 단 막대그래프 함수를 생성해서 인수값으로 걸음수, 요일을 입력하면 그래프가 그려지도록하세요.
def steps(*data):
    from pandas import Series, DataFrame 
    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc
    
    data = [i for i in data]
    df = DataFrame(data, index=['월','화','수','목','금','토','일'])
    df.plot(kind='bar')

steps(1000,2000,3000,2000,3500,2300,2800)

## Another solution 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def create_bar_chart(data, labels,bar):
    num_bars = len(data)
    positions = range(1, num_bars+1)
    if bar == 1:        
        plt.bar(positions, data, align='center')
        plt.xticks(positions, labels)
        plt.xlabel('요일')
        plt.ylabel('걸음수')      
    else:
         plt.barh(positions, data, align='center')
         plt.yticks(positions, labels)
         plt.xlabel('걸음수')
         plt.ylabel('요일')

    plt.title('한주간 동안 걸음수') 
    plt.grid()
    plt.show()
    
if __name__=='__main__':
    step = [1090,2000,3000,4000,10000,50000,2000]
    labels = ['월','화','수','목','금','토','일']
    create_bar_chart(step,labels,2)

# [문제195] 클래스로 만듬
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
 
class Step:
    def __init__(self, *data):
        self.data = [i for i in data]
    def steps(self, *data): 
        self.data = [i for i in data]
        df = DataFrame(self.data, index=['월','화','수','목','금','토','일'])
        return df.plot(kind='bar')

if __name__=='__main__':
    steps(11000,12000,13000,12000,13500,12300,12800)

s1 = Step()
s1.steps(11000,12000,13000,12000,13500,12300,12800)

import sys
sys.path
sys.path.append("C:/data")

from step import *
s1 = Step()
s1.steps(11000,12000,13000,12000,13500,12300,12800)

## Another solution 
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class create_bar_chart:
    def __init__(self,data, labels, bar):
        self.data = data
        self.labels = labels
        self.bar = bar        
    def create_bar_chart(self):    
        num_bars = len(self.data)
        positions = range(1, num_bars+1)
        if self.bar == 1:
            plt.bar(positions, self.data, align='center')
            plt.xticks(positions, self.labels)
            plt.xlabel('요일')
            plt.ylabel('걸음수')        
        else:
            plt.barh(positions, self.data, align='center')
            plt.yticks(positions, self.labels)
            plt.xlabel('걸음수')
            plt.ylabel('요일') 
        plt.title('한주간 동안 걸음수') 
        plt.grid()
        plt.show()
    
if __name__=='__main__':
    step = [5000,6000,7500,10000,10000,20000,2000]
    labels = ['월','화','수','목','금','토','일']
    cbc = create_bar_chart(step,labels,1)
    cbc.create_bar_chart()

# [문제196] knn 프로그램을 작성하세요.
"""
      pointlist[(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]
       

        <수행>
        knn([2,1],pointlist,2)

        <결과>
   [(1, 1), (2, 0)]
"""    
# 답1
 
import numpy as np
import operator
from math import sqrt

point = [2,1]
k = 2
pointlist=[(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]

def knn(point, lists, k):   
    dic={}  
    for p in lists:      
        d = dist(point, p)    
        dic[p]=d
    res = []
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))         
    for key in sorted_dic:
        if len(res) < k:            
            res.append(key[0])           
    return res
 
def dist(x, y):
    x = np.array(x)
    y = np.array(y)  
    return  sqrt(sum(pow(x - y,2)))

knn(point,pointlist,k)

from sklearn.neighbors import NearestNeighbors
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)
indices  
distances
nbrs.kneighbors_graph(X).toarray()

# [문제197] 키, 몸무게에 따른 성별을 분류해주세요.

## 키, 몸무게 데이터
data = np.array([[158, 64],
[170, 86],
[183, 84],
[191, 80],
[155, 49],
[163, 59],
[180, 67],
[158, 54],
[170, 67]])

one = np.array([155, 70])

## 성별 레벨
gender = np.array(['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']) ### np.take()할 때 집어넣을 것! 

## [155, 70] 성별을 분류하세요.
## 'female'
distances = np.sqrt(np.sum(pow(one - data, 2), axis=1)) 
indices = distances.argsort()[:3]
nn = np.take(gender, indices, axis = 0)

from collections import Counter
c = Counter(nn) 
freq = c.most_common(1)[0][0]
freq

df = DataFrame({'height':data[:,0], 'weight':data[:,1], 'gender':gender})



## 다른 test data 사용
Julia = np.array([155,53])
distances = np.sqrt(np.sum(pow(Julia - data, 2), axis=1)) 
indices = distances.argsort()[:3]
nn = np.take(gender, indices, axis = 0)
from collections import Counter
c = Counter(nn) 
freq = c.most_common(1)[0][0]
freq



## KNeighborsClassifier 이용 
from sklearn.neighbors import KNeighborsClassifier as knn
clf = knn(n_neighbors = 3)
clf.fit(data, gender)
clf.predict(np.array([155,53]).reshape(1,-1))[0] ### data는 2차원 -> 비교하는 값도 2차원으로 만들어줘야 함!(reshape) <- reshape(1,2) 이렇게 써도 됨
clf.predict(np.array([[155,53]]))[0] ### 이렇게 괄호를 하나 더 씌워도 됨 

clf.predict(np.array([[176,70]]))[0]

# [문제198] 상품구매여부를 knn으로 분류해주세요.
import pandas as pd
buy = pd.read_csv("C:/data/buy.csv")      
buy
train = buy.loc[:19,['나이','월수입']]
test = buy.loc[20,['나이','월수입']]
label = buy.loc[:19,'상품구매여부'] ### label 만들 때 주의! 

import numpy as np
distances = np.sqrt(np.sum(pow(test - train, 2), axis=1))
indices = distances.argsort()[:3]
n = np.take(label, indices, axis = 0)
from collections import Counter
c = Counter(n)
c.most_common(1)[0][0]

## KNeighborsClassifier 이용 
from sklearn.neighbors import KNeighborsClassifier as knn
clf = knn(n_neighbors = 3)
clf.fit(train, label)
clf.predict(np.array(test).reshape(1,2))[0] ### KNeighborsClassifier 사용할 때는 np.array로 변환! 

## Another solution 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
import pandas  as  pd
import numpy as np

df = pd.read_csv("c:/data/buy.csv")
                  
x_train = np.array([scale(df['나이']),scale(df['월수입'])]).T
label = list(df['상품구매여부'])
age_mean = np.mean(df['나이'])
age_std = np.std(df['나이'])

pay_mean = np.mean(df['월수입'])
pay_std = np.std(df['월수입'])

K = 3
clf = KNeighborsClassifier(n_neighbors=K)
clf.fit(x_train,label)
prediction_label = clf.predict(np.array([[(40-age_mean)/age_std, (500-pay_mean)/pay_std]]))[0]
prediction_label

# [문제199]
## 테니스유무: 목표변수 
from scipy.stats import chisquare
import pandas as pd
import numpy as np
tree = pd.read_csv("C:/data/tree.csv")
tree
tree[['습도','테니스유무']]
a = np.array(tree['습도'])
b = np.array(tree['테니스유무'])
c = pd.crosstab(a,b, rownames=['습도'], colnames=['테니스유무']) ### array형 주의! 
## chi-stats가 가장 작은 컬럼(최적의 변수)을 우선적으로 생각! 

a = np.array(tree['바람'])
b = np.array(tree['테니스유무'])
c = pd.crosstab(a,b, rownames=['바람'], colnames=['테니스유무'])

from scipy.stats import chi2_contingency
from scipy.stats import chi2
stat, p, dof, expected = chi2_contingency(c)
# interpret test-statistic
prob = 0.99
critical = chi2.ppf(prob, dof)
if abs(stat) >= critical:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
