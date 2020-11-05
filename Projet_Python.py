from numpy import *
from random import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import turtle
from turtle import *



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
                    if enfant1[i] == j:
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
                   [0,68,40,90,94,82,15,24,15],
                   [68,0,77,22,49,16,79,58,51],
                   [40,77,0,99,80,93,25,65,55],
                   [90,22,99,0,52,14,99,80,86],
                   [94,49,80,52,0,52,88,94,91],
                   [82,16,93,14,52,0,93,72,79],
                   [15,79,25,99,88,93,0,39,30],
                   [24,58,65,80,94,72,39,0,14],
                   [15,51,55,86,91,79,30,14,0]])
    b = 0
    i = 0
    j = 0
    valeurChemin = 0
    
    while j < len(matrice):
        while i != 9:
                if matrice[j] == chemin[i]:
                    valeurChemin += distance[j,b]
                    b = j
                    i += 1
        
                j += 1
                if j == 9:
                    j = 0
                    
        if i == 9:
            break
      
        
    return valeurChemin
    



def selectionChemin(tousLesChemins) :
    
    i = 0
    valeurChemins = [1,2,3,4]
    
    while i < 4 :
        valeurChemins[i] = calculDeCoût(tousLesChemins[i])
        i += 1
    valeurChemins.sort()
    print(valeurChemins)
    del valeurChemins[2:]
    
    nouveauParents = []

    for j in tousLesChemins :
        if ((calculDeCoût(j) == valeurChemins[0] or calculDeCoût(j) == valeurChemins[1]) and len(nouveauParents) < 2):
            nouveauParents.append(j)
            
            
            
    if(nouveauParents[0] == nouveauParents[1]):
        nouveauParents[1] = tousLesChemins[3]
                
    return nouveauParents

def pointChemin(point):
    t = 0
    

    
#liste a = avec les 2 premier
#for i in a: si plus petit alors tu remplace avec celui que compare i


#Main
ville = ['P', 'M', 'L', 'S', 'A', 'N', 'B', 'V']
cheminC = ['T', 'N', 'M', 'V', 'B', 'P', 'A', 'L', 'S']
chemin1 = initialisation(ville)
chemin2 = initialisation(ville)
print(chemin1)
print(chemin2)
  



i = 0
while i < 20:
    
    #Croissement
    if(random() < 0.5):
        Enfant1 = chemin1[:3] + chemin2[3:5] + chemin1[5:]
        Enfant2 = chemin2[:3] + chemin1[3:5] + chemin2[5:]
    else:
        Enfant1 = chemin2[:3] + chemin1[3:5] + chemin2[5:] 
        Enfant2 = chemin1[:3] + chemin2[3:5] + chemin1[5:]
        
    enfant1 = GeneCommun(Enfant1, Enfant2)
    enfant2 = GeneCommun(Enfant2, Enfant1)
    
    if (i == 100 or i == 1000 or i == 2000 or i == 5000 or i == 10000 or i == 10500):
      print("JE SUIS LA AAAA")
      enfant1 = initialisation(ville)
      enfant2 = initialisation(ville)
    
    print(enfant1)
    print(enfant2)

 
    mutation1 = Mutation(enfant1)
    mutation2 = Mutation(enfant2)
    
    cout = calculDeCoût(chemin1)
    cout2 = calculDeCoût(chemin2)

    print(cout)
    print(cout2)
    tousLesChemins = [chemin1, chemin2, mutation1, mutation2]
    
    select = selectionChemin(tousLesChemins)
    print(select)
  
    
   
    
    chemin1 = select[0]
    chemin2 = select[1]
    i +=1
    
    
    
    
    

#turtle.setup(500, 500)
#up()
#goto(-100,-100)
#down()
#for k in range(5):
  #  forward(200)
   # left(72)
    
#up()
#goto(-10,-30)
#down()
#turtle.write("T")


#for k in select[0]:
 #   pointChemin(k)
  #  goto(i + 5,i + 5)
   # turtle.write(k)

#exitonclick()
    
# (calculDeCoût(chemin1) > 250 and calculDeCoût(chemin1) > 249)


# le meilleur chemins fait 249
# t n m v b p a l s

