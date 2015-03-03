# coding: utf-8
# In[1]:

class Section:
    def __init__(self, crn, course, timeSlot, cap, majors):
        self.crn = crn
        self.timeSlot = timeSlot
        self.majors = majors
        self.cap = cap
        self.course = course

# In[13]:

import csv
dataFile = 'C:\Users\Tiawna\Downloads\sectionData.tsv'
data = csv.reader(open(dataFile), delimiter = '\t')
fields = data.next()

sectionLIst = []
sectionList = [Section(row[0], row[1], row[2], row[3], row[4]) for row in data]

class Student:
    def __init__(self, sid, major):
        self.sid = sid
        self.major = major
        self.section = []


# Hardcoded values for population
pop_size = 355
chemTotal = 64
compTotal = 56
csTotal = 84
eeTotal = 68
meTotal = 83


studentList = []
majorsList = ['chem']*chemTotal+['comp']*compTotal+['cs']*csTotal+['ee']*eeTotal+['me']*meTotal

#reqList = {} #NEED TO BRING IN THE LIST OF REQUIRED COURSES FOR EACH MAJOR

# Create Student Population
studentList = [Student(count, majorsList[count]) for count in range(pop_size)]
len(studentList)
studentList[6].major

reqFile = 'C:\Users\Tiawna\Downloads\\requirements.csv'
req = csv.reader(open(reqFile,'r'))
requirements = {}
for row in req:
    requirements[row[0]] = row[1:]
    
