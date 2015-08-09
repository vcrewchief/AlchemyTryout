#######################################################
###  THIS FILE CREATES AND GRAPHS THE TWITTER DATA  ###
#######################################################
import matplotlib 
matplotlib.use('Agg') 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
import datetime as dt
import os

###  UPDATE WITH FRESH DATA  ###
os.system('python /home/matt/src/recipes/alchemyapi-recipes-twitter/delete.py && python /home/matt/src/recipes/alchemyapi-recipes-twitter/recipe.py "alchemyapi" 1000 >> /home/matt/src/recipes/alchemyapi-recipes-twitter/output.txt && python /home/matt/src/recipes/alchemyapi-recipes-twitter/write.py')


###  OPEN FILES  ###
f = open('/home/matt/src/recipes/alchemyapi-recipes-twitter/scores.neg', 'r')
negs = f.readlines()
g = open('/home/matt/src/recipes/alchemyapi-recipes-twitter/scores.pos', 'r')
poss = g.readlines()
h = open('/home/matt/src/recipes/alchemyapi-recipes-twitter/times.neg', 'r')
negt = h.readlines()
i = open('/home/matt/src/recipes/alchemyapi-recipes-twitter/times.pos', 'r')
post = i.readlines()

###  FORMAT DATA FOR GRAPH  ###
NEGS = []
NEGT = []
POSS  = []
POST = []
for j in negs:
    NEGS.append(float(j[:7]))
for k in negt:
    NEGT.append(k[:19])
for l in poss:
    POSS.append(float(l[:6]))
for m in post:
    POST.append(m[:19])

### PLOT DATA  ###
plt.close('all')
xneg = [dt.datetime.strptime(d,'%Y-%m-%d %H:%M:%S') for d in NEGT]
xpos = [dt.datetime.strptime(e,'%Y-%m-%d %H:%M:%S') for e in POST]
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.scatter(xpos,POSS,color='red', s=10, label = 'Positive')
ax.scatter(xneg,NEGS,color='blue', s=10, label='Negative')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gca().xaxis.grid(True) 
plt.gcf().autofmt_xdate() 
minimum = []
minimum.append(min(xneg))
minimum.append(min(xpos))
xmin = min(minimum)
maximum = []
maximum.append(max(xneg))
maximum.append(max(xpos))
xmax = max(maximum)
plt.xlim(xmin,xmax)
plt.ylim(-.8,1)
plt.title('AlchemyAPI Twitter Sentiment')
ax.legend(loc='lower left', shadow=True, fancybox=True)
plt.savefig('/home/matt/django/africa/mfc/static/mfc/twit.png', dpi=100*2)


