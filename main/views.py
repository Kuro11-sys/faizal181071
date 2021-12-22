import contextlib

from django.shortcuts import render
from sympy import *


def home(request):
    return render(request, 'main/home.html')


def turunan(request):
    if request.method == 'POST':
        var1 = request.POST['var1']
        x = Symbol(var1)
        y = request.POST['pers']
        yprime = diff(y,x)

        context = {
            'yprime': yprime,
            'y': y,
            'var1' : var1
        }
        return render(request, 'main/turunan.html', context)
    else:
        return render(request, 'main/turunan.html')

def integral(request):
    if request.method == 'POST':
        var1 = request.POST['var1']
        x = Symbol(var1)
        y = request.POST['pers']
        yprime = integrate(y,x)

        context = {
            'yprime': yprime,
            'y': y,
            'var1' : var1
        }
        return render(request, 'main/integral.html', context)
    else:
        return render(request, 'main/integral.html')
