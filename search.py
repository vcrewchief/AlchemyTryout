#########################################################################
###  THIS FILE SEARCHES STACKOVERFLOW AND CREATES USEABLE DATA FILES  ###
#########################################################################
import os
import stackexchange
import sys
import time
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

term = 'alchemyapi'
#..stackexchange key:
user_api_key = 'ZYP5cLfqKp)kuCfRSLPanw(( '
if not user_api_key: user_api_key = None
so = stackexchange.Site(stackexchange.StackOverflow, app_key=user_api_key, impose_throttling=True)
qs = so.search(tagged=term)
ids = []    
for q in qs:
    ids.append(q.id)
so.be_inclusive()
anslist = []
os.system('rm /home/matt/src/Alchemy/alchemyapi_python/text.txt')
os.system('rm /home/matt/src/Alchemy/alchemyapi_python/negscores.txt')
os.system('rm /home/matt/src/Alchemy/alchemyapi_python/posscores.txt')
f = open('/home/matt/src/Alchemy/alchemyapi_python/text.txt','a')
fneg = open('/home/matt/src/Alchemy/alchemyapi_python/negscores.txt', 'a')
fpos = open('/home/matt/src/Alchemy/alchemyapi_python/posscores.txt', 'a')

for id in ids:
    question = so.question(id)
    f.write(question.title+'\n')
    try:
        f.write(question.body+'\n\n')
    except UnicodeEncodeError:
        print 'Uni'
    for line in question.answers:
        anslist.append(line.id)
        for ans in anslist:
            answer = so.answer(ans)
            f.write(answer.body)
    f.close()
    f = open('/home/matt/src/Alchemy/alchemyapi_python/text.txt','r')
    html = f.read()
    response = alchemyapi.sentiment('html', html)
    try:
        if response["docSentiment"]["type"] == 'negative':
            fneg.write(response['docSentiment']['score']+'\n')
        if response["docSentiment"]["type"] == 'positive':
            fpos.write(response['docSentiment']['score']+'\n')
    except KeyError:
        print 'Error'
    f.close()
    os.system('rm /home/matt/src/Alchemy/alchemyapi_python/text.txt')
    f = open('/home/matt/src/Alchemy/alchemyapi_python/text.txt','a')
fneg.close()
fneg = open('/home/matt/src/Alchemy/alchemyapi_python/negscores.txt', 'r')
neglist = fneg.readlines()
mostneg = 0
for i in neglist:
    i = float(i[:-1])
mostneg = min(neglist)
for z,r in enumerate(neglist):
    if r == mostneg:
        fposneg.write(str(ids[z])+'\n')
        break
fpos.close()
fpos = open('/home/matt/src/Alchemy/alchemyapi_python/posscores.txt', 'r')
poslist = fpos.readlines()
mostpos = 0
for w in poslist:
    w = float(w[:-1])
mostpos = max(poslist)
for f,s in enumerate(poslist):
    if s == mostpos:
        fposneg.write(str(ids[f])+'\n')
        break
