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
chemin2 = ['T', 'S', 'L', 'M', 'P']
 
#Croissement
#Enfant = chemin2[:2] + chemin1[1:4]
Enfant=[]
for v in Enfant:
    if (randint(1, 4) < 2):
        
        child1=chemin1[:a]+chemin2[a:]
        Enfant.append(child1)
        child2=chemin2[:a]+chemin1[a:]
        Enfant.append(child2)
        print(Enfant)




print(Enfant)





#Mutation
if(random() < 0.5):
    r = randint(1, 4)
    index = randint(1,4)
    print(r)
    print(index)
    for i in Enfant:
        if(r != index):
            tmp = None
            tmp = Enfant[index]  
            Enfant[index] = Enfant[r]   
            Enfant[r] = tmp   
            print (Enfant)