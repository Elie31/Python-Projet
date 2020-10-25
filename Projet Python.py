from numpy import *
from random import *



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




def calculDeCoût(chemin) :
    
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
    valeurChemin = 0

    while j < len(matrice) and i < len(chemin):  # ici c'est cassé
        if matrice[j] == chemin[i]:
             valeurChemin += distance[j,b]
             b = j
             i += 1
        j += 1
    
    return valeurChemin

def selectionChemin(tousLesChemins) :
    
    i = 0
    valeurChemins = [1,2,3,4]
    
    while i < 4 :
        valeurChemins[i] = calculDeCoût(tousLesChemins[i])
        i += 1
    valeurChemins.sort()
    
    nouveauParents = [1,2]
    i = 0
    j = 0
    while i < len(nouveauParents) :
        for j in range(0, len(tousLesChemins)) :
            if calculDeCoût(tousLesChemins[j]) == valeurChemins[j] :
                nouveauParents[i] = tousLesChemins[j]
                j= 0
                i+=1          
    print(nouveauParents)
    return nouveauParents


    
#liste a = avec les 2 premier
#for i in a: si plus petit alors tu remplace avec celui que compare i


#Main
ville = ['P', 'M', 'L', 'S', 'A', 'N', 'B', 'V']
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
print("")
tousLesChemins = [chemin1, chemin2, mutation1, mutation2]
selectionChemin(tousLesChemins)
Enfant1 = selectionChemin(nouveauParents[0])
Enfant2 = selectionChemin(nouveauParents[1])
