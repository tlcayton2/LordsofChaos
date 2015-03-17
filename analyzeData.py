# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:14:26 2015

@author: Tiawna
"""
import numpy as np
import matplotlib.pyplot as plt
import time

filename = 'C:\Users\Tiawna\Documents\GitHub\LordsofChaos\\newFile'
effectOfSpread = np.genfromtxt(filename, delimiter = ' ')

#%%

maxCol = np.amax(effectOfSpread,axis = 0)
maxRow = np.amax(effectOfSpread,axis = 1)

plt.plot(maxCol)
plt.ylabel('Max Number of Students Infected')
plt.xlabel('Day')
plt.title('Most Students Infected Per Day')
plt.savefig('maxTime')
plt.show()

plt.plot(maxRow)
plt.ylabel('Students Infected')
plt.xlabel('Original Sick Student')
plt.title('Who Infects the Most Students?')
plt.savefig('maxStudent')
plt.show()

#%%

avgCol = np.average(effectOfSpread, axis = 0)
avgRow = np.average(effectOfSpread, axis = 1)

plt.plot(avgCol)
plt.ylabel('Number of Students Infected')
plt.xlabel('Day')
plt.title('Average Students Infected Per Day')
plt.savefig('avgTime')
plt.show()

plt.plot(avgRow)
plt.ylabel('Number of Students Infected')
plt.xlabel('Original Sick Student')
plt.title('Average Students Infected Over Quarter')
plt.savefig('avgStudent')
plt.show()



#%%

for t in range(355):
    temp = effectOfSpread[t,:]
    plt.plot(temp)
    plt.show()
    

    
