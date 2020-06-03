# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:43:14 2019

@author: Saurabh
"""


#Algorithm to get matches
import numpy as np
import pandas as pd


#Implementing the algorithm
def compute(list,couples,final_men,final_women):
    '''
    The function checks for couples in final array and returns it using the algorithm
    
    
    '''
    for m in list: #Ordered list of males
        temp = final_men.loc[m]
        for s in temp.index.values:
          if temp[s] in [val for sublist in couples for val in sublist]:
              t = (final_women.loc[temp[s]]).tolist()
              old_men = [x for i,x in enumerate(couples) if x[1] == temp[s]]
              old_men_index = [i for i,x in enumerate(t) if x == old_men[0][0]][0]
              new_men_index = [i for i,x in enumerate(t) if x == m][0]
              #Checks priority  
              if new_men_index < (old_men_index):
                   couples.remove((old_men[0]))
                   couples.append((m,temp[s]))
                   break
               
          else:
              couples.append((m,temp[s]))
              break
    return couples
     

def Gale_Shapley(final_men,final_women):
    
    '''
    For forming ordered pair of couples and calling the algorithm
    
    '''
    couples = []  #For finally forming couples
    #Initialized list with values
    list  = np.setdiff1d(final_men.index.values,[val[0] for val in couples])

    while True:
         couples = compute(list,couples,final_men,final_women)
         list  = np.setdiff1d(final_men.index.values,[val[0] for val in couples])
         if len(list) == 0:
             break
    return ("The couples formed are : %s"%str(couples))




# For user defined couples Run only if you want to manuall enter else enter manually
num = int(input("Enter total number of couples: "))


#Getting women and men name and their priority choice
men_list = []
for i in range(num):
    elem = str(input("Enter the %d men: "%(i + 1)))
    men_list.append( str(elem) )
    
women_list = []
for i in range(num):
    elem = str(input("Enter the %d women: "%(i + 1)))
    women_list.append( str(elem) )

men = []
for m in men_list:
    temp = []
    print("Enter the women choice in priority for %s"%m)
    for i in range(num):
        temp.append(str(input("Select the women from women_list: " )))
    print("Done for men: %s"%m)
    men.append(temp)

final_men = pd.DataFrame({men_list[i] : men[i] for i in range(len(men_list))})
final_men = pd.DataFrame(final_men).T
final_men.index = men_list
print(final_men)


women = []
for w in women_list:
    temp = []
    print("Enter the men choice in priority for %s"%w)
    for i in range(num):
        temp.append(str(input("Select the men from men_list: " )))
    print("Done for women: %s"%w)
    women.append(temp)

final_women = pd.DataFrame({women_list[i] : women[i] for i in range(len(women_list))})
final_women = pd.DataFrame(final_women).T
final_women.index = women_list
print(final_women)




# Call the algorithm by passing a dataframe of men and women it will return a list of couple formed
couples = Gale_Shapley(final_men,final_women)
print("The couples formed are : %s"%str(couples))

