from numpy import *
from random import *

class Application():


        
 distance = array([[0,700,200,900,900],
                   [700,0,500,200,300],
                   [200,500,0,900,800],
                   [900,200,900,0,300],
                   [900,300,800,300,0]])

 
 pointDepart = distance[0,0]
 


chemin1 = ['T', 'P', 'M', 'L', 'S','T']
chemin2 = ['T', 'M', 'S', 'L', 'P','T']
 
#Croissement
Enfant = chemin1[:2] + chemin2[2:4] + chemin1[-2:]
Enfant2 = chemin2[:2] + chemin1[2:4] + chemin2[-2:]

for v in Enfant:
        
        print(v)
        
print(Enfant)
print(Enfant2)






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