# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 00:54:02 2018

@author: Julia and Cavin 
"""

# Short-sentence summeriser with Markov Chain 

# 0. 텍스트 파일 로드 
with open('C://data/ordo.txt', 'r') as myfile:
    txt = myfile.read().replace('\n', '')

# 1. 영어
import nltk
tokenized = nltk.word_tokenize(txt)
is_noun = lambda pos: pos[:2] == 'NN' 
tokenized_nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
tokenized_nouns

# 빈도수 체크 
eng = nltk.Text(tokenized_nouns) ### 분석해야 할 토큰 분석 
eng.tokens ### 만들어진 토큰들 확인 
len(eng.tokens) ### 전체 토큰 수 
len(set(eng.tokens)) ### 중복 제거 후의 토큰 수 
eng.vocab() ### 빈도 수 체크 
eng.vocab().most_common(10) ### 상위 10개만 뽑아냄 

## 불용어 처리 
stopword = ['.',',',')','(',':',';','be','are','is','have','has','A','”','’','“','i','ii','iii','s','‘','…']
eng = [eachword for eachword in eng if eachword not in stopword]

eng = nltk.Text(eng)
len(eng.tokens) ### 불용어 제거 작업 이후 단어의 수가 눈에 띄게 줄어들었음! 
len(set(eng.tokens))
eng.vocab()
eng.vocab().most_common(10)

## Visualisation 
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family = font_name)
plt.figure(figsize = (12,6))
eng.plot(50)
plt.show()

## Markov Chain 
stopword = ['.',',',')','(',':',';','”','’','“','i','ii','iii','‘','…']
token = [eachword for eachword in tokenized if eachword not in stopword]
chain = []
for i in range(1,len(token)):
    chain.append((token[i-1], token[i]))

chain_dict = {}
for i, j in chain:
    if i in chain_dict.keys():
        chain_dict[i].append(j)
    else:
        chain_dict[i] = [j]

import numpy as np
topwords = list(np.array(eng.vocab().most_common(20))[:,0])
topwords_cap = [i for i in topwords if i[0].isupper()]
first = np.random.choice(topwords_cap)
mark = [first]
number = 30

## Summary
for i in range(number):
    mark.append(np.random.choice(chain_dict[mark[-1]]))
' '.join(mark) 
