# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:14:26 2015

@author: Tiawna
"""
import numpy as np
import matplotlib.pyplot as plt
import time

filename = 'C:\Users\Tiawna\Documents\GitHub\LordsofChaos\\effectOfSpread_nSim1000'
effectOfSpread = np.genfromtxt(filename, delimiter = ' ')
effectOfSpread= np.around(effectOfSpread/1000)

for t in range(355):
    temp = effectOfSpread[t,1:10]
    plt.plot(temp)
    plt.show()


G = nx.from_numpy_matrix(masterAdjacency)
draw_graphviz(G)
