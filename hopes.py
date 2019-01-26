# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:01:57 2019

@author: mypc
"""
'''
実行結果:
xは10です。
yは20です。
x+yの結果は30です。
x*yの結果は200です。
x+y割る2は15です。
'''


'''
実行結果:
xは12.5です。
yは20.5です。
x+yの結果は33です。
x*yの結果は256.25です。
x+y割る2は16.5です。
'''


'''
問題3
実行結果:
整数値7(←ここはキーボードから入力)
10を加えた値は17です。
10を減じた値は-3です。
'''
def ten():
    a = int(input("整数値:"))
    print("10を加えた値は"+str(a+10)+"です。")
    print("10を減じた値は"+str(a-10)+"です。")
ten()

'''
問題4
実行結果:
整数値:1275
最下位桁を除いた値は127です。
最下位桁は5です。
'''
def last():
    a = str(input("整数値:"))
    print("最下位桁を除いた値は"+a[0:-1]+"です。")
    print("最下位桁は"+a[-1]+"です。")
last()

'''
問題５
実行結果:
三角形の面積を求めます。
底辺:6.5←ここは入力
鷹さ:3.5←ここは入力
面積は11.375です
'''
def triangle():
    a = float(input("底辺:"))
    b = float(input("鷹さ:"))
    print("面積は"+str(a*b/2)+"です")
triangle()

'''
問題6
実行結果その1:
整数値:62
その値の絶対値は62です。

実行結果その2:
整数値-62
その値の絶対値は62です。
'''
def absolute():
    a = int(input("整数値:"))
    print("その値の絶対値は"+str(abs(a))+"です。")
absolute()

'''
問題7
実行結果その1:
変数A:12
変数B:4
BはAの約数です。

実行結果その2:
変数A:12
変数B:5
BはAの約数ではありません。
'''
def factor():
    a = int(input("変数A:"))
    b = int(input("変数B:"))
    if a%b == 0:
        print("BはAの約数です")
    else:
        print("BはAの約数ではありません。")
factor()

'''
問題8
実行結果その1:
整数値:37
その値は正です。

実行結果その2:
整数値:0
その値は0です。

実行結果その3:
整数値:-35
その値は負です。
'''
def check():
    a = int(input("整数値:"))
    if a>0:
        print("その値は正です。")
    elif a==0:
        print("その値は0です。")
    else:
        print("その値は負です。")
check()

'''
問題9
実行結果その1:
変数a　:12
変数b　:3
aのほうが大きいです。

実行結果その2:
変数a　:4.8
変数b　:12.1
bのほうが大きいです。
'''
def compare():
    a = float(input("変数a　:"))
    b = float(input("変数b　:"))
    if a>b:
        print("aのほうが大きいです。")
    elif b>a:
        print("bのほうが大きいです。")
compare()

'''
問題10
実行結果その1:
整数値:1251
その値は3で割り切れます。

実行結果その2:
整数値:1253
その値は3で割った余りは2です。
'''
def divideby3():
    a = int(input("整数値:"))
    if a%3==0:
        print("その値は3で割り切れます。")
    else:
        print("その値は3で割った余りは"+str(a%3)+"です。")
divideby3()

'''
問題11
キーボードから読み込んだ点数に応じて、優/良/可/不可を判定して表示するプログラムを
作成せよ。判定は以下のように行うこと。

0~59→不可/60~69→可/70~79→良/80~100→優
(それ以外は不正な値としてエラーをだすこと)
'''
def score():
    a = int(input("点数:"))
    if a>=0 and a<60:
        print("不可")
    elif a>=60 and a<70:
        print("可")
    elif a>=70 and a<80:
        print("良")
    elif a>=80 and a<=100:
        print("優")
    else:
        print("エラー")
score()

'''
問題12
実行結果:
整数a:3
整数b:1
整数c:2
最小値は1です。
'''
def mini():
    a=int(input("整数a:"))
    b=int(input("整数b:"))
    c=int(input("整数c:"))
    lst = [a,b,c]
    print("最小値は"+str(min(lst))+"です。")
mini()

'''
問題13
実行結果:
整数a:152
整数b:324
整数c:75
中央値は152です。
'''
def med():
    a=int(input("整数a:"))
    b=int(input("整数b:"))
    c=int(input("整数c:"))
    lst = [a,b,c]
    print("中央値は"+str(min(lst))+"です。")
med()

'''
問題14
3桁の正の整数値を読み込むプログラムを作成せよ。3桁の正の整数値でない値が入力された場合は、再入力させること。
実行例:
3桁の正の整数値:59
3桁の正の整数値:10000
3桁の正の整数値:592
入力された値は592です。
'''
def third():
    a = input("3桁の正の整数値:")
    if len(a) == 3:
        print("入力された値は"+a+"です。")
    else:
        third()
third()

'''
問題15
二つの整数値を読み込んで、小さいほうの数以上で大きい方の数以下の全整数を小さい順に表示するプログラムを作成せよ。
実行例:
整数A:33
整数B:28
28　29　30　31　32　33
'''
def order():
    a = int(input("整数A:"))
    b = int(input("整数B:"))
    if a>b:
        y,x = a,b
    else:
        x,y = a,b
    lst = []
    for i in range(x,y+1):
        lst.append(i)
    for i in lst:
        print(i, end=" ")
order()

'''
問題16
正の整数値を読み込んで、その桁数を出力するプログラムを作成せよ
実行例:
正の整数値の桁数を求めます。
正の整数値:1234←ここはキーボードから入力
その値は4桁です。
'''
def digit():
    a=str(input("正の整数値:"))
    lst=[]
    for i,j in enumerate(a):
        lst.append((i,j))
    print(lst[-1][0]+1)
digit()

'''
問題17
正の整数値nを読み込んで１からnまでの積を求めるプログラム
'''
def fact(n):
    if n == 1 or n <= 0:
        return 1
    else:
        return n * fact(n-1)

'''
問題18
記号文字(*)をキーボードから読み込んだ数だけ表示するプログラム
実行例
何個*を表示させますか?:8
********
'''
def star1():
    a = int(input("何個*を表示させますか?:"))
    return '*'*a
star1()

'''
問題19
記号文字(*)をキーボードから読み込んだ数だけ表示するプログラム
ただし、5つずつで改行すること
実行例
何個*を表示させますか?:8
*****
***
'''
def star2():
    a = int(input("何個*を表示させますか?:"))
    for i in range(0,a):
        print('*',end='')
        if (i+1)%5==0:
            print('\n',end='')
star2()

'''
問題20
1からnまでの整数値の2乗値を表示するプログラムを作成せよ。
実行例
nの値:3←キーボードから
1の2乗は1
2の2乗は4
3の2乗は9
'''
def square():
    a = int(input("nの値:"))
    for i in range(1,a+1):
        print(str(i)+"の2乗は"+str(i**2))
square()

'''
問題21
記号文字*を並べてn段の正方形を表示するプログラムを作成せよ。
実行例:
正方形を表示します。
段数:3←キーボードから入力
***
***
***
'''
def quad():
    a = int(input("段数:"))
    for j in range(0,a):
        for i in range(1,a+1):
            print('*',end='')
        print('\n',end='')
quad()

'''
問題22
実行例
左下直角三角形を表示します。
段数は:5←キーボードから
*
**
***
****
*****
'''
def triangle():
    a = int(input("段数は:"))
    for j in range(1,a+1):
        for i in range(1,j+1):
            print('*',end='')
        print('\n',end='')
triangle()

def tri3():
    a = int(input("段数は:"))
    for j in range(1,a+1):
        for i in range(1,a+1):
            if i+j>=1+a:
                print('*',end='')
            else:
                print(' ',end='')
        print('\n',end='')
tri3()

'''
問題23
左上直角の二等辺三角形を表示します。
段数は:5
*****
****
***
**
*
'''
def tri2():
    a = int(input("段数は:"))
    for j in range(a,0,-1):
        for i in range(1,j+1):
            print('*',end='')
        print('\n',end='')
tri2()

def tri4():
    a = int(input("段数は:"))
    for j in range(1,a+1):
        for i in range(1,a+1):
            if i<j:
                print(' ',end='')
            else:
                print('*',end='')
        print('\n',end='')
tri4()
