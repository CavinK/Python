# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 00:54:02 2018

@author: Julia and Cavin 
"""

# Short-sentence summeriser with Markov Chain 

# pip install PyPDF2 
## PyPDF info: https://www.geeksforgeeks.org/working-with-pdf-files-in-python/

# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('C://data/ordo.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
type(pdfReader.numPages)

# creating a page object(for example)
pageObj = pdfReader.getPage(3)

# extracting text from page 
print(pageObj.extractText()) 

# data cleansing 
art = []
for i in range(0,pdfReader.numPages):
    pageObj = pdfReader.getPage(i) 
    txt = pageObj.extractText()
    txt = txt.split('\n')
    txt = ''.join(txt)
    txt = txt[0:txt.find(' Page')]
    art.append(txt)
len(art)
art[5]

# closing the pdf file object 
pdfFileObj.close() 


##############################################################################


# 1. English NLP 
## NLP info: https://www.nltk.org/
## Regex: https://docs.python.org/3.3/howto/regex.html
## Regex2: https://docs.python.org/2/library/re.html
'''
* LIST OF TAGS 
CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent’s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO, to go ‘to’ the store.
UH interjection, errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when
'''
import nltk

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
This article serves two purposes, to introduce “The Comparative Order
and its Implementation,” a seminal article published in 1949 by Walter
Eucken, ordoliberalism’s, or the “Freiburg School’s,” most prominent scholar,
and to compare some ordoliberalist competition policy recommendations
to those of a consumer welfare standard. The article provides an overview of
the key concepts of ordoliberalism (such as “competitive order,” “economic

constitution” and “Ordnungspolitik”) and outlines its implications for compe-
tition policy. It provides examples for the ordoliberal legacy in German and

European competition policy, such as, inter alia, the market share thresholds
for dominance, and the control of exploitative abuses such as excessive pricing.
Finally, the article gives a critique of ordoliberalism from a consumer welfare

perspective, and looks, among other things, at the implications of ordoliberal-
ist policies for innovation and dynamic competition, the roots of the structure-
conduct-performance paradigm, and the classification of certain forms of uni-
lateral behavior (e.g., tying).
'''

nltk.download('punkt') ### skip 
txt = ''.join(art) ### skip 
tokens = nltk.word_tokenize(txt)
tokens

nltk.download('averaged_perceptron_tagger')
tagged = nltk.pos_tag(tokens)
tagged
tokenized = nltk.word_tokenize(txt)
# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN' ### or pos[:2] == 'VB'
# do the nlp stuff
tokenized = nltk.word_tokenize(txt)
tokenized_nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
tokenized_nouns

## (skip)
nltk.download('maxent_ne_chunker')
nltk.download('words')
entities = nltk.chunk.ne_chunk(tagged)
entities

## (skip)
from nltk.corpus import treebank
nltk.download('treebank')
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()



# 빈도수 체크 
## nltk에 속한 메소드들 확인 
eng = nltk.Text(tokenized_nouns) ### 분석해야 할 토큰 분석 
eng.tokens ### 만들어진 토큰들 확인 
len(eng.tokens) ### 전체 토큰 수 
len(set(eng.tokens)) ### 중복 제거 후의 토큰 수 
eng.vocab() ### 빈도 수 체크 
eng.vocab().most_common(10) ### 상위 10개만 뽑아냄 

## 불용어 처리 
stopword = ['.',',',')','(',':',';','be','are','is','have','has','A','”','’','“','i','ii','iii','s']
eng = [eachword for eachword in eng if eachword not in stopword]

eng = nltk.Text(eng)
len(eng.tokens) ### 불용어 제거 작업 이후 단어의 수가 눈에 띄게 줄어들었음! 
len(set(eng.tokens))
eng.vocab()
eng.vocab().most_common(10)

eng.count('Freiburg') 

## Visualisation 
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family = font_name)
plt.figure(figsize = (12,6))
eng.plot(50)
plt.show()

## 상위 10개에 해당되는 단어들이 포함된 문장들 추출 
txt = ''.join(art)
txt = txt.split('.')
import numpy as np
topwords = list(np.array(eng.vocab().most_common(10))[:,0])
sent = []
for i in txt:
    for j in topwords:
        if j in i:
            sent.append(i)
sentences = set(sent)    

## 문장 별로 점수 매기기 
## https://dev.to/davidisrawi/build-a-quick-summarizer-with-python-and-nltk
board = {}
for i in sentences:
    board[i] = 0
    for j in topwords:
        if j in i:
            board[i] += 1
        else:
            board[i] += 0
board.values() 

## 점수를 기준으로 요약본 작성 

## Multiple Perceptron 

## Markov Chain 
### https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
token = tokenized
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
topwords = list(np.array(eng.vocab().most_common(10))[:,0])
topwords_cap = [i for i in topwords if i[0].isupper()]
first = np.random.choice(topwords_cap)
mark = [first]
number = 30

for i in range(number):
    mark.append(np.random.choice(chain_dict[mark[-1]]))
' '.join(mark) 

# Result 
'''
Ordo-liberalism is fundamentally one of the context of free markets . Its theoretical stance developed in the fore a state-centric neo-liberalism , and debates about the strong state as a tradition
'''

## Naive Bayes 
### https://github.com/rachitjain2706/Auto-Text-Summarizer
### 해당 문장이 summary인지 아닌지 파악하는 데에 사용! 


##############################################################################


# 2. Korean NLP 
# 1) Twitter()  
import konlpy
from konlpy.tag import Twitter 

twitter = Twitter() ### 함수 이름 대체 
malist = twitter.pos('아버지 가방에 들어가신다.', norm = True, stem = True) ### norm: "그래욬ㅋㅋㅋ" -> "그래요" 변환! // stem: "그렇다"라는 원형(동사원형)을 찾아줌! 
print(malist) ### 형태소 분석 결과 

txt = "텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집, 처리, 분석, 요약하는 연구기법을 통칭하는 용어이다." 
twitter.nouns(txt) ### 명사만 뽑아내는 작업 -> 완벽하진 않음! 
print(twitter.pos(txt, norm = True, stem = True))



# 2) Kkma() 
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



# 3) nltk 패키지 
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



## 4) 불용어 처리 
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



# 5) Wordcloud 
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

import collections 



## 6) Counter 컨테이너(자료형)에 동일한 값의 자료가 몇 개인 지를 파악한다. 
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



# 7) 사용자 사전 
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


##############################################################################


# 3. Japanese 

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
print(txt)
txt = txt.replace('\n','')
txt_split = txt.split('。')

## http://taku910.github.io/mecab/
## Binary package for MS-Windows
## 環境変数 -> PATH -> C:\Program Files (x86)\MeCab\bin
from MeCab import *
t = Tagger()
print(t.parse(txt))
type(t.parse(txt))

div = t.parse(txt).split('\n')
div[0].split('\t')[1]
lst = []
for i in div:
    if len(i.split('\t')) == 2:
        lst.append(i.split('\t'))

import numpy as np
lst_np = np.array(lst)
token = list(lst_np[:,0])

lst[0][1][0:lst[0][1].find(',')]

noun = [lst[i] for i in range(0,len(lst)) if lst[i][1][0:lst[i][1].find(',')] == '名詞'] ### 명사 추출 

## 불용어 처리 
import numpy as np
noun_np = np.array(noun)
nouns = list(noun_np[:,0])
stopword = ['.',',',')','(','の','もの','そ','年','的','よう','これら','者','中','さ','を','こと']
jp = [eachword for eachword in nouns if eachword not in stopword]

## 빈도 수 
np.unique(jp, return_counts=True) ### 각 단어들의 빈도 수
## Container 
from collections import *
Counter(jp) ### container 이용해서 빈도 수 파악 
ct = Counter(jp)
ct.most_common(10) ### 상위 10개 추출 

## 문장 추출 
topword = np.array(ct.most_common(10))
topword = topword[:,0]

txt_split = txt.split('。')
sent_jp = []
for i in txt_split:
    for j in topword:
        if j in i:
            sent_jp.append(i)
set(sent_jp)



## Markov Chain 
### https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
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
topwords = list(np.array(ct.most_common(10))[:,0])
first = np.random.choice(topwords)
mark = [first]
number = 80

for i in range(number):
    mark.append(np.random.choice(chain_dict[mark[-1]]))
''.join(mark) 

# Result 
'''
日本において英文学の新たな疑問に議論してしかるべきな可能性を批判の豊かされたの構築」であるべきな要素を意識した。こうしたプロジェクトを試み
'''



## NaiveBayes(10-18-2018)
topword = np.array(ct.most_common(10))
len(topword)

data = {}
for i in range(0,len(topword)):
    data[topword[i,0]] = topword[i,1]    



import MeCab as mc
mc.DictionaryInfo_swigregister()
