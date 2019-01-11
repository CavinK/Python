
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:25:34 2018

@author: Cavin
"""





"""
09-04-2018 
"""
# procedure, function, package <- 어디서 호출하는 지에 따라 다름! 
# procedure
# function
# package: procedure와 function을 합침, 글로벌 변수 표현 

# R: 통계에 국한 
# Python: 보다 범용적(통계, 게임, 시스템 유틸리티, ...) 

# 32-bit vs 64-bit <- 주소의 체계(도로의 차선 수에 비유하면 이해하기 쉬움) 



# Python

## 1990년 암스테르담 귀도 반 로섬(Guido van Rossum) 개발한 인터프리터 언어 
## 인터프리터 언어는 "한줄씩" 소스 코드를 해석해서 바로 실행해 결과를 확인할 수 있는 언어(easy, 직관적) 
## -> R도 인터프리터 언어(한줄씩 실행) 
## cf. C, Java는 인터프리터 언어가 아님!

## BBC에서 방영되는 Monty pythons flying circus tv프로그램 이름 

## Python -> 객체 지향 프로그래밍 언어(반복되는 구문을 심플하게!) -> 클래스 이용 
## cf. C -> 구조적 언어 

# python 특징 
## - 문법이 아주 쉽다. 
## - 가독성 좋다. 
## - 풍부한 라이브러리 <- R처럼 모듈 갖다 써도 되지만, 그래도 어느 정도의 프로그래밍 스킬이 필요 
### 	- numpy: 수학, 과학 모듈
### 	- pandas: 데이터 검색 모듈
### 	- beautiple soup: 웹스크롤링 모듈
### 	- scikit-learn: 머신러닝 모듈 
## - 이식성
### 	- 쉽게 라이브러리를 추가할 수 있다(Java에서 짠 프로그램을 파이썬에 연동) 
### 	- 파이썬은 C언어로 구현된 부분이어서 C계열 프로그램은 사용하기 편하다. 
## - 무료 
### 	- FLOSS(Free Libre and Open Source Software) 
### 	- 자유 오픈 소스 소프트웨어 
### 	- 소프트웨어의 복사본을 마음대로 배포할 수 있고 소스코드가 공개되어 있어 언제든지 읽을 수 있으며 
### 	  필요한 부분을 고칠수 있고 새로운 자유 소프트웨어를 작성할 때 이 프로그램의 일부를 사용해도 된다는 의미
### 	- FLOSS는 지식을 공유하는 공동체 
## - 동적타이밍 
### 	- 런타임시에 TYPE을 체크를 하는 동적타이밍을 지원 <- ex. R도 코드 실행할 때마다 일일히 변수 선언하지 않음! 
### 	- 메모리관리를 자동(다른 언어보다 메모리를 덜 잡고 수행) 

# 파이썬언어로 할수 있는 일
## 1. 시스템 유틸리티
## 2. GUI 프로그램 
## 3. C, C++ 결합 
## 4. 웹프로그래밍(장고) 
## 5. 수치연산프로그래밍
## 6. 데이터베이스 프로그래밍
## 7. 머신러닝, 딥러닝 

# 파이썬 종류
## Cython(C), jython(Java), Ironpython(C#), pypy(python) 

print("오늘하루도 행복하자") ### print() 출력 기능 
# 사칙연산 
1 + 2
2 - 1
2 * 3
7 / 2 ### 부동소수점 나누기 
7 // 2 ### 나눗셈의 몫(정수나누기, 소수점이하는 버림) cf. R: 7 %/%2
7 % 2 ### 나눗셈의 나머지 cf. R: 7 %% 2
2 ** 3 ### 제곱연산 cf. SQL: power() 



# 수학 관련 메소드 -> math(import하는 모듈을 앞에 꼭 써야 함!) 
import math
math.pow(2,3)

# 연산자 우선순위
1 + 2 * 3 * 2 ** 3 ### 거듭제곱(**) > 곱하기(*) > 더하기(+)
(1 + 2) * 3 * 2 ** 3 ### 괄호 활용! 
## ()
## **
## * /
## + -



# 변수(variable)
## - 데이터를 저장할수 있는 메모리 공간 
## - 변수이름: 첫글자는 영문, _(밑줄) <- Python은 .으로 시작 안 됨!(cf. R은 가능) 
## - 두번째 글자부터는 영문자, 숫자, _
## - 대소문자 구분한다. 
## - 예약어는 사용할 수 없다 

## 예약어 확인
import keyword ### 모듈 이름
keyword.kwlist

## =: 변수 대입 
x = 10

## type(): 해당 변수의 타입 확인 가능
### R에서는 str(), class(), mode()로 확인! 
type(x) ### int

## 연산자 축약으로 사용 
### +=, -=, *=, /=, //= 
a = 1
a = a+1
a += 1 
print(a) 
a = a-1
a -= 1
print(a)
a = a*1
a *= 1
a = a/2
a /= 2
a = a//2
a //= 2

f = 10.12
type(f) ### float <- 부동소수점 <- cf. R: numeric 
f = 10.4e3 ### 지수표현 <- 10.4 * 10**3 <- "e=10" 
type(f) 

## 논리연산자 
### ==, !=, >, <, >=, <=, and, or, not 
x = 1
y = 2
y > x ### True 
y >= x
y < x ### False 
y <= x
y == x
y != x

2 > 1 and 3 > 2
2 > 1 or 3 > 2
not 1 > 2

## dir(): 선언되어 있는 변수들 이름 확인 cf. R: ls()
dir() ### 값은 안 보임 
locals()
del(x) ### 변수 삭제 

## 문자열
'대한민국'
'짝짝짝'
"""대한민국
짝짝짝""" ### 실행해보면, "\n"이 껴 있음(줄바꿈)

## escape 식별자
### 1. \n: 줄바꿈
print("오늘 하루도 \n 행복하자")
### 2. \t: tab key
print("오늘 하루도 \t 행복하자")
print("잘하자 \t 파이썬")
### 3. \0: null
print("잘하자 \0 파이썬") ### 그냥 공백문자 하나 들어감!
### 4. \\: \표시
print("잘하자 \0 파이썬 \\R")
### 5. \': 따옴표 표현
print("잘하자 \'파이썬\'")
print("잘하자 '파이썬'") ### 그냥 이렇게 써도 상관 없음! (R과 비슷)

x = '홍길동'
y = '파이썬개발자'
type(x) ### str 
type(y)

## string에 사칙연산 사용 가능! 
### +: 문자 연결
x + y ### 문자 + 문자 연결연산자 cf. R: paste0()
### *: 문자 반복 
(x + y)*2 ### 문자 반복 작업, 두번복제(*) cf. R: rep() 
print("=" * 15)
print("hello world")
print("=" * 15)

## {} .format(): literal 문자 사이에 변수 집어넣는 메소드 
## %() <- 포맷팅 코드(%d, %s) 표현 
name = "제임스"
music = "클래식"
print("안녕하세요. {}입니다. 즐겨듣는 음악은 {}입니다." .format(name, music)) ### 문장 사이에 변수 집어넣음! 
print("안녕하세요. %s입니다. 즐겨듣는 음악은 %s입니다." %(name, music)) ### %: type까지 구분! 

##################################
## 포맷팅 코드
### %s: 문자열
### %d: 정수 
### %f: 실수 
##################################

x = 996
y = 8
result = x % y
print("{}를 {} 나누면 {}가 나머지 입니다." .format(x,y,result))
print("%d를 %d 나누면 %d가 나머지 입니다." %(x,y,result))

result1 = x // y
result2 = x % y
print("%d를 %d 나누면 %d는 몫이고 %d 나머지입니다." %(x,y,result1,result2))

## divmod(): 두 변수의 몫과 나머지를 동시에 추출 
divmod(x,y) ### 두 숫자가 1차원 배열(벡터) 안에 들어 있음
divmod(x,y)[0] ### Python은 배열이 0부터 시작!! 
divmod(x,y)[1]

print("원주율은 %d 입니다." %3.14159) ### 3이라고만 출력됨!(%d는 정수로만 표현됨)
print("원주율은 {} 입니다." .format(3.14159)) ### 이건 문자형으로 출력! 
print("원주율은 %f 입니다." %3.14159) ### %f: 실수 표현 



x = "행복한 하루를 보내자"
print(x)

## len(): 문자 길이 리턴 
len(x)

## 인덱싱 & 슬라이싱 
### x[1:5] <- 1<=x<5 <- 부등호 주의! 
x[0] ### x변수(문장)의 첫번째 글자 리턴
x[:] ### 전부 뽑아짐 
x[1]
x[-1] ### 맨 마지막 글자
x[0:3] ### x[시작요소번호 : 끝요소번호-1] <- 맨 마지막 숫자는 안 나옴! 
x[:3] ### 앞의 3글자만 리턴 
x[3:] ### 앞의 3글자 빼고 리턴 

x[4:-5] ### "하루"만 뽑아짐 <- 외울 것! 
x[::2] ### 짝수 번호에 해당되는 요소만 제외 
x[1:7:2] ### 1번과 6(7-1)번 사이에서 짝수 
x[5::2] ### 5번부터 시작해서 짝수 
x[::-1] ### 문장 순서 reverse 

x[1:7]
x[1:7:2]



# 문자 함수
## 변수이름.replace(이전값, 수정값)
x = "파리썬"
x.replace("리","이") ### x에 바로 수정 안 됨(함수는 미리보기!) -> 변수에 담아놓는 작업 해야함! 
x = x.replace("리","이")
x

## 변수이름.startswith()
### 원본 문자열이 매개변수로 입력한 문자열로 시작되는지를 판단 
x = "hello world"
x.startswith("h") ### True 
x.startswith("H") ### False <- Python은 대소문자 구분 

## 변수이름.endswith()
### 원본 문자열이 매개변수로 입력한 문자열로 끝나는지를 판단 
x.endswith("ld") ### True 
x.endswith("D") ### False 

## 변수이름.find()
### 원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서부터 찾는다. 
### 만약에 존재하지 않으면 "-1"로 나온다. (0번방이 존재하기 때문)
x.find("w") ### 6번 요소에 있다고 알려줌 
x.find("world") ### 6 
x.find("W") ### -1 <- 없다는 뜻 

## 변수이름.count()
### 원본 문자열 안에 매개변수로 입력한 문자열이 몇번 나오는지에 대한 건수 
x.count("l")

## 변수이름.upper()
### 원본 문자열을 대문자로 변환 
x.upper()

## 변수이름.lower()
### 원본 문자열을 소문자로 변환
x.lower()

## 변수이름.capitalize()
### 원본 문자열을 첫글자 대문자 변환 
x.capitalize()

## 변수이름.title()
### 모든 단어의 첫글자 대문자로 변환
x.title()

## 변수이름.swapcase()
### 대문자를 소문자로, 소문자를 대문자로 변환 
s = "HELLO, world"
s.swapcase()

## 변수이름.center(숫자)
### 원본 문자열을 지정한 공간에서 중앙에 배치 
s.center(20)

## 변수이름.ljust(숫자)
### 원본 문자열을 지정한 공간에 왼쪽에 배치 
s.ljust(20)

## 변수이름.rjust(숫자)
### 원본 문자열을 지정한 공간에 오른쪽에 배치 
s.rjust(20)

## 변수이름.strip()
### 원본 문자열 양쪽에 공백을 제거 
x = "                             hello                               "
x
x.strip()

## 변수이름.lstrip()
### 원본 문자열 왼쪽에 공백을 제거 
x.lstrip()

## 변수이름.rstrip()
### 원본 문자열 오른쪽에 공백을 제거 
x.rstrip()

### 공백 뿐만 아니라 글자도 제거 가능! 
x = 'hello'
x.strip('h') ### h가 없어짐 
x.lstrip('h') ### 왼쪽 h 제거 
x.rstrip('h') ### 오른쪽 h 제거 

## 변수이름.isalpha()
### 원본 문자열이 숫자, 기호를 제외한 알파벳, 한글로 이루어졌는지 확인 
x = "hello"
y = "hello2018"
z = "안녕하세요"

x.isalpha() ### True
y.isalpha() ### False <- 숫자 포함! 
z.isalpha() ### True 

## 변수이름.isalnum()
### 원본 문자열이 알파벳, 숫자로 이루어져 있는지 확인 
### 알파벳만 들어 있어도 True, 알파벳+숫자로 들어 있어도 True 
x.isalnum() ### True
y.isalnum() ### True
z.isalnum() ### True

## 변수이름.isnumeric()
### 원본 문자열이 수로만 이루어져 있는지 확인 
x.isnumeric() ### False
y.isnumeric() ### False 
z.isnumeric() ### False 

d = "2018"
d.isnumeric() ### True(type이 str인데 True로 나옴!)
type(d)

## 변수이름.replace(이전꺼, 수정하려는거)
### 원본 문자열에서 어떤 문자열을 찾아서 새로운 문자열로 변경 
x.replace("hello","python")

## 변수이름.index()
### 원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서부터 찾는다. 없으면 오류
### cf. 변수이름.find() <- 없으면 -1이라고 리턴 
x.find('o') ### 4 
x.find('O') ### -1(존재하지 않음)
x.index('o') ### 4
x.index('O') ### 오류!

## 변수이름.rfind()
### 존재하는 위치를 "뒤에서부터" 찾음 
x.rfind('o')

## in 연산자를 이용해서 문자열이 존재여부를 확인 -> True/False로 리턴  
'o' in x ### True

## 변수이름.split()
### 원본 문자열에 매개변수로 입력한 문자열을 기준으로 원본 문자열을 나눠 리스트로 만든다 
x = "hello, world" 
x.split(',') ### ','를 기준으로 2개의 글자로 나뉨 

## 문자열.join()
### 원본 글자 사이에 특정한 문자열을 추가한다. 
x = 'abc'
x = ','.join(x)
x ### 글자들이 ,를 기준으로 나뉘었음 



## input(): 문자형으로 받음! 
x = input() ### 커맨드라인에 값 입력하면 변수에 저장됨! 
y = input()
x + y ### 12341234로 나옴!(문자 타입)
type(x) ### str

int(x) + int(y) ### int(): integer형으로 바뀜! 



# R의 자료형
## 1. vector: 같은 데이터 타입을 갖는 1차원 배열 
## 2. list: 서로 다른 데이터 타입을 갖는 1차원 배열, 중첩 가능 <- list(컬럼명 = 값, 컬럼명 = 값)
## 3. matrix: 같은 데이터 타입을 갖는 2차원 배열 <- matrix(벡터, nrow, ncol, byrow = T/F, dimnames = list(c(행), c(열)))
## 4. array: 같은 데이터 타입을 갖는 3차원 배열 <- array(c(데이터), dim = c(행,열,면)) <- x[,,1]
## 5. factor: 목록, 범주형 데이터 <- factor(c(특정값), c(레벨)) // ordered()
## 6. data.frame: 서로 다른 데이터 타입을 갖는 컬럼으로 이루어진 2차원 배열 <- data.frame(컬럼명1 = c(값), 컬럼명2 = c(값)) <- list를 모아놓은 거! 
## 7. table: data.frame 동일한 구조를 갖는데 속도가 빠르다. 

# Python의 자료형
## 1. list([]): "서로 다른" 데이터 타입을 갖는 1차원 배열 
## 2. tuple(()): 차이점은 수정, 삭제, 추가 안된다 <- 데이터 분석할 땐 잘 안 씀! 
## 3. dictionary({key:value}): key(키)와 value(값)를 확인하는 자료형(key와 value를 한 쌍으로 저장) <- 영한사전처럼 단어와 그 의미를 짝지어 저장 <- 빈도수 체크할 때 사용! 
## 4. set({}, set()): index가 없다. 중복을 허용하지 않는다. <- 유일키 
## 5. bool(True/False): 참(True), 거짓(False)을 나타내는 자료형

# 1. list([])
##          "서로 다른" 데이터 타입을 갖는 1차원 배열 
##          데이터의 목록을 다루는 자료형
##          []로 표현 
##          중첩 가능!(R과 비슷) 
x = [10,20,30]
x
len(x) ### 3
type(x) ### list 

## 리스트 인덱싱
x[0]
x[-1]

## 리스트 슬라이싱 [시작 : 끝-1]
x[0:2]
x[1:]
x[:-1]
x[-1:]

## 리스트 값 수정 
x[0] = 100
x[1:3] = [200,300]

## 리스트변수 끝에 값을 추가 
x.append(400)
x

## 기존 리스트 변수에 다른 리스트변수를 이어 붙이는 방법 
x1 = [600,700]
x1
x.extend(x1)
x

## 인덱스를 사용하여 특정 위치에 값을 입력하는 방법
x.insert(4,500)

## + 를 이용해서 리스트변수 결합하는 방법 
x2 = [800, 900, 1000]
x = x + x2 ### 이렇게 해도 이어 붙일 수 있음! 
x

## 리스트변수에 있는 값 중에 마지막값을 제거하는 방법 
x.pop()
x
x.pop(4) ### 4번째 인덱스에 있는 값을 pop 
x

## 리스트 인덱스 값을 삭제하는 방법 
del x[3]
x

drink = ['콜라','사이다','환타','콜라','사이다','콜라']
len(drink)
drink.count("콜라")
drink.find("콜라") ### list는 find()를 쓸 수 없음 
drink.index("콜라") ### 첫번째로 나온 거에 해당되는 인덱스 밖에 안 나옴 
drink.index("콜라",1) ### 1번 인덱스 다음에 나오는 거에 해당되는 인덱스 -> 3번으로 나왔으면, 그 다음부터는 4를 입력하고 검색해야 함! 
drink.index("콜라",4) ### 모든 걸 한 번에 보는 메소드는 없음 -> 구현! 

## 리스트변수에 값을 기준으로 삭제 
drink.remove("콜라")
drink ### 맨 첫번째 꺼 하나 밖에 안 없어졌음! -> 다 remove하기 위해 여러 번 수행해야 함!(count()를 먼저 할 필요가 있음)
drink.remove("콜라")
drink





"""
09-05-2018
"""
# 중첩 리스트
## 리스트 안에 리스트 
## R에서는 list() 함수 사용
## Python에서는 [] 사용(x = []) 
x = [1,2,3,['a','b','c'],4,5]
x
x[2:5] ### 인덱스 2번부터 4번까지 뽑아냄 
x[3] ### 중첩된 리스트를 뽑아냄 
x[3][0] ### 중첩된 리스트 중에서 0번 요소를 뽑아냄 
x[3][0:2] ### 중첩된 리스트 중에서 0번과 1번 요소를 뽑아냄 
x[3][-1]
x[3].append('d') ### 중첩된 리스트에 값 추가 
del x[3][3] ### 중첩된 리스트 중에서 3번 요소를 삭제 
x

x[3][0] = x[3][0].upper() ### 수정하려면 이렇게 변수에 대입시켜줘야 함 
x[3][1] = x[3][1].upper()
x[3][2] = x[3][2].upper() ### 중첩된 리스트에 있는 모든 변수가 한 번에 수정 안 됨! => 이렇게 일일히 바꿔줘야 함 
                          ### x[3] = x[3].upper() <- 이런 식으로 안 됨! 
x
type(x[3][0])
type(x[3][0:1])

x[0] = x[0] * 10
x
x[3][0] = x[3][0] * 2 

## 리스트 변수에 값을 다 지운다. 
x.clear()
x ### 값들은 없어졌어도 리스트 타입은 남아 있음! 

# 정렬 
x = [1,5,3,4,2]

## 변수명.sort()
x.sort()
x.sort
x.sort(reverse=True) ### 내림차순 
x

## cf1. 변수명.reverse()
### 정렬 작업을 하는 게 아니라, 기존에 나열된 값들을 그냥 반대로 바꿔놓음! <- 변수명.sort()와 다름!! 
### 리스트 인덱스 순서를 반대로 뒤집을 때 사용 
x = [1,5,3,4,2]
x.reverse() 
x

## cf2. sorted(변수명)
sorted(x) ### 미리보기 <- 변수에 대입해야 함! cf. 변수명.sort(): 그냥 아예 정렬시킴 
sorted(x,reverse=True) ### 내림차순 



# 2. tuple
##          리스트자료형과 똑같다. 
##          차이점은 수정, 삭제, 추가 안된다 <- 상수처럼 사용! 
##          리스트 [], 튜플 () 
list1 = []
type(list1)
tuple1 = ()
type(tuple1)

tuple2 = 10, 20
type(tuple2) ### tuple이라고 나옴! <- () 쓰지 않고 그냥 ,로 나열해도 됨! 
tuple2 = 10
type(tuple2) ### 이건 그냥 int라고 나옴! 
tuple3 = (1,)
type(tuple3)
tuple4 = (1,2,3,4)
type(tuple4)

## 중첩 가능! 
tuple5 = (1,2,3,('a','b'))

## 인덱싱, 슬라이싱하는 방법은 리스트와 똑같음! 
tuple5[3][0]
tuple5[0]

## 튜플 변수 값을 수정, 삭제, 추가하려면 오류 
tuple5[0] = 10 ### 오류!(tuple은 수정이 안 됨) 
del tuple5[0] ### 오류!(삭제도 안 됨) 
tuple5.append(4) ### 오류!(추가도 안 됨) <- (4,)라는 tuple을 새로 만들어서 +를 이용해 붙이면 됨 

## 두 개의 tuple을 새로운 변수에 합치는 건 가능! 
x = (1,2,3)
y = (4,5,6)
z = x + y ### 붙이는 건 가능 

x = x + (4,) ### 변수명.append()는 안 되지만, 새로운 tuple을 만들어서 붙이는 건 가능 <- 이 경우는 추가한 게 아니라, 새로운 tuple을 만든 거! 
x
id(x) ### 위의 +를 쓰고 id()를 확인하면 바뀌어 있음 -> 새로운 변수가 만들어진 거! 

x.index(3)
x.count(1)



# 3. dictionary 
##          key(키)와 value(값)를 확인하는 자료형(key와 value를 한 쌍으로 저장) <- 영한사전처럼 단어와 그 의미를 짝지어 저장 
##          {key:value}
##          key가 지워지면 value도 같이 지워짐 
'''
key      value
이름     홍길동
전화번호  01012345678
주소     경기도
'''
dic = {'이름':'홍길동', '전화번호':'01012345678', '주소':'경기도'}
type(dic)

dic['이름'] ### 사전에서 단어 찾듯이, key를 이용해서 거기에 해당되는 value를 찾음! cf. 리스트: 요소 번호로 찾음 

sports = {'축구':'메시', '농구':'커리', '야구':'박찬호'}

sports['축구']
sports['컬링'] = '김영미' ### 새로운 값 추가 
sports['컬링'] = ['김은정','김경애','김영미','김선영','김초희'] ### 리스트로 넣음 <- 이 5개가 하나! <- "'김영미' in sports.values()"로 검색하면 False로 나옴 
sports.keys() ### dictionary 변수의 key만 확인
sports.values() ### dictionary 변수의 value만 확인 
sports.items() ### key, value 같이 확인 
sports['농구']
sports.get('농구') ### 위와 같음! 

sports['봅슬레이'] ### 오류! <- dictionary 안에 없는 key 
sports.get('봅슬레이') ### 해당 key가 없지만 오류는 안 뜸! <- 그 key가 있는 지 없는 지 모를 때 사용 

'컬링' in sports.keys() ### True <- 이런 식으로 key가 dictionary에 포함되어 있는 지 확인할 수 있음 
'봅슬레이' in sports.keys() ### False 
'메시' in sports.values()
'호날두' in sports.values()
'김영미' in sports.values() ### False라고 나옴! 
['김은정','김경애','김영미','김선영','김초희'] in sports.values() ### 하나라도 빠지면 안 됨! 

del sports['야구']
sports
sports['축구'] = []
sports
sports.clear() ### 다 지워짐 
sports

x = sports.values() ### value만 따로 뽑아서 변수에 저장
x
type(x) ### dict_values 타입
list(x) ### 리스트 타입으로 만듬(형변환 함수) 



# 4. set
##          list type 비슷하다. 
##          index가 없다. 
##          중복을 허용하지 않는다. <- 유일키 
x = {1,1,1,2,3,2,3}
x ### 중복이 자동으로 사라짐 
type(x)
y = {2,3,4,5}

## 합집합
x.union(y) ### x와 y 합집합 수행 
x|y ### 위와 같음 

## 교집합
x.intersection(y)
x&y 

## 차집합 
x.difference(y)
x-y
y.difference(x)
y-x

## in 연산자 사용 
1 in x
6 in x

x[0] ### 오류! (set은 요소 번호를 가질 수 없음) 

## 변수이름.remove()
### 집합 변수에 값을 삭제 
x.remove(1) ### set에서 1 제거 

## 변수이름.add()
### 집합 변수에 값을 입력 
x.add(1) ### set에서 1 추가 

## 변수이름.update([])
### 집합 변수에 여러 개의 값을 추가할 때 
x.update([5,6,7])

a = []
b = ()
c = {} ### dictionary! (set이라고 안 나옴!)
s = set() ### set을 만들고 싶으면 이렇게 해야 함! 
type(a) ### list 
type(b) ### tuple 
type(c) ### dictionary 
type(s) ### set 



# 5. bool 
##          참(True), 거짓(False)을 나타내는 자료형 <- True/False 대소문자 구분! 
x = True
type(x) ### boolean 
y = False
type(y) ### boolean 
x == y ### False라고 나옴! 
1 == 1
2 > 1

not 0 ### True 
not None ### True

## True 표현방법
bool(1)
bool(-1)
bool('python')
bool([1,2,3])
bool((1,2,3))
bool({1,2})

## False 표현방법
bool(0)
bool([])
bool(())
bool({})
bool(None)
bool('')



# 조건 제어문
# IF문 
'''
if 조건문:
    수행해야할 문장 <- 들여쓰기에도 주의! 
    
if 조건문:
    수행해야할 문장
else:
    수행해야할 문장 
    
위의 True 표현방법과 False 표현방법을 생각하며 조건문 입력! 
'''
if 1:
    print("참")
    print("오늘 하루도 행복하자")
if 0:
    print("참")
    print("오늘 하루도 행복하자") ### 아무 작업 안 함!(0: False) 
if 0:
    print("참")
    print("오늘 하루도 행복하자")
else:
    print("거짓")
    print("그냥 사는거지 뭐...")

x = []
if x: ### False 표현방법! 
    print("참")
    print("오늘 하루도 행복하자")
else:
    print("거짓")
    print("그냥 사는거지 뭐...")

x = 1
if x == 1: 
    print("참")
    print("오늘 하루도 행복하자")
else:
    print("거짓")
    print("그냥 사는거지 뭐...")



## 1. and, & 
x = 0
if x>10 and 1/x: ### 1/x(1/0)는 오류가 나야 하는데, 그냥 False로 나옴 -> x>10가 애초에 False니까 뒤에는 물어보나마나 False로 처리! 
    print("x는 10보다 크다")
else:
    print("x는 10보다 작다")

### cf1. and 조건의 순서를 바꿈 
x = 0
if 1/x and x>10: ### 오류!(파이썬의 특징: and에서 앞의 조건이 False면 뒤의 조건은 무시)
    print("x는 10보다 크다")
else:
    print("x는 10보다 작다")

### cf2. 앞의 조건이 False라도 두 조건 다 적용하고 싶은 경우 -> & 사용! 
x = 0
if x>10 & 1/x: 
    print("x는 10보다 크다")
else:
    print("x는 10보다 작다")



## 2. or, | 
x = 0
if x<10 or 1/x: ### 앞의 조건이 True니까 뒤의 조건은 보지 않음! 
    print("x는 10보다 크다")
else:
    print("x는 10보다 작다")

x = 0
if x<10 | 1/x: ### 오류! <- 두 조건을 모두 체크하고 싶을 때는 | 사용! 
    print("x는 10보다 크다")
else:
    print("x는 10보다 작다")



## 3. elif 
score = 88
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")



x = [1,2]
y = [2,1]
if x == y:
    print("참")
else:
    print("거짓") ### 리스트는 인덱스값을 가지고 있음(인덱스끼리 비교) -> 순서가 다르면 다른 거! 

x = {1,2}
y = {2,1}
if x == y:
    print("참") ### set의 경우는 True로 인지! 
else:
    print("거짓")



# 반복문 
# 1. while문 
## 조건이 참인 동안에 while문을 반복해서 수행한다. 
'''
while 조건문: 
    반복수행해야할 문장 
'''





"""
09-06-2018 
"""
i = 0
while 1: ### True -> break 없으면 무한루프! 
    i += 1
    print("반복하는 값: %d" %i) ### 무한루프! 

# break: 종료하는 보조제어문 
i = 0
while 1:
    if i > 10: 
        break ### 무한루프 방지 
    else:
        i += 1
        print("반복하는 값: %d" %i)

i = 10
while 1:
    if i < 1: 
        break 
    else:
        print("반복하는 값: %d" %i)
        i -= 1

i = 10
while 1:
    print("반복하는 값: %d" %i)
    i -= 1
    if not i: ### i로 boolean을 만드는 법! 
        break 
    
i = 10
while 1:
    if i == 0:
        break
    else:
        print('반복하는 값: %d'%i)
        i -= 1 

i = 0 
while i < 10:
    i += 1
    print(i)
    
# continue문은 while문으로 돌아가게 하는 문
i = 0
while i < 10:
    i += 1
    if i%2 == 0: ### 짝수는 출력되지 않게 빼는 용도로 사용! 
        continue
    print(i)



# 2. for문 
'''
for 반복변수 in (리스트, 튜플, 문자열): <- 리스트, 튜플, 문자열의 개수에 종속 
    반복수행해야할 문장
'''
for i in [1,2,3,4,5]:
    print(i)
    
x = [1,2,3,4,5]
for i in x:
    print(i)

for i in ['a','b','c']:
    print(i)

x = ['sql','plsql','r','python']
for i in x:
    print(i)
for i in '대한민국':
    print(i)

x = [(1,2),(3,4),(5,6)]
for (a,b) in x: ### sub-tuple 내의 요소 분리 
    print(a+b)

## range(시작점, 끝점-1, 간격) <- 간격: default = 1
range(1,11,1) ### 이 자체는 실행 안 됨!(object 형식) 
list(range(1,11,1))
list(range(0,101,1))
list(range(0,101,5))

for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)

### cf. 역순 
for i in range(10,1,-1): ### 10부터 역으로 계산 
    print(i)

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

## enumerate() 
### 리스트 안의 인덱스와 값을 리턴 
for i, name in enumerate(lst): 
    print('{}번 {}값이 있습니다.' .format(i, name))



# end = ',': print()에서 리스트를 세로에서 가로로 바꿔주는 기능 
for x in lst1:
    for y in lst2:
        print(x*y, end = ',') ### 세로로 나열된 리스트를 가로로 바꿔줌!! 



# 리스트 내장 객체 
## 리스트 안에 for문을 만듬 
'''
[표현식 for 반복변수 in 반복가능한객체]
'''
z = [i*2 for i in x] ### 뒤에서부터 해석!(for문부터 수행하고 표현식 수행)
z





"""
09-07-2018 
"""
# 함수 
## - 기능의 프로그램 
## - 반복되는 코드를 하나로 묶어서 처리하는 방법 
'''
def 함수이름(인수, 인수, 인수, ...)
        수행할 문장...
        [return 값]          <- return은 Python에서는 옵션 // 값이 없는 return: 종료 
'''
def message():
    print("오늘 하루도 행복하자")
message()
def message(x): ### 인수값의 타입은 넣는 순간 만들어짐 
    print("홍창식")
message("홍창식")

def message2():
    print("매일 행복하자")
    return "happy"
message2()
word = message2()
print(word) ### 여기선 return값이 나옴! 

## 인수값 선언 cf. PL/SQL: 레코드 변수 
'''
def 함수이름(*인수):
    수행할 문장 
'''
def sum(*x): ### for문 사용! 
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

## return문 2개를 연달아 쓰는 경우 -> 오류는 나지 않지만, 첫번째 꺼만 수행되고 끝남 -> return문은 하나만 입력해야 함! 
def f1(x,y):
    return x+y
    return x*y
z = f1(2,3)
print(z) ### 첫번째 것만 return됨! 

def f1(x,y):
    return x+y, x*y ### 이런 식으로 return문에 나열해야 함! 
sum1, mul1 = f1(2,3) ### 변수 저장할 때도 ,로 구분! 
print(sum1, mul1)

## 값이 없는 return문 
def f2(x,y):
    if y == 0:
        return ### 값이 없는 return문 -> 그냥 종료시킴!(분모가 0이 되는 걸 방지)
    print(x/y, " 값 입니다.")
f2(4,2)
f2(4,0)

## 형식매개변수에 기본값을 만듬 
### 본래 매개변수를 입력하지 않으면 오류! 
### 하지만 형식매개변수에 초기값(default)을 설정해놓으면, 입력하지 않아도 리턴됨! 
def f3(name, age, gender='M'):
    print("이름은 ", name)
    print("나이는 ", age)
    if gender == "M":
        print("남자")
    else:
        print("여자")
f3("홍길동", 30)
f3("송하빈", 20, "F") ### 기본값 이외에 다른 값을 입력해도 됨! 



# 전역변수(global): 프로그램이 종료될 때까지 어디서든지 사용할 수 있는 변수 
# 지역변수(local): 프로그램 안에서만 사용하는 변수 
x = 10 ### global 
def f4(x): ### 매개변수 <- 해당 함수 안에서만 사용! 
    print("x 변수 값은", x) ### global 변수가 들어감 
    x = 20 ### local 
    print("x 변수 값은", x) ### local 변수가 들어감 
f4(x)
print(x)

x = 10
def f5(arg):
    global x
    x = 20
    print("x 변수 값은", x)
f5(x)
print(x)



# 리스트 복제 
## copy 
a = [1,2,3]
b = a
print(a,b)
print(id(a), id(b))
a.append(4)
print(a,b)
print(id(a),id(b)) ### 복제했는데 원본까지 바뀜! 

## deepcopy 
c = a[:] ### 이걸로 복제!!! <- 안 쓰면 바깥에 있는 변수에도 영향 줌! 
print(a,b,c)
print(id(a),id(b),id(c))
a.append(5)
print(a,b,c)
print(id(a),id(b),id(c))

## 변수를 복제하되, 다른 메모리 주소(id())를 할당하는 모듈 
import copy
d = copy.deepcopy(a) ### 복제 
print(id(a), id(d)) ### 다른 id 
a.append(6)
print(a,d) ### 원본(a)만 바뀌고, 복제된 것(d)은 바뀌지 않음 

a = [1,2,3]
b = a
print(id(a),id(b)) ### 같은 메모리 주소 

a = [1,2,3]
b = a[0]
print(id(a),id(b)) ### 다른 메모리 주소 





"""
09-10-2018
"""
# 숙제: 초등학교 수학을 파이썬으로 구현 

# 재귀호출
## 자기 자신을 다시 호출한다. <- 호출하려면 오브젝트(함수 안에서 내 함수를 다시 호출!)
## 함수 안에서 내 함수를 호출한다. => 반복문 필요 
## 알고리즘: 반복문 + stack 

## 성능이 저하될 수도 있지만, 표현이 심플해지고, 보다 전문적으로 보일 수 있음! 
## 반드시 끝내는 시점을 만들어야 함! -> 그렇지 않으면 무한루프! 

### Queue: 양쪽이 뚫려 있어서 하나씩 순서내로 집어넣음 
### Stack: 한쪽이 막혀 있어서 쌓아놓기만 함(Push) -> 맨 밑에 있는 걸 뽑아내려면 위에 있는 것들을 pop 해야 함! 



# Stack
## FILO(First In Last Out): 선입후출 
## LIFO(Last In First Out): 후입선출 
### ex. 옷장, 뒤로(인터넷 브라우저) 
### cf. Queue: FIFO(First In First Out)

# Push: push 스택의 구조상 마지막 데이터 위치에 입력된다 
# Pop: 마지막 데이터 위치에서 데이터를 꺼내는 작업(삭제) 

# stack [] 
## push 하면 stack 변수에 값을 넣는다. 
## pop 하면 stack 변수에 값을 삭제한다. 
stack = []
def push(n):
    global stack
    stack.append(n)
def pop():
    global stack
    if len(stack) == 0:
        return None
    return stack.pop()

push(1)
push(2)
push(3)

pop()



# factorial 함수 
## n! = n * (n-1) * (n-2) * ... * 2 * 1
## n! = n * (n-1)!

## factorial 공리: n * factorial(n-1) if n>=1
## factorial(n) = 1 if n=0
### 위 식을 함수로 정리! 
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1) ### 재귀호출!(함수 안에 자기 함수를 불러냄) -> 반복문을 쓸 수도 있음 
recur_factorial(5)

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



# 최대공약수 
# 최소공배수 



# 유클리드 알고리즘 
## 주어진 두 수 사이에 존재하는 최대공약수(GCD(Greatest Common Divisor))를 구하는 알고리즘 

## 1. 두 수 m,n(m>n) 입력으로 들어온다. 
## 2. n이 0이라면 m을 출력하고 알고리즘은 종료 
## 3. m이 n으로 나누어 떨어지면, n을 출력하고 알고리즘은 종료 
## 4. 그렇지 않으면 m을 n으로 나눈 나머지를 새롭게 m에 대입하고 m과 n을 바꾸고 3번으로 돌아간다. 
def gcd(x, y):
    if(x<y):
        x,y = y,x
    while(y!=0):
        n = x%y
        x = y
        y = n
    return x

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
gcd(18,24)

def gcd(x, y):
    r = x%y
    if r == 0:
        return y
    return gcd(y, r)

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)
gcd(6,0)





"""
09-11-2018 
"""
# Exception 처리
## Exception: 실행 중에 발생한 오류 

def divide(x,y):
    return x/y
divide(10,2)
divide(10,0) ### ZeroDivisionError: division by zero <- Python에서 제공하는 exception(오류 번호는 없음)
divide(10,'둘') ### TypeError: unsupported operand type(s) for /: 'int' and 'str' 

# Exception Handling 
## try가 적용되면 except절로 가게 됨 
try:
        z = divide(10,2)
        print(z)
except: 
        print("오류가 발생했습니다.")

try:
        z = divide(10,0)
        print(z)
except: 
        print("오류가 발생했습니다.") ### try에 오류가 발생해서 except로 이동 <- 실질적인 오류는 발생하지 않고, 정상적으로 종료 

## "except 오류이름:" 
### except절을 여러 개 나열해서 쓸 수 있음! 
### else절 <- try 부분에 exception이 없을 경우 수행 
try:
        z = divide(10,0)
        print(z)
except TypeError: ### TypeError가 발생했을 때 수행! 
        print("인수값을 숫자로 입력하세요") 
except ZeroDivisionError: ### ZeroDivisionError가 발생했을 때 수행!
        print("0값으로 나눌 수 없습니다.") 
except: 
        print("오류가 발생했습니다" )
else: ### else절도 쓸 수 있음! (try에서 exception이 발생하지 않은 경우 else 부분 수행) 
        print("결과 : {}" .format(z))

### "finally:" <- 오류가 나던 안 나던 상관 없이 수행! 
try:
        z = divide(10,2)
        print(z)
except TypeError:  
        print("인수값을 숫자로 입력하세요") 
except ZeroDivisionError: 
        print("0값으로 나눌 수 없습니다.") 
except: 
        print("오류가 발생했습니다" )
else: 
        print("결과 : {}" .format(z)) ### 실제 결과와 이 else의 내용이 같이 출력됨! <- optional
finally: 
        print("프로그램 종료")



# User가 만드는 예외 상황 
def func(arg):
    try:
        if arg < 1 or arg > 10:
            raise Exception("유효하지 않은 숫자입니다.:{}" .format(arg)) ### Exception 이름 지정 
        else: 
            print("입력한 수는 {} 입니다." .format(arg))
    except Exception as error: ### raise에서 가져옴(raise 부분이 error가 됨)
        print("오류가 발생했습니다. {}" .format(error))
func(100)



# 리스트의 없는 방을 인덱싱 
lst = [1,2,3]
try:
    print(lst[3]) ### 없는 요소 번호를 참조 
except: 
    print("오류가 발생했습니다.")

lst = [1,2,3]
try:
    print(lst[3]) 
except Exception as error: ### exception의 내용을 확인 
    print(error)

lst = [1,2,3]
try:
    print(lst[3]) 
except IndexError as error: 
    print(error)



# 날짜
## datetime 패키지에서는 날짜 시간을 제공하는 datetime class, 
## 날짜만 제공하는 date class, 
## 시간만 제공하는 time class, 
## 일수, 시간, 분, 초 구간 제공하는 timedelta class 
import datetime
datetime.date.today() ### 오늘 날짜 정보 
datetime.datetime.now() ### 날짜에 시간까지 나옴 

datetime.date.today().year ### 연도만 따로 뽑음 
datetime.date.today().month
datetime.date.today().day

d = datetime.date.today() ### 변수에 집어넣음 
d.year ### 이렇게 표현해도 됨 

datetime.datetime.now().year
datetime.datetime.now().month
datetime.datetime.now().day
datetime.datetime.now().hour
datetime.datetime.now().minute
datetime.datetime.now().second

n = datetime.datetime.now()
n.year
n.microsecond ### 100만 분의 1초 

n.date() ### datetime.datetime.now() 안에 있는 날짜 정보 
n.time() ### datetime.datetime.now() 안에 있는 시간 정보 
n.weekday() ### 0: 월요일 ~ 6: 일요일 

## 변수명.strftime() 
### strftime: date => char 
### strptime: char => date 
### 날짜를 str 형식으로 표현 
d = datetime.datetime.now()
d.year 
type(d.year) ### int

d.strftime('%Y')
type(d.strftime('%Y')) ### str 
d.strftime('%Y %m %d %B')
d.strftime('%x')
d.strftime('%X')
d.strftime('%A')
d.strftime('%a')
d.strftime('%z')

'''
%Y: 년도 4자리
%m: 달 
%d: 일
%B: 영어 달 이름 
%H: 시간(24시간!)
%I: 시간(12시간으로 환산)
%M: 분 <- "%m: 달"과 구분! 
%S: 초
%x: 현재 날짜(월/일/년)
%X: 현재 시간(시:분:초)
%A: 요일
%a: 요일(축약형)
%c: 날짜 시간 <- Tue Sep 11 14:15:04 2018
%p: AM or PM 
%j: 누적날짜 
%U: 누적주(일요일 시작)
%W: 누적주(월요일 시작)
%w: 요일(0~6)
%z: 시간대 <- 시간대 정보를 가지고 있지 않으면 리턴되지 않음 
'''

datetime.datetime.strptime("2018-09-11 14:50:00", "%Y-%m-%d %H:%M:%S") ### char를 date로 바꿈! 

d = datetime.date(2018,9,11) ### 날짜 정보 
t = datetime.time(14,52,00) ### 시간 정보 

datetime.datetime.combine(d,t) ### 날짜 정보와 시간 정보를 합침 

## 날짜 - 날짜 
datetime.datetime(2018,5,24) - datetime.datetime(2018,11,22)

## timedelta 메소드 
### 해당 날짜로부터 몇 일 후인지 계산 
datetime.datetime(2018,9,24) + datetime.timedelta(days = 72)

datetime.datetime(2018,9,1) + datetime.timedelta(days = 100)

datetime.timedelta(days = 72)
datetime.timedelta(hours = 1) ### 초 단위로 환산! 
datetime.timedelta(minutes = 1)

datetime.date.today()

## 해당 시점의 구간을 파악 
start = datetime.datetime.now()
end = datetime.datetime.now()
delta = end - start
delta.total_seconds() ### delta값을 초 단위로 리턴 



## time.time(): 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴해주는 함수 
### UTC(Universal Time Coordinated 세계협정표준시)를 이용해서 실수 형태로 반환 
import time
time.time() ### 초 단위로 실수형처럼 나옴 
time.localtime() ### 아까 했던 날짜 정보와 비슷하지만, 더 알아보기 쉽게 되어 있음 
time.localtime().tm_year
time.localtime().tm_mon
time.localtime().tm_wday ### 현재 요일(0~6)
time.localtime().tm_yday ### 누적 일수 (1~365(366))
time.localtime().tm_isdst ### 서머타임일 경우 1, 아닐 경우 0, 모를 경우 -1 

time.gmtime() ### UTC 기준의 현재 시간 
time.asctime()
time.ctime()

## time.strftime('포맷 문자열',time.localtime())
### time => char 
time.strftime('%Y',time.localtime()) ### 연도 4자리 뽑아냄 
time.strftime('%Y %z',time.localtime()) ### localtime에서는 시간대 정보가 있음 => %z에 해당되는 값 리턴! 

## time.sleep()
for i in range(10):
    print(i)
    time.sleep(2) ### 2초 간 for문을 쉬게 해줌 -> 과도한 성능 저하 방지 



import calendar 
calendar.calendar(2018)
print(calendar.calendar(2018))

calendar.prcal(2019)

calendar.prmonth(2018,9) ### 해당 월 
calendar.weekday(2018,9,11) ### 해당 일자의 요일 

calendar.monthrange(2018,9) # 그달의 첫째날짜의 요일, 마지막일 <- 9월 1일: 토요일 // 마지막 날은 30일 
calendar.mdays[1]



from korean_lunar_calendar import KoreanLunarCalendar
calendar = KoreanLunarCalendar()
# params : year(년), month(월), day(일)
calendar.setSolarDate(2017, 6, 24)
# Lunar Date (ISO Format)
print(calendar.LunarIsoFormat())
# Korean GapJa String
print(calendar.getGapJaString())
# Chinese GapJa String
print(calendar.getChineseGapJaString())

# params : year(년), month(월), day(일), intercalation(윤달여부)
calendar.setLunarDate(1956, 1, 21, False)
# Solar Date (ISO Format)
print(calendar.SolarIsoFormat())
# Korean GapJa String
print(calendar.getGapJaString())
# Chinese GapJa String
print(calendar.getChineseGapJaString())





"""
09-12-2018 
"""
# 파일 입출력 

# 파일 생성 

# 파일 객체 = open("C:/data/test.txt", mode)

# mode
## r: 읽기 
## w: 쓰기(파일 안에 원본 데이터는 지우고 작성된다.)
## a: 추가 

# 파일객체.close 

# write 모드 
## open - 실행 - close <- 이 작업을 같이 수행해야 함! 
## 이전 내용들은 다 없어지고 새로운 걸로 수정됨 
f = open("C:/data/test.txt", "w") ### 파일 객체 선언
for i in range(11,21): ### range 값 바꾸고 다시 실행해보면, 이전 값들이 없어짐! 
    txt = "%d 오늘 하루도 행복하자\n" %i ### 줄바꿈(\n) 안 하면 한 줄로 계속 늘여써짐! 
    f.write(txt)
f.close() ### 꼭 해줘야 파일에 저장됨! 

# append 모드 
## 기존의 내용은 남겨두고 새로운 것을 추가 
f = open("C:/data/test.txt", "a") ### append mode -> 기존의 내용들은 남겨두고 추가시킴! 
for i in range(1,11): 
    txt = "%d 오늘 하루도 행복하자\n" %i 
    f.write(txt)
f.close()

## os.path.exists(): 해당 파일이 존재하는 지 알고 싶을 때 쓰는 메소드 
import os
os.path.exists("C:/data/test.txt") ### 이 파일이 존재하는 지의 여부 파악(True/False)

# read 모드: 파일 읽기 
## 1. readline(): 한 줄 씩 불러들임 
file = open("C:/data/test.txt","r")
data = file.readline() ### 파일에서 한 줄만 읽어옴
print(data) ### 한 줄씩만 출력 -> 위의 코드와 print()를 반복하면 그 다음 줄도 계속 출력 -> 1000줄을 출력하고 싶으면 1000번 실행시켜야 함! -> Loop문 사용!! 
file.close() ### 항상 마지막에는 close! 

file = open("C:/data/test.txt","r")
while True:
    data = file.readline() ### 더 이상 파일에서 읽어올 라인이 없으면 None 리턴 
    if data == "": ### not data <- if에 이렇게 써도 됨! 
        break
    print(data, end = "") ### end = "" <- 줄 사이의 공백을 없앰 
file.close()

## 2. readlines(): 모든 라인을 읽어서 리스트에 저장 
### 리스트로 되어 있어서 보기 불편 
### for문을 이용해서 하나씩 뽑아내야 함 
file = open("C:/data/test.txt","r")
data = file.readlines()
print(data, end = "")
file.close()

file = open("C:/data/test.txt","r")
data = file.readlines()
for i in range(1,10):
    print(data[i], end = "")
file.close()

file = open("C:/data/test.txt","r")
data = file.readlines()
for i in data:
    print(i, end = "")
file.close()

## 3. read(): 파일 전체를 문자열로 리턴한다. 
### 리스트형이 아니라서 굳이 loop문을 쓸 필요가 없음 
file = open("C:/data/test.txt","r")
data = file.read()
print(data)
file.close()

# with문 <- SQL: 가상 결과 집합을 table 형식으로 만들어 놓은 거 
## 파일 객체를 자동으로 닫아주는 문
## 끝에 file.close() 쓸 필요 없음! 
with open("C:/data/test.txt","w") as file:
    for i in range(1,101):
        txt = "%d 오늘 하루도 행복하자 \n" %i
        print(txt, end="")
        file.write(txt)

## 리스트 변수 
txt = ['야!! 가을이다','오늘 하루 신나게 놀아보자']
with open("C:/data/test_new.txt","w") as file:
    for i in txt:
        file.write(i + "\n") ### + "\n" <- 이거 안 쓰면 그냥 한 줄로 쭉 write됨! 

txt = ['야!! 가을이다','오늘 하루 신나게 놀아보자']
with open("C:/data/test_new.txt","w") as file:
    for i in txt:
        file.write("{}\n" .format(i))

### read 모드 
with open("C:/data/test_new.txt","r") as file:
    txt = file.readlines()
    for i in txt:
        print(i, end="")



# csv 파일: ,로 구분 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) ### csv 파일 형식의 메소드로 read -> 그냥 object 모양으로 주소만 저장! -> pandas 모듈을 이용하면 보다 간편 
emp_csv = csv.reader(file)
emp_csv ### object 정보만 보이고 그 안의 내용은 확인 못 함! 

next(emp_csv) ### 첫 행(컬럼명)은 skip하고 다음행부터 불러들임 
for emp_list in emp_csv:
    print(emp_list)





"""
09-13-2018
"""
# lambda(람다) 함수 
## - 이름이 없는 한줄짜리 함수 
## - 가독성을 위해서 
### def 대신 lambda 쓰는 거! 

def f(x,y):
    return x*y
f(2,3)

(lambda x,y : x*y)(2,3) ### 한줄짜리! 

f = lambda x,y : x*y
f(2,3) ### 이렇게 써도 됨! 



## R의 벡터 -> 인덱스별 사칙연산 자동 적용(리스트는 어려움!) -> Python에서 벡터 기능 사용하는 법: pandas 

# pandas 
## - 데이터 분석 기능을 제공하는 라이브러리 
## - 1차원 배열: Series <- R의 벡터 
## - 2차원 배열: DataFrame <- R의 데이터프레임 

import pandas as pd ### "pandas.메소드" 이렇게 하면 코드가 길어져서 "pd"라고 축약! 
from pandas import Series, DataFrame ### 특정 기능만 가져옴(앞에 pd. 일일히 안 붙여도 됨!) 



# 1. Series 
## - 1차원 배열 
## - 인덱스(색인) 배열의 데이터에 연관된 이름을 가지고 있다. 
Series([10,20,30,40,50]) 
s = Series([10,20,30,40,50]) ### 인덱스는 0번부터 시작 
s[0]
s.index ### 인덱스 확인 <- RangeIndex(start=0, stop=5, step=1)
s.values ### 값 확인 
s.index = ['a','b','c','d','e'] ### 인덱스 변경 가능!(방번호 수정)
s

## R의 벡터를 사용하듯이 자유롭게 데이터 작업 가능! 
s + 10
s - 10
s * 10
s / 3
s // 3
s % 3

## Series 안의 값 조회 
s2 = Series([10,20,30,40], index = ['a','b','c','d']) ### 인덱스를 바로 설정하는 것이 가능 
s2
s2['a']
s2['a','b'] ### 오류! -> 2개 이상의 인덱스를 보려면 안에 []를 써줘야 함! 
s2[['a','b']]
s2[0] ### 인덱스 이름과는 별개로 내부적으로 인덱스 번호도 저장됨 
s2[0:3]
s2[-1]
s2[s2>20] ### 안에 비교 연산자를 넣어서 그 조건에 맞는 값들만 확인할 수 있음 

## in: 인덱스 이름이 존재하는 지의 여부 확인 
'a' in s2 ### 인덱스 이름이 있느냐 없느냐를 확인하는 것이 가능 
'e' in s2

## Series 수정, 추가, 삭제 
s2['a'] = 100 ### 수정
s2['e'] = 50 ### 추가 
del s2['e'] ### 삭제 
s2['a'] = '' ### 자리는 남겨놓고 값만 지움 
del s2 ### 변수 삭제 

## Dictionary를 1차원 배열로 적용
### key:value => 인덱스:값 
dict = {'a':10, 'b':20, 'c':30, 'd':40} ### key:value 
dict
s3 = Series(dict) ### Series()에 dictionary 변수를 집어넣으면 자동으로 Series로 바뀜! 
s3

dict = {'a':10, 'b':20, 'c':30, 'd':40} 
ix = {'a','b','c','d'}
s4 = Series(dict, index = ix)
s4

dict = {'a':10, 'b':20, 'c':30, 'd':40} 
ix = {'a','b','c','z'} ### z라는 키는 없음! -> 새로운 1차원 배열에 z는 있지만, 값은 NaN으로 되어 있음 <- NaN: NULL값과 같다고 보면 됨, NaN이 뜨면 타입이 str로 바뀜! 
                       ### NaN(Not a Number): 인덱스 값을 찾을 수 없기 때문에 NaN 저장 
s5 = Series(dict, index = ix)
s5

dict = {'a':10, 'b':20, 'c':30, 'd':40} 
ix = {'a','b'} ### 1차원 배열에 넣고 싶은 key만 따로 인덱싱할 수 있음! 
s6 = Series(dict, index = ix)
s6



## pd.isnull(), pd.notnull(): Series에 NULL값이 있는지 없는지 확인 
pd.isnull(s5)
pd.notnull(s5)

dict = {'서울':100, '부산':200, '광주':300, '제주':400}
s7 = Series(dict)

city = ['서울','광주','제주','인천']
s8 = Series(dict, index = city)
s8
s8['인천'] = 500 ### 해당 인덱스에 값 추가시켜서 NaN 없앨 수 있음! 
s8



# 2. DataFrame 
## - 2차원 배열 
## - 표 형식의 자료 구조 
## - 각 컬럼은 서로 다른 종류의 값(문자, 숫자, Boolean)
## - R의 data.frame 
df1 = DataFrame([[1,2,3],[4,5,6],[7,8,9]])
df1

data = {'도시':['광주','부산','강원','인천'], 
        '인구수':[100,200,50,300]}
data
df2 = DataFrame(data)
df2

df3 = DataFrame({'도시':['광주','부산','강원','인천'], 
        '인구수':[100,200,50,300]}) ### 그냥 이렇게 넣어도 상관 없음(인덱스 번호는 자동으로 설정됨)
df3 
### Series와 비슷 -> 컬럼으로 구성, 서로 다른 타입 

## 변수명.columns 
df3.columns ### 컬럼명 확인 가능 

df3.columns = ['지역','가구수']
df3
df3.지역 ### 변수명.컬럼명 
df3.가구수

df3['지역']
df3['가구수']
df3['가구수'] * 100 ### Series처럼 연산 작업 가능 

df3.index ### 인덱스 확인 <- RangeIndex(start=0, stop=4, step=1) 
df3.index = ['one','two','three','four'] ### 인덱스 이름 변경 
df3
df3.ix['one'] ### 인덱스의 'one'에 해당되는 값 확인 가능 
df3.ix[0] ### 위와 같음 



## 2개의 열을 붙이고 싶은 경우 
v = Series([1000,2000,3000,4000],
           index = ['one','two','three','four']) 
v

df3['부채'] = v ### v열이 df3로 들어감 
df3['인구수'] = [10000,20000,30000,5000]
df3.columns
df3
del df3['부채'] ### 컬럼 삭제 
df3

data = {'서울':{2001:200,2002:300},
        '부산':{2000:10,2001:20,2002:30}}
df4 = DataFrame(data) ### 서울에는 2000년 정보가 없어서 NaN로 나옴 

## 변수명.T <- 인덱스와 컬럼 위치가 바뀜 
df4.T ### transpose 
df4.columns
df4.index
df4.values ### array 모양! 

## reindex(재색인): 새로운 색인에 맞도록 객체를 새로 생성하는 기능 
obj = Series([10,20,30,40], index=['c','d','a','b'])
obj ### 인덱스 순서가 랜덤하게 정해짐 -> 정렬! 
obj2 = obj.reindex(['a','b','c','d']) ### 인덱스가 순서에 맞게 정렬됨! 
obj2
obj3 = obj.reindex(['a','b','c','d','z']) ### z는 위의 인덱스에 없음 -> 값이 NaN가 됨! 
obj3





"""
09-14-2018 
"""
import pandas as pd
from pandas import Series, DataFrame

# Series
## - 1차원 배열

# DataFrame
## - 2차원 배열 

obj = Series([10,20,30,40], index=['c','d','a','b'])
obj

obj2 = obj.reindex(['a','b','c','d'])
obj2

obj3 = obj.reindex(['a','b','c','d','f'])

## fill_value: NaN을 특정값으로 만듬 
obj4 = obj.reindex(['a','b','c','d','f'], fill_value=0) ### "fill_value=0" <- NaN을 0으로 만듬! 



# numpy: 수학과 관련된 메소드 다수 가지고 있음 
import numpy as np

# np.arange(): array형을 만들어야 될 때 사용 
np.arange(4) ### 배열을 만드는 메소드 
np.arange(4).reshape(2,2)
np.arange(9).reshape(3,3)
np.arange(12).reshape(3,4)

df = DataFrame(np.arange(9).reshape(3,3), index=['a','b','c'], columns = ['x','y','z'])
df

## method = 'ffill' // method = 'pad': NaN을 없애는데 바로 앞에 있는 데이터 그대로 복사 
## cf. method = 'bfill': 뒤에 있는 값들로 채워짐 
df2 = df.reindex(['a','b','c','d']) ### NaN
df3 = df.reindex(['a','b','c','d'], method = 'ffill') ### 바로 앞에 있는 녀석의 데이터로 채워짐!! 
df4 = df.reindex(['a','b','c','d'], method = 'pad')

obj = Series(['sql','r','python'], index=[0,2,4])
obj2 = obj.reindex(range(6)) ### 1,3,5번이 NaN으로 설정됨 
obj3 = obj.reindex(range(6), method='ffill') ### 각각 바로 앞에 있는 값들로 채워짐! 
obj4 = obj.reindex(range(6), method='pad')
obj5 = obj.reindex(range(6), method='bfill') ### 뒤에 있는 값들로 채워짐! -> 5번 인덱스는 뒤의 값이 없어서 그냥 NaN으로 나옴! 

obj2[5] = 'sql'
obj2 ### NaN가 특정값으로 수정됨! 

## 행을 삭제하는 방법 
obj = Series(np.arange(5), index=['a','b','c','d','e'])
obj.drop('e') ### 미리보기! -> 행 삭제가 실제로 적용된 건 아님(안전을 위해서)
obj
obj = obj.drop(['c','d']) ### 이렇게 변수에 직접 적용시켜야 함! 

df = DataFrame(np.arange(16).reshape(4,4), 
               index=['w','x','y','z'],
               columns=['one','two','three','four'])

## df.drop( , axis= )행, 열 구분해서 삭제 <- 이것도 미리보기! 
df.drop('x', axis=0) ### "axis = 0" <- 행 의미 
df.drop('four', axis=1) ### "axis = 1" <- 열 의미
df = df.drop(['w','y'], axis=0)
df = df.drop(['one','two'], axis=1)

obj = Series([10,20,30,40], index=['a','b','c','d'])
obj['a']
obj[0]
obj[1:3] ### 1번과 2번 뽑힘 
obj['b':'c'] ### 이렇게 인덱스 이름을 가지고 뽑아도 됨 
obj[['a','c']] ### 2개의 데이터를 따로 보고 싶으면 이렇게 리스트로 만들어서 인덱싱해야 함! 
obj[[0,2]]
obj[obj < 30] ### 안에 조건식 넣어서 True에 해당되는 데이터만 볼 수 있음! 

df = DataFrame(np.arange(16).reshape(4,4),
               index=['w','x','y','z'],
               columns=['one','two','three','four'])
df['one']
df[['one','two']]
df[2:]
df[0:2]
df[df<5]
df[df['one']<5] ### 컬럼 one에서 조건식이 만족되는 데이터만 뽑아냄 

## 변수명.ix[[로우],[컬럼]]
## 변수명.loc[인덱스이름]
## 변수명.iloc[인덱스번호]
df
df.ix['x']
df.ix[0]
df.loc['x']
df.iloc[0]
df.ix['x','one']
df.ix['x',['one','two']]
df.ix[['x','y']]
df.ix[['x','y'],['one','two']]
df.ix[['x','y'],[0,1]] ### 이렇게 섞어서 표현 가능! 
df.ix[0,'one']
df.ix[[0,2],[0,1]]
df.ix[:]
df.ix[0:2]
df.ix[0:2,0:2]
df.ix[:,0:2]
df.ix[-1]
df.ix[:,-1]

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
### 변수명.at[] 써서 일일히 추가! 
df.at['2013','PLSQL'] = 50
df.at['2014','PLSQL'] = 60
df.at['2015','PLSQL'] = 70
df.at['2016','PLSQL'] = 80

## 인덱스, 컬럼 순서 조정 
df = df.reindex(['2013','2014','2015','2016'])
df = df.reindex(columns = ['SQL','PLSQL','R','PYTHON'])



# 100번 사원의 급여 추출 
import csv
file = open("C:/data/emp.csv","r")
csv.reader(file) 
emp_csv = csv.reader(file)
emp_csv 
next(emp_csv) 
for emp_list in emp_csv:
    if emp_list[0] == "100":
        print(emp_list[7])

# pandas를 통해 보다 간편하게 뽑아냄! 
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")                                                                          
emp

## 변수명.dtypes 
emp.dtypes ### 컬럼별 structure 확인 
emp.info() ### R의 str()과 비슷한 기능 

# 100번 사원의 급여 추출
emp.ix[emp["EMPLOYEE_ID"] == 100, "SALARY"]



student = DataFrame([[60,80,70],[50,70,85],[90,80,95]],
                  index=['홍길동','박찬호','손흥민'],
                  columns=['영어','수학','국어'])
student.at['제임스','영어']=100
student.at['제임스','수학']=50
student.at['제임스','국어']=80
student_new=DataFrame([[60,80,70],[50,75,85],[90,80,85]],
                      index=['윤건','김건모','이문세'],
                      columns=['영어','수학','국어'])
student_new

# 여러개를 한꺼번에 합치는 방법(student변수와 stdent_new변수를 합치는 방법)
## 변수1.append(변수2)
student.append(student_new)
student.append(student_new)

student=student.append(student_new) ### 변수 저장! 
student

# 여러개를 한꺼번에 합치는 방법2
## pd.concat([변수1,변수2])
student=DataFrame([[60,80,70],[50,70,85],[90,80,95]],index=['홍길동','박찬호','손흥민'],columns=['영어','수학','국어'])
student_new=DataFrame([[60,80,70],[50,75,85],[90,80,85]],index=['윤건','김건모','이문세'],columns=['영어','수학','국어'])
pd.concat([student,student_new])

student=pd.concat([student,student_new]) ### 변수 저장 
student

student1 = DataFrame([[60,80,70],[50,75,85],[90,80,85]],
                        index=['싸이','나얼','윤상'],
                        columns=['영어','수학','국어'])
student=pd.concat([student,student1])
student.info()
student['과학']=[100,80,90,60,50,60,70,80,70,60]
student

student['한국사']='조선' ### 모든 필드값이 동일한 걸로 들어감! 
student

student['음악']='' ### 필드값이 없는 컬럼 
student

del student['음악'] ### 컬럼 삭제
student

## student.drop(, axis=): 해당 로우(0)/컬럼(1) 삭제 
student = student.drop('홍길동',axis=0) ### "axis=0": 로우 삭제 
student

student = student.drop('한국사',axis=1) ### "axis=1": 컬럼 삭제 
student

student.ix['윤건']
student.loc['윤건']
student.xs('윤건')
student.xs('윤건',axis=0) ### 로우 뽑아냄 
student.xs('영어',axis=1) ### 컬럼 뽑아냄 

student['영어']

student.rename(index={'윤상':'김상'}) ### 윤상을 김상으로 변경한 것(미리보기이므로 변수에 지정을 해줘야함)

student=student.rename(index={'윤상':'김상'})
student.rename(columns={'과학':'물리'})

student=student.rename(columns={'과학':'물리'})
student



# 1. Series끼리 연산 작업
obj1 = Series([10,5,3,7], index=['a','b','c','d'])
obj2 = Series([2,4,6,8,10], index=['a','b','c','e','f'])

obj1 * 100
obj1 + obj2 ### 인덱스 이름을 기준으로 연산 작업 수행 -> Series별로 해당 인덱스가 없으면 NaN으로 나옴! 

## 변수1.add(변수2, fill_value=0)
### NaN가 될 데이터는 0으로 알아서 변환! 
obj1.add(obj2, fill_value=0)

## 변수1.sub(변수2, fill_value=0)
obj1 - obj2
obj1.sub(obj2, fill_value=0)

## 변수1.mul(변수2, fill_value=1)
obj1 * obj2
obj1.mul(obj2, fill_value=1)

## 변수1.div(변수2, fill_value=1)
### 분모에 0이 들어가면 안 되니까 "fill_value=1"로 설정 
obj1 / obj2
obj1.div(obj2, fill_value=1)



# 2. DataFrame끼리의 연산 작업 
## 마찬가지로 인덱스 이름을 기준으로 연산 작업 수행 
df1 = DataFrame(np.arange(6).reshape(2,3),
                index=['2015','2016'],
                columns=['python','sql','plsql'])
df2 = DataFrame(np.arange(12).reshape(3,4),
                index=['2014','2015','2016'],
                columns=['python','sql','plsql','r'])

df1.add(df2, fill_value=0)
df1.sub(df2, fill_value=0)
df1.mul(df2, fill_value=1)
df1.div(df2, fill_value=1)



# 브로드캐스팅(broadcasting)
obj1 = np.arange(15).reshape(5,3) ### 5x3
obj2 = np.arange(3) ### 1x3 
### 위 둘은 본래 계산이 되면 안 되는데, 실제로는 계산됨!(1x3이 5x3로 맞춰짐 -> broadcasting)
### 1x3이 여러 행으로 쭉 반복되서 5행으로 맞춰짐 
obj1 + obj2
obj1 - obj2
obj1 * obj2
obj1 / obj2

obj2.repeat(5) 
obj2.repeat(5).reshape(3,5)
obj2.repeat(5).reshape(3,5).T ### 이렇게 늘려서 연산 작업 수행(내부적으로 broadcasting을 통해 이런 모양으로 만들어 지는 것)
obj1 + obj2.reshape(5).reshape(3,5).T ### 실제로 연산 작업이 수행되는 형태 
obj1 + obj2

df1 = DataFrame(np.arange(15).reshape(5,3),
                index=[str(i) for i in range(2012,2017)],
                columns=['a','b','c'])
df1
type(df1)

s = df1.ix[0] ### [0,1,2]
s
type(s)
df1 + s ### 여기서도 자동적으로 broadcasting이 수행됨! 



# 정렬 <- 인덱스를 통해 정렬 
## obj.sort_index(): 인덱스 기준 정렬 
## obj.sort_values(): 데이터 기준 정렬 
obj = Series([2,3,5,6], index=['d','c','b','a'])
obj
obj.sort_index() ### 인덱스를 기준으로 오름차순 정렬 
obj.sort_index(ascending = False) ### 내림차순 정렬 
obj.sort_values() ### 값을 기준으로 오름차순 정렬 
obj.sort_values(ascending = False) ### 내림차순 정렬 

df = DataFrame(np.arange(8).reshape(2,4),
               index=['two','one'],
               columns=['d','a','c','b'])
df.sort_index()
df.sort_index(ascending=False)
df.sort_index(axis=0) ### "axis=0": row 정렬 
df.sort_index(axis=1) ### "axis=1": column 정렬 

df.sort_values(by='b', axis=0, ascending=False) ### 컬럼 b를 기준으로 내림차순 정렬(행이 바뀜! -> axis=0)
df.sort_values(by='one', axis=1, ascending=False) ### 로우 one을 기준으로 내림차순 정렬(열이 바뀜! -> axis=1)
0





"""
09-17-2018 
"""
# [문제135] 급여 10000 이상인 사원들의 이름과 급여, 입사일를 출력하세요. 급여를 기준으로 내림차순하세요.
import pandas as pd
emp = pd.read_csv("C:/data/emp.csv")   
emp2 = emp.ix[emp["SALARY"]>=10000, ["LAST_NAME","SALARY","HIRE_DATE"]]
emp2.sort_values(by="SALARY",axis=0,ascending = False) ### by절에 여러 컬럼을 쓰고 싶은 경우 -> [] 모양으로 컬럼을 쭉 넣어주면 됨! 



# 변수명.rank(): 순위 정하는 메소드 

obj = Series([78,88,92,79,67,91,70,86,90,90])
obj.sort_values() ### 값을 기준으로 오름차순 정렬 
obj.sort_values(ascending = False) ### 내림차순 정렬 

obj.rank() ### 오름차순 순위(제일 작은 값이 윗 순위) 
           ### 7.5 <- 동점!(7등과 8등이 없고, 동일 순위를 평균으로 계산!)
obj.rank(ascending = False) ### 내림차순 순위 <- 3.5: 동점의 경우는 평균으로 계산! 

obj.rank() 
obj.rank(ascending = False, method = 'average') ### method = 'average': 동일한 순위일 경우 평균(3.5등)으로 표현(default) 
obj.rank(ascending = False, method = 'min') ### method = 'min': 윗 순위(3등)로 통일(평균이 아닌 동일한 순위로 표현) <- SQL의 rank와 같은 기능 
obj.rank(ascending = False, method = 'max') ### method = 'max': 아래 순위(4등)로 통일(3등 없어지고 4등으로 표현됨) 
obj.rank(ascending = False, method = 'first') ### method = 'first': 동률일 경우, 인덱스 번호가 앞에 있는 걸 위에 랭크 
rank = obj.rank(ascending = False, method = 'dense') ### method = 'dense': 중간에 빠지는 순위 없이 연달아 표현!(3등이 동점이고 바로 뒤에 5등이 아닌 4등!) <- SQL의 dense_rank와 같은 기능 

df = DataFrame([obj,rank], index = ["score","rank"]).T
df = DataFrame({'순위': obj.rank(ascending=False, method='dense'), '점수': obj})
df.sort_values(by="rank")



# NaN 데이터에 대해 sorting 수행 
import numpy as np
obj2 = Series([70,60,80,np.nan,90]) ### np.nan: NaN 표현하는 방법 
obj2.sort_values() ### NaN는 맨 뒤로 감! 
obj2.sort_values(ascending = False) ### 내림차순으로 해도 맨 뒤에 위치! 
obj2.sort_values(ascending = False, na_position = 'first') ### na_position = 'first': NaN을 제일 앞에 위치시킴! 
obj2.sort_values(ascending = False, na_position = 'last') ### na_position = 'last': 제일 뒤에 위치(default) 

obj2.rank() ### NaN는 ranking에서 무시됨! 
obj2.rank(ascending = False)
obj2.rank(na_option = 'keep') ### na_option = 'keep': NaN 무시(default) 
obj2.rank(na_option = 'top') ### na_option = 'top': NaN을 맨 윗 순위에 위치 
obj2.rank(ascending = False, na_option = 'top') ### 내림차순으로 해도 1위! 
obj2.rank(na_option = 'bottom') ### na_option = 'bottom': NaN을 맨 아래 순위에 위치 
obj2.rank(ascending = False, na_option = 'bottom') ### NaN 꼴등! 

df = DataFrame({'영어':[60,80,70], '수학':[50,72,86]},
                index = ['홍길동','박찬호','손흥민'])
df.sort_values(by='수학', ascending=False)
df.sort_values(by='수학', ascending=False)['수학']
df.rank(ascending=False)
df.rank(ascending=False, axis=1) ### 행 단위(학생별)로 랭크! (기존에는 컬럼으로 매겼음!) 

df['영어'].rank(ascending=False)
df.ix['홍길동'].rank(ascending=False) ### 해당 학생이 어느 과목을 더 잘 봤는지에 대한 순위 확인! 



# df['컬럼이름'].isin([데이터])
## in 연산자와 같은 기능 수행! 
## cf. ~: not의 의미! 
df = DataFrame({'영어':[60,80,70], '수학':[50,72,86]},
                index=['홍길동','박찬호','손흥민'])
df[df['수학'].isin([72,86])] ### 수학 점수가 72이거나 86인 row 출력(OR) 
df[~df['수학'].isin([72,86])] ### 수학 점수가 72가 아니고 86가 아닌 row 출력(NAND) 



# NaN값을 처리하는 법 
obj = Series([1,2,3,None,5]) ### None <- np.nan과 같은 기능! 
import pandas as pd 
import numpy as np
from numpy import nan as NA
obj = Series([1,2,3,NA,5]) ### np.nan이 너무 길면 이렇게 NA 별칭을 따로 만들어도 됨! 

obj.fillna(0) ### NA를 0로 바꿔줌 -> 미리보기! 
obj.isnull() ### True/False로 리턴 
pd.isnull(obj) ### 위와 같음(pandas에서 제공) 
obj.notnull()
obj[obj.isnull()] ### NaN만 뽑아냄 
obj[obj.notnull()] ### NaN이 아닌 것들만 뽑아냄 
obj.dropna() ### NaN을 제외시키고 리턴 

df = DataFrame([[1,2,3],[1,None,NA],[NA,NA,NA],[NA,2,3]])
df.dropna() ### []에 NaN이 하나라도 있으면 제외! 
df.dropna(how = 'all') ### []의 원소가 다 NaN일 경우에만 제거! 
df.dropna(axis = 0) ### row 기준 
df.dropna(axis = 1) ### column 기준 
df.dropna(how = 'all', axis = 0) ### 행의 값들이 전부 NaN일 경우 제거 
df.dropna(how = 'all', axis = 1) ### 열의 값들이 전부 NaN일 경우 제거 

df[4] = NA
df
df.dropna(how = 'all', axis = 1) 

df.fillna(0) ### NaN을 다 0으로 채움 <- 미리보기! 
df[0].fillna(0) ### 0번 열의 NaN만 0으로 채움 

df.fillna({0:0,1:1,2:2,4:4}) ### dictionary를 응용해서 각 컬럼 별로 NaN에 채워질 값을 다르게 함! 
df.fillna(0, inplace=True) ### 아예 적용시킴!(미리보기가 아님) 
df

df = DataFrame([[1,2,5],[NA,NA,4],[3,2,NA],[2,NA,3]])
df

df.fillna(method = 'ffill')
df.fillna(method = 'pad')
df.fillna(method = 'bfill')
df.fillna(method = 'backfill')



# apply 함수는 행, 열값을 인수값으로 받아서 반복하여 그 함수를 적용한다. 
s1 = Series([1,2,3])
def square(x):
    return x**2
square(s1)

s1.square() ### 오류! 
s1.apply(square) ### apply 쓰면 각 원소에 함수가 적용됨! 
s1.apply(lambda x:x**2) ### 이렇게 람다 함수를 써도 됨! 

df = DataFrame([[1,2,3],[4,5,6]])
df
df.apply(square)
df.apply(square, axis=0)
df.apply(square, axis=1)

df.apply(np.sum, axis=0) ### 열을 합한 거(세로로 늘어뜨림) 
df.apply(np.sum, axis=1) ### 행을 합한 거 
df.apply(lambda x:x**2, axis=0)
df.apply(lambda x:x**2, axis=1)





"""
09-18-2018 
"""
import pandas as pd 
from pandas import Series, DataFrame 

import numpy as np 
s = Series([2,4,8,np.nan,6]) 

s.sum() ### 자동적으로 NULL을 제외하고 계산 <- 내부적으로 "skipna = True"가 수행되고 있는 것 
s.sum(skipna = True) ### default 
s.sum(skipna = False) ### 연산 작업이 수행되지 않음! 

s.mean()
s.var() ### 표본분산 -> Degree of Freedom! 
s.std()
s.max()
s.min()
s.cumsum() ### 각각의 필드의 누적합을 구할 수 있음 

s.idxmin() ### 최소값의 인덱스 
s.idxmax() ### 최대값의 인덱스 
s[s.idxmin()] ### s.min()과 같음 
s[s.idxmax()] ### s.max()와 같음 

s = Series([2,4,8,np.nan,6,8,2])
s.idxmin() ### 최소값이 2개 있는 데도 하나의 인덱스만 리턴
s.idxmax() ### 최대값이 2개 있는 데도 하나의 인덱스만 리턴 -> max와 min 값을 가지고 비교! 

s[s == s.min()]
s[s == s.max()]
s[s == s.min()].index ### 인덱스만 확인 
s[s == s.max()].values ### 값 확인 -> array형 

s.describe() ### R의 summary와 비슷한 기능 
s.count() ### NaN 제외하고 계산! 
len(s) ### NaN 포함한 개수! 



df = DataFrame([[60,80,70],[50,75,83],[90,83,81]],
               index = ['홍길동','박찬호','손흥민'],
               columns = ['영어','수학','국어'])
df
df.sum() ### 과목별로 sum <- "axis = 0" 
df.sum(axis = 0) ### default 
df.sum(axis = 'rows')
df.sum(axis = 1) ### "axis = 1": 인덱스 별로 계산 
df.sum(axis = 'columns') ### 이름이 혼동되지 않게 주의할 것! 

df.mean()
df.mean(axis = 1)

## 행 추가 
df.at['제임스','영어'] = 100
df.at['제임스','수학'] = np.nan
df.at['제임스','국어'] = 90
df

df.sum()
df.mean()
df.mean(skipna = False)
df.mean(axis = 1, skipna = False)
df.idxmin()
df.idxmax() ### 과목 별로 누가 제일 높은 점수를 받았는지 알 수 있음! 
df.idxmax(axis = 1) ### 학생 별로 제일 높은 점수를 받은 과목이 뭔지 확인 가능! 
df.cumsum()

df['영어'].sum()
df['영어'].mean()
df['영어'].var()
df['영어'].std()
df['영어'].max()
df['영어'].min()
df.loc['홍길동'].sum() ### 행으로 계산 
df.describe()



# Series, DataFrame으로 데이터 조작 
## 리스트 변수를 Series에 집어넣고 수행! 
from pandas import Series, DataFrame
s = Series([1,2,3,4,1,2,3,4,5,1,2,3,4,5,6,np.nan])

## 변수.unique(): unique한 값만 추출 
s.unique() ### nan 값 포함 
ss = s.unique()
ss.dropna() ### 오류! 

ss = Series(s.unique()) ### 이렇게 array를 Series로 만들고 nan을 없애야 됨! 
ss.dropna()

## 변수.value_counts(): 껀수 리턴 
s.value_counts()
s.value_counts(sort = True) ### 빈도 수가 높은 애들부터 리턴 
s.value_counts(sort = False) ### 그냥 인덱스 순서대로 리턴 
s.value_counts(normalize = True) ### 상대 비율값 



df = DataFrame({'a':['a1','a1','a1','a2','a2','a2','a3'],
                'b':['b1','b1','b1','b2','b2','b3',np.nan]})
df['a'].unique()
df['b'].unique()
df['a'].value_counts()
df['b'].value_counts() ### nan 빠짐! 
df['b'].value_counts(dropna = True) ### default 
df['b'].value_counts(dropna = False) ### nan 포함됨! 





"""
09-19-2018 
"""

# groupby() 
'''
# SQL의 group by 

select deptno, sum(sal)
from emp
group by deptno
'''
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp['sal'].groupby(emp['deptno'].dropna().apply(lambda x:round(x))).sum()
emp['sal'].groupby(emp['deptno']).mean()
emp['sal'].groupby(emp['deptno']).var()
emp['sal'].groupby(emp['deptno']).std()
emp['sal'].groupby(emp['deptno']).count()
emp['sal'].groupby(emp['deptno']).max()
emp['sal'].groupby(emp['deptno']).min()

deptno_group = emp['sal'].groupby(emp['deptno'])
deptno_group ### 변수에 들어있는 정보만 확인 가능 
Series(deptno_group.sum().index).apply(lambda x:round(x))
deptno_group.mean()

emp['sal'].groupby([emp['deptno'], emp['job']]).sum()

dept_group = emp['sal'].groupby([emp['deptno'], emp['job']])
dept_group.sum()
dept_mean = dept_group.mean()
dept_mean

emp.groupby(['deptno','job'])['sal'].sum()
emp.groupby(['deptno','job'])['sal'].sum().unstack() ### row에 deptno, column에 job 

## 부서 별로 Data Frame을 다르게 해서 리턴! 
emp.groupby('deptno') ### 리스트? 
for name, group in emp.groupby('deptno'):
    print(name)
    print(group)

## 2개의 카테고리로 구분하고 싶으면 튜플로 구분! 
for (name1, name2), group in emp.groupby(['deptno','job']):
    print(name1, name2)
    print(group)

## groupby()로는 NaN을 집계할 수 없음! -> 가공 필요!! (fillna()를 통해 NaN을 다른 값으로 대체!)
emp['sal'].groupby(emp['deptno'].fillna(0)).sum()
b = list(Series(emp['sal'].groupby(emp['deptno'].fillna(0)).sum().index).apply(lambda x:int(x)))
a = list(emp['sal'].groupby(emp['deptno'].fillna(0)).sum().values)
Series(a, index = b)



# join 
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("C:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])

emp.shape
emp.columns
emp.dtypes

## pd.merge()
pd.merge(emp, dept) ### SQL의 merge는 여러 DML을 한 번에 수행하는 기능 // R과 Python의 merge는 같은 기능을 수행 
pd.merge(emp, dept, on='deptno') ### deptno을 기준으로 merge 수행 
pd.merge(emp[['name','deptno']], dept[['deptno','dname']], on='deptno') ### 일부 컬럼들만 따로 추출해서 merge 수행 
pd.merge(emp[['name','deptno']], dept[['deptno','dname']], left_on='deptno', right_on='deptno') ### merge할 컬럼 이름들이 다르면 이렇게 left_on, right_on으로 나눠서 수행 <- ex. EMPLOYEE_ID vs MANAGER_ID 

pd.merge(emp[['name','deptno']], dept[['deptno','dname']], on='deptno', how='inner') ### 부서코드를 가지고 있지 않은 사원 1명 누락 
pd.merge(emp[['name','deptno']], dept[['deptno','dname']], on='deptno', how='left') ### 왼쪽 데이터프레임은 다 출력!(left outer join)
pd.merge(emp[['name','deptno']], dept[['deptno','dname']], on='deptno', how='right') ### 오른쪽 데이터프레임은 다 출력!(right outer join)
pd.merge(emp[['name','deptno']], dept[['deptno','dname']], on='deptno', how='outer') ### 양쪽 데이터프레임은 다 출력!(full outer join)



## left_index = True // right_index = True 
### 한 쪽에 키 컬럼이 없는 경우 -> 기준 컬럼과 인덱스를 매칭! 
dept = DataFrame({'dname':['관리팀','마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀','영업팀','기획팀','재무팀','회계팀']},
                  index = [10,20,30,40,50,60,70,80,90,100,110])
pd.merge(emp[['name','sal','deptno']], dept, left_on='deptno', right_index=True) ### dept에 해당 컬럼이 없어서 인덱스가 그 역할을 대신 수행! 





"""
09-20-2018
"""

# map(함수, 리스트): 리스트(자료형)와 함수를 묶어서 사용 
## map 함수는 입력받는 자료형의 각 요소가 함수에 수행된 결과를 묶어서 리턴하는 함수
def f(arg):
    result = []
    for i in arg:
        result.append(i*2)
    return result
f([1,2,3,4,5]) ### 곱하기 연산 수행 -> 이렇게 짜는 게 맞지만, 함수가 복잡함! -> map 함수 사용 

def f1(arg):
    return arg*2
f1([1,2,3,4,5]) ### 그냥 같은 숫자가 반복됨(복제)
list(map(f1, ([1,2,3,4,5]))) ### 제대로 수행됨! 

## lambda 사용 
list(map(lambda x:x*2, [1,2,3,4,5]))



from pandas import Series, DataFrame 
import pandas as pd
import numpy as np

x = Series([1,2,3], index=['one','two','three'])
y = Series(['하나','둘','셋'], index=[1,2,3])
### Series는 merge 안 됨! -> DataFrame으로 바꿔야 함! 

x1 = DataFrame(x)
y1 = DataFrame(y)
pd.merge(x1, y1, left_on = 0, right_index = True) ### 한쪽의 컬럼과 다른 한쪽의 인덱스를 붙이는 작업 -> 이것도 map()을 통해 수행 가능! 

## 변수1.map(변수2): 두 Series를 연결! 
### 키값과 키값을 붙이는 기능!! 
x.map(y) ### merge() 수행할 때보다 더 깔끔해짐! (정제 작업도 알아서!) 





"""
09-21-2018 
"""

# matplotlib: 시각화 패키지 
import matplotlib as mpl
import matplotlib.pylab as plt

plt.plot([1,5,10,15,20])
plt.grid(True) ### 격자 
plt.show ### 웹에서 표현하기 위해 사용! 

##  plt.plot([x축],[y축])
### plt.plot([x축],[y축], color=선색깔, linestyle=선종류) 
plt.plot([100,200,300,400,500],[1,5,10,15,20],color='blue')
plt.show 

plt.plot([100,200,300,400,500],[1,5,10,15,20],color='c') ### r, g, b, c, m, y, k 
plt.show 

plt.plot([100,200,300,400,500],[1,5,10,15,20],color='0.75') ### 0~1: 회색조 
plt.show 

plt.plot([100,200,300,400,500],[1,5,10,15,20],color='blue',linestyle='dotted') ### solid, dashed, dashdot 
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20],'--r') ### red dashed 
plt.show 

plt.plot([100,200,300,400,500],[1,5,10,15,20],'-.b') ### blue dashdot 
plt.show 

plt.plot([100,200,300,400,500],[1,5,10,15,20],'-g') ### green solid 
plt.show 

plt.plot([100,200,300,400,500],[1,5,10,15,20],':c') ### dotted cyan
plt.show 

plt.plot([250,200,150,200,250],[2.5,5.5,10,11,12.5],'-r') 
plt.show



data = {'홍길동':[15,13,11],
        '윤건':[13,14,15],
        '나얼':[10,9,12]}
data

df = DataFrame(data, index=['2015','2016','2017'])
df.rank()

x = df.rank()
x
plt.plot(x)
plt.show()

## legend 
plt.plot(x.ix[:,0], label='나얼') 
plt.plot(x.ix[:,1], label='윤건', linestyle='--')
plt.plot(x.ix[:,2], label='홍길동', linestyle=':')
plt.title('기록 순위 비교 그래프', fontsize=15) ### 한글 깨짐! 
plt.xlabel('년도',fontsize=10)
plt.ylabel('순위',fontsize=10)
### plt.xlim([2015.9,2017.1]) ### x축의 범위 
plt.ylim([1,2,3]) ### y축의 범위 
plt.xticks([2015,2016,2017],['2015년','2016년','2017년'])
plt.yticks([1,2,3],['1등','2등','3등']) ### 기존의 label을 다른 형식으로 변환 
plt.legend() ### legend 출력 
plt.show()

## 수평 막대 그래프 
df.plot(kind='barh')

## 수직 막대 그래프
df.plot(kind='bar')

## 스택형 막대 그래프 
df.plot(kind='barh', stacked=True)
df.plot(kind='bar', stacked=True)



%matplotlib inline
import pylab
import scipy
x = scipy.linspace(-2,2,1500)
y1 = scipy.sqrt(1-(abs(x)-1)**2)
y2 = -3*scipy.sqrt(1-(abs(x)/2)**0.5)
pylab.fill_between(x, y1, color='red')
pylab.fill_between(x, y2, color='red')
pylab.xlim([-2.5, 2.5])
pylab.text(0, -0.4, 'Cavin ♥ Julia', fontsize=30, fontweight='bold',
           color='blue', horizontalalignment='center')

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
from skimage import measure
n = 100 
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
z = np.linspace(-3,3,n)
X, Y, Z =  np.meshgrid(x, y, z)
def f_heart(x,y,z):
    F = 320 * ((-x**2 * z**3 -9*y**2 * z**3/80) +
               (x**2 + 9*y**2/4 + z**2-1)**3)
    return F
vol = f_heart(X,Y,Z) 
verts, faces ,_ ,_ = measure.marching_cubes_lewiner(vol, 0, spacing=(0.1, 0.1, 0.1))
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(verts[:, 0], verts[:,1], faces, verts[:, 2],
                cmap='Reds', lw=1)
ax.view_init(15, -15)
### ax.set_title("Cavin ♥ Julia", fontsize=20)
ax.text(4.5,4.5,5.0, "Cavin ♥ Julia", fontsize=25, fontweight = "bold", color="white")
plt.show()

'''
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, 
CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, 
OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, 
Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, 
PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, 
RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, 
Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, 
YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, 
brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, 
copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, 
gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, 
gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, 
gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, 
jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, 
plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spring, spring_r, 
summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, 
terrain, terrain_r, viridis, viridis_r, winter, winter_r
'''





"""
09-27-2018 
"""

# sqlite 패키지 
## 별도의 DB서버가 필요 없이 DB 파일 기초하여 DB 처리하는 엔진 
## Python으로 DB 컨트롤
## 데이터를 구성하기 위해서는 DB를 만들어야 하는데 메모리에 가상 DB 만듬(cursor를 통해 메모리 포인터 지정 )
## 가상 DB -> 메모리에 DB처럼 만들어 사용 -> DB를 잠깐 사용하고 없앰! 

import sqlite3 ### 기본적으로 내장되어 있음!(별도 설치 필요 없음)

conn = sqlite3.connect(":memory:") ### 메모리에 DB 구성
c = conn.cursor() ### 메모리변수.cursor() <- cursor: 메모리 <- SQL을 실행할 수 있는 메모리 영역 <- 별도 변수에 저장! 

## 커서변수.execute("SQL문")
### 실행할 때마다 해당 작업에 대한 메모리 정보 밖에 볼 수 없음 
c.execute("create table emp1(id integer, name text, sal integer)") 
c.execute("insert into emp1(id,name,sal) values(1, '홍길동', 1000)")
c.execute("select * from emp1") ### 메모리에 대한 정보 밖에 안 보임! <- 해당 메모리에서 정보를 가져오는 작업(fetch)을 수행해야 함! 

## 커서변수.fetchone()
### parse => bind => execute => fetch
### execute: 결과물을 메모리에 담아둠 
### fetch: 그 메모리에 있는 정보를 끄집어냄 
c.fetchone() ### "한 줄"만 fetch! 

c.execute("insert into emp1(id,name,sal) values(2, '박찬호', 2000)")
c.execute("select * from emp1")
c.fetchone() ### 처음 실행하면 홍길동만 나오고, 그 다음 실행하면 박찬호만 나옴 <- fetchone()은 하나씩 수행해야 함!  

## 커서변수.fetchall()
### select문을 온전히 수행 가능! 
### transaction이 자동 수행되진 않음! -> 따로 rollback/commit 작업을 수행해야! 
c.execute("select * from emp1")
c.fetchall()

## 메모리변수.rollback() // 메모리변수.commit()
### transaction 수행!(커서변수가 아닌 메모리변수(conn)를 사용해야!)
conn.rollback()
conn.commit()

c.execute("select * from emp1")
c.fetchall()

## 변수.close()
### 메모리 안에 있는 테이블은 지워짐! 
### 메모리에서 사용하고 close 하면 다 사라짐 
### 데이터를 계속 보유하고 싶으면 file 형태로 떨어뜨려야 함! 
c.close() ### 커서 닫음 
conn.close() ### 메모리 닫음 

conn = sqlite3.connect(":memory:") 
c = conn.cursor()
c.execute("select * from emp1")
c.fetchall() ### 해당 테이블이 없음! 

## 파일 형태로 저장 
### sqlite3.connect()에 :memory:가 아닌, 파일 디렉토리를 적음! 
conn = sqlite3.connect("C:/data/insa.db") 
c = conn.cursor()

c.execute("create table emp1(id integer, name text, sal integer)") 
c.execute("insert into emp1(id,name,sal) values(1, '홍길동', 1000)")
c.execute("select * from emp1")
c.fetchone()
conn.commit()

c.close()
conn.close()

conn = sqlite3.connect("C:/data/insa.db") 
c = conn.cursor()
c.execute("select * from emp1")
c.fetchone() ### 메모리와 커서를 닫았다가 열어도 테이블이 그대로 남아 있음! 

## sqlite_master
### 내가 만든 테이블에 대한 정보 <- Oracle의 user_tables // user_objects 
c.execute("select name from sqlite_master where type = 'table'")
c.fetchall()
 
## PRAGMA 
### Oracle의 desc 
### 해당 테이블의 컬럼 정보 확인 가능 
c.execute("PRAGMA table_info(emp1)")
c.fetchall()

## insert문에 ? 입력 
### 해당 필드에 위치 대응되게! 
### insert문을 변수로 만들어서 간편하게 사용할 때 씀! 
c.execute("insert into emp1(id,name,sal) values(?, ?, ?)", (3, '나얼', 3000))
c.execute("select * from emp1")
c.fetchall()

### SQL문을 변수로 저장해서 쓸 수도 있음! 
insert_sql = "insert into emp1(id, name, sal) values(?, ?, ?)"
c.execute(insert_sql, (4, '윤건', 4000)) ### 보다 간편하게 insert 작업 수행! 
c.execute("select * from emp1")
c.fetchall()
conn.commit()

## 커서변수.fetchmany(숫자)
### fetch할 건수 지정 가능 
c.fetchmany(4)

c.execute("update emp1 set sal = 6000 where id = 1") ### 1번 사원의 급여 수정 
c.execute("select * from emp1 where id = 1")
c.fetchall()
conn.rollback()
c.execute("select * from emp1 where id = 1")
c.fetchall() ### 수정되기 전의 값이 리턴됨 

c.execute("delete from emp1 where id = 2")
c.execute("select * from emp1")
c.fetchall()
conn.rollback()
c.execute("select * from emp1")
c.fetchall()

## 컬럼 추가
c.execute("alter table emp1 add column deptno integer")
c.execute("PRAGMA table_info(emp1)")
c.fetchall()

## 테이블 삭제 
c.execute("drop table emp1")
c.fetchall()



c.execute("create table emp(id integer, name text, sal integer, deptno integer)") 
c.execute("insert into emp(id,name,sal,deptno) values(1, '홍길동', 1000, 10)")
c.execute("insert into emp(id,name,sal,deptno) values(2, '박찬호', 2000, 20)")
c.execute("insert into emp(id,name,sal,deptno) values(3, '나얼', 3000, 30)")
c.execute("insert into emp(id,name,sal,deptno) values(4, '윤건', 4000, 40)")
conn.commit()
c.execute("select * from emp")
c.fetchall()

c.execute("create table dept(deptno integer, dname text)")
c.execute("insert into dept(deptno,dname) values(10,'총무부')")
c.execute("insert into dept(deptno,dname) values(20,'영업1')")
c.execute("insert into dept(deptno,dname) values(30,'영업2')")
c.execute("insert into dept(deptno,dname) values(40,'분석팀')")
conn.commit()
c.execute("select * from dept")
c.fetchall()

c.execute("insert into emp(id,name,sal,deptno) values(5, '김건모', 5000, null)")
c.execute("insert into dept(deptno,dname) values(50,'인사팀')")
conn.commit()
c.execute("select * from emp")
c.fetchall()
c.execute("select * from dept")
c.fetchall()



## 1. JOIN 
### Inner Join 
c.execute("""select emp.id, emp.name, emp.deptno, dept.dname 
          from emp inner join dept 
          on emp.deptno = dept.deptno""")
c.fetchall() ### 김건모, 인사팀 정보 안 나옴! <- 김건모는 부서 코드 값이 없고, 인사팀은 소속 사원이 없기 때문(inner join)

### Left Outer Join 
c.execute("""select emp.id, emp.name, emp.deptno, dept.dname 
          from emp left outer join dept 
          on emp.deptno = dept.deptno""")
c.fetchall()
### Right Outer Join과 Full Outer Join은 지원하지 않음! 

c.execute("""select emp.id, emp.name, emp.deptno, dept.dname 
          from dept left outer join emp 
          on emp.deptno = dept.deptno""")
c.fetchall()

## 2. Union 
### Full Outer Join의 기능 수행 가능! 
c.execute("""select emp.id, emp.name, emp.deptno, dept.dname 
          from emp left outer join dept 
          on emp.deptno = dept.deptno
          union
          select emp.id, emp.name, emp.deptno, dept.dname 
          from dept left outer join emp 
          on emp.deptno = dept.deptno""")
c.fetchall()

## 3. Union All 
### 중복이 제거되지 않음! 
c.execute("""select emp.id, emp.name, emp.deptno, dept.dname 
          from emp left outer join dept 
          on emp.deptno = dept.deptno
          union all
          select emp.id, emp.name, emp.deptno, dept.dname 
          from dept left outer join emp 
          on emp.deptno = dept.deptno""")
c.fetchall()

## 4. Intersect 
c.execute("""select emp.id, emp.name, emp.deptno, dept.dname 
          from emp left outer join dept 
          on emp.deptno = dept.deptno
          intersect
          select emp.id, emp.name, emp.deptno, dept.dname 
          from dept left outer join emp 
          on emp.deptno = dept.deptno""")
c.fetchall()

## 5. Except 
### Minus의 기능 
c.execute("""select emp.id, emp.name, emp.deptno, dept.dname 
          from emp left outer join dept 
          on emp.deptno = dept.deptno
          except
          select emp.id, emp.name, emp.deptno, dept.dname 
          from dept left outer join emp 
          on emp.deptno = dept.deptno""")
c.fetchall()

## Nested Query
c.execute("""select id
          from (select id, name from emp)""")
c.fetchall()

c.execute("""select id, sal
          from emp 
          where sal > (select sal from emp where id = 2)""")
c.fetchall()



conn = sqlite3.connect("C:/data/phonebook.db")
c = conn.cursor()
### c.execute("drop table phonebook")
c.execute("create table phonebook(name text, pn text)")
c.execute("insert into phonebook(name,pn) values('오주혜','010-9526-8184')")
c.execute("select * from phonebook")
c.fetchall()

## 대량의 데이터 -> 딕셔너리로 간편하게 insert! 
def dataGenerator():
    datalist = {('윤건','010-7777-8888'),('나얼','010-1004-1004')}
    for i in datalist:
        yield i ### yield: return과 동일한 기능 수행 
c.executemany("insert into phonebook(name,pn) values(?,?)", dataGenerator()) ### 테이블에 집어넣어야 할 데이터를 딕셔너리 형으로 만들어서 insert 작업 수행 
c.execute("select * from phonebook")
c.fetchall()
conn.commit()
c.close()
conn.close()

# Generator 
## list는 list 안에 속한 데이터를 메모리에 적재하기 때문에 list 크기만큼 메모리 사이즈가 늘어나게 된다. 
## generator의 경우는 데이터 값을 한꺼번에 메모리에 적재하는 것이 아니라 next() 메소드를 통해 차례로 값에 접근할 때마다 메모리에 적재하는 방식이다. 
lst = [x*x for x in range(5)] ### 리스트 내장 객체(리스트 결과물이 메모리에 만들어져 있음) -> 데이터 사이즈가 작으면 상관 없는데, 크면 메모리 낭비가 심해질 수 있음!!! 
for i in lst:
    print(i)
lst = (x*x for x in range(5)) ### Generator 방식(generator라는 오브젝트를 만듬, 내부적으로 next 수행) -> 값이 메모리에 미리 만들어지지 않기 때문에 메모리를 보다 효율적으로 사용 
for i in lst:
    print(i)

## next()
### 포인터 정보만 가지고 있음 
### loop문과의 차이점에 주목! 
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g)) ### 4번 수행하면 exception 발생!(4에 해당되는 데이터가 없기 때문)



## Order By절 
c.execute("select * from emp order by sal")
c.execute("select * from emp order by sal desc")



# sqlite와 pandas를 연동 
conn = sqlite3.connect("C:/data/phonebook.db")
c = conn.cursor()

import pandas as pd
from pandas import Series, DataFrame

data = {'id':[1,2,3,4], 'name':['홍길동','박찬호','이병헌','김태리'], 'sal':[1000,2000,3000,4000]}
df = DataFrame(data)
df

## to_sql()
### DataFrame의 정보를 sqlite에 저장 
df.to_sql('test',conn,index=False)

c.execute("select * from test")
c.fetchall() ### pandas의 DataFrame을 그대로 sqlite에 테이블로 구성 

data = pd.read_csv("C:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
data.to_sql('emp_new',conn, index=False)

df_new = pd.read_sql_query("select * from test", conn)
df_new



# Oracle 설치 
# Oracle에 있는 DB 사용 
## Anaconda Prompt 
## python -m install cx_Oracle --upgrade 

import cx_Oracle
dsn = cx_Oracle.makedsn("localhost", 1521, "XE")
db = cx_Oracle.connect("hr", "hr", dsn)
cursor = db.cursor()
cursor.execute("select * from employees")
row = cursor.fetchone()
row
row = cursor.fetchmany()
row
cursor.rowcount

## for문 이용해서 fetch 작업 수행 
cn = 0
for i in cursor.execute("select * from employees"):
    cn += 1
    print(i)

cursor.close()

import csv
import cx_Oracle
con = cx_Oracle.connect("hr/hr@localhost/xe")
cursor = con.cursor()
csv_file = open("C:/data/emp_20180927.csv", "w")
writer = csv.writer(csv_file, delimiter=',')
for row in cursor.execute("select * from employees"):
    writer.writerow(row)

cursor.close()
con.close()
csv_file.close()

## 컬럼 정보 write 
import csv
import cx_Oracle
con = cx_Oracle.connect("hr/hr@192.168.21.31/xe")
cursor = con.cursor()
csv_file = open("C:/data/emp_20180927.csv", "w")
writer = csv.writer(csv_file, delimiter = ',')
col = []
for i in cursor.execute("select column_name from user_tab_cols where table_name = 'EMPLOYEES'"):
    print(i)
    col.append(''.join(i))
writer.writerow(col)
for row in cursor.execute("select * from employees"):
    writer.writerow(row)
cursor.close()
con.close()
csv_file.close()





"""
09-28-2018
"""
# Web Crawling 

# beautifulsoup 
## Anaconda Prompt -> pip install beautifulsoup4
from bs4 import BeautifulSoup

html = '''
<html>
    <body>
        <h1> 스크래핑 </h1>      <- 여기 있는 것만 긁어오고 싶음! 
            <p> 웹페이지 분석하기 </p>
            <p> 데이터 정제작업하기1 </p>
            <p> 데이터 정제작업하기2 </p>
    </body>
</html>
'''
## 1. 분석기(parser) 돌림
soup = BeautifulSoup(html, "html.parser") ### parser라는 분석기를 꼭 돌려야 함! 
### BeautifulSoup는 웹페이지를 긁어오는 작업은 수행할 수 없음 -> 다른 유틸리티를 사용해야 함!(BS는 분석만 하는 거!)

## 2. extracting and untagging 
### html 안에 body 안에 h1 태그! 
h1 = soup.html.body.h1 ### h1 태그에 해당되는 부분만 가져옴! -> 태그 정보(<h1> </h1>)까지 포함! 
h1.string ### 태그 제외! <- BS에 들어있는 기능! 

p1 = soup.html.body.p ### h1 태그는 제외! 첫번째 p만 확인할 수 있음! 
p1.string 
p2 = p1.next_sibling.next_sibling ### 첫번째 p의 다음 줄로 넘어가는 작업(next_sibling을 2번 수행해야 다음 줄을 볼 수 있음!!) -> 두번째 p 확인 가능! 
p2.string
p3 = p2.next_sibling.next_sibling
p3.string



html = '''
<html>
    <body>
        <h1 id='title'> beautifulsoup </h1>
            <p id='subtitle'> 스크래핑 </p>
            <p> 데이터 추출 </p>
    </body>
</html>
'''
## find(): 속성, 문자열 바로 추출 가능 
soup = BeautifulSoup(html, "html.parser")
title = soup.find(id='title').string ### id 속성에 title만 찾아달라는 뜻 <- 굳이 tag 신경 쓸 필요 없이 키워드를 바로 찾을 수 있음 
title.string
soup.find(id='subtitle').string



html = '''
<html>
    <body>
        <ul>
        <li> <a href="http://www.itwill.com"> 아이티윌 </a> </li>        <- li: link 만드는 tag 
        <li> <a href="http://www.naver.com"> 네이버 </a> </li>
    </body>
</html>
'''
soup = BeautifulSoup(html, "html.parser")

a1 = soup.html.body.ul.li.a
a1.string
a2 = soup.html.body.ul.li.next_sibling.next_sibling

## find_all(): 해당 키워드(태그)가 포함된 모든 문장을 찾음 
### 이 메소드는 리스트 형식으로 찾기 때문에, 바로 string을 적용하면 오류! -> for문 이용해야! 
link = soup.find('a').string ### 첫번째 것만 찾아짐 <- find()는 처음만 찾도록 만들어진 기능 
soup.find_all('a')

## 변수.attrs: url 확인(dictionary 타입)
a = soup.a ### 이렇게 해도 찾아짐(첫번째 앵커 태그 a) <- find('a')와 같음! 
a.attrs ### url 확인(a 태그의 속성의 값) <- dictionary 
'href' in a.attrs ### True 

a['href'] ### value만 확인!(dictionary 타입)
a.attrs['href']

link = soup.find_all('a')
for i in link:
    print(i.attrs['href'])
    print(i.string)



html = '''
<html>
    <head>
        <title> 나의 홈페이지 </title>
    </head>
    
    <body>
        <p align = 'center'> 환영합니다. </p>
        <p align = 'left'> 이름: 홍길동 <br> 나이: 25 <br> 취미: 음악감상 </p>
        <p align = 'right'> 오늘 하루도 행복하세요... </p>
        <a href = 'http://itwill.co.kr' class = 'cafe1' id = 'link1'> 아이티윌 </a>
        <a href = 'http://www.naver.com' class = 'cafe2' id = 'link2'> 네이버 </a>
        <a href = 'http://www.google.com' class = 'cafe3' id = 'link3'> 구글 </a>
    </body>
</html>
'''
with open("c:/data/a.html", encoding='UTF8') as html:
    soup = BeautifulSoup(html, 'html.parser')
soup.find('title').string
soup.find('body')
p = soup.find_all('p') ### list 

## 변수.get_text(): string 작업 시 br 태그가 되어 있는 문장들도 잘 출력되게 해줌 
for i in p:
    print(i.string) ### 이름, 나이, 취미는 None이라고 나옴 -> br 태그(줄 바꿈)로 되어 있는 것들은 뽑아지지 않았음! 
for i in p:
    print(i.get_text()) ### br 태그가 되어 있는 부분도 출력됨! 

## 변수.findAll(): find_all()과 같은 기능 
p = soup.findAll('p')
for i in p:
    print(i.get_text())

soup.find('body') ### body 태그 부분 확인 가능  
soup.find('body').string ### 아무 것도 리턴되지 않음 
soup.find('body').get_text() ### tag들 다 없어지고 문장 확인 가능 -> 하지만 '\n' 부분이 남아 있음 
soup.find('body').get_text(strip = True) ### '\n'도 제거됨! -> 하지만 띄어쓰기가 없어져서 불편 
print(soup.find('body').get_text())

body = soup.find('body')
for i in body:
    print(i.get_text()) ### 오류! -> get_text()는 find_all()과 같이 사용할 것!
body = soup.findAll('body')
for i in body:
    print(i.get_text()) ### body 태그에 있는 문장이 하나 밖에 없어도 find_all()이나 findAll()을 사용해서 써야 함! 

a = soup.findAll('a')
for i in a:
    print(i.get_text())

link = soup.find_all('a')
for i in link:
    print(i.attrs['href'])
    print(i.string)

link = soup.findAll('a')
for i in link:
    print(i.attrs['href'])
    print(i.get_text())

## 2번째, 3번째 문장만 추출하는 법
### 1번째 문장은 그냥 find() 쓰면 됨! 
### 각 문장마다 배정된 id가 다른 걸 이용! 
a1 = soup.findAll('a',{'class':'cafe1'}) ### 이 형태로 찾는 거! 
for i in a1:
    print(i.attrs['href'])
    print(i.get_text())

a1 = soup.find('a',{'class':'cafe1'}) ### find() 쓸 때는 for문의 내용을 string으로 바꿔줄 것! 
for i in a1:
    print(i.string)

soup.find('a',{'class':'cafe2'}).string ### 한 줄로 간편하게 표현! 
a2 = soup.findAll('a',{'class':'cafe2'}) ### 2번째 문장 
for i in a2:
    print(i.attrs['href'])
    print(i.get_text())
a2 = soup.findAll('a',{'id':'link2'})
for i in a2:
    print(i.attrs['href'])
    print(i.get_text())

soup.find('a',{'class':'cafe3'}).string    
a3 = soup.findAll('a',{'class':'cafe3'}) ### 3번째 문장 
for i in a3:
    print(i.attrs['href'])
    print(i.get_text())
a3 = soup.findAll('a',{'id':'link3'})
for i in a3:
    print(i.attrs['href'])
    print(i.get_text())

for i in soup.findAll(class_ = 'cafe3'): ### class 값으로 직접 찾는 경우 -> class 뒤에 _ 표시 없으면 syntax 오류! 
    print(i.attrs['href'])
    print(i.get_text())

for i in soup.findAll(id = 'link3'): ### cf. id로 찾을 때는 _ 표시하면 안 됨!(오류는 안 나지만 아무 값도 리턴되지 않음)
    print(i.attrs['href'])
    print(i.get_text())

## get()
for i in soup.findAll('a'):
    print(i.get('href'))

## 2개의 태그를 한꺼번에 검색 
soup.findAll(['a','p']) ### 2개의 태그를 한꺼번에 찾고 싶을 때 <- 리스트로 검색! 

for i in soup.findAll(['a','p']):
    print(i.get_text())



# 기상청 홈페이지 
## http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
## html 형식 
import urllib.request as req
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url) ### 해당 url의 정보 담아둠 

soup = BeautifulSoup(res, 'html.parser')
soup.find('title').string
body = soup.findAll('title')
for i in body:
    print(i.get_text())
soup.find('wf').string
print(soup.find('body').get_text())



# 동아일보 
## 1. URL 추출해서 리스트 저장 
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





"""
10-01-2018 
"""
from bs4 import BeautifulSoup
html="""
<html>
        <body>
                <div id='lecture1'>
                <h1> 데이터 과학 </h1>
                </div>
                <div id = 'lecture2'>
                <h1> 빅데이터분석 </h1>
                <ul class= 'subject'>
                <li> SQL</li>
                <li> R</li>
                <li> PYTHON</li>
        </body>
</html>
"""

soup=BeautifulSoup(html,'html.parser')

# h1의 데이터과학이란 값 찾는 방법
soup.html.div.h1.string ### 방법1
soup.find('h1').string ### 방법2
soup.find('h1').get_text() ### 방법3
soup.find('h1').text ### 방법4
h1=soup.find('h1') ### 방법5
h1.string ### 방법5-1


## SQL/R/PYTHON출력하기
h2=soup.find(id='lecture2')
h2.find('h1').string

soup.find('ul',class_='subject').string
soup.find('ul',class_='subject').get_text()
ul=soup.find('ul',class_='subject')
for i in ul:
    print(i.string) ### 공백줄 나옴
    
for i in ul:
    print(i.get_text()) ### 공백줄 안나오게 하는 방법/그러나 find를 사용했을 경우에 이 매소드는 쓸 수 없음 findAll사용해야함
    
for i in ul:
    print(i.text) ### 공백줄 안나오게 하는 방법/그러나 find를 사용했을 경우에 이 매소드는 쓸 수 없음 findAll사용해야함
    
ul=soup.findAll('ul',class_='subject')
for i in ul:
    print(i.get_text())
    
ul=soup.findAll('ul',class_='subject')
for i in ul:
    print(i.text)

ul=soup.find_all('ul',{'class':'subject'})
for i in ul:
    print(i.text)
    
# css(cascading stylesheets)



# select_one은 css선택자 요소 하나를 추출/find와 같은 기능/한개찾는것

soup.select_one('div > h1').string ### id값 중 첫번째 값 추출
soup.select_one('div#lecture1 > h1').string ### id 1에 대한 lecture2검색
soup.select_one('div#lecture2 > h1').string ### id 1에 대한 lecture2검색

# select는 css선택자로 요소 여러개를 리스트로 추출
s=soup.select('div#lecture2 > ul.subject > li')
for i in s:
    print(i.string)
# 꼭 select사용하지 않고 find_all이나 findAll써도 됨

# 네이버 증권 usd값 크롤링
import urllib.request as req

url="http://finance.naver.com/marketindex"
res=req.urlopen(url)
soup=BeautifulSoup(res,"html.parser")
dollar=soup.select_one("div.head_info > span.value").string
print('USL/KRW',dollar)

soup.select_one("#exchangeList > li.on > a.head.usd > div.head_info.point_up > span.value").string

soup.select_one("#exchangeList > li > a.head.jpy > div.head_info.point_dn > span.value").string
soup.select_one("a.head.cny > div > span.value").string

soup.select_one('a.head.usd > div > span.value').string
soup.select_one('a.head.jpy > div > span.value').string
soup.select_one('a.head.cny > div > span.value').string
soup.select_one('a.head.eur > div > span.value').string

html="""
<ul id= '조선왕'>
<li id= '태조'> '이성계' </li>
<li id= '정종'> '이방과' </li>
<li id= '태종'> '이방원' </li>
<li id= '세종'> '이도' </li>
<li id= '문종'> '이향' </li>
</ul>
"""

# 세종대왕의 이름을 출력하시오
soup=BeautifulSoup(html,"html.parser")
soup.find(id='세종').string
soup.select_one('#세종').string
soup.select_one('li#세종').string
soup.select_one('ul > li#세종').string
soup.select_one('#조선왕 > li#세종').string
soup.select_one('ul#조선왕 > li#세종').string
soup.select_one('li[id=세종]').string
soup.select_one('li:nth-of-type(4)').string ### li를 기준으로 4번째 것을 뽑아낸 것/기준:nth-of-type(순서)
for i in soup.select('li'):
    print(i.string)

soup.select('li')[0].string
soup.select('li')[3].string

# nth-of-type()을 통해 네이버 증권 usd,jpy,chn값출력

# 한 번에 안 될 때는 변수에 담아놓고 시작! 
l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(1)') 
l.select_one('span:nth-of-type(2)').string

l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(1)') 
l.select_one('span:nth-of-type(2)').string

l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(1)') 
l.select_one('span:nth-of-type(3)').string

l = soup.select_one('div.market2 > div.data > ul.data_lst > li:nth-of-type(1)') 
l.select_one('span:nth-of-type(2)').string



# konlpy  
## Anaconda Prompt > pip install konlpy // pip install jpype1
## Java 기반! 

## https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
## pip install Jpype1-0.6.3-cp36-cp36m-win_amd64.whl <- import 안 될 경우!

# 1. Twitter()  
import konlpy
from konlpy.tag import Twitter 

twitter = Twitter() ### 함수 이름 대체 
malist = twitter.pos('아버지 가방에 들어가신다.', norm = True, stem = True) ### norm: "그래욬ㅋㅋㅋ" -> "그래요" 변환! // stem: "그렇다"라는 원형(동사원형)을 찾아줌! 
print(malist) ### 형태소 분석 결과 

txt = "텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집, 처리, 분석, 요약하는 연구기법을 통칭하는 용어이다." 
twitter.nouns(txt) ### 명사만 뽑아내는 작업 -> 완벽하진 않음! 
print(twitter.pos(txt, norm = True, stem = True))





"""
10-02-2018 
"""

# KoNLPy(코엔엘파이)
## - 한국어 정보처리를 위한 파이썬 패키지 
## - 형태소(morpheme, 의미가 있는 말의 최소 단위) <- 자연어 처리에서는 토큰으로 형태소를 이용한다(공백 문자로 나누는 건 한계가 있음)

## - 형태소 분석(morphological analysis)
### 단어로부터 어근, 접두사, 접미사, 품사 등 다양한 언어적 속성을 파악하고 이를 이용하여 형태소를 찾아내거나 처리하는 작업이다. 

## - KoNLPy 
### 형태소 분석을 하기 위해서 필요한 라이브러리를 모아 놓은 패키지이다. 

## - KoNLPy에 속한 라이브러리 
### Twitter: 트위터 코리아에서 개발(http://github.com/twitter/twitter-korean-text)
### Kkma: 꼬꼬마 <- 서울대학교 개발(http://kkma.snu.ac.kr)
### Hannanum: 한나눔 <- KAIST 개발 (http://semanticweb.kaist.ac.kr/hannanum)
### Mecab: 매카브 <- 일본어 형태소 분석기를 한국어에도 사용할 수 있도록 수정 (http://bitbucket.org/eunjeon/mecab-ko)
### Komoran: 코모란 <- shineware에서 개발 (http://github.com/shin285/KOMORAN)

## in Anaconda Prompt 
### pip install konlpy
### pip install jpype1



# 2. Kkma() 
from konlpy.tag import Kkma
kkma = Kkma()

txt = '통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이다. 통찰력을 얻는 좋은 방법은 독서이다'

## kkma.sentences(): 문장을 분석
kkma.sentences(txt) ### .을 기준으로 문장을 2개로 나눔! 

txt2 = '통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이고, 통찰력을 얻는 좋은 방법은 독서이다'
kkma.sentences(txt2) ### 여기선 한 문장으로 나옴! 

## kkma.pos(): 형태소 분석 
### http://kkma.snu.ac.kr <- 이 웹사이트에 들어가면 각 형태소가 뭘 의미하는 지 나옴! 
kkma.pos(txt)

## kkma.nouns(): 명사 분석 
k = kkma.nouns(txt) ### 명사들만 따로 추출! 

### cf. Twitter()로 명사 분석 
from konlpy.tag import Twitter
twitter = Twitter()
twitter.pos(txt)
t = twitter.nouns(txt) ### Kkma()로 분석할 때와 결과가 다름! 

len(k)
len(t)

txt = "텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집, 처리, 분석, 요약하는 연구기법을 통칭하는 용어이다." 
kkma.nouns(txt) ### 이 경우에는 Kkma()가 더 분석 잘 했음! 
twitter.nouns(txt)

import turtle
turtle = turtle.Turtle()
turtle.circle(100)



# nltk 패키지 
## Twitter()나 Kkma()로 추출해낸 명사들의 "빈도 수" 파악! 
## C:\Users\stu\Anaconda3\Lib\site-packages\konlpy\data\corpus\kolaw
## pip install nltk 
import nltk
from konlpy.corpus import kolaw
kolaw.fileids() ### 파일 리스트 정보 확인 가능 

## 파일 오픈 
doc_ko = kolaw.open('constitution.txt').read()
tokens_ko = twitter.nouns(doc_ko)
tokens_ko

## nltk에 속한 메소드들 확인 
ko = nltk.Text(tokens_ko) ### 분석해야 할 토큰 분석 
ko.tokens ### 만들어진 토큰들 확인 
len(ko.tokens) ### 전체 토큰 수 
len(set(ko.tokens)) ### 중복 제거 후의 토큰 수 
ko.vocab() ### 빈도 수 체크 
ko.vocab().most_common(10) ### 상위 10개만 뽑아냄 

import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family = font_name)

plt.figure(figsize = (12,6))
ko.plot(50)
plt.show()



doc_ko = kolaw.open('moon.txt').read()
tokens_ko = twitter.nouns(doc_ko)
tokens_ko
ko = nltk.Text(tokens_ko) 
ko.tokens
ko.vocab()
ko.vocab().most_common(10) 

font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family = font_name)
plt.figure(figsize = (12,6))
ko.plot(50)
plt.show()

## 불용어 처리 
stopword = ['.',',',')','(','의','지','에','간','것','곳','달','것임','겟습','저','제']
ko = [eachword for eachword in ko if eachword not in stopword]

ko = nltk.Text(ko)
len(ko.tokens) ### 불용어 제거 작업 이후 단어의 수가 눈에 띄게 줄어들었음! 
len(set(ko.tokens))
ko.vocab()
ko.vocab().most_common(10)

ko.count('국민') ### '국민'이라는 단어의 빈도 수 확인 
ko.concordance('약속') ### 연관 있는 문구들 
ko.count('것임')



# Wordcloud 
## pip install wordcloud 
from wordcloud import WordCloud
data = ko.vocab().most_common(50)
wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', background_color = 'white', width = 1000, height = 800).generate_from_frequencies(dict(data))
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

## Kkma로 수행 
tokens_ko = kkma.nouns(doc_ko)
ko = nltk.Text(tokens_ko)
stopword = ['.',',',')','(','의','지','에','간','것','곳','달','것임','겟습','저','제','대','분']
ko = [eachword for eachword in ko if eachword not in stopword]
ko = nltk.Text(ko)
len(ko.tokens) 
len(set(ko.tokens))
ko.vocab()
ko.vocab().most_common(10)

data = ko.vocab().most_common(50)
wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', background_color = 'white', width = 1000, height = 800).generate_from_frequencies(dict(data))
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
print([ordinal(n) for n in range(1,32)])



# 워드클라우드를 이미지 형태로 만듬 
## pip.exe list
## Anaconda Prompt에 입력하면 설치된 모듈 리스트 확인 가능 
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("c:/data/moon.txt","r",encoding='UTF-8') as file:
	text = file.read()

from scipy.misc import imread

heart_mask = imread("c:/data/heart.jpg")

wordcloud = WordCloud(font_path = "c://Windows//Fonts//malgunbd.ttf", 
		stopwords=STOPWORDS, ### 불용어가 자동으로 내장되어 있음! 
		background_color="white",
		width=1000,
		height=800,
		mask=heart_mask).generate(text)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()



# 한겨레 만평(이미지 저장)
## 1. URL 추출해서 리스트 저장 
import urllib.request as req 
content = []
url = "http://www.hani.co.kr/arti/cartoon/home01.html" 
res = req.urlopen(url)
soup= BeautifulSoup(res, "html.parser")
lnk = soup.select_one('div.today-comic > a > img').get('src')

from urllib import request
request.urlretrieve(lnk, "C:/data/20181002.jpg") ### 파일 저장 





"""
10-04-2018 
"""
#10/04


# selenum
# 웹브라우저를 컨트롤하여 웹 UI(User Interface)를 자동화하는 도구

# anaconda prompt에 설치하기
# pip install selenium
    
# selenium driver를 설치
# firefox driver : https://github.com/mozilla/geckodriver/releases
# chrom driver : https://sites.google.com/a/chromium.org/chromedriver/downloads
# phantomJS : https://phantomjs.org

from selenium import webdriver
url = "http://www.naver.com"
driver = webdriver.PhantomJS("c:/data/phantomjs.exe") ### 웹브라우저를 조종하는 하나의 프로그램
driver.implicitly_wait(3)
driver.get(url)
driver.save_screenshot("c:/data/naver.png") ### 스크린샷! 
driver.quit()



# 네이버 로그인을 파이썬에서 수행 
from selenium import webdriver
from bs4 import BeautifulSoup

user = 'wine_cooler2'
mypass = 'tolang0825'

## 0. 드라이버 실행 
### driver = webdriver.PhantomJS('c:/data/phantomjs.exe') 
driver = webdriver.Chrome('c:/data/chromedriver.exe') ### 구글 크롬 드라이버로 실행! 
driver.implicitly_wait(3) ### 3초 간 대기 후 들어감 
url_login = 'http://nid.naver.com/nidlogin.login'
driver.get(url_login) ### 해당 URL에 접속(phantomjs driver 이용)

## 1. 아이디 부분 요소 선택 
## driver.find_element_by_id(): 아이디를 입력하는 input 요소를 찾는 메소드 -> id 속성으로 요소를 하나 추출한다. 
inputid = driver.find_element_by_id("id") ### 굳이 키워드를 일일히 찾지 않아도 됨!
inputid.clear() ### 입력박스를 우선 공란으로 만듬 
inputid.send_keys(user) ### 아이디 입력 -> user에 저장된 아이디가 inputid에 들어감! 

## 2. 비밀번호 입력하는 input 요소를 찾는다. 
inputpw = driver.find_element_by_id("pw")
inputpw.clear()
inputpw.send_keys(mypass)

## 3. 로그인 버튼 요소 선택 <- class 기준으로 찾아야! 
## driver.find_element_by_css_selector(): css 선택자로 요소 하나 추출 
loginbn = driver.find_element_by_css_selector("input.btn_global[type=submit]")
loginbn.submit() ### 해당 버튼 클릭 => 아이디와 비밀번호 전송! 

## 4. 분석하고 싶은 웹사이트에 들어감(driver 이용)
## driver.get(URL)
driver.get("https://pay.naver.com/introduction/merchant/list?searchMerchantCategoryCode=50000003&searchTapType=merchant&searchSortType=payOrderCount&searchType=merchantName&searchKeyword=")

## page에 있는 element들 전부 가져옴 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') ### BS는 가져오는 작업 못 하니, driver 이용하는 거! 
notices = soup.find_all('table', class_='tb_list tb_store')
for n in notices:
    print(n.text)
driver.quit()



# 검색해서 이미지를 크롤링
## 이미지 검색하는 URL 찾아야 함 
## 검색 자동화 작업 
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys ### 네이버 이미지는 END키 누를 때마다 새 페이지가 리프레쉬됨 -> 키 제어하는 모듈 사용! 
import time

browser = webdriver.Chrome('C:/data/chromedriver.exe')
browser.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=') ### 네이버 이미지 검색창 주소 
elem = browser.find_element_by_id('nx_query')
elem.send_keys("베놈")
elem.submit()

## browser.find_element_by_tag_name(): 특정 tag 이름만으로도 찾을 수 있음
for i in range(1,2): ### 2페이지까지 해당 작업 반복 -> 더 하고 싶으면 숫자 늘리면 됨  
    browser.find_element_by_tag_name("body").send_keys(Keys.END) ### END 키를 이용할 수 있도록 내부적으로 설정(밑으로 계속 스크롤링될 수 있게!)
    time.sleep(5) ### 너무 빠르게 END키를 누르면 이미지를 제대로 확인할 수 없으니까 5초 정도 keep! 

## 가지고 온 소스들 분석 
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser') ### 분석기 

params = []
imglist = soup.find_all("img", class_="_img") ### 리스트 형식으로 한꺼번에 저장 
for im in imglist:
    params.append(im['src'])

a = 1
for p in params:
    req.urlretrieve(p, 'c:/data/'+str(a)+'.jpg')
    a += 1

browser.quit() 




"""
10-05-2018
"""

# 정규표현식(Regular Expression)

import re

source = "Data Science"

# re.match : 문자열 처음에 일치하는 것이 있는지 찾는다.

re.match('Da',source)
## <_sre.SRE_Match object; span=(0, 2), match='Da'>
## span=(0,2) : 'Da'는 source의 0에서 1번 위치에 있다.

re.match('da',source)
print(re.match('da',source))

m = re.match('Da',source)
if m:
    print("패턴이 일치한다.")
else:
    print("패턴이 불일치한다.")
    
if re.match('Da',source):
    print("패턴이 일치한다.")
else:
    print("패턴이 불일치한다.")
    
if re.match('da',source):
    print("패턴이 일치한다.")
else:
    print("패턴이 불일치한다.")

if re.match('da',source,re.I):  ## re.I : 대소문자를 구분하지 않는다.
    print("패턴이 일치한다.")
else:
    print("패턴이 불일치한다.")

m = re.match('da',source,re.I) 
if m:
    print("패턴이 일치한다.")
    print(m.group())    ## .group() : 일치하는 패턴 출력
    print(m.start())    ## .start() : 시작하는 위치 출력
    print(m.end())      ## .end() : 끝나는 위치+1 출력
    print(m.span())     ## .span() : (시작하는 위치, 끝나는 위치+1) 출력
else:
    print("패턴이 불일치한다.")

bool(re.match('D','Data'))  ## bool() : True or False로 리턴
bool(re.match('[0-9]th','2th'))     ## [0-9] : 한 자리 숫자
bool(re.match('[0-9]th','21th'))
bool(re.match('[0-9][0-9]th','21th'))
bool(re.match('[0-9]*th','21th'))   ## * : 0개 또는 1개 이상
bool(re.match('[0-9]*th','2th'))
bool(re.match('[0-9]*th','th'))
bool(re.match('[0-9]th','th'))
bool(re.match('[0-9]*th','212th'))
bool(re.match('\d\dth','21th'))     ## \d = [0,9]
bool(re.match('\d*th','21th'))

# 매타문자

##    -a.b : .위치에 모든 문자가 온다.
##          aab, acb, aob
          
bool(re.match('D.','Data'))
bool(re.match('D...','Data'))

##    -[.]b : .을 문자로 인식해서 찾는다.
  
bool(re.match('D[.]','D.ata'))

##    -a*b : *은 0번, 1번, 몇 번 이상

bool(re.match('D*','Data'))
bool(re.match('D*','DData'))

##    -a+b : + 앞에 글자가 최소 1번 이상 반복
  
bool(re.match('c+','ccat'))
bool(re.match('c+','cat'))
bool(re.match('c+','at'))

bool(re.match('c*','at'))

##    -a?b : ? 앞에 글자가 0번, 1번 반복
  
bool(re.match('c?','ccat'))
bool(re.match('c?','cat'))
bool(re.match('c?','at'))

##     -a{2}b : a가 2번 반복 aab
  
bool(re.match('c{2}a','ccat'))
bool(re.match('c{2}a','cat'))
bool(re.match('c{2}a','cccat'))

##    -a{2,3}b : a가 2번 또는 3번 반복 aab, aaab
  
bool(re.match('c{2,3}a','ccat'))
bool(re.match('c{2,3}a','cccat'))
bool(re.match('c{2,3}a','cat'))
bool(re.match('c{2,3}a','ccccat'))

##    -a|b : a 또는 b
  
bool(re.match('c|a','cat'))
bool(re.match('c|a','aat'))
bool(re.match('c|a','bat'))

'''
    -[a-zA-Z] : 알파벳 모두
    -[0-9] : 숫자 모두
    -\d : 숫자 [0-9]
    -\D : 숫자가 아닌 것과 매치, [^0-9]
    -\s : 공백문자와 매치
    -\S : 공백문자가 아닌 것과 매치
    -\w : 문자, 숫자와 매치, [a-zA-Z0-9]
    -\W : 문자, 숫자가 아닌 문자, [^a-zA-Z0-9]
'''
  
source = "Data Science"

m = re.match('.*Science',source,re.I) 
if m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.")
    
m = re.match('.+Science',source,re.I) 
if m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.")

m = re.match('.?Science',source,re.I) 
if m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.")

# re.serch : 문자열 전체에서 일치하는 것이 있는지 찾는다.

bool(re.search('Science',source,re.I))

m = re.search('Science',source,re.I)
if m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.")
    
# re.findall : 정규식에 일치하는 문자열을 리스트로 반환한다.
  
source = "Data Science"
re.findall('a',source)
re.findall('A',source)
re.findall('A',source,re.I)

re.findall('a.',source) ## 'a'라는 문자 뒤에 어떤 문자가 왔는지 궁금할 때
re.findall('.a',source)

re.findall('a.?',source)
re.findall('a.+',source)
re.findall('a.*',source)

re.findall('[0-9]','오늘은 2018년 10월 5일 입니다.')
re.findall('\d','오늘은 2018년 10월 5일 입니다.')

re.findall('[0-9]+','오늘은 2018년 10월 5일 입니다.')
re.findall('\d+','오늘은 2018년 10월 5일 입니다.')

re.findall('[^0-9]+','오늘은 2018년 10월 5일 입니다.')
re.findall('\D+','오늘은 2018년 10월 5일 입니다.')

re.findall('[a-zA-Z]+','오늘은 2018년 10월 5일 입니다.')
re.findall('[가-힣]+','오늘은 2018년 10월 5일 입니다.')

# re.sub : 일치하는 패턴을 대체한다.(.replace 와 같은 기능을 한다.)
  
source = "Data Science"

source = source.replace('Science', 'Scientist')
source

source = re.sub('Scientist','Science',source)
source

# re.split : 입력된 패턴을 구분자로 분리한다.

re.split('[:]','python:programming')
re.split('[\:]','python:programming')
re.split('[\,]','python,programming')
re.split('[\,\:]','python,programming:R')
re.split('[ ]','python programming R')
re.split('[\s]','python programming R')
re.split('[,\s]','python,programming R')


## 010101-1234567 -> 010101-*******
re.sub('(\d{6})[-]\d{7}','\g<1>-*******','010101-1234567')
## () 안에는 group 으로 묶여져 \g<n>(n번째 그룹)으로 불러올 수 있다.

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
p.sub("\g<1> \g<2>","james 010-1234-1234")

p.sub("\g<2> \g<1>","james 010-1234-1234")  ## 두 그룹의 위치를 바꾼다.
m = p.search("james 010-1234-1234")
m.group(1)
m.group(2)

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)") ## ?P<> : 그룹의 이름 표현
m = p.search("james 010-1234-1234-1234")
m.group("name")
m.group("phone")

txt = "of the people,  by the people, for the people"

re.findall('people',txt)
re.findall('of|by|for',txt)
re.findall('^of',txt)   ## ^ : 시작 ([^0-9] ^ : not)
re.findall('people$',txt)   ## $ : 끝

re.findall('for (?=the)',txt)   ## the 이전에 나오는 for를 찾는다.
re.findall('(?<=the) people',txt)   ## the 다음에 나오는 people를 찾는다.





"""
10-08-2018 
"""
# 클래스 
## 변수 + 함수

## 모듈화: 작은 단위의 프로그램을 개발한다음 끼워 맞춤 -> 패키지에 모아놓음(유지 보수에 편리, 종속 관계가 심플해짐)
## 메소드: 기능(함수) -> 기능의 프로그램(파이썬은 프로시져 안 만듬)
### PLSQL: 구조적 언어(코드 순차적 수행) // Python: 객체 지향 언어(반복된 코드들은 호출해서 사용 -> 클래스 사용하면 간결해짐)



# 절차(구조적) 지향 프로그램(procedural language) <- PLSQL 
## - C 언어 
## - 물이 위에서 아래로 흐르는 것처럼 순차적으로 처리가 중요시되며 프로그램 전체가 유기적으로 연결되도록 만드는 프로그래밍 기법 
## - 단점
###         - 재사용할 수 없다.
###         - 확장성이 떨어진다. (비슷한 기능임에도 계속 별도의 프로그램을 만들어야 함)
###         - 유지보수가 어렵다. 

adder(3)
adder(4)
## 결과는 7이 되도록 함수를 만드세요. 
### 글로벌 변수 <- 함수가 끝나더라도 지속되는 변수 

### 사용자 A가 프로그램 사용
sum0 = 0
def adder(x):
    global sum0
    sum0 += x
    return sum0
adder(3)
adder(4)

### 사용자 B가 프로그램 사용
sum2 = 0
def adder(x):
    global sum2
    sum0 += x
    return sum2
adder(5)
adder(5)

## 하나의 PC 안에서 다른 사람(사용자 B)이 adder(5), adder(5) 사용 
## => 글로벌 변수에 계속 누적됨!(따로따로 호출할 수 없음)
## => 변수를 따로 선언할 수 밖에 없음 
## <- 구조적 프로그램의 단점!!(똑같은 프로그램을 변수만 바꿔서 2개 만들어야 함 -> 유지보수 어려움!!)
## => 객체 지향 프로그램(하나의 프로그램을 다른 사용자가 각각 따로 쓰는 것처럼 표현)



# 객체 지향 프로그램(object oriented language)
## - Java, C++, C#, Python <- R은 객체 지향 아님! 
## - 구조적 프로그래밍과 다르게 큰 문제를 작게 쪼개는 것이 아니라, 
##   먼저 작은 문제들을 해결할 수 있는 객체들을 만든 후, 
##   이 객체들을 조합하서 큰 문제를 해결하는 방법
## - 객체: 사물 개념 중에서 명사로 표현할 수 있는 것을 의미한다. ex. 사람, 건물, 학생 
## - 클래스: 객체를 설명해 놓은 것(객체의 설계도!) 
## - 인스턴스: 클래스를 "메모리"에 만들어서 사용하도록 하는 의미(객체를 시공!)

## ex. 
### 객체 = 사람 
### 속성(attribute, field) = 변수: 팔, 다리, 머리, 눈, 코, 입, 이름, 키, 나이, 민번, 주소, 학번, 성적, 성격 => 수치나 값으로 표현 
### 메소드(method) = 함수: 기능의 프로그램 처리, 동작하는 것, 속성의 값을 변경하는 기능 



# 클래스 선언 
class Calculator:
    def __init__(self): ### __init__: 초기화시키는 메소드 <- 인스턴스 선언할 때 제일 먼저 수행됨(변수들 초기화시키는 메소드)
        self.result = 0 ### self: 자기자신(클래스 사용하는)을 지정 <- 사용자 A, 사용자 B 
    def adder(self, num):
        self.result += num
        return self.result

### 사용자 A가 클래스 사용 
cal1 = Calculator() ### 인스턴스 선언! (메모리에 변수 저장)
print(cal1.adder(3))
print(cal1.adder(4))

### 사용자 B가 클래스 사용 
cal2 = Calculator() ### 인스턴스 다르게 설정! (메모리에 인스턴스 이름이 다르게 저장됨 -> 같은 클래스를 사용하더라도 결국 다른 거!)
print(cal2.adder(5))
print(cal2.adder(5)) ### cal1(사용자 A)과는 별개로 수행됨!! -> 하나의 프로그램을 2개의 프로그램인 것처럼 수행!!! 



class myClass:
    pass ### 함수, 클래스에서 아무 작업하지 않을 때 사용 

class girlFriend: 
    name = '오주혜' ### __init__ 메소드에 속해 있지 않음 <- 글로벌 변수처럼 취급됨 
    age = 23 ### 만 나이 
    
    def myPrint(self): ### self: 이 클래스/인스턴스를 사용하는 자기 자신을 표현 <- Java에서는 this로 표현 
        print("내 여친 이름은 {}" .format(self.name)) ### 자기 자신의 변수는 꼭 self.변수 이런 식으로 사용 
        print("내 여친 나이는 {}" .format(self.age))

p1 = girlFriend() ### 클래스를 기반으로 인스턴스 생성 
p1.myPrint()

class koiBito: 
    name = '오주혜' ### 변수 선언 
    age = 23 
    
    def herName(self): 
        print("내 여친 이름은 {}" .format(self.name)) 
    def herAge(self):
        print("내 여친 나이는 {}" .format(self.age))

p2 = koiBito() ### 클래스를 인스턴스와 -> 이제부터는 클래스를 사용할 때 인스턴스를 써서 사용해야 한다는 뜻 
p2.herName() ### 인스턴스.메소드() 
p2.herAge()

p3 = koiBito() ### 변수는 똑같이 사용 -> 내 인스턴스 안에서 변수 변경 가능!(p2의 변수는 변화 없음) -> 하나의 클래스를 구미에 맞게 "재사용"(객체 지향 프로그램의 장점!!)
p3.name = 'Julia'
p3.age = 25 ### 한국 나이 
p3.herName()
p3.herAge()
p3.job = '심리학 데이터 사이언티스트' ### 클래스에는 없는 변수를 새로 생성하는 것도 가능 
print("내 여친 직업은", p3.job)



## 변수를 클래스에 미리 지정하지 말고, 인스턴스 생성할 때 변수도 같이 만들고 싶을 경우 
### __init__(self)을 통해 변수 선언! 
class Kanojo:
    def __init__(self): ### 인스턴스 만들 때 무조건 초기화(내가 호출하지 않아도 자동적으로 수행되는 메소드)
        self.info = '' ### 빈 문자열 변수(info) 하나 만듬 <- info: 클래스 안에서만 사용되는 변수 (글로벌 변수가 아님)
    def showinfo(self, name, age):
        self.info += "이름 : " +name+ ", " + "나이 : " +str(age)+ "\n" ### +=: 문자열을 append하게 넣는 거 
        print(self.info)

p4 = Kanojo()
p4.showinfo('오주혜',23)
p4.showinfo('Julia',25) ### 이전 출력값도 포함되어 append하게 나옴! 

class kanoJo:
    def __init__(self): 
        self.info = '' 
    def showinfo(self, name, age):
        self.info += "이름 : " +name+ ", " + "나이 : " +str(age)+ "\n"  

p5 = kanoJo()
p5.showinfo('오주혜',23)
p5.showinfo('Julia',25) ### 이전 출력값도 포함되어 append하게 나옴! 
print(p5.info)

p6 = kanoJo()
p6.showinfo('주혜찡',15) ### 얼굴 나이
p6.showinfo('주혜',16)
print(p6.info) ### 같은 클래스라도 인스턴스를 다르게 하면 다른 메모리에 저장됨! 

name = 'Julia'
class herName:
    def herSet(self, setname):
        self.name = setname
    def myPrint(self):
        print(name) ### self 안 쓰면 글로벌 변수(name = 'Julia') 사용! 
        print(self.name)

p1 = herName()
p1.herSet('오주혜')
p1.myPrint() 

## self.변수: 인스턴스 안에서만 사용
## 클래스.변수: 인스턴스와 상관 없이 변경된 값을 지속적으로 사용 
class Employee:
    empCount = 0 ### 메소드 외부에서 변수 선언(클래스.변수) 
    empInfo = ''
    def __init__(self, name, salary):
        self.name = name ### self.변수이름: 인스턴스 변수(해당 인스턴스에서만 사용)
        self.salary = salary
        Employee.empCount += 1 ### 클래스.변수이름 <- 진정한 글로벌 변수! (인스턴스에 상관없이 공통적으로 사용) cf. self.empCount(): 자기 자신의 인스턴스에서만 수행됨
        Employee.empInfo += "이름 : " +name+ ", " + "급여 : " +str(salary)+ "\n" ### 메모리에 공통으로 사용하는 변수가 만들어짐 
    def displayCount(self):
        print('전체 종업원 수는 %d' %Employee.empCount)
    def displayEmployee(self):
        print("이름 : ", self.name, ", 급여 : ", self.salary)
    def displayTable(self):
        print(Employee.empInfo)

emp1 = Employee('오주혜', 1000)
emp1.displayCount()
emp1.displayEmployee()
emp1.displayTable()

emp2 = Employee('Julia', 2000)
emp2.displayCount()
emp2.displayEmployee()
emp2.displayTable() ### 서로 다른 인스턴스이지만 공유하는 변수(empCount, info)가 있음! <- 클래스.변수 

class Shain:
    pass

emp1 = Shain()
emp2 = Shain()

print(id(emp1))
print(id(emp2)) ### 인스턴스는 메모리의 다른 곳에 저장 

print(emp1.__class__) ### emp1의 클래스 정보 확인 <- 해당 인스턴스가 어떤 클래스에 있는 지 확인 
print(emp2.__class__)
print(id(emp1.__class__))
print(id(emp2.__class__)) ### 클래스는 같은 곳에 저장되어 있음! 

print(id(Shain)) ### 위의 emp1.__class__, emp2.__class__와 같은 곳에 저장 

## 클래스 변수 
Shain.name = '오주혜' ### 클래스 변수 생성(클래스 내부에 아무런 로직도 구현되어 있지 않은데도 변수만 만들어 놓음) 
emp1.name
emp2.name ### 클래스 변수를 만들면, 클래스에 속한 모든 인스턴스에 해당 변수(name)가 생성됨 <- 해당 클래스를 참조하고 있는 모든 인스턴스에 적용 

## 인스턴스 변수 
emp1.name = 'Julia' ### 인스턴스 변수 변경 -> 해당 인스턴스의 변수만 바뀌고, 다른 인스턴스는 자신의 인스턴스 변수가 없으면 클래스 변수 사용! 
emp1.name
emp2.name

emp1.salary = 2000
emp1.salary
emp2.salary ### 오류! (인스턴스 변수가 따로 지정되어 있지 않기 때문) 





"""
10-10-2018 
"""
class Person:
    hobbys = [] ### 클래스 변수(인스턴스 간에 공유) 
    def add_hobby(self, hobby): ### hobby: 매개변수 
        self.hobbys.append(hobby) ### self.hobbys(인스턴스가 클래스 변수를 가져와서 씀)

p1 = Person() ### 인스턴스 만듬 
p1.add_hobby("노래부르기")
print(p1.hobbys)
print(Person.hobbys) ### 클래스 변수를 직접 호출할 수도 있음 

p2 = Person()
p2.add_hobby("글쓰기")
print(p2.hobbys)

class Person2:
    def add_hobby(self, hobby): 
        self.hobbys = [] ### 인스턴스 변수로 만듬 -> 해당 인스턴스에만 적용 
        self.hobbys.append(hobby) 
    def show(self):
        for i in self.hobbys:
            print("내 취미는 " + i + "\n")

p3 = Person2() 
p3.add_hobby("노래부르기")
print(p3.hobbys)
p3.show()

p4 = Person2()
p4.add_hobby("글쓰기")
print(p4.hobbys) ### 각각의 인스턴스 변수에만 저장되고 다른 인스턴스에는 영향을 주지 않음 
p4.show()

class Person3:
    def __init__(self, name): ### 초기화 메소드 <- 인스턴스가 생성될 때마다 변수 초기화 
        self.name = name
        self.hobbys = []
    def add_hobby(self, hobby):
        self.hobbys.append(hobby)
    def show(self):
        for i in self.hobbys:
            print("내 취미는 " + i + "\n")

p5 = Person3('오주혜')
p5.add_hobby('음반수집')
p5.add_hobby('노래부르기') ### 리스트 원소 추가 -> 해당 인스턴스에만 영향 
print(p5.hobbys)
p5.show()

p6 = Person3('곽윤신')
p6.add_hobby('글쓰기')
print(p6.hobbys)
p6.show()



class Person:
    hobbys = [] ### 클래스 변수 
    def __init__(self, name):
        self.name = name
    def add_hobby(self, hobby):
        self.hobbys.append(hobby)
    def show_info(self):
        print(self.name, self.hobbys)

p1 = Person('오주혜')
p1.add_hobby('음반수집')
p1.add_hobby('윤신이랑 놀기')
p1.show_info()

p2 = Person('곽윤신')
p2.add_hobby('주혜랑 놀기')
p2.show_info()

class Person2:
    ### hobbys = [] 
    def __init__(self, name):
        self.name = name
        self.hobbys = [] ### 인스턴스 변수로 초기값 만듬 
    def add_hobby(self, hobby):
        self.hobbys.append(hobby)
    def show_info(self):
        print(self.name, self.hobbys)

p1 = Person2('오주혜')
p1.add_hobby('음반수집')
p1.add_hobby('윤신이랑 놀기')
p1.show_info()

p2 = Person2('곽윤신')
p2.add_hobby('주혜랑 놀기')
p2.show_info() ### 인스턴스에만 변수를 적용시키고 싶을 때는 def __init__ 안에다 넣기! 



## 클래스 변수와 인스턴스 변수의 구분 
class Employee:
    empCount = 0 
    raise_ratio = 1.1 ### 클래스 변수 
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def showCount(self):
        print("전체 종업원의 수는 {}".format(Employee.empCount))
    def showEmp(self):
        print("이름 {}, 급여 {}".format(self.name,self.salary))
    def raise_salary(self):
        print(self.raise_ratio)
        self.salary = int(self.salary * self.raise_ratio)
        print(self.salary)

emp1 =Employee("오주혜",1000)
emp1.showCount()
emp1.raise_salary()
emp1.showEmp()
emp1.raise_ratio = 1.2 ### raise_ratio 재설정 -> 이건 인스턴스 변수(다른 인스턴스에 영향 주지 않음!)
emp1.raise_salary() ### salary 계산 
emp1.showEmp() ### 출력 

emp2 =Employee("곽윤신",2000)
emp2.showCount()
emp2.raise_salary() ### 위에 raise_ratio를 재설정 했음에도, 이 인스턴스에는 변동 사항이 반영되지 않았음! -> 다른 인스턴스에도 반영시키고 싶으면 "클래스 메소드" 사용! 
emp2.showEmp() 

class Employee2:
    empCount = 0 
    raise_ratio = 1.1 
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee2.empCount += 1
    def showCount(self):
        print("전체 종업원의 수는 {}".format(Employee2.empCount))
    def showEmp(self):
        print("이름 {}, 급여 {}".format(self.name,self.salary))
    def raise_salary(self):
        print(Employee2.raise_ratio)
        self.salary = int(self.salary * Employee2.raise_ratio) ### 클래스 변수로 바꿔줌 
        print(self.salary)

emp3 =Employee2("오주혜",1000)
emp3.showCount()
emp3.raise_salary()
emp3.showEmp()
emp3.raise_ratio = 1.2 ### 프로그램의 메소드에 클래스 변수로 되어 있음 -> 변경 안 됨! 
emp3.raise_salary() 
emp3.showEmp()

emp4 =Employee2("곽윤신",2000)
emp4.showCount()
emp4.raise_salary() 
emp4.showEmp() 



# 클래스 메소드 
## 클래스 변수의 변동 사항을 다른 인스턴스에 지속적으로 반영시키는 방법 
## 클래스 메소드를 이용하여 변경 작업 수행 

## 1. 인스턴스 메소드: 인스턴스를 통해 호출되고 인수값은 인스턴스 자신을 자동으로 전달하는 self를 사용해야 한다. 
## 2. 클래스 메소드: 클래스를 통해서 호출되고 @classmethod 데코레이터로 정의하고 클래스 자신을 자동으로 전달하는 인자 cls 사용 
## 3. 스태틱 메소드: 인자(self, cls)를 받지 않는다. ex. 함수 
class Employee:
    empCount = 0 
    raise_ratio = 1.1 ### 클래스 변수 
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def showCount(self):
        print("전체 종업원의 수는 {}".format(Employee.empCount))
    def showEmp(self):
        print("이름 {}, 급여 {}".format(self.name,self.salary))
    def raise_salary(self):
        print(self.raise_ratio)
        self.salary = int(self.salary * self.raise_ratio)
        print(self.salary)
    @classmethod ### 바로 밑은 클래스 메소드라는 걸 알리는 지시자 
    def change_raise_ratio(cls, ratio): ### cls: 클래스 변수를 표현하는 지시자(self가 아님!)
        cls.raise_ratio = ratio 
        print("인상률", round((ratio-1)*100), '%')

emp1 =Employee("오주혜",1000)
emp1.showCount()
emp1.raise_salary() ### 1.1 
emp1.showEmp()
emp1.change_raise_ratio(1.2) ### raise_ratio 재설정 -> emp1에서 변경했지만 emp2에도 영향을 미침(클래스 메소드!) -> ex. 온라인 게임 
emp1.raise_salary() ### 1.2 
emp1.showEmp() 

emp2 =Employee("곽윤신",2000)
emp2.showCount()
emp2.raise_salary() ### 위의 변동 사항이 다른 인스턴스에도 반영이 됨! 
emp2.showEmp() 

## cf1. 다른 인스턴스의 변경 사항도 내 인스턴스에 반영 
emp2.change_raise_ratio(1.5) 
emp2.raise_salary() ### 1.5 
emp2.showEmp()
emp1.raise_salary() ### 1.5
emp1.showEmp() ### 반대로 emp2에서 변경해도 emp1에 영향! 

## cf2. 클래스 변수의 변경도 모든 인스턴스에 반영
Employee.change_raise_ratio(1.6) ### 클래스 변수로 변경 -> 결과는 마찬가지! 
emp1.raise_salary() ### 1.6
emp1.showEmp()
emp2.raise_salary() ### 1.6 
emp2.showEmp() 



# Static Method 
## 인스턴스화 하지 않고 그냥 함수처럼 사용 
class test:
    num = 0
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def sub(x,y):
        num = x-y
        return num ### 맨 위의 "num = 0"와는 아무 상관 없는 변수 
    @staticmethod
    def mul(x,y):
        return x*y
    @staticmethod
    def div(x,y):
        if y == 0:
            return "infinity"
        return x/y

t = test
t.add(1,1) ### 인스턴스를 통해 호출 
test.add(10,20) ### 클래스를 통해 호출 
test.div(1,0) 



# 클래스를 이용해서 게임 만들어보기 
class Viva:
    cnt = 0
    def __init__(self, name):
        self.name = name
        print("{}님이 게임방에 입장하였습니다." .format(self.name))
        Viva.cnt += 1
    @classmethod
    def count_viva(cls): ### 클래스 메소드: 인스턴스 상관 없이 공통적으로 사용하는 메소드 
        print("현재 {} 명이 남았습니다." .format(cls.cnt)) ### cnt는 클래스 변수 -> "cls.cnt" 대신 "Viva.cnt" 이렇게 써도 상관 없음! 
    ### count_viva = classmethod(count_viva) <- 데코레이터(@classmethod) 대신 이렇게 표현해도 됨 
    def __del__(self): ### __del__() <- 소멸자: 인스턴스를 삭제할 때 클래스를 종료하는 메소드 <- "del 인스턴스이름" 이거 수행할 때 메소드가 실행됨! 
        print("{}님이 게임방에서 나갔습니다." .format(self.name))
        Viva.cnt -= 1

man1 = Viva('오주혜')
man1.count_viva()
del man1 ### __del__(self) 수행됨! 

man2 = Viva('곽윤신')
man2.count_viva()
del man2





"""
10-11-2018 
"""
id_number1 = "010101-3123456" 
id_number2 = "990101-2123456"

def id_process(id):
    gender = id[7]
    if gender == "1" or gender == "2":
        year = "19" + id[:2]
    else:
        year = "20" + id[:2]
    
    if gender == "2" or gender == "4":
        gender = "여성"
    else:
        gender = "남성"
    
    month = id[2:4]
    day = id[4:6]
    
    return year, month, day, gender 
    
id_process(id_number1)
id_process(id_number2)

class Person:
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender 
    def __str__(self): ### __str__(): print()와 함께 쓰도록 만듬  
        return "{}년 {}월 {}일 성별은 {}입니다." .format(self.year, self.month, self.day, self.gender)

p = Person(2018, 10, 11, "남")
print(p) ### __str__() 수행됨 

p1 = Person(*id_process(id_number1)) ### * 표현 안 하면 오류! <- id_process를 Person에 집어넣을 때는 인스턴스 메소드가 아닌, 클래스 메소드로 써야함! 
print(p1)

class Person:
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender 
    def __str__(self): ### __str__(): print 기능 
        return "{}년 {}월 {}일 성별은 {}입니다." .format(self.year, self.month, self.day, self.gender)
    @classmethod
    def id_process(cls, id): ### 호출해야 될 함수는 인스턴스 메소드로 구현되면 안 됨! -> 클래스 메소드! 
        gender = id[7]
        if gender == "1" or gender == "2":
            year = "19" + id[:2]
        else:
            year = "20" + id[:2]
    
        if gender == "2" or gender == "4":
            gender = "여성"
        else:
            gender = "남성"
    
        month = id[2:4]
        day = id[4:6]
    
        return cls(year, month, day, gender) 

p1 = Person.id_process(id_number1)
print(p1)

p2 = Person.id_process(id_number2)
print(p2)



# 상속 
## 재사용의 방법 
## 상위 클래스의 일부 속성을 갖다 쓰는 거 
## 클래스 -> 재사용(객체 지향 프로그램의 가장 큰 장점) -> 중복된 코드를 줄이겠다는 뜻(모듈화) 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{} 객체를 만드는 중" .format(self.name))
    def show_info(self):
        print("이름은 {}, 나이는 {}세이다" .format(self.name, self.age))

p1 = Person("오주혜", 23)
p1.show_info() 

class Student(Person): ### Person 클래스를 상속 받겠다는 뜻 
    def __init__(self, name, age, hakbun): ### name, age <- Person 클래스로부터 상속 받음! 
        Person.__init__(self, name, age) ### Person 클래스의 __init__() 메소드도 그대로 상속 받아서 쓰겠다는 의미 
        self.hakbun = hakbun
    def show_info(self):
        Person.show_info(self) ### Person 클래스의 메소드를 상속 받음 
        print("학번은 {}입니다" .format(self.hakbun))

s1 = Student("오주혜", 23, 20181011)
s1.show_info()

class Professor(Person):
    def __init__(self, name, age, years):
        Person.__init__(self, name, age)
        self.years = years
    def show_info(self):
        Person.show_info(self)
        print("근무년수가 {}년입니다" .format(self.years))

f1 = Professor("곽윤신", 29, 10)
f1.show_info()



# static 메소드 
## 인스턴스를 통해서 액세스하고 클래스를 통해서도 액세스하고 싶은 경우 

class Calculator:
    def add(self, x, y): ### 인스턴스 메소드(self 지시자)
        return x+y
    def sub(self, x, y):
        return x-y
    def multiply(self, x, y):
        return x*y
    def divide(self, x, y):
        if y == 0:
            return "infinity"
        return x/y

Calculator.add(1,2) ### 오류! -> 인스턴스 메소드는 인스턴스를 통해서만 수행됨 
c = Calculator()
c.add(1,2)

class Calculator:
    def add(x, y): 
        return x+y
    def sub(x, y):
        return x-y
    def multiply(x, y):
        return x*y
    def divide(x, y):
        if y == 0:
            return "infinity"
        return x/y
    
Calculator.add(1,2) ### 수행됨! 
c = Calculator()
c.add(1,2) ### 인스턴스 액세스는 안 됨! 

## static 메소드 하고 싶은 경우 -> self, cls 쓰면 안 됨! 
class Calculator:
    @staticmethod
    def add(x, y): 
        return x+y
    @staticmethod
    def sub(x, y):
        return x-y
    @staticmethod
    def multiply(x, y):
        return x*y
    @staticmethod
    def divide(x, y):
        if y == 0:
            return "infinity"
        return x/y

Calculator.add(1,2) ### 수행됨! 
c = Calculator()
c.add(1,2) ### 이렇게 해도 수행됨! 



# 모듈화
## 클래스 코드를 메모장에 *.py 형식으로 저장(인코딩: utf-8)
import sys
sys.path
sys.path.append("C:/data")

import cal ### 저장한 파일 로드 -> 모듈로 사용 가능! 
dir(cal) ### cal 안에 어떤 클래스가 있는 지 확인할 수 있음 

c = cal.Calculator() ### 모듈이름.클래스이름() <- 이 형태로 인스턴스 저장 
c.add(1,2)

from cal import *
c = Calculator() ### 이 경우에는 모듈이름 적지 않아도 됨 
a = Add()



# __name__ == "__main__" 
## 이 이하의 로직은 import되지 않음! 
PI = 3.141592
class Math:
    def cal(self, r):
        return PI*(r**2)
def mySum(i,j):
    return i+j   
if __name__ == "__main__": ### 프로그램 테스트용(Spyder에서 드래그하고 실행할 때는 수행됨) <- Math를 import할 때는 수행되지 않게 만듬! 
    print(PI)
    m = Math()
    print(m.cal(10))
    print(mySum(PI,10))

## math_1.py로 저장 
import math_1
dir(math_1)
print(math_1.PI)
m = math_1.Math()
m.cal(10)
math_1.mySum(math_1.PI,10)

from math_1 import *
m = Math() ### 인스턴스
mySum(1,2) ### 메소드 
print(PI) ### 변수 



# 다중 상속 
class Mutter:
    def sprechen(self):
        print("Ich spreche")
class Vater:
    def laufen(self):
        print("Ich laufe")
class Kind(Mutter, Vater):
    def spielen(self):
        print("Ich spiele gern")

m = Mutter()
m.sprechen()
f = Vater()
f.laufen()
c = Kind()
c.sprechen()
c.laufen()
c.spielen()

print(Kind.__mro__) ### 해당 클래스가 어떤 클래스를 상속 받았는 지 확인 

class Hito:
    country = "일본" ### 클래스 변수 -> 인스턴스 변수로도 쓸 수 있음 
    def __init__(self, name):
        self.name = name
    def myPrint(self):
        print(self.name + "은 " + self.country + " 사람이다")

p1 = Hito("곽윤신")
p1.myPrint()

p2 = Hito("오주혜")
p2.country = "독일" ### 인스턴스 변수로 만듬 <- 이게 더 우선순위가 높음! 
p2.myPrint()

Hito.country = "영국" ### 클래스 변수에 적용 
p2.myPrint()
p1.myPrint() ### 이것만 바뀜! (인스턴스 변수가 더 우선)



class Hito:
    __country = "일본" ### __country: 변수 내용을 수정 못 시키게 고정 
    def __init__(self, name):
        self.name = name
    def myPrint(self):
        print(self.name + "은 " + self.__country + " 사람이다")

p1 = Hito("곽윤신")
p1.myPrint()

p2 = Hito("오주혜")
p2.country = "독일" ### 인스턴스 변수로 만듬 
p2.myPrint() ### 하지만 인스턴스 변수가 아닌 클래스 변수가 출력됨 

Hito.country = "영국" ### 클래스 변수 내용 변경 
p2.myPrint() 
p1.myPrint() ### 수정 사항이 반영되지 않음! 



"""
10-12-2018 
"""
import collections 

## Counter 컨테이너(자료형)에 동일한 값의 자료가 몇 개인 지를 파악한다. 
collections.Counter(['a','b','a','c','a','b']) ### 각 원소의 빈도 수 파악 
collections.Counter(['우리','나라','우리','대한민국','우리','행복'])

container = collections.Counter() ### 이렇게 변수로 만들어서 쓸 수도 있음! 
container.update('aaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccddddddddddddddddzzzzzzzzzzzzzzzzzzzz')
print(container)

container.update({'c':2, 'e':5}) ### c를 2개 더함(sum 기능)! e는 새로 추가! 
print(container)

for i in 'abcdefyz':
    print("%s : %d" %(i, container[i]))

c = collections.Counter("hello Julia")
print(c) ### dictionary 형으로 나옴! 
c.keys()
c.values()
list(c.keys())

ct = collections.Counter()
with open("c:\data\Julia.txt","r") as f:
    for i in f:
        ct.update(i.rstrip().lower())
print(ct) ### 컨테이너 안의 빈도 수가 기본적으로 내림차순으로 되어 있음 

for i,c in ct.most_common(5): ### 상위 5개 추출 
    print("%s : %d" %(i,c))



# 사용자 사전 
## pip install customized_konlpy
from konlpy.tag import Twitter ### Kkma보다 Twitter가 속도가 더 빠름! 
twitter = Twitter()
txt = "텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집, 처리, 분석, 요약하는 연구기법을 통칭하는 용어이다."

collections.Counter(twitter.nouns(txt)) ### 일부 단어가 사전에 포함되어 있지 않음 

## 일부 단어들을 사전에 추가 
from ckonlpy.tag import Twitter
twitter = Twitter()
twitter.add_dictionary('마이닝','Noun') ### 단어 추가! 
collections.Counter(twitter.nouns(txt)) 

'♥'*999





"""
10-15-2018 
"""

# Numpy
## https://docs.scipy.org/doc/numpy/user/quickstart.html 
## - 과학 계산을 위한 라이브러리로 다차원배열을 처리하는데 필요한 기능을 제공한다. 
## - numpy 배열은 동일한 타입의 값들을 갖는다. 
## - 배열의 차원을 rank라고 한다. 
import numpy as np

# numpy 배열을 생성
## - 파이썬의 리스트를 사용하는 방법 
### np.array(리스트): 배열을 만드는 메소드 <- 인자값으로 리스트를 집어넣음 
z = np.array([1,2,3])
print(z)
type(z) ### 다차원 배열의 의미 
z.dtype ### int32 <- 32비트 운영 체제에서 사용되는 int형 
z.shape ### 1x3 <- 몇 행 몇 열인지 표시 <- 1차원: (3,) <- 개수 정보만 나옴! 

### 여러 리스트를 인자로 집어넣음 
w = np.array([[1,2,3,],[4,5,6]])
print(w)
type(w)
w.dtype
w.shape ### 2x3



# 인덱싱 
## 정수 인덱싱(integer indexing)
## numpy 배열 n에 대해서 n[[row1, row2], [col1, col2]]는 n[row1, col1], n[row2, col2]와 같음 

lst = [[1,2,3],[4,5,6],[7,8,9]]
x = np.array(lst)
x.shape

x[0,] ### 0행 부분 출력 

## 행 단위 인덱싱 
x[0]
x[1]
x[2]

## 열 단위 인덱싱 
x[:,0]
x[:,1]
x[:,2]

## 슬라이싱 
x[0:2,0] ### x[행, 열] <- 0행, 1행의 1열 리턴 
x[1:,1:] ### 1행부터 쭉, 1열부터 쭉 
x[1:,:1]
x[0:2,0:2]

lst2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n = np.array(lst2)
n[:,:]
n[0,1]
n[2,3]
n[[0,2],[1,3]] ### "0행 1열"과 "2행 3열"에 해당되는 값들을 추출 <- 혼동하지 말 것! 



# Boolean 인덱싱(True/False)
lst3 = [[1,2,3],[4,5,6],[7,8,9]]
n = np.array(lst3)
print(n)
b = np.array([[False,True,False],[True,False,True],[False,True,False]])
print(b)
n[b] ### Boolean indexing <- True 값만 해당되는 것들 추출 <- 조건절과 같이 사용 

b = (n % 2 == 0) 
b ### array b가 Boolean 형식으로 바뀜! 
n[b]
n[n%2 == 0] ### array n에서 짝수인 것들만 뽑아냄 <- Boolean indexing! 



# - numpy에서 제공하는 함수를 사용해서 만드는 방법 

## 1. zeros() 함수는 배열에 모두 0을 넣는 함수 
np.zeros((3,3)) ### 3x3 짜리 영행렬 

## 2. ones() 함수는 배열에 모두 1을 넣는 함수 
np.ones((4,4))

## 3. full() 함수는 사용자가 지정한 값으로 채우는 함수 
np.full((3,3),2)

## 4. eye() 함수는 대각선으로 1이고 나머지는 0인 2차원 배열을 생성하는 함수 <- 단위행렬! 
np.eye(3) ### 정방행렬(nxn)로만 만들 수 있음! 
np.eye(4)

## 5. range(n) 함수는 0~(n-1)까지의 숫자를 생성하는 함수 
np.array(range(20)) ### 0에서 19까지의 값들로 구성되어 있는 벡터(1차원 배열)

## 6. reshape(): 다차원을 변형하는 함수 
z = np.array(range(20)).reshape((4,5)) ### reshape() <- 배열의 차원을 바꿈 
z.reshape((20,)) ### 원위치 
z.reshape((5,4))
z.reshape(5,4) ### 괄호를 한 번만 써도 됨 



# numpy 연산 
x = np.array([1,2,3])
y = np.array([4,5,6])

x[0] + y[0]
x[1] + y[1]
x[2] + y[2]
x + y ### x와 y의 배열 모양이 동일해서 각 인덱스에 맞춰서 연산 작업 수행됨 

## 1. add(a,b)
np.add(x,y) ### 위의 x + y와 값이 같음! 

## 2. subtract(a,b)
np.subtract(x,y) ### x - y

## 3. multiply(a,b)
np.multiply(x,y) ### 같은 인덱스끼리 곱해짐(행렬곱이 아님!)
np.matmul(x,y) ### 행렬곱 

## 4. divide(a,b)
np.divide(x,y) ### x / y

lst1 = [[1,2],[3,4]]
lst2 = [[5,6],[7,8]]
x = np.array(lst1)
y = np.array(lst2)

x[0,0] + y[0,0]
x[0][0] + y[0][0]

## 5. dot(a,b): 행렬곱
np.dot(x,y)
np.matmul(x,y)

np.sum(x) ### 배열 원소들을 전부 더함 
np.sum(x, axis=0) ### axis=0 <- 열을 기준으로 sum 수행 
np.sum(x, axis=1) ### axis=1 <- 행을 기준으로 sum 수행 

np.mean(x) ### 배열 원소들 전체의 평균 
np.mean(x, axis=0) ### axis=0 <- 열을 기준으로 mean 수행 
np.mean(x, axis=1) ### axis=1 <- 행을 기준으로 mean 수행 

np.var(x) ### 배열 원소들 전체의 분산
np.var(x, axis=0) ### axis=0 <- 열을 기준으로 var 수행 
np.var(x, axis=1) ### axis=1 <- 행을 기준으로 var 수행 

np.std(x) ### 배열 원소들 전체의 표준편차
np.std(x, axis=0) ### axis=0 <- 열을 기준으로 var 수행 
np.std(x, axis=1) ### axis=1 <- 행을 기준으로 var 수행 

np.max(x) ### 배열 원소들 전체의 최대값
np.max(x, axis=0) ### axis=0 <- 열을 기준으로 최대값 찾음
np.max(x, axis=1) ### axis=1 <- 행을 기준으로 최대값 찾음 

np.min(x) ### 배열 원소들 전체의 최소값
np.min(x, axis=0) ### axis=0 <- 열을 기준으로 최소값 찾음 
np.min(x, axis=1) ### axis=1 <- 행을 기준으로 최소값 찾음 

## 6. argmin(a): 최소원소의 색인값
np.argmin(x) ### nxm 형식으로 나오는 게 아니라, 한 줄로 쭉 풀어서 인덱스 표현 
np.argmin(x, axis=0)
np.argmin(x, axis=1)

## 7. argmax(a): 최대원소의 색인값 
np.argmax(x)
np.argmax(x, axis=0)
np.argmax(x, axis=1)

## 8. cumsum(a): 누적합 
np.cumsum(x)
np.cumsum(x, axis=0) ### 열 단위 누적합 
np.cumsum(x, axis=1) ### 행 단위 누적합 

## 9. cumprod(a): 누적곱 
np.cumprod(x)
np.cumprod(x, axis=0)
np.cumprod(x, axis=1)

## 10. prod(x): 전체곱(배열 원소들을 모두 곱합)
np.prod(x)
np.prod(x, axis=0)
np.prod(x, axis=1)



# numpy 자료형 
## int, float, bool, complex 

## 정수형(integer)
### int8(2**7), int16(2**15), int32(2**31), int64(2**63) 

## 실수형(float)
### float16, float32, float64 

## complex(복소수): 부동소수점으로 표시하는 복소수 
### complex64, complex128

x = np.float32(1.0)
print(x)
type(x)
x.dtype

z1 = np.arange(5)
z1.dtype

z2 = np.arange(5, dtype="f")
z2.dtype

np.arange(3,5, dtype="f")
np.arange(3,10, dtype="f") ### 3부터 9까지 실수형으로!(1씩 증가)

np.arange(2,3,.2) ### 2에서 3까지 .2씩 증가 

arr = np.arange(10)
arr.shape
arr.reshape(5,2) ### 행 우선! 
arr.reshape((5,2), order="C") ### default 
arr.reshape((5,2), order="F") ### 열 우선 

arr = np.arange(10).reshape((5,2), order="F")



## flatten(), ravel()
### 2차원 배열을 1차원 배열로 평탄화 
arr.flatten() 
arr.flatten("C") ### default 
arr.flatten("F") ### 열 우선 

arr.ravel() ### 위와 같은 기능 
arr.ravel("C")
arr.ravel("F")



## concatenate()
### 2개의 array 합치기 
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
np.concatenate([arr1, arr2], axis=0) ### 열로(길게) 붙임 <- 두 array를 리스트형으로 안 하면 오류! 
np.concatenate([arr1, arr2], axis=1) ### 행으로(넓게) 붙임 

## hstack(), vstack() 
### stack 형식으로 붙임 
np.hstack((arr1,arr2)) ### "np.concatenate([arr1, arr2], axis=1)"와 같음! <- 여기서는 두 array를 ()로 묶어야 함! 
np.vstack((arr1,arr2)) ### "np.concatenate([arr1, arr2], axis=0)"와 같음! 



## numpy 브로드캐스트(broadcast) 
x = np.array([[1,2],[3,4]])
y = 10
x + y ### 본래는 연산 작업이 안 되어야 하지만, y가 x 모양(2x2)에 맞게 broadcast 되었음! 

w = np.array([10,20])
x * w ### w가 x 모양(2x2)에 맞게 자동적으로 변형됨 



## random.rand(): 0~1 사이에 균일한 확률분포로 실수, 난수를 생성하는 함수 
np.random.rand(10) ### 0에서 1 사이의 값을 랜덤하게 10개 뽑음 
np.random.rand(3,5) ### 3x5 

## random.randn(): 기대값이 0이고 표준편차가 1인 표준 정규분포를 나타내는 난수를 생성 
np.random.randn(3,5)

## random.randint(): 균일한 분포의 정수 난수 
### np.random.randint(low, high=None, size=None)
np.random.randint(10, size=10) ### 0부터 10 사이라는 의미 
np.random.randint(10, 20, size=10)
np.random.randint(10, 20, size=(3,5))



## repeat(): 반복 
arr = np.arange(3)
arr.repeat(2) ### 2번씩 반복 
arr.repeat([2,3,4]) ### 0은 2번, 1은 3번, 2는 4번 반복 

arr = np.random.randint(10,20,size=(2,5))
arr.repeat(2)
arr.repeat(2, axis=0)
arr.repeat(2, axis=1)
np.tile(arr,2) ### axis=1과 같은 결과 

## unique(): 유니크한 값들만 뽑힘 
np.unique([11,11,2,3,2,12,12]) 
u = np.array(['a','b','a','a','b','c'])
np.unique(u)
np.unique(u, return_counts=True) ### 값과 빈도 수가 같이 출력됨! 

index, count = np.unique(u, return_counts=True)
print(index)
print(count) ### 따로따로 변수 선언해서 출력 가능! 

u = np.array([[1,0,0],[1,0,0],[2,3,4]])
np.unique(u)
np.unique(u, axis=0) ### 유니크한 row들만 뽑아짐 
np.unique(u, axis=1) ### 순서가 완전히 바뀜! <- 주의! 



## maximum(), minimum() 
### 인덱스끼리 비교해서 최대값, 최소값 리턴 <- 각 array의 개수가 같을 때만 사용 
data1 = np.arange(0,20,2) ### 10개 
data2 = np.arange(0,30,3) ### 10개 
np.maximum(data1,data2) ### 두 array의 요소들을 각각 비교해서 최대값만 뽑아냄 
np.minimum(data1,data2)

## union1d()
np.union1d(data1,data2) ### 중복값 제거하고 union 작업 수행 
np.add(data1,data2) ### 두 array의 각 요소를 단순히 더하는 것(연산 작업) 



## argsort()
arr = np.array([5,4,3,2,1])
ix = arr.argsort() ### 인덱스 번호를 리턴(오름차순 정렬)
arr[ix]

ix = arr.argsort()[::]
arr[ix]
ix = arr.argsort()[::-1] ### descending 
arr[ix]



## cf. pandas의 경우 
lst = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(lst)

import pandas as pd
df = pd.DataFrame(arr)

df.index
df.columns

## pandas의 slicing 
df.loc[1,[0,1]]
df.ix[0:2,[0,1]]
df.iloc[1,[0,1]]





"""
10-16-2018 
"""
# knn
## k값이 너무 높으면 overfitting
## knn의 알고리즘은 유클리드 거리계산

# KNN(K Nearest Neighbors, 최근접이웃)
## - K:갯수를 의미함, 루트 n값으로 표현함,보편적으로 홀수 단위로 하는 것이 좋음
## - 사회적인 관계를 기준: 대략적으로 비슷한 사람끼리 모이는 성질
### 비슷한 취향의 사람들끼리 모여서 동호회를 만듦
### 비슷한 부류의 계층의 사람끼리 친분을 맺기도 함
## - 공간적인 관계를 기준: 가구점이 모이는 상가지역이 따로 형성이 되어 있음
### 한약방이 밀집되어 있는 지역이 따로 모여 있는 경우가 많음
### c=루트((x1-x2)^2+(y1-y2)^2)
## - 가장가까운거리내에서  빈도수가 많은 쪽으로 분류됨
## - 과적합(overffiting): K값이 클수록 유의한 값이 너무 많아지는 현상(유의해야함)
## - 알고리즘은 유클리드 거리(Euclidean distance)를 사용

# 토마토 단맛  6  아삭한맛  4

# 재료     단맛       아삭한맛       음식종류       토마토와의 거리(소수점 첫째자리까지만)
# 포도      8            5            과일         math.sqrt((6-8)**2 + (4-5)**2)==2.2
# 콩        3            7            채소         math.sqrt((6-3)**2 + (4-7)**2)==4.2
# 견과      3            6            단백질       math.sqrt((6-3)**2 + (4-6)**2)==3.6
# 오렌지    7            3            과일         math.sqrt((6-7)**2 + (4-3)**2)==1.4

import math ### 수학과 관련된 함수가 들어있음/sqrt는 루트함수
math.sqrt((6-8)**2 + (4-5)**2) ### 2.23606797749979
math.sqrt((6-3)**2 + (4-7)**2) ### 4.242640687119285
math.sqrt((6-3)**2 + (4-6)**2) ### 3.605551275463989
math.sqrt((6-7)**2 + (4-3)**2) ### 1.4142135623730951
 
# k=1일 경우
## 오렌지 토마토 거리는 1.4로 가까운 이웃하여 과일로 분류함

# k=3일 경우
## 오렌지, 포도, 땅콩 세가지 사이에 다수결로 정함
## 과일이 전체 3개중 2개이기 때문에 과일로 분류함 



a = [4,3,5,7,6,8]
indices = [0,1,4] ### 인덱스 번호 <- 0번, 1번, 4번 인덱스의 값을 뽑아내고 싶음

## np.take(리스트, 인덱스, axis=0)
np.take(a, indices) ### a에서 해당 인덱스 번호에 해당하는 값을 자동 선별하는 기능을 numpy에서 제공함! <- pandas와 numpy를 자유자재로 사용할 줄 알아야 함! 

lst1 = [2,1]
lst2 = [(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]

point1 = np.array(lst1)
point2 = np.array(lst2)

distances = point1 - point2 ### broadcast
distances = pow(point1 - point2, 2) ### square
distances = np.sum(pow(point1 - point2, 2), axis=1) ### sum in numpy
distances = np.sqrt(np.sum(pow(point1 - point2, 2), axis=1)) ### sqrt -> Euclidean 

indices = distances.argsort() ### 오름차순 정렬(인덱스 값을 보여줌)
indices = distances.argsort()[:3] ### slicing 

nn = np.take(lst2, indices, axis = 0) ### "axis = 0"를 설정해야 제대로 된 값들이 나옴!  

from collections import Counter
nn[:,0] ### 모든 행의 첫번째 열 
c = Counter(nn[:,0]) ### 빈도 수 체크 
freq = c.most_common(1)[0][0] ### 제일 빈도가 높은 key 
nn[nn[:,0]==freq] ### 우리가 필요한 값들만 뽑아내어짐!(knn)





"""
10-18-2018 
"""
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

data = {'국민':26, '대통령':33, '대한민국':9, '좋은나라':50, '오주혜':100} ### Crawling 안 하고 이렇게 임의로 지정해서 wordcloud 만들 수 있음! 
wordcloud = WordCloud(font_path = 'C:\Windows\Fonts\malgunbd.ttf', 
                      stopwords=STOPWORDS, 
                      background_color='white', 
                      width=1000, height=800).generate_from_frequencies(data)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()



from nltk.tokenize import word_tokenize
import nltk
from konlpy.tag import Twitter

pos_tagger = Twitter()
train = [('오주혜는 좋아','긍정'), 
         ('강아지는 너무 좋아','긍정'), 
         ('수업이 재미없어','부정'), 
         ('오주혜는 내 여친이야','긍정'),
         ('난 수업 마치고 주혜랑 놀거야','긍정'),
         ('오늘 하루는 너무 짜증스러운 날이야','부정'),
         ('하루가 너무 짜증스러운 날이야','부정'),
         ('날이 맑아서 좋아','긍정'),
         ('오늘 지하철에 사람이 너무 많아서 짜증이 난다','부정'),
         ('지하철에서 질서는 너무 없어 짜증이 난다','부정'),
         ('비가 오니 짜증난다','부정'),
         ('친구가 짜증난다','부정'),
         ('하늘이 맑아서 행복하다','긍정'),
         ('공기가 맑아서 좋다','긍정'),
         ('밝게 인사해주니 행복하다','긍정')] ### (키워드, 목표변수)
train[1][0]

import numpy as np
train = np.array(train)
train[:,1]

import nltk
nltk.download('punkt')

allword = set(word for sentence in train ### train의 값들을 sentence에 넣어서 token 작업 수행하고 난 다음 word에 집어넣음 
                for word in word_tokenize(sentence[0])) ### 0번 요소만 tokenize해서 word에 전달 
allword

t = [({word : (word in word_tokenize(x[0])) for word in allword}, x[1]) for x in train]
t

## NaiveBayes <- nltk 모듈 안에 있음 
classifier = nltk.NaiveBayesClassifier.train(t)
classifier.show_most_informative_features() ### 너무=False <- "너무"라는 말이 "없을" 때 긍정의 확률이 더 높은 지 부정의 확률이 더 높은 지 표현 

## 테스트 
test = '난 수업을 마치면 주혜랑 놀 거야'
test_f = {word:(word in word_tokenize(test)) for word in allword}
classifier.classify(test_f)

test2 = '오늘 왠일이니 짜증난다'
test2_f = {word:(word in word_tokenize(test)) for word in allword}
classifier.classify(test2_f) 

## 함수를 따로 생성해서 텍스트 마이닝 
def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

train_doc = [(tokenize(row[0]), row[1]) for row in train]
train_doc

tokens = [t for d in train_doc for t in d[0]]
tokens

def term_exists(doc):
    return {word:(word in set(doc)) for word in tokens}

train_x = [(term_exists(d),c) for d,c in train_doc]
train_x

classifier = nltk.NaiveBayesClassifier.train(train_x)
classifier.show_most_informative_features()

## 테스트 
test = [('주혜랑 놀거야')]
test_doc = tokenize(test[0])
test_f = {word:(word in tokens) for word in test_doc}
classifier.classify(test_f)



## 카이제곱(Chi-squared)
## 엔트로피(Entropy)
## 지니지수(Gini Index) 

# 의사결정트리
## - 의사결정규칙(Decision rule)을 나무구조(Tree)로 도표화하여 분류(classification)와 예측(prediction)을 수행하는 방법 

# 활용분야 
## - 은행분야: 도산업체 분류(예측) -> 과거의 데이터로부터 도산기업과 도산하지 않은 기업을 찾아내는 방법 
## - 카드발급대상: 신용불량자 분류(예측)
## - 통신: 이탈고객(해지자, 번호이동) 분류, 새로운 서비스 대상 고객 선정 
## - 쇼핑: Direct Mailing 대상 고객 선정 

# 결정트리의 장점 
## - 지도학습(분류, 예측)의 데이터마이닝 기법 
## - 적용결과에 의해 if - then 으로 표현하는 규칙이 생성
## - 규칙의 이행이 쉽고 SQL로도 할 수 있다. 
## - 많은 분야에서는 결정을 내리게 되는 것에 대한 이유를 설명하는 능력이 중요하다(해석력, 근거자료) ex. 이러이러한 항목에 의해 대출을 불허합니다. 

# 분류나무(classification tree) 
## - 목표변수: 범주형 데이터가 보편적(도산 vs 정상, 좋음 vs 나쁨)
## - 분류 알고리즘 
###     CART: 지니지수(Gini Index)
###     C5.0: 엔트로피 지수(Entropy Index)
###     CHAID: 카이제곱통계량(Chi-Square Statistics) 

# 교차분석
## - 교차분석은 범주형(명목척도, 서열척도)으로 구성된 자료들간의 연관관계를 확인하기 위해 교차표를 만들어 관계를 확인하는 방법
## - 변수들의 빈도를 확인하고 그 빈도를 이용하여 상호 연관성을 판단한다(빈도를 이용하는 이유는 명목척도이기 때문에)
## - 이때 검정통계량으로 카이제곱(χ²) 통계량을 이용하기 때문에 카이제곱검정이라고 한다. 
## - 카이제곱(Chi-Square)검정을 하기 위해서 교차표, 관측빈도, 기대빈도(<- 주변확률), 카이제곱통계량의 자유도(df=(r-1)*(c-1))가 있어야 한다. 

# 교차표 
## - 2개의 조사요인에 대한 자료값을 각각 행과 열로 배열하여 교차되는 항목에 대한 빈도를 나타낸 표를 교차표라 한다. 
## - 교차표의 행과 열에 범주형(명목척도) 변수를 구분하여 넣으면 서로 연관성이 있는 빈도를 확인할 수 있다. 

## ex. 지역 1과 지역 2로 구분하여 최신 스마트폰의 구매 의사에 대한 각각의 행과 열에 해당하는 빈도를 표시한 교차표 
'''
<교차표> 
                    구매의사
            있음               없음          행의 합

지역1        154(관측빈도)      52            206
기대빈도     102               104
차이         51                -52  

지역2         7                112           119
기대빈도      59                60
차이         -52               52

카이제곱 

열의 합      161               164           325     

df = (행의수-1)*(열의수-1) = (2-1)*(2-1) = 1
'''
## 관측빈도(observed frequency) 
### - 교차표를 작성할 때에는 직접 수집하는 데이터를 기준으로 빈도를 입력해야 하는데 이처럼 실제로 수집된 데이터의 빈도를 관측빈도라고 한다. 
### - 실제로 수집된 데이터에 대한 빈도! 

## 기대빈도(expected frequency)
### - 기대빈도를 전체빈도 n에 대하여 행과 열의 합을 기준으로 보았을 때 각 교차되는 셀에 몇 번의 빈도가 확인될 수 있을 지를 예상하는 기대값이다. 
'''
                행의 합 * 열의 합
기대빈도 = ---------------------------      <- 이 공식을 셀마다 적용하면 됨! <- 이걸 토대로 Chi-statistics 만듬! 
                    관측 수
'''
206*161/325
206*164/325
119*161/325
119*164/325

## 카이제곱 통계량(카이제곱검정) 
### - 카이제곱통계량이란 관측빈도와 기대빈도 사이의 유의한 차이가 있는지를 확인하는 통계량을 의미한다. 
'''
                    (관측빈도 - 기대빈도)²
카이제곱(χ²) = Σ ---------------------------
                          기대빈도
'''
(51**2)/102 + (52**2)/104 + (52**2)/59 + (52**2)/60

# 카이제곱 분포에서의 자유도 
## - 카이제곱검정을 실시하는 경우에는 p값을 이용할 수 있으며, 카이제곱분포의 유의수준과 자유도에 따라 결과를 판단한다. 
### 자유도가 높아지면 그래프가 정규분포에 가까워짐! 

## df(Degree of Freedom) 자유도 = k-1 (k는 범주형 변수의 수)
### - 교차표에서 구성된 범주에 대한 자유도를 계산하는 방법은 교차표의 (행의수-1)*(열의수-1)

# 독립성 검정(independence test)
## 1. 가설수립: 각 범주가 서로 독립적인지 아닌지에 대한 검정이므로 귀무가설은 독립인 것이다. <- 귀무가설: 일반적으로 알고 있는 사실 
'''
H0(Null Hypothesis) 귀무가설, 영가설 
- 귀무가설은 일반적으로 믿어온 사실을 가설로 설정한다. 
- 귀무가설은 당연한 사실이나 연구할 의미가 없는 가설로 설정한다. 

H1(Alternative Hypothesis) 대립가설, 연구가설 
- 공공연하게 사실로 받아들여진 현상에 대립되는 가설로 연구를 통한 대립가설의 조사는 의미가 있다. 

H0: 지역과 구매의사는 독립이다. (지역과 구매의사는 아무런 상관관계가 없다.) <- 이걸 빨리 찾으면 됨!(~이다, ~없다)
H1: 지역과 구매의사는 독립적이지 않다. (지역과 구매의사 간에는 상관관계가 있다.)
''' 
## 2. 교차표, 교차빈도
## 3. 기대빈도
## 4. 카이제곱통계량
## 5. 자유도 
## 6. 임계치: 카이제곱 분포표에서 α=0.01(99%의 유의수준), 자유도(df=1) 임계치는 6.63(table 참조)이므로, 143.3(chi-stats)보다 작다
##            <- 어느 선까지는 괜찮다(H0를 채택한다)는 기준
## 7. 결론: 귀무가설을 기각하고 대립가설을 채택한다 





"""
10-19-2018
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:01:14 2018

@author: stu
"""

# 정보이론(information theory)
## information
## degree of surprise 놀람의 정도

# 앤트로피(entropy)
## -무질서
## -열역학 제2법칙
## -entrophy는 정보량의 평균
## (-Σp)*log2p

# 의사결정트리
## 제일먼저 물어봐야할 컬럼이 무엇인가를 찾는 것

import pandas as pd
tree = pd.read_csv("C:/data/tree.csv")
tree
tree[['습도','테니스유무']]
a = np.array(tree['습도'])
b = np.array(tree['테니스유무'])
pd.crosstab(a,b, rownames=['습도'], colnames=['테니스유무'])
'''
테니스유무  아니요  예
습도           
높음        4       3   7     
보통        1       6   7
            5       9   14

'''
import numpy as np ### 로그계산을 위해서 numpy를 사용
## 앤트로피(전체)
(-9/14)*np.log2(9/14)+(-5/14)*np.log2(5/14)

## 앤트로피(습도높음)
(-3/7)*np.log2(3/7)+(-4/7)*np.log2(4/7)

## 앤트로피(습도보통)
(-6/7)*np.log2(6/7)+(-1/7)*np.log2(1/7)

## 정보이득=전체앤트로피+(-7/14)*앤트로피(높음)+(-7/14)*앤트로피(보통)
##        =0.94+(-7/14)*0.98+(-7/14)*0.59
##        =0.154

## 모든 변수에 관한 정보 이득값을 계산하고 "가장높은 정보이득값"을 가진 변수를 선택

import pandas as pd
tree = pd.read_csv("C:/data/tree.csv")
tree
tree[['날씨','테니스유무']]
a = np.array(tree['날씨'])
b = np.array(tree['테니스유무'])
pd.crosstab(a,b, rownames=['날씨'], colnames=['테니스유무'])

'''
테니스유무  아니요  예   
날씨           
맑음        3       2    5
비          2       3    5
흐림        0       4    4
           5       9    14
'''

## 앤트로피(전체)
(-9/14)*np.log2(9/14)+(-5/14)*np.log2(5/14)

## 앤트로피(날씨맑음)
(-3/5)*np.log2(3/5)+(-2/5)*np.log2(2/5)

## 앤트로피(날씨비)
(-2/5)*np.log2(2/5)+(-3/5)*np.log2(3/5)

## 앤트로피(날씨흐림)
(-0/4)*np.log2(0/4)+(-4/4)*np.log2(4/4)

## 정보이득=전체앤트로피+(-5/14)*앤트로피(맑음)+(-5/14)*앤트로피(비)+(-4/14)*앤트로피(흐림)
##        =0.94+(-5/14)*0.97+(-5/14)*0.97+(-4/14)*0
##        =0.247

## 브라질이 이길확률의 앤트로피
-np.log(0.99)=0.01
-np.log(0.01)=4.6

0.99*-np.log(0.99)+0.01*-np.log(0.01)=0.05
0.5*-np.log(0.5)+0.5*-np.log(0.5)=0.69

0.05<0.69
'''
지니계수
1- Σp²
'''
## 습도 지니 기댓값 구하기
1-pow(3/7,2)-pow(4/7,2) ### =0.49
1-pow(6/7,2)-pow(1/7,2) ### =0.24

(7/14)*0.49+(7/14)*0.24 ### =0.365
## 습도 지니 기댓값=(7/14)*0.49+(7/14)*0.24=0.37


import pandas as pd
tree = pd.read_csv("C:/data/tree.csv")
tree
tree[['바람','테니스유무']]
a = np.array(tree['바람'])
b = np.array(tree['테니스유무'])
pd.crosstab(a,b, rownames=['바람'], colnames=['테니스유무'])

'''
테니스유무  아니요  예   
바람           
강함       3       3    6
약함       2       6    8
           5       9    14

'''
## 바람 지니 기댓값 구하기
1-pow(3/6,2)-pow(3/6,2) ### =0.5
1-pow(2/8,2)-pow(6/8,2) ### =0.375

(5/14)*0.5+(9/14)*0.375 ### =0.419
## 바람 지니 기댓값=(5/14)*0.5+(9/14)*0.375#=0.419

## 모든 변수에 관해 지니 기댓값을 계산하고 "최소 지니기댓값을 가진 변수"를 최적변수로 선택한다.

# 카이제곱
## 습도=2.8
## 바람=0.94

## 카이제곱검정에 대한 결과를 가지고 p값을 찾음
## p값의 가장 낮은 값을 가진 변수를 선택하면 됨



# 붓꽃 품종 분류
## 붓꽃의 꽃잎(petal),꽃받침(sepal)의 폭, 길이를 측정하여 품종을 예측
## 붓꽃의 품종은 150종류 이상있고 크게 3가지로 분류됨(setosa,versicolor,virginia)

import pandas as pd
dataset=pd.read_csv("C:/data/iris.csv")
dataset.head()
x=dataset.drop('Name',axis=1)
y=dataset['Name']
x
y ### 목표변수/label값

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
x_train
y_test
y_train

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





"""
10-22-2018 
"""

# Graphviz 
## Visualisation for Python 
## C:\Program Files (x86)\Graphviz2.38\bin
## 내 컴퓨터 마우스 오른쪽 클릭 -> 속성 -> 고급 시스템 설정 -> 환경 변수 -> 시스템 변수 -> PATH 편집 -> 주소 맨 끝에 세미콜론 하고 붙여넣기 
## http://www.graphviz.org 

## pip install pydotplus
## pip install graphviz 



#그래프비즈 다운로드 받기
##그래프비즈파일 다운로드 받는 경로
###http://www.graphviz.org
##파일이 다운로드 받아진 경로의 주소를 복사해두기
###C:\Program Files (x86)\Graphviz2.38\bin
###컴퓨터->속성->고급시스템설정->환경변수->Path변수를 누르기->편집->기본경로에 ;C:\Program Files (x86)\Graphviz2.38\bin 쓴 후 저장
##anaconda prompth
###pip install pydotplus
###pip install graphviz

from graphviz import Digraph
dot = Digraph(comment='The Round Table')
dot
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
print(dot.source)
dot.render('test-output/round-table.gv', view=True)



import pydotplus
import graphviz
from sklearn.tree import export_graphviz
from IPython.display import Image

##########################################################################
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
##########################################################################

dot_data = export_graphviz(classifier, out_file = None, ### classifier: 모델
                           feature_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'], ### feature_names: 모델 안에 사용한 변수들 표현(리스트 형식)
                           class_names = ['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], ### class_names: 꽃의 종류(category) 적음 
                           filled=True, rounded=True, special_characters=True) ### 그래프의 모양 
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png()) 
'''
1. 먼저 PetalWidth에 대해 물어봄
2. gini index <- default // If you wanna use entropy, you should fix "classifier=DecisionTreeClassifier()"
'''



# titanic from Kaggle 
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





"""
10-24-2018 
"""

# K Means
## Unsupervised Learning <- no target! 
## 목표 변수가 없으니, 독립 변수들 간의 특징들을 파악해서 분류!
## cf. KNN <- supervised learning(목표 변수 존재) 

## - 데이터 클러스터(cluster, 유사한 아이템의 그룹)로 자동 분리하는 비지도학습의 머신러닝이다. 
## - 군집화는 데이터 안에서 발견되는 자연스런 그룹에 대한 통찰력을 제공 
## - 클러스터 안에 있는 아이템들은 서로 아주 비슷해야 하지만 클러스터 밖에 있는 아이템과는 아주 달라야 한다. 

# 군집화 활용 범위 
## - 마케팅 캠페인을 위해 유사한 인구 통계나 구매 패턴을 가진 그룹으로 고객을 세분화 
## - 알고 있는 클러스터 밖에 사용 패턴을 찾아 무단 네트워크 침입과 같은 이상 행동을 탐지 

# k-means algorithm 
## k <- 군집으로 나눠야 할 그룹의 개수 
## cf. KNN의 k <- test data와 거리가 가장 가까운 점들의 수 

## - n개의 예시를 k개의 클러스터 중 하나에 할당하는데 이때 k는 사전에 결정되는 수 
## - 클러스터 내의 차이를 최소화하고 클러스터 간의 차이는 최대화한다. 

## 적당한 k값은? -> "k = n/2" 

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

model ### init='k-means++' <- 'k-means++' : selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. 



academy = pd.read_csv("c:/data/academy.csv")
academy.columns
model = KMeans(n_clusters=4)
model.fit(academy.iloc[:,2:4])
model.labels_
model.cluster_centers_ ### 중심 좌표 

colormap = np.array(['red','blue','black','yellow'])
plt.scatter(academy.iloc[:,2], academy.iloc[:,3], c=colormap[model.labels_], s=30)
centers = pd.DataFrame(model.cluster_centers_)
plt.scatter(centers.iloc[:,0], centers.iloc[:,1], s=50, marker='D', c='g') ### 중심 좌표의 위치 표시 
plt.show()



ks = range(1,10)
inertia = []
for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(academy.iloc[:,2:4])
    inertia.append(model.inertia_) ### k값이 늘어나면서 inertia 값은 줄어듬 -> 감소하는 정도는 점점 더뎌짐 -> 값이 작을 수록 응집도가 좋아짐(여기에 해당하는 k값을 찾아야!)
plt.plot(ks, inertia, '-o')
plt.xlabel("number of cluster K")
plt.ylabel("inertia")
plt.xticks(ks) ### x축 정보 
plt.show()

# inertia value 
## 각 중심점에서 군집의 데이터 간의 거리를 합산한 것으로 군집의 응집도를 나타내는 값이다. 
## 이 값이 작을 수록 응집도가 높게 군집화가 잘 되었다고 평가한다. <- 값이 작을 수록 거리가 작고 서로 가깝다는 뜻!(그룹이 잘 만들어진 거) 





"""
10-29-2018
"""

# Covariance 
## 1. numpy 이용 
import numpy as np
x = [184,170,180]
y = [85,70,82]

np.cov(x,y)
np.cov(x,y)[0][1]

np.corrcoef(x,y) ### coefficient of correlation 

## 2. pandas 이용 
import pandas as pd
df = pd.DataFrame({'x':x,'y':y})
df['x']
df['y']

df['x'].cov(df['y'])

df['x'].corr(df['y']) ### coefficient of correlation 



# scipy 
height = [176, 172, 182, 160, 163, 165, 168, 163, 182, 182]
weight = [72, 72, 70, 43, 48, 54, 51, 52, 73, 88]

from scipy.stats import pearsonr
pearsonr(height, weight) ### (상관계수, p-value)

## pvalue = 0.00002614 + 0.0002614 합이 양측검정에서는 pvalue 0.0005228이기 때문에 유의수준 0.05라고 하고
## pvalue < 0.05가 되어 귀무가설을 기각하고 대립가설을 채택한다. 
## 유의수준 0.05 아래에서는 두 변수는 상관관계가 있다. 



# 회귀분석 
from scipy import stats 
## 월별 전기 생산금액(억원) -> 독립변수 
x = [3.52, 2.58, 3.31, 4.07, 4.62, 3.98, 4.29, 4.83, 3.71, 4.61, 3.90, 3.20]
## 월별 전기사용량(백만kwh) -> 종속변수 
y = [2.48, 2.27, 2.47, 2.77, 2.98, 3.05, 3.18, 3.46, 3.03, 3.25, 2.67, 2.53]
## 단순선형 회귀분석 
### stats.linregress(독립변수,종속변수)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) ### r_value: 상관계수, std_err: 에러의 표준편차 

## 생산금액 4억 => 사용량 ? 2.9백만kwh 
slope * 4 + intercept

## H0: 전기생산금액과 전기사용량은 상관관계가 없다. 
## H1: 전기생산금액과 전기사용량은 상관관계가 있다. 
p_value < 0.05
## 상관관계가 있다! 

# Visualisation 
import numpy as np
import matplotlib.pyplot as plt
x1 = np.array(x)
plt.scatter(x,y)
plt.plot(x1, slope*x1+intercept, c='red') ### array 형식으로 만들어야 함! 



import pandas as pd
df = pd.read_csv("C://data/ozone.csv")
df.head()
## 컬럼별 결측값 개수 
df.isnull().sum() ### 각 변수의 NaN 건수 카운트  
## 행 단위로 결측값 개수 
df.isnull().sum(axis=1) ### 행 단위로 계산 

df2 = df.dropna(axis=0)
df2.isnull().sum()

x = df2['Temp'].values
y = df2['Ozone'].values
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

## H0: 온도와 오존은 상관관계가 있다. 
## H1: 온도와 오존은 상관관계가 없다. 
p_value < 0.05
## 상관관계가 있다! -> reject H0

## 온도가 화씨 80도일 때 오존량 예측? 
slope*80 + intercept



# sklearn 이용 
score = pd.read_csv("C://data/score.txt")
score
slope, intercept, r_value, p_value, std_err = stats.linregress(score.iloc[:,2], score['성적'])

p_value < 0.05
## IQ와 성적에는 상관관계가 있다! -> reject H0

from sklearn import linear_model ### 선형회귀모형을 만듬 
reg = linear_model.LinearRegression() ### 인스턴스화 
reg.fit(score.iloc[:,2:6], score['성적']) ### fitting 
print('절편 : \n',reg.intercept_)
print('기울기 : \n',reg.coef_)





"""
11-01-2018 
"""

# OR Gate 
'''
x1  x2  y
---------
0   0   0
0   1   1
1   0   1
1   1   1
'''

# AND Gate 
'''
x1  x2  y
---------
0   0   0
0   1   0
1   0   0
1   1   1
'''

# NAND Gate 
'''
x1  x2  y
---------
0   0   1
0   1   1
1   0   1
1   1   0
'''

# XOR Gate 
'''
x1  x2  y
---------
0   0   0
0   1   1
1   0   1
1   1   0
'''

# y = ax + b
# y = a1x1 + a2x2 + b
## i) y=0 -> w1*x1 + w2*x2 <= θ         <- θ: 임계값(critical value) 
## ii) y=1 -> w1*x1 + w2*x2 > θ

## 위 두 식들을 b로 변환! -> 임계값을 좌측으로 이동 -> θ를 -b로 바꿈! 

# b: 편향(bias)
## 가중치와 편향을 도입한 퍼셉트론 식 
## i) y=0 -> w1*x1 + w2*x2 <= -b
## ii) y=1 -> w1*x1 + w2*x2 > -b

## i) y=0 -> w1*x1 + w2*x2 + b <= 0
## ii) y=1 -> w1*x1 + w2*x2 + b > 0
### 이 식들을 이용해 신경망 분석! 

import numpy as np
def AND(x1, x2):
    x = np.array([x1, x2]) ### array 형식(행렬 모양)으로 만들어서 계산하기 편하게 함! 
    w = np.array([0.5, 0.5]) ### weight 
    b = -0.7 ### bias 
    tmp = np.sum(w*x) + b ### numpy의 array는 각 element간의 곱이 성립됨! 
    if tmp <= 0:
        return 0 ### 지도학습! -> 원하는 결과가 나오도록 weight(기울기), bias(편향) 조정! -> 퍼셉트론에서는 수동으로 조정 // 신경망은 자동으로 조정!  
    else:
        return 1
AND(0,1)
AND(1,1)

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2 ### bias값 조정 
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) ### weight값 조정 
    b = 0.7 ### bias값 조정 
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y



# 인공신경망(ANN, Artificial Neural Network) 
## 인간의 뇌 구조를 모방하여 모델링한 수학적 모델이다. 

# 신경세포(neuron 뉴런)
## 뉴런의 입력은 다수이고 출력은 하나이며, 여러 신경세포로부터 전달되어 온 신호들은 합산되어 출력된다. 
## 합산된 값이 설정값(threshold) 이상이면 출력 신호가 생기고 이하이면 출력 신호가 없다. 

## 세포체(cell body): 노드(node) 
## 수상돌기(dendrites): 입력(input)
## 축삭(axon): 출력(output)
## Synapse: Weight(가중치) 
'''
input -> neuron -> output
            ^
            |
          bias

affine sum(∑): 최종적으로 출력값(y)을 만들기 위해 모으는 작업 
         weight w
input x ---------> sum(∑) ---------> y output
                    ^
                    |
                  bias
'''
## σ = w*x + b
## x = 0.6
## w = 3
## b = 1
## σ = 0.6*3 + 1 = 2.8



# 활성화함수(activation function) 
## 1. 계단함수 
## 2. 시그모이드 

## - synapse는 전달된 전기신호가 최소한의 자극값을 초과하면 활성화되어 다음 뉴런으로 전기신호를 전달한다. 
## - 활성화 함수는 이것을 모방하여 값이 작을 때는 출력값을 작은값으로 막고 일정한 값을 초과하면 출력값이 "급격히" 커지는 함수를 이용한다. 
## - 신경망에서는 전달받은 데이터를 가중치를 고려해서 합산하고 그 값을 활성화 함수를 적용해 다음 층에 전달한다. 
'''
         weight w
input x ---------> σ|f(σ) ---------> y output
                     ^
                     |
                   bias
'''
## σ = w*x + b
## f(σ) = f(w*x+b)

# 1. 계단함수 
## 임계값을 경계로 출력이 바뀌는 함수 
## 입력이 0을 넘으면 1을 출력하고 그 외에는 0을 출력하는 함수 
def step_function(x):
    if x>0:
        return 1
    else:
        return 0

import numpy as np
step_function(1)
step_function(-1)
step_function(100) ### 무조건 0 아니면 1 
### 다음 뉴런에 값을 전달할 때, 임계값을 0으로 해서, 임계값을 넘으면 1의 강도로 전달! 

## array 형태도 인자값으로 받을 수 있게 수정(boolean 형식 이용)
def step_function(x):
    y = x>0 ### boolean(True/False)
    return y.astype(np.int) ### astype 자료형 변환 메소드: True/False 값을 1/0으로 변환! (boolean -> int)
step_function(np.array([1,2]))
step_function(np.array([1.0,-2.0]))
step_function(np.array([-1.0,1.0,2.0]))

## 더 간단하게! 
def step_function(x):
    return np.array(x > 0, dtype=np.int)

## Visualisation 
import matplotlib.pylab as plt
X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1) ### y축의 범위 지정
plt.show()

# 2. sigmoid(시그모이드)
## 신경망에서는 활성화 함수로 시그모이드 함수를 이용하여 신호를 변환하고 그 변환된 신호를 다음 뉴런에 전달하는 함수이다. 
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x)) ### e^(-x) <- e: 자연상수 2.7182... 

X = np.arange(-5.0, 5.0, 0.1)
Y = sigmoid(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show()

sigmoid(1)
sigmoid(2) ### 숫자가 커질 수록 1에 수렴 
sigmoid(100) ### 1로 딱 떨어져도 실수형인 1.0으로 표현됨 
sigmoid(-100)
sigmoid(np.array([-1.0, 2.0, 3.0]))

## - 계단함수는 최종적인 결과가 0과 1중 하나의 값만 전달 
## - 시그모이드 함수는 0과 1 "사이"의 실수값을 전달 
## - 시그모이드 함수는 곡선, 계단함수는 계단처럼 구부러진 직선 
### 단층 퍼셉트론 -> 계단함수 // 다층 퍼셉트론 -> 시그모이드(신경망에서는 비선형인 시그모이드가 더 적절 )

## - 신경망에서는 활성함수로 비선형함수를 사용해야 한다. 
## - 비선형함수를 사용해야 은닉층을 표현할 수 있다. 

# 3. ReLU(Rectified Linear Unit)
## 입력이 0을 넘으면 그 입력값으로 "그대로" 출력하고, 0 이하면 0을 출력한다. 
import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x) ### 두 입력 중에 큰 값을 선택해 반환하는 함수 

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()

relu(2)
relu(-1)
relu(np.array([-1.0, 1.0, 2.0]))



# 다차원 배열의 계산 
## np.dim(변수): 배열의 차원 수 
## 변수.shape: 배열의 모양 
## np.dot(변수1, 변수2): 행렬의 내적 곱
a = np.array([1,2,3,4])
a
np.ndim(a) ### 배열의 차수 
a.shape ### 배열의 모양 
'''
3행 2열 
1 2
3 4
5 6
''' 
b = np.array([[1,2],[3,4],[5,6]]) ### 2차원 배열은 꼭 []로 한 번 더 묶어야 함! 
b
np.ndim(b)
b.shape 

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
x
y

np.dot(x,y) ### 행렬의 내적 곱 -> x의 컬럼 수와 y의 로우 수가 일치해야 성립! 

'''
x <- 2x3
1 2 3
4 5 6 

y <- 3x2
1 2
3 4
5 6
'''
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2],[3,4],[5,6]])
x
y
np.dot(x,y) ### (2x3) x (3x2) -> (2x2)

'''
x <- 3x2
1 2
3 4
5 6

y <- 1x2 or 2x1
7 8
'''
x = np.array([[1,2],[3,4],[5,6]])
y = np.array([7,8])
x
y
np.dot(x,y) ### y가 자동으로 transpose 됨



x = np.array([1,2])
w = np.array([[1,3,5],[2,4,6]])
y = np.dot(x,w)
y



# 3층 신경망
## 1개의 입력층, 2개의 은닉층, 1개의 출력층 
 
## 1) 입력층에서 1층의 첫번째 뉴런으로 신호 전달 
x = np.array([1.0,0.5]) ### 입력층
w1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) ### weight값은 2행 3열로 설정 
b1 = np.array([0.1,0.2,0.3])

x.shape ### 입력값 
w1.shape ### weight 
b1.shape ### bias 

a1 = np.dot(x,w1) + b1 ### affine sum: a1 = x*w1 + b1 <- 행렬의 차원 신경써줘야!! 
z1 = sigmoid(a1) ### 1층의 출력값 <- 활성화 함수(계단함수, sigmoid, ReLU)를 통해 신호 크기 증폭 

## 2) 1층에서 2층으로 신호 전달
### 첫번째 은닉층이 새로운 입력층의 역할 수행 
w2 = np.array([[0.1,0.4], [0.2,0.5], [0.3,0.6]]) ### weight값은 3행 2열로 설정 
b2 = np.array([0.1,0.2])

z1.shape ### 입력값 <- 1층의 출력값이 2층의 입력값이 됨! 
w2.shape ### weight 
b2.shape ### bias 

a2 = np.dot(z1, w2) + b2 ### affine sum 
z2 = sigmoid(a2) ### 2층의 출력값 

## 3) 2층에서 출력층으로의 신호 전달 
### 활성화 함수가 은닉층에서 썼던 거랑 다름!  
def identity_function(x): ### 항등함수 <- 출력층에서 사용하는 활성화 함수(항등함수 말고 소프트맥스를 사용할 수도 있음)
    return x

w3 = np.array([[0.1,0.3],[0.2,0.4]]) ### weight값은 2행 2열로 설정
b3 = np.array([0.1,0.2])
a3 = np.dot(z2,w3) + b3 ### affine sum 
y = identity_function(a3) ### 출력! 



# 소프트맥스 함수(softmax function): 지수값을 출력한다. 
## 분류할 때 "비율"을 따질 때는, 항등함수보다 소프트맥스가 더 좋음 <- 소프트맥스는 합이 1.0(100%)으로 고정 
## 문제점1: 숫자가 너무 크면 inf라고 나옴 <- overflow => 입력신호 중에 최대값을 미리 설정해놔야 함! 
## 문제점2: 지수 계산 수행 시 컴퓨터 자원 낭비 발생 
a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
sum_exp_a = np.sum(exp_a)
exp_a / sum_exp_a

d = np.array([100,1000,10000])
softmax(d)

def softmax(a):
    c = np.max(a) ### 최대값 설정! -> 확률값으로만 나오게 설정 
    exp_a = np.exp(a - c) ### 분자와 분모에 최대값(c)을 뺌으로서 오버플로우 방지! 
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

y = softmax(a3) 
