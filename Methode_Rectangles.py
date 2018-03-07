#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:40:50 2018

@author: talecbni
"""
import numpy as np
import matplotlib.pyplot as plt

######################################################

def f1(x):
    return x**3-x

def F1(x):
    return (x**4)/4 - (x**2)/2

def f2(x):
    return np.sin(x)

def F2(x):
    return np.cos(x)

def f3(x):
    return 2*x*np.exp(-x**2)

def F3(x):
    return -np.exp(-x**2)
    
def f4(x):
    return 4*x+2

def F4(x):
    return 2*x*(x+1)

#####################################################
    ###TEST numero 1###

#print ('f1(0) = ', f1(0))
#print ('f1(2) = ', f1(2))
#print ('f2(0) = ', f2(0))
#print ('f2(pi/2) = ', f2((np.pi)/2))
#print ('f3(0) = ', f3(0))
#print ('f3(1) = ', f3(1))
#print ('f4(10) = ', f4(10))
    
######################################################

def reclangleGauche(a,b,n,f):
    pas = (b-a)/n
    I = 0
    for i in range(len(n)):
        ai = a+i*pas
        I += f(ai)
    return I*pas


def reclangleDroit (a,b,n,f):
    s,x,h=0,a ,(b-a)/n
    for i in range(len(n)):
        x += h
        s += h*f(x)
    return s

def reclangleCentre (a,b,n,f):
    s,x,h=0,a ,(b-a)/n
    for i in range(len(n)):
        s +=h*f(x+h /2)
        x+=h
    return s

#print (reclangleGauche(0, 3, 100, f1))
#print (reclangleDroit(0, 3, 100, f1))
#print (reclangleCentre(0, 3, 100, f1))


a= 0 
b= 3
n= np.arange(1, 10000, 100)



fonctions = [f1,f2,f3,f4]
primitives = [F1,F2,F3,F4]


for i in range (len(fonctions)):
    approx = reclangleGauche(a, b, n, fonctions[i])
    exacte = primitives[i](b)-primitives[i](a)

for i in range (len(fonctions)):
    approx2 = reclangleDroit(a, b, n, fonctions[i])
    exacte2 = primitives[i](b)-primitives[i](a)
    
#print (approx)
#print (exacte)

erreur = abs(approx - exacte)
erreur2 = abs(approx2 - exacte2)
#print (abs(erreur))

print (erreur)
print (erreur2)



plt.loglog(n, erreur)
plt.grid(True)
plt.title ('logarithme de lerreur commise en fonction du logarithme de n')
plt.show()



#X = np.arange(0, 20, 0.01)
#Y = f1(X)
#plt.plot(X, Y)
#plt.show()
