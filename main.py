# -*- coding: utf-8 -*-
"""
Created on Mon Mar 09 16:06:19 2015

@author: Tiawna, and some other losers
"""
# ----------------------------- Import packages -----------------------------
import csv                  # to read timeSchedule.csv & make adjacency matrix
import numpy as np          # maths
import random as rd         # randoms
import math                 # more maths
from operator import add    # array manipulation

# ----------------------------- SIS Model Globals ---------------------------
beta = .5                           # Infection rate
kappa = .35                         # Mixing parameter
start = 0
stop = 10*11*7

# ----------------------------- Create Network -----------------------------
pop = 355 #student population
slots = 44 #number of timeslots

#create adjacency array 
#filename = 'C:\Users\Tiawna\Documents\GitHub\LordsofChaos\\timeSchedule.csv'
filename = 'timeSchedule.csv'
crn_adjacency = np.genfromtxt(filename, delimiter = ',')
#print crn_adjacency # student x timeslot

# adjacency(i,j,k) = adjacency(st1,st2,ts)
adjacency = np.zeros([pop,pop,slots+33])

for k in range(slots):
    for j in range(pop):
        for i in range(pop):
            if (int(crn_adjacency[i,k%22]) != 0 and crn_adjacency[i,k%22] == crn_adjacency[j,k%22]):
                adjacency[i,j,k] = 1

schedFile = 'schedules.csv'
sched = csv.reader(open(schedFile,'r'))
StuSchedDict = {}
for row in sched:
    StuSchedDict[row[0]] = row[1]

# ----------------------------------------------------------------------------
# |                           Function Definitions                           |
# ----------------------------------------------------------------------------
# (1.) SIS Model Funtion
# ----------------------------------------------------------------------------
def sis_model(current_adjacency, infected, beta, kappa):
    sick_student = np.zeros(355)   
    for i, student in enumerate(infected):     # Iterate through status vector:
        if student > 0:                        # if student is sick, increment
            sick_student[i] += 1               # sick timeslot counter.
    for i, student in enumerate(infected):  
        if student > 0:
            index = np.where(current_adjacency[:,i] == 1)[0] # for each sick student
                                                             # count students they share
                                                             # class with
            index = index.astype(int)          # cast index as vector of ints
            l = len(index)                     # sum I-S "contacts", call it l
            new = int(math.ceil(l*kappa))      # l*kappa = # of S exposed
            contact = rd.sample(index,new)     # draw exposed from S+I in class
            for item in contact:               # Spread infection
                x = rd.random()                # Roll the dice
                if x < beta and infected[item] == 0:  # If not infected and x < beta
                    sick_student[item] = 1     # infect
    temp_infected = map(add, infected, sick_student) # update the list of infected
                                                     # students after timestep elapses
    return temp_infected                             # and return.
# ----------------------------------------------------------------------------
# (2.) Recovery Function
# ----------------------------------------------------------------------------
def healthy(id_infected):
    for i,student in enumerate(id_infected):
        if student > 44:                       # if sick for 4 days,
            id_infected[i] = 0                 # return to susceptible state
    return id_infected                         # return infected vector
# ----------------------------------------------------------------------------
# (3.) Disease Spread Function
# ----------------------------------------------------------------------------
def disease_spread(start, stop, adjacency, id_infected):   # fcn to create array 
                                                           # of status vectors
    infection_array = np.zeros([pop,(stop - start + 2)])   
    infection_array[:,0] = id_infected
    j = 1
    for time in range(start, stop+1):
        current_adjacency = adjacency[:,:,time]
        current_id = np.zeros([pop,1])
        infected = infection_array[:,j-1]
        current_id = sis_model(current_adjacency, infected, beta, kappa )
        infection_array[:,j] = healthy(current_id)
        if (infection_array[:,j]!=0).sum(0) > 0:
            j += 1
        else:
            break
    return infection_array
# ----------------------------------------------------------------------------
# (4.) Sick Count
# ----------------------------------------------------------------------------
def sickCount(infection_array):                # function to return the # of 
    timeslot_sum = (infection_array!=0).sum(0)        # infected individuals at the
    sickperday = np.zeros(77)                         # end of each day. 
    i = 0    
    for x in range(stop - start):
        if (x%11) == 10:
            sickperday[i] = timeslot_sum[x]
            i += 1
    return sickperday

# ----------------------------- run tempSis -----------------------------

def AnalySIS(adjacency, nSimulations):
    effectOfSpread = np.zeros([355, 77])
    for patient0 in range(355):
        tempEffectOfSpread = np.zeros(77)
        for run in range(nSimulations):
            id_infected = np.zeros(355)
            id_infected[patient0] = 1       
            infection_array = disease_spread(start, stop, adjacency, id_infected)
            tempEffectOfSpread += sickCount(infection_array)
        effectOfSpread[patient0,:] = tempEffectOfSpread
    return effectOfSpread

nWeeks = 10
nSlots = 11*7*nWeeks
nSimulations = 1

x = AnalySIS(adjacency, nSimulations)
print x

