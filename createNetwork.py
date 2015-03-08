# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 12:30:09 2015

@author: Tiawna, and some other losers
"""
import numpy as np
import csv

pop = 355 #student population
slots = 22 #number of timeslots

#create adjacency array 
filename = 'C:\Users\Tiawna\Documents\GitHub\LordsofChaos\\timeSchedule.csv'
crn_adjacency = np.genfromtxt(filename, delimiter = ',')
#print crn_adjacency # student x timeslot

# adjacency(i,j,k) = adjacency(st1,st2,ts)
adjacency = np.zeros([pop,pop,slots])

for k in range(slots):
    for j in range(pop):
        for i in range(pop):
            if (int(crn_adjacency[i,k]) != 0 and crn_adjacency[i,k] == crn_adjacency[j,k]):
                adjacency[i,j,k] = 1

beta = 1.3  #infection rate
gamma = 1.    #recovery rate
patient = 1 #first infected student
id_infected = np.zeros([pop,1]) #x in SIS model function
id_infected[patient] = 1
time = 0

#chi(t) = beta(I-diag(x))Ax-gamma*x
#I = identity
#x = id_infected
def sis_model(adjacency, beta, gamma, time, id_infected):
    identity = np.eye(pop)
    diag_x = np.diag(id_infected)
    current_adjacency = np.matrix(adjacency[:,:,time])
    chi = beta*(identity - diag_x)*current_adjacency*id_infected - gamma*id_infected
    return chi
    
snapshot = sis_model(adjacency, beta, gamma, time, id_infected)


