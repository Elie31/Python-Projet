from numpy import *
from random import *

class Application():


                    
 distance = array([[0,700,200,900,900],
                   [700,0,500,200,300],
                   [200,500,0,900,800],
                   [900,200,900,0,300],
                   [900,300,800,300,0]])
 


ville = ['P', 'M', 'L', 'S', 'A', 'N', 'B', 'V']


def initialisation(ville):
    chemin = ['T']
    while len(chemin) < len(ville) + 1:
        random = randint(0,len(ville) - 1)
        if chemin.count(ville[random]) == 0:
            chemin.append(ville[random])
    return chemin
    
    






def GeneCommun(enfant1, enfant2):    
    ajouter = 2;
    i = 0 
    while i < len(enfant1) :
        if enfant1.count(enfant1[i]) > 1 :
            indice = enfant1.index(enfant1[i])
            if (indice == 3 or indice == 4) :
                save = False
                index = 0
                for j in enfant1:
                    if enfant1[i] == j :
                        if save == True :
                            enfant2.append(enfant1[index])
                            enfant1.pop(index)
                        save = True
                    index = index + 1
            else :
                index = 0
                delete = False
                for j in enfant1:
                    if enfant1[i] == j:
                        if delete == False :
                            enfant2.append(enfant1[index])
                            enfant1.pop(index)
                            delete = True
                    index = index + 1
        i = i+1
    return enfant1


           
           

#Mutation
def Mutation(enfant):
    if(random() < 0.5):
        r = randint(1, 4)
        index = randint(1,4)
        for i in enfant:
            if(r != index):
                   tmp = None
                   tmp = enfant[index]  
                   enfant[index] = enfant[r]   
                   enfant[r] = tmp   
                
    return enfant
            






#Main
chemin1 = initialisation(ville)
chemin2 = initialisation(ville)
print(chemin1)
print(chemin2)
#Croissement
Enfant1 = chemin1[:3] + chemin2[3:5] + chemin1[5:]
Enfant2 = chemin2[:3] + chemin1[3:5] + chemin2[5:]
print("")
print(Enfant1)
print(Enfant2)
enfant1 = GeneCommun(Enfant1, Enfant2)
enfant2 = GeneCommun(Enfant2, Enfant1)
print("")
print(enfant1)
print(enfant2)
mutation1 = Mutation(enfant1)
mutation2 = Mutation(enfant2)
print("")
print (mutation1)
print (mutation2)
