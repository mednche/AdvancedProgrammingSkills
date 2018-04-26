# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:49:29 2018

@author: mednche

This is a simple script that reads through the rows of an SQLITE database
"""


import sqlite3
import os

# Change directory here
#os.chdir("") 

# Connect to database
conn = sqlite3.connect('resultsdb.sqlite')
c = conn.cursor()

for row in c.execute('SELECT * FROM Results ORDER BY burglaries'):
    print(u'{1} burglaries have happened at {0}'.format(row[0], row[1]))
