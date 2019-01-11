# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 02:18:45 2018

@author: mypc
"""

txt = '''
Ordo-liberalism is the theory behind the German social market economy. Its theoretical
stance developed in the context of the economic crisis and political turmoil of the Weimar
Republic in the late 1920s. It is premised on the strong state as the locus of liberal
governance, and holds that economic freedom derives from political authority. In the context
of the crisis of neoliberal political economy and austerity, and debates about the resurgence of
the state vis-à-vis the economy, the article introduces the ordoliberal argument that the free
economy presupposes the exercise of strong state authority, and that economic liberty is a
practice of liberal governance. This practice is fundamentally one of social policy to secure
the sociological and ethical preconditions of free markets. The study of ordo-liberalism brings
to the fore a tradition of a state-centric neo-liberalism, one that says that economic freedom is
ordered freedom, one that argues that the strong state is the political form of free markets, and
one that conceives of competition and enterprise as a political task. 
'''

txt = '''
日本において英文学とは一体どういうものだったのか。これから英文学はどうあるべきなのか。
こうした素朴だが決して放置すべきではない重要な疑問に真正面から取り組んだ先行研究はそ
れほど多くないが、近年になって、正木恒夫『植民地幻想』（1995 年）、宮崎芳三『太平洋戦争と英
文学者』（1999 年）、山口誠『英語講座の誕生』（2002 年）といった研究が現れてきた。これらの研
究は、〈脱亜入欧〉や〈近代の超克〉といったスローガンに象徴される、西欧を意識した日本の国
家的戦略の中において、英文学なるものがどのような機能を担っていたのかを批判的に分析したと
いう点において、高く評価できるだろう。ただし、残念ながら、これらの研究は、英文学の批判の
後にあってしかるべき、英文学の新たな可能性については本格的に議論してはいないのである。
本論文は、以上紹介した先行研究が扱わなかった事例を取り上げると同時に、〈脱亜入欧〉や〈近
代の超克〉というプロジェクトの中で構築された英文学が、こうしたプロジェクトを揺るがしかね
ないような要素を含み込んでいたことを明らかにすることで、英文学の豊かさ、その可能性を示す
ことを試みている。本論のタイトルが「英文学の構築」ではなく「英文学の脱構築」である所以で
ある。
'''

# c. LSTM 이용 
## 시간의 순서를 기반으로 데이터를 다룸 -> 과거(이전)의 데이터(어구)를 "기억" -> 머신러닝으로 해당 어구에 이어서 다음에 위치할 문장을 예측하여 생성
## ex. "오늘"이라고 입력 -> 이후에 "아침", "날씨" 등의 글자가 이어질 것이라고 예상하고 조합 

from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

text = txt.replace('\n',' ')

# 텍스트 데이터에서 문자를 하나하나 읽어 들이고, 각 문자에 인덱스를 ID로 부여
chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars)) ### (문자, 인덱스)
indices_char = dict((i, c) for i, c in enumerate(chars)) ### (인덱스, 문자)

# 텍스트를 maxlen개의 문자로 자르고(X) 다음에 오는 문자(y) 등록하기
## X(해당 어구)를 입력하면 y(어구에 이어서 올 어구)가 label로 나오게 만드는 것이 핵심!!
'''
예시)
X: 입력값 
y: 결과값

X              y
they	        are
they are    	 learning
they are      learning	data
they are      learning data	science
'''
maxlen = 20
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])

# 텍스트 데이터를 벡터(텐서)로 만듬 -> 그래야 딥러닝에 사용할 수 있음! 
## 참고) 텐서(tensor): 벡터와 매트릭스를 총칭하는 용어 
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

# 모델 구축하기(LSTM)
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax')) ### 활성화 함수 
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

# 후보(해당 어구 중 일부) 선정
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# 학습시키고 텍스트 생성하기 반복
for iteration in range(1, 20):
    print()
    print('-' * 50)
    print('반복 =', iteration)
    model.fit(X, y, batch_size=128, nb_epoch=1) # 
    ## 임의의 시작 텍스트 선택하기
    start_index = random.randint(0, len(text) - maxlen - 1)
    ## 다양한 다양성의 문장 생성
    for diversity in [1.2, 1.5, 2.0, 2.2]:
        print()
        print('--- Weight값 = ', diversity)
        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('--- 해당 어구 = "' + sentence + '"' +"\n")
        sys.stdout.write(generated)
        ## 시드를 기반으로 텍스트 자동 생성
        for i in range(200):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.
            ## 다음에 올 문자를 예측하기
            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]
            ## 출력하기
            generated += next_char
            sentence = sentence[1:] + next_char
            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()