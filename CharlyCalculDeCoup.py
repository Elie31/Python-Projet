from numpy import *
from random import *


def calculDeCoût(ville) :
    matrice = ['T','P','M','L','S','A','N','B','V']              
    distance = array([
                   [0,70,20,90,90,40,25,45,60],
                   [70,0,50,20,30,30,10,50,20],
                   [20,50,0,90,80,20,10,60,30],
                   [90,20,90,0,30,30,70,25,50],
                   [90,30,80,30,0,50,60,10,30],
                   [40,30,20,50,30,0,15,30,20],
                   [25,10,10,70,60,15,0,15,30],
                   [45,50,60,25,10,30,15,0,10],
                   [60,20,30,50,30,20,30,10,0]])
 

    b = 0
    i = 0
    j = 0
    x = 0
    valeurChemin = 0
    while x < len(ville):
        while i < len(ville):
             if matrice[j] == ville[i]:
                 valeurChemin += distance[j,b]
                 tmp = j
                 b = tmp
                 i += 1
             j += 1
        j = 0
        x += 1
    return valeurChemin

ville = ['P', 'M', 'L', 'S', 'A', 'N', 'B', 'V']
valeurChemin = calculDeCoût(ville)
print (valeurChemin)