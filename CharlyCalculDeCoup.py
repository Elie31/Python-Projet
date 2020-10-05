from numpy import *
from random import *

class Application():


        
 distance = array([[0,700,200,900,900],
                   [700,0,500,200,300],
                   [200,500,0,900,800],
                   [900,200,900,0,300],
                   [900,300,800,300,0]])

 
 pointDepart = distance[0,0]
 
 
 chemin1 = ['T', 'P', 'M', 'L', 'S']
 

 #print (len(chemin1))
 #while i < len(chemin1):
     
 valeurChemin = distance[distance[0], distance[1]]
 print (valeurChemin)
     
     #i = i+1
     
 
 
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