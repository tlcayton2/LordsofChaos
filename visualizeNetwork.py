# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:39:26 2015

@author: Ayme
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random as rd


adjacency = np.zeros([10, 10])
adjacency[:, 0] = [ 0, 0, 1 ,1 ,0, 1, 1, 0, 1, 0 ]
adjacency[:, 1] = [ 0, 0, 0 ,1 ,1, 1, 0, 1, 0, 0 ]
adjacency[:, 2] = [ 1, 0, 0 ,0 ,0, 0, 1, 0, 1, 0 ]
adjacency[:, 3] = [ 1, 1, 0 ,0 ,0, 1, 1, 0, 1, 0 ]
adjacency[:, 4] = [ 0, 1, 0 ,0 ,0, 1, 0, 0, 1, 1 ]
adjacency[:, 5] = [ 1, 1 ,0 ,1 ,1, 0, 1, 1, 0, 1 ]
adjacency[:, 6] = [ 1, 0 ,1 ,1 ,0, 1, 0, 0, 0, 0 ]
adjacency[:, 7] = [ 0, 1 ,0 ,0 ,0, 1, 0, 0, 1, 1 ]
adjacency[:, 8] = [ 1, 0 ,1 ,1 ,1, 0, 0, 1, 0, 0 ]
adjacency[:, 9] = [ 0, 0 ,0 ,0 ,1, 1, 0, 1, 0, 0 ]


snapshot = [ rd.randint(0,4) for i in range(10)]

def showSpread(adjacency, snapshot):

    G = nx.from_numpy_matrix(adjacency)

    healthColor = {0: 0.6,
                   1: 1.0,
                   2: 1.0,
                   3: 1.0,
                   4: 1.0}

    hColors = [healthColor.get(student) for student in snapshot]

    nx.draw(G, node_color=hColors)

    plt.show()
    

showSpread(adjacency, snapshot)

