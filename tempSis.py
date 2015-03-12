# -*- coding: utf-8 -*-
"""
Created on Mon Mar 09 16:06:19 2015

@author: Tiawna
"""

import random as rd
import math
from operator import add

beta = .5
kappa = .35
patient = 1
id_infected = np.zeros(pop)
id_infected[patient] = 1

#current_adjacency = adjacency[:,:,time]



def sis_model(current_adjacency, infected, beta, kappa):
    sick_student = np.zeros(355)   
    
    for i, student in enumerate(infected):
        if student > 0:
            sick_student[i] += 1
    
    for i, student in enumerate(id_infected):
        
        if student > 0:

            index = np.where(current_adjacency[:,i] == 1)[0]
            index = index.astype(int)
            l = len(index)
            new = int(math.ceil(l*kappa))
            contact = rd.sample(index,new)
            for item in contact:
                x = rd.random()
                if x < beta and infected[item] == 0:
                    sick_student[item] = 1
                    
    temp_infected = map(add, infected, sick_student)
    return temp_infected
        
#snapshot = sis_model(current_adjacency, id_infected, beta, kappa)

def disease_spread(start, stop, adjacency, id_infected):
#    infection_array = np.zeros([pop, (stop - start+1)])    
    infection_array = np.zeros([pop,(stop - start + 2)])    
    infection_array[:,0] = id_infected
    j = 1
    for time in range(start, stop+1):
        current_adjacency = adjacency[:,:,time]
        current_id = np.zeros([pop,1])
        infected = infection_array[:,j-1]
        current_id = sis_model(current_adjacency, infected, beta, kappa )
#        infection_array = np.insert(infection_array, current_id,,1)
        infection_array[:,j] = healthy(current_id)
        j +=1  
    return infection_array
    
def healthy(id_infected):
    for i,student in enumerate(id_infected):
        if student > 44:
            id_infected[i] = 0
    return id_infected
    
snapshot = disease_spread(1,76, adjacency, id_infected)