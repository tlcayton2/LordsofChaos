# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 12:30:09 2015

@author: Tiawna
"""
import numpy as np
import csv

pop = 355 #student population
slots = 22 #number of timeslots

#create adjacency array 
filename = 'C:\Users\Tiawna\Documents\GitHub\LordsofChaos\\timeSchedule.csv'
crn_adjacency = np.genfromtxt(filename, delimiter = ',')
print crn_adjacency # student x timeslot

# adjacency(i,j,k) = adjacency(st1,st2,ts)
adjacency = np.zeros([pop,pop,slots])

for k in range(slots):
    for j in range(pop):
        for i in range(pop):
            if (int(crn_adjacency[i,k]) != 0 and crn_adjacency[i,k] == crn_adjacency[j,k]):
                adjacency[i,j,k] = 1
