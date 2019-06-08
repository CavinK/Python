'''
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
for i in range(2000,3201,1):
    if i%7==0 and i%5!=0:
        print(i, end=', ')
'''
Solution:
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print ','.join(l)
'''

'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a * factorial(a-1)
factorial(8)
'''
Solution:
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input())
print fact(x)
'''

'''
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary 
that contains (i, i*i) such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
def dictionary():
    dic = {}
    a = int(input("Enter your number: "))
    for i in range(1,a+1):
        dic[i] = i*i 
    return dic
dictionary()

'''
Solution:
n=int(raw_input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print d
''' 

'''
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
def listup():
    a=input()
    lst=a.split(',')
    tup=tuple(lst)
    print(lst)
    print(tup)
listup()
'''
Solution:
values=raw_input()
l=values.split(",")
t=tuple(l)
print l
print t
'''

'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class dual:
    def __init__(self):
        self.cha=""
    def getString(self):
        a=input("Enter your string: ")
        self.cha=a
        return self.cha
    def printString(self,cha):
        return self.cha.upper()
    def __main__(self):
        self.cha="I am the best"
        self.getString(self.cha)
        
st=dual()
st.printString(st.getString())
'''
Solution:
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()
'''

'''
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''
def root():
    import math
    a=input()
    lst=a.split(',')
    lst2=[]
    for i in lst:
        lst2.append(int(i))
    lst3=[]
    for j in lst2:
        lst3.append(str(round(math.sqrt(((2*50*j)/30)))))
    return ','.join(lst3)
root()
'''
Solution:
#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)
'''

'''
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''
def twodim():
    import numpy as np
    a=input()
    lst=a.split(',')
    npz = np.zeros((int(lst[0]),int(lst[1])))
    for i in range(0,int(lst[0])):
        for j in range(0,int(lst[1])):
            npz[i,j]=i*j
    return npz
twodim()
'''
Solution:
input_str = raw_input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print multilist
'''

'''
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and 
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
def sortstr():
    a=input()
    lst=a.split(',')
    lst.sort()
    return ','.join(lst)
sortstr()
'''
Solution:
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
'''

'''
Question 9
Level 2

Question:
Write a program that accepts sequence of lines as input and prints the lines 
after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
def makeCap():
    a = input("Enter your sentences: ")
    return a.upper()

def makeCap2():
    lst = []
    while 1:
        a = input("Enter your sentences: ")
        if a == '':
            break
        lst.append(a)
    for i in lst:
        print(i.upper())
    
makeCap()
makeCap2()
'''
Solution:
lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print sentence
'''

'''
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
def sortAlpha():
    x = input("Enter your sentence: ")
    y = list(set(x.split(" ")))
    y.sort()
    return " ".join(y)
sortAlpha() 
'''
Solution:
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
'''

'''
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
def binDec(n): 
    if len(n)==1:
        return int(n[0]) 
    else: 
        return int(n[0])*(2**(len(n)-1)) + binDec(n[1:len(n)])
def findDiv():
    x = input("Enter your binary numbers: ")
    y = x.split(',')
    l = []
    for i in y:
        if binDec(i)%5==0:
            l.append(i)
    return ",".join(l)
findDiv() 
'''
Solution:
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print ','.join(value)
'''

'''
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def eachEven():
    l = []
    for i in range(1000,3001):
        if int(str(i)[0])%2==0 and int(str(i)[1])%2==0 and int(str(i)[2])%2==0 and int(str(i)[3])%2==0: 
            l.append(str(i))
    return ",".join(l) 
eachEven()
'''
Solution:
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print ",".join(values)
'''

'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
def letDig():
    x = input("Enter your sentences: ")
    cnt1, cnt2 = 0, 0
    import re
    for i in x: 
        if bool(re.match('[a-zA-Z]',i)):
            cnt1+=1
        elif bool(re.match('[0-9]',i)):
            cnt2+=1
    print("LETTERS", cnt1)
    print("DIGITS", cnt2)
letDig()
'''
Solution:
s = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]
'''

'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
def upLow():
    x = input("Enter your sentences: ")
    cnt1, cnt2 = 0, 0
    import re 
    for i in x:
        if bool(re.match('[A-Z]',i)):
            cnt1+=1
        elif bool(re.match('[a-z]',i)):
            cnt2+=1
    print("UPPER CASE",cnt1)
    print("LOWER CASE",cnt2)
upLow() 
'''
Solution:
s = raw_input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print "UPPER CASE", d["UPPER CASE"]
print "LOWER CASE", d["LOWER CASE"]
'''

'''
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
def weird():
    x = input("Enter your number(0-9): ")
    if int(x)<0 or int(x)>9:
        print("Error! The number must be between 0 and 9!!")
        return weird()
    else: 
        x2, x3, x4 = x+x, x+x+x, x+x+x+x 
        return int(x)+int(x2)+int(x3)+int(x4)
weird()

'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
def eachOdd():
    x = input("Enter your numbers: ")
    l = [i for i in x.split(',') if int(i)%2!=0] 
    return ','.join(l)
eachOdd()
'''
Solution:
values = raw_input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print ",".join(numbers)
'''

'''
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
logD, logW = [], []
def bankAccount():
    x = int(input("Enter your amount of money: "))
    y = input("Deposit or Withdrawal?(D/W)")
    if y=='D':
        logD.append(x)
    elif y=='W':
        logW.append(x)
    
    z = input("Any other transactions?(Y/N)")
    if z=='N':
        for i in logD:
            print("D",i)
        for j in logW:
            print("W",i)
        return sum(logD)+sub(logW)
    elif z=='Y':
        return bankAccount()

def sum(x):
    sum0=0
    for i in x:
        sum0+=i
    return sum0
def sub(x):
    sub0=0
    for i in x:
        sub0-=i
    return sub0

bankAccount()

'''
Question 18
Level 3

Question:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords 
and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
def password():
    import re 
    x = input("Enter your passwords: ") 
    l = x.split(",")
    for i in l:
        if bool(re.search('[a-z]',i)) and bool(re.search('[0-9]',i)) and bool(re.search('[A-Z]',i)) and bool(re.search('[$#@]',i)) and len(i)>=6 and len(i)<=12: 
            print(i)
password()
'''
Solutions:
import re
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print ",".join(value)
'''

'''
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples 
by ascending order where name is string, age and height are numbers. 
The tuples are input by console. 
The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
def sortTuple():
    import pandas as pd
    raw, cover = [], []
    while 1:
        x = input()
        if not x:
            break
        l = x.split(",")
        raw.append(tuple(l))
    df1 = pd.DataFrame(raw)
    df2 = df1.sort_values(by=[0,1,2])
    for i in range(0,len(df2)):
        cover.append(tuple(df2.iloc[i]))
    return cover
sortTuple()
'''
Solutions:
from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))
'''

'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.
'''
def divSeven(n):
    l = [i for i in range(0,n+1) if i%7==0]
    return l 
divSeven(50)
'''
Solution:
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print i
'''

'''
Question 21
Level 3

Question: 
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. 

Please write a program to compute the distance from current position 
after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.

Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
def botStep(): 
    from math import sqrt
    l = [] 
    while 1: 
        z = input() 
        if not z:
            break 
        e = z.split(" ") 
        l.append(e) 
    x,y = 0,0 
    for (i,j) in l: 
        if i == "UP": 
            y += int(j) 
        elif i == "DOWN": 
            y -= int(j)
        elif i == "LEFT": 
            x -= int(j)
        elif i == "RIGHT": 
            x += int(j) 
    return round(sqrt(x**x + y**y))
botStep() 
'''
Solution:
import math
pos = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print int(round(math.sqrt(pos[1]**2+pos[0]**2)))
'''

'''
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
def freqWord(): 
    x = input("Enter your sentence: ") 
    d = {}
    l = x.split(" ")
    l.sort() 
    for i in l: 
        if not bool(d.get(i)):
            d[i] = 1
        else: 
            d[i] += 1 
    return d 
freqWord() 
'''
Solution:
freq = {}   # frequency of words in text
line = raw_input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print "%s:%d" % (w,freq[w])
'''

'''
Determines the maximal 'binary gap' in an integer
:param N: a positive integer (between 1 and maxint or 2million odd)
:return: a count of the longest sequence of zeros in the binary representation of the integer
'''
def longZero(n): 
    x = str(decBin(n))
    l, d = [], 0 
    for i in range(0,len(x)):
        if x[i]=='1':
            l.append(d)
            d=0
            continue
        elif i==len(x)-1 and x[len(x)-1]=='0':
            d+=1
            l.append(d)
            break
        elif x[i]=='0':
            d+=1
    return decBin(n), max(l)

def decBin(n):
    l1, l2 = [], [] 
    while 1:
        if n==0:
            break
        l1.append(n%2)
        n = n//2 
    for i in range(len(l1)-1,-1,-1):
        l2.append(str(l1[i]))
    return int("".join(l2))

'''
Rotate the array A by k steps
:param A: an array of integers
:param K: number of times to shift right
:return: the rotated array
'''
def rotate(a, k=1):
    b = a.copy()
    for i in range(0,len(a)):
        if i==len(a)-1:
            b[0] = a[i]
            break 
        b[i+1] = a[i]
    if k>1:
        k-=1
        a = b.copy()
        return rotate(a,k)
    return b

'''
Find the value that does not have a match in an odd sized array
:param A: an array of integers with an odd number of elements
:param N: length of the array
:return: the one element which does not have a complementary element
''' 
def unmatched(a):
    import random
    n = len(a)
    if n%2 != 0:
        return a[random.randint(0,n-1)] 
    else: 
        return -1 
unmatched([1,2,3,4,5])

'''
Calculate the miminum number of jumps from X to Y
:param X: start integer
:param Y: minimum end integer
:param D: size of the jump
:return: minium number of jumps in O(1) time and space complexity
'''

'''
Problem: Given a string of alphabetical characters following the rules 
seen down below in part A and part B 
return a new string with the characters in the alphabetical order. 
Capital letters should appear before the same lowercase letter(s) in part B (Ex. aBbbCcdEe...). 
There will be no spaces in any of the strings.

Part A.) The string contains only lowercase letters
Part B.) The string contains both lowercase and uppercase letters

Sample Input/Output:

A.) Input: “hello”   Output: “ehllo”

B.) Input: “eLEPhAnt”   Output: “AEehLnPt”

'''

'''
Introduction: A magic square is a 2D matrix composed of n^2 integers 
where n is the length of one row/column. 
In a magic square each row, 
each column and the two diagonals must sum to the same value (see example below). 

Problem: Given a 2D matrix in the same form as shown and mentioned above your program must determine 
if the square is magic or not magic. It will output “magic” or “not magic” accordingly.

Input: Your program will first take an input n, representing the length of one row of the matrix. 
It will then take n lines of input containing n integers separated by spaces. 

Sample Input/Output:

1.)
Input: 
3
2 2 2
2 2 2
2 2 2
Output: “magic”

2.) 
Input:
4
16 2 3 13
5 11 10 8
9 7 6 12
4 14 15 1
Output: “magic”

3.)
Input:
4
12 3 4 5
5 67 8 9
102 3 4 6
34 2 89 0

Output: “not magic”
'''
def cubeSum(): 
    import numpy as np 
    l1 = []
    while 1:
        x = input()
        if not x:
            break
        e = [int(i) for i in x.split(" ")]
        l1.append(e)
    
    n = np.array(l1)
    l2 = [] 
    a, b = 0, 0
    for i in range(0,n.shape[0]):
        l2.append(n[i].sum())
    for i in range(0,n.shape[1]):
        l2.append(n[:,i].sum())
    for i in range(0,n.shape[0]):
        a += n[i,i]
    for i in range(0,n.shape[1]):
        for j in range(0,n.shape[0]):
            if i+j == n.shape[1]-1:
                b += n[i,j]
    l2.append(a)
    l2.append(b)
    if all(i==l2[0] for i in l2):
        return "magic" 
    else: 
        return "not magic"
cubeSum() 
