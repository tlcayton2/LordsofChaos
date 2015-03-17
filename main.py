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

import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import Tkinter as tk

# ----------------------------- SIS Model Globals ---------------------------
beta = .05                           # Infection rate
kappa = .35                         # Mixing parameter
start = 0
stop = 10*11*7
# ============================================================================
# |                               Create Network                             |
# ============================================================================
pop = 355 #student population
slots = 44 #number of timeslots
try:
    adjacency
except NameError:
    #create adjacency array 
    filename = 'C:\Users\Tiawna\Documents\GitHub\LordsofChaos\\timeSchedule.csv'
    #filename = 'timeSchedule.csv'
    crn_adjacency = np.genfromtxt(filename, delimiter = ',')
    #print crn_adjacency # student x timeslot

    # adjacency(i,j,k) = adjacency(st1,st2,ts)
    adjacency = np.zeros([pop,pop,slots+33])

    for k in range(slots):
        for j in range(pop):
            for i in range(pop):
                if (int(crn_adjacency[i,k%22]) != 0 and crn_adjacency[i,k%22] == crn_adjacency[j,k%22]):
                    adjacency[i,j,k] = 1

    masterAdjacency = adjacency.sum(2)
    
    schedFile = 'schedules.csv'
    sched = csv.reader(open(schedFile,'r'))
    StuSchedDict = {}
    for row in sched:
        StuSchedDict[row[0]] = row[1]
        
masterAdjacency = adjacency.sum(2)

# ============================================================================
# |                           Function Definitions                           |
# ============================================================================
#
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
    for time in range(start, stop):
        current_adjacency = adjacency[:,:,time%77]
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
# (4.) Batch Model Sick Count
# ----------------------------------------------------------------------------
def sickCount(infection_array):                   # function to return the # of 
    timeslot_sum = (infection_array!=0).sum(0)    # infected individuals at the
    sickperday = np.zeros(77)                     # end of each day. 
    i = 0    
    for x in range(stop - start):
        if (x%11) == 10:
            sickperday[i] = timeslot_sum[x]
            i += 1
            print x
    return sickperday/nSimulations
# ----------------------------------------------------------------------------
# (5.) SIS Model
# ----------------------------------------------------------------------------
def AnalySIS(adjacency, nSimulations):
    effectOfSpread = np.zeros([355, 77])
    for patient0 in range(355):
        print patient0
        tempEffectOfSpread = np.zeros(77)
        for run in range(nSimulations):
            id_infected = np.zeros(355)
            id_infected[patient0] = 1       
            infection_array = disease_spread(start, stop, adjacency, id_infected)
            tempEffectOfSpread += sickCount(infection_array)
        effectOfSpread[patient0,:] = tempEffectOfSpread
    return effectOfSpread
# ----------------------------------------------------------------------------
# (6.) GUI SIS Model
# ----------------------------------------------------------------------------
def GUIAnalySIS(adjacency, patient0, start, stop):
    id_infected = np.zeros(355)
    id_infected[patient0] = 1       
    infection_array = disease_spread(start, stop, adjacency, id_infected)
    #effectOfSpread = singleSickCount(infection_array)
    #return (infection_array, effectOfSpread)
    return infection_array
    
# ----------------------------------------------------------------------------
# (8.) GUI Class
# ----------------------------------------------------------------------------

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
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
  
        infection_array = GUIAnalySIS(adjacency, int(perm), int(day), stop)
        patientCount = max((infection_array!=0).sum(0))
        mostSick = np.argmax((infection_array!=0).sum(0))

        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("WHAT HAPPENS WHEN YOU GO TO CLASS SICK?")
        l1 = tk.Label(t, text="Student Perm: "+perm)
        l1.pack()
        l5 = tk.Label(t, text="Student Perm: "+day)
        l5.pack()
        l2 = tk.Label(t, text="Major: "+ StuSchedDict[perm])
        l2.pack()
        l3 = tk.Label(t, text="Peak infection time:"+ str(mostSick))
        l3.pack()
        l4 = tk.Label(t, text="Number of people infected at peak: "+ str(patientCount) )
        l4.pack()

        G = nx.from_numpy_matrix(masterAdjacency)
#        G.node[perm]['shape']='square'

#        nodeList = np.arange(10)
#        nodeShape = np.array(['o']*10)
#        nodeShape[perm] = '*'

        pos = nx.spring_layout(G)       
        nx.draw(G, node_color=infection_array[:,start]/44.0, cmap = plt.get_cmap('YlOrBr'))
        #nx.draw(G, pos, nodelist=nodeList, node_shape=nodeShape, node_color=range(10), cmap = plt.get_cmap('YlOrBr'))          
        
        canvas = FigureCanvasTkAgg(plt.figure(1), master=t)

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    
# ----------------------------------------------------------------------------
# (9.) Dynamic Visualization
# ----------------------------------------------------------------------------
def presentationGUI():
    patient0 = input('What is your perm?')
    start = 0
    stop = 770
    i = 0
    
    root = tk.Tk()
    root.wm_title("Dynamic Spread of Sickness")
    root.wm_protocol('WM_DELETE_WINDOW', root.quit())

    f = plt.figure()
    a = f.add_subplot(111)
    plt.axis('off')


    # initial network
    infection_array = GUIAnalySIS(adjacency, patient0, start, stop)
    G = nx.from_numpy_matrix(adjacency[:,:,0])
#    pos = nx.spring_layout(G)
    nx.draw(G, node_color=infection_array[:,0], cmap = plt.get_cmap('YlOrBr'), ax=a)
    xlim=a.get_xlim()
    ylim=a.get_ylim()

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    def next_graph(infection_array):
        a.cla()
        #np.delete(adjacency, 0, 2)
        #infection_array = np.delete(infection_array, 0, 1)
        G = nx.from_numpy_matrix(masterAdjacency)        
        nx.draw(G, node_color=infection_array[:,0], cmap = plt.get_cmap('YlOrBr'), ax=a)
        a.set_xlim(xlim)
        a.set_ylim(ylim)
        plt.axis('off')
        canvas.draw()
        
    b = tk.Button(root, text="next",command=next_graph(infection_array=np.delete(infection_array,0,1)))
    b.pack()

    tk.mainloop()



# ============================================================================
# |                       Run Single or Batch Simulation                     |
# ============================================================================
option = raw_input('Do you want to run a single (s), batch (b), or presentation (p) simulation? ')
if option=='s':
    if __name__ == "__main__":
        root = tk.Tk()
        def quit(root):
            root.destroy()
        tk.Button(root, text="Quit", command=lambda root=root:quit(root)).pack()
        main = MainWindow(root)
        main.pack(side="top", fill="both", expand=True)
        root.mainloop()            
elif option=='b':
    nSimulations = input('Enter number of simulations to run per student: ')
    effectOfSpread_file = raw_input('Enter path to save data to, e.g., /Desktop/data:')    

    effectOfSpread = AnalySIS(adjacency, nSimulations)
    print effectOfSpread
    np.savetxt(effectOfSpread_file,effectOfSpread)
elif option =='p':
    presentationGUI()
else:
    print 'Unexpected input, try again.'
    execfile('main.py')
