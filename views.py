######################################################################
###  THIS FILE HANDLES THE FUNCTION REQUESTS ON THE DJANGO SERVER  ###
######################################################################
from django.shortcuts import render 
from django.http import HttpResponse
from django.template import RequestContext, loader
import os


def index(request):
    return render(request,"mfc/double.html")

def cached_alch(request):
    with open('/home/matt/src/recipes/alchemyapi-recipes-twitter/output.txt','r') as f:
        output = f.readlines()
    return render(request,"mfc/alchemy.html", {'a':output[26],'b':output[27],'c':output[28],'d':output[29],'e':output[30],'f':output[31],'g':output[32],'h':output[33],'i':output[34],'j':output[35],'k':output[36],'n':output[39],'o':output[40],'p':output[41],'q':output[42],'r':output[43],'s':output[44],'t':output[45],'u':output[46],'v':output[47],'w':output[48],'x':output[49],'y':output[50]})

def alchemy(request):
    os.system('python /home/matt/src/recipes/alchemyapi-recipes-twitter/Plot.py')
    with open('/home/matt/src/recipes/alchemyapi-recipes-twitter/output.txt','r') as f:
        output = f.readlines()
    return render(request,"mfc/alchemy.html", {'a':output[26],'b':output[27],'c':output[28],'d':output[29],'e':output[30],'f':output[31],'g':output[32],'h':output[33],'i':output[34],'j':output[35],'k':output[36],'n':output[39],'o':output[40],'p':output[41],'q':output[42],'r':output[43],'s':output[44],'t':output[45],'u':output[46],'v':output[47],'w':output[48],'x':output[49],'y':output[50]})

def cached_stack(request):
    g = open('/home/matt/src/Alchemy/alchemyapi_python/posscores.txt', 'r')
    lines0 = g.readlines()
    PosPages = len(lines0)
    h = open('/home/matt/src/Alchemy/alchemyapi_python/negscores.txt', 'r')
    lines1 = h.readlines()
    NegPages = len(lines1)
    return render(request,"mfc/stack.html", {'PosPages':PosPages,'NegPages':NegPages})

def stack(request):
    os.system('python /home/matt/src/Alchemy/alchemyapi_python/search.py')
    os.system('python /home/matt/src/Alchemy/alchemyapi_python/stackplot.py')
    g = open('/home/matt/src/Alchemy/alchemyapi_python/posscores.txt', 'r')
    lines0 = g.readlines()
    PosPages = len(lines0)
    h = open('/home/matt/src/Alchemy/alchemyapi_python/negscores.txt', 'r')
    lines1 = h.readlines()
    NegPages = len(lines1)
    return render(request,"mfc/stack.html", {'PosPages':PosPages,'NegPages':NegPages})

