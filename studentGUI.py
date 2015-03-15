# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:33:33 2015

@author: Ayme
"""

import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import random as rd
import tkinter as tk

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

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #self.root = tk.Tk()
        #self.root.wm_title("What happens when you go to class sick")
        self.label1 = tk.Label (self, text= "Enter your perm number")
        self.label1.pack()
        self.entrytext1 = tk.StringVar()
        tk.Entry(self, textvariable=self.entrytext1).pack()

        self.label2 = tk.Label (self, text= "What day of the week is it?")
        self.label2.pack()
        self.entrytext2 = tk.StringVar()
        tk.Entry(self, textvariable=self.entrytext2).pack()
        
        self.button = tk.Button(self, text="Run Simulation", 
                                command=self.simulation)
        self.button.pack()

    def simulation(self):
        perm = self.entrytext1.get()
        day = self.entrytext2.get()
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("WHAT HAPPENS WHEN YOU GO TO CLASS SICK?")
        l1 = tk.Label(t, text="Student Perm: "+perm)
        l1.pack()
        l5 = tk.Label(t, text="Student Perm: "+day)
        l5.pack()
        l2 = tk.Label(t, text="Major: "+ "chemE")
        l2.pack()
        l3 = tk.Label(t, text="Number sick from first class attended: "+ "10")
        l3.pack()
        l4 = tk.Label(t, text="Total number sick in quarter: "+"45")
        l4.pack()

        G = nx.from_numpy_matrix(adjacency)
#        G.node[perm]['shape']='square'

#        nodeList = np.arange(10)
#        nodeShape = np.array(['o']*10)
#        nodeShape[perm] = '*'

        pos = nx.spring_layout(G)       
        nx.draw(G, pos, node_color=range(10), cmap = plt.get_cmap('YlOrBr'))
        #nx.draw(G, pos, nodelist=nodeList, node_shape=nodeShape, node_color=range(10), cmap = plt.get_cmap('YlOrBr'))          
        
        canvas = FigureCanvasTkAgg(plt.figure(1), master=t)

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()