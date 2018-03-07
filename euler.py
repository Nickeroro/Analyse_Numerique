import numpy as np
import matplotlib.pyplot as plt



#etat -> y
def f(t, etat):
    a= 1
    return -a*etat


etat = np.array([1]) #condition initiale
solution=[etat] #limite pour stocker les résulatats
h= 0.1          #pas dintegration stable si h*a apartient a [0, 2]
tmax= 10
T = np.arange(0, tmax, h)


for t in T[1:]: #care T0 deja traité ligne 2
    etat = etat + h*f(t, etat) #euler
    solution.append(etat) #on sauvegarde le resultat
solution = np.array(solution) #conversion en array numpy




plt.plot(T, solution) #affichage

##ERREUR
erreur = np.abs((solution.flatten()) - (np.exp(-T))) 
plt.plot(T, erreur)

print (erreur)

plt.show()