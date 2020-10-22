from numpy import *
from random import *

class Application():


def calculDeCoût(mutation1, mutaion2) :
    
 distance = array([[0,70,20,90,90,40,25,45,60],
                   [70,0,50,20,30,30,10,50,20],
                   [20,50,0,90,80,20,10,60,30],
                   [90,20,90,0,30,30,70,25,50],
                   [90,30,80,30,0,50,60,10,30],
                   [40,30,20,50,30,0,15,30,20],
                   [25,10,10,70,60,15,0,15,30],
                   [45,50,60,25,10,30,15,0,10],
                   [60,20,30,50,30,20,30,10,0]])
 a = 0
 i = 0
 valeurChemin = 0
 while i < len(chemin1):
  tmp = None
  x = mutation1[1]
  valeurChemin += distance[a,x]
  tmp = x
  a = tmp
  x = randint(1,4)
  i += 1
 print(valeurChemin) 
  



 #print (len(chemin1))
 #while i < len(chemin1):
     

# valeurChemin = distance[a, b]
# print (valeurChemin)

    
 
 #
 #Pour index de depart 
 # tant que toutes les villes n'ont pas été parcouru :
 #      index = [abscisse T, ordonné P]
 #      valeur chemin = index + index2 + index3 + index4
 #      index = [abscisse M, ordonné P]
 #      valeur chemin += index
 #
 #
 #
 #
 #