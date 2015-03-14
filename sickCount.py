# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:35:40 2015

@author: Tiawna
"""

columns = (snapshot!=0).sum(0)
days = []
for x in range(0,76):
    if (x%11) == 10:
        days.append(columns[x])
