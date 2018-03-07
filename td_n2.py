import numpy as np
import matplotlib.pyplot as plt



#etat -> y
def f(t, etat):
    a= 4
    b= 3
    c= 3
    d= 2
    return np.array([a*etat[0]-b*etat[0]*etat[1],
                     -c*etat[1] + d*etat[0]*etat[1]])


etat = np.array([2, 0.25])             #condition initiale
solution_E=[etat]  
solution_RK=[etat]                   #limite pour stocker les résulatats
h= 0.01                           #pas dintegration stable si h*a apartient a [0, 2]
tmax= 20
T = np.arange(0, tmax, h)

##EULER##
#for t in T[1:]:                     #care T0 deja traité ligne 2
#    etat = etat + h*f(t, etat)      #euler
#    solution_E.append(etat)           #on sauvegarde le resultat
#solution_E = np.array(solution_E)       #conversion en array numpy

###RUNGE KUTTA 2##
#lambda1 = 2/3
#c2 = 1/(2*lambda1)
#c1 = 1 - c2
#
#
#for t in T[1:]:                     #care T0 deja traité ligne 2
#    f1 = f(t, etat)
#    f2 = f(t+lambda1*h, etat+lambda1*h*f1)
#    etat = etat + h*(c1*f1+c2*f2)   #runge kutta range 2
#    solution_RK.append(etat)           #on sauvegarde le resultat
#solution_RK = np.array(solution_RK)       #conversion en array numpy




##RUNGE KUTTA 3##
lambda1 = 2/3
c2 = 1/(2*lambda1)
c1 = 1 - c2

for t in T[1:]:                     #care T0 deja traité ligne 2
    f1 = f(t, etat)
    f2 = f(t+(h/3), etat+(h/3)*f1)
    f3 = f(t+((2*h)/3), etat+((2*h)/3)*f2)
    
    etat = etat + (h/4)*(f1+3*f2)   #runge kutta range 2
    solution_RK.append(etat)           #on sauvegarde le resultat
solution_RK = np.array(solution_RK)       #conversion en array numpy


plt.plot(T, solution_RK)               #affichage

#plt.plot(solution_RK[:,0],solution_RK[:,1])
#plt.plot(solution_E[:,0],solution_E[:,1])


##ERREUR
#erreur = np.abs((solution.flatten()) - (np.exp(-T))) 
#plt.plot(T, erreur)

plt.grid()
plt.show()