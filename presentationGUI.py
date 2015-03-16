# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:33:33 2015

@author: Ayme
"""

import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random as rd
import tkinter as Tk
import networkx as nx
#from tkMessageBox import showinfo

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


root = Tk.Tk()
root.wm_title("Animated Graph embedded in TK")
root.wm_protocol('WM_DELETE_WINDOW', root.quit())

f = plt.figure(figsize=(5,4))
a = f.add_subplot(111)
plt.axis('off')

# Show the data
l1 = Tk.Label(root, text="Student Perm: "+'3')
l1.pack()
l5 = Tk.Label(root, text="Student Perm: "+'monday')
l5.pack()
l2 = Tk.Label(root, text="Major: "+ "chemE")
l2.pack()
l3 = Tk.Label(root, text="Number sick from first class attended: "+ "10")
l3.pack()


# initial network
G = nx.from_numpy_matrix(adjacency)
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=snapshot, cmap = plt.get_cmap('YlOrBr'))
xlim=a.get_xlim()
ylim=a.get_ylim()

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def next_graph():
    a.cla()
    adjacency[2,0]=0
    adjacency[0,2]=0
    G = nx.from_numpy_matrix(adjacency)
    snapshot = [ rd.randint(0,4) for i in range(10)]
    nx.draw(G, pos, node_color=snapshot, cmap = plt.get_cmap('YlOrBr'), ax=a)
    a.set_xlim(xlim)
    a.set_ylim(ylim)
    plt.axis('off')
    canvas.draw()
        

b = Tk.Button(root, text="next",command=next_graph)
b.pack()

Tk.mainloop()