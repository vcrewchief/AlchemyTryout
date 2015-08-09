####################################################################
###  THIS FILE CREATES A HISTOGRAM OF THE STACKOVERFLOW RESULTS  ###
####################################################################
import matplotlib 
matplotlib.use('Agg') 
import matplotlib.pyplot as plt 
import os

f = open('negscores.txt', 'r')
negs = f.readlines()
g = open('posscores.txt', 'r')
poss = g.readlines()

NEGS = []
POSS = []
for line0 in negs:
    NEGS.append(float(line0[:-1]))
for line1 in poss:
    POSS.append(float(line1[:-1]))
plt.close('all')
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.hist(NEGS, color='blue',rwidth=.5,label='Negative')
ax.hist(POSS, color='red', rwidth=.5,label='Positive')
plt.xlim(-1,1)
plt.title('AlchemyAPI StackOverflow Sentiment')
ax.legend(loc='upper left', shadow=True, fancybox=True)
plt.savefig('/home/matt/django/africa/mfc/static/mfc/stack.png', dpi=100*2)
