from numpy import *
from random import *

class Application():


        
 distance = array([[0,700,200,900,900],
                   [700,0,500,200,300],
                   [200,500,0,900,800],
                   [900,200,900,0,300],
                   [900,300,800,300,0]])


 chemin1 = ['T', 'P', 'M', 'L', 'S']
 
 a = 0
 i = 0
 valeurChemin = 0
 while i < len(chemin1):
  tmp = None
  x = randint(1,4)
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