#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Création de fonction mathématique simple en Python (12 points) :
#Dans cette partie, vous devrez implémenter en Python les fonctions ci-dessous :
# a) Implémenter la fonction polynomiale


# In[19]:


# on creer la fonction 
def fonc (x):
    Polynome = (x**3) - 1.5*(x**2)- (6*x) + 5
    print("Polynome (5) = ", Polynome  ) 
fonc(5)


# In[ ]:


# b)Implémenter la fonction factorielle (Approche récursive ou classique) :
#Soit n un entier naturel, on définit la fonction factorielle


# In[34]:


def Fact (n): 
    fact = 1
    for i in range(1, n+1):
      fact = fact * i
    print (n,'! = ',fact)

Fact(3)


# In[ ]:


#c) Implémenter la suite de Fibonnaci


# In[60]:


nbr = int(input("Inserer un nombre: "))
 
nbr1 = 0
nbr2 = 1
 
print("\n la suite fib est :")
print(nbr1, ",", nbr2, end=", ")
 
for i in range(2, nbr):
  neXt = nbr1 + nbr2
  print(neXt, end=", ")
 
  nbr1 = nbr2
  nbr2 = neXt


# In[67]:


# 2 ) #Création de fonction comportant des modules de gestions des exceptions 
#En utilisant l’une des trois fonctions mathématiques précédentes, 
#implémenter un script permettant de gérer les exceptions pours les cas suivants : 
#- Saisie d'une chaine de caractère dans les arguments de la fonction - Saisie un nombre complexe -
#Saisie d'un nombre négatif - Saisie d'un très grand nombre - Saisie d'un très petit nombre



# In[72]:


#le code de la question 1b "FACTORIELLE"
#variable qui permet a l'utilisateur de rentrer un nombre
try:   
    val = int(input("Entrez un nombre "))  

    # boucle qui check la variable val 
    # et grand nombre retoure une erreur sinon execute 
    if val < 0 or val >= 500 or type(val) != float: 
        print("introduire un nombre entre 0 et 500 ")
    else:
        if val == 0:
            x=1
        function = (val*3) - (1.5(val**2))- (6*val) + 5
        print(function)

except ValueError:
    print(" valeur incorrect ")


# In[ ]:


#3. Question Bonus : Implémentation de la formule Pricer d’option avec Python


# In[69]:


#on va avoir besoin des librairies suivantes
import numpy as np
import scipy.stats as si
import sympy as sy
import sympy.stats as systats


# In[70]:


def Pricer(S, X, T, r, sigma):    
    
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / X) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = (S * si.norm.cdf(d1) - X * np.exp(-r * T) * si.norm.cdf(d2))
    return call


# In[ ]:




