# -*- coding: utf-8 -*-
"""
Created on Tue Mar 03 11:10:35 2015

@author: Tiawna
"""
import random as rd

sectionTotal = len(sectionList)
count = 0

for k in range(pop_size):
    
    student = studentList[k]
    
    # Shuffle the list of sections to create random enrollment
    rd.shuffle(sectionList)
    
    # Create temporary schedule and counts(22 time slots available)
    tempSched = [0]*22
    i = 0
    j = 0
    count+=1
    print count

    # Assign required class list to each student according to major
    student.req = requirements[student.major]
    
    # Fill the students' schedules     
    while i < len(student.req):
        
        # Reset schedule and try again
        if j > sectionTotal-1:
            i = 0
            j = 0
            tempSched = [0]*22
            student.section = []
            rd.shuffle(sectionList)
            

        # Find sections that fulfill the requirements
        if student.req[i] == sectionList[j].course:
            sec = sectionList[j]
            
            # Make sure the section is not already full
            if int(sec.cap) > 0:
                
                # Check that the class time is not already taken on the schedule
                if len(sec.timeSlot) < 3:
                    if tempSched[int(sec.timeSlot)] == 0:
                        tempSched[int(sec.timeSlot)] = 1
                        sec.cap = str(int(sec.cap)-1)
                        student.section.append(sectionList[j].crn)
                        i+=1
                        j = 0
                
                # Tokenize the string and then check each individual class time for availability
                else:
                    timeDivide = sec.timeSlot.find(',')
                    firstTimeSlot = sec.timeSlot[:timeDivide]
                    secondTimeSlot = sec.timeSlot[timeDivide+1:]
                    
                    if (tempSched[int(firstTimeSlot)] == 0 & tempSched[int(secondTimeSlot)] == 0):
                        tempSched[int(firstTimeSlot)] = 1
                        tempSched[int(secondTimeSlot)] = 1
                        sec.cap = str(int(sec.cap)-1)
                        student.section.append(sectionList[j].crn)
                        i+=1
                        j = 0
        j+=1
        
print(count)

filename = 'C:\Users\Tiawna\Documents\GitHub\LordsofChaos\schedules.csv'


f = open(filename, 'wt')
writer = csv.writer(f, lineterminator = '\n')

for student in studentList:
    temp = [student.sid] + student.section
    writer.writerow(temp)
    
f.close()
    

