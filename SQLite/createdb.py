# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:19:48 2018

@author: mednche

This is a simple script that creates an SQLITE database with a single row
"""

import sqlite3
import os

# change directory
# os.chdir("")

# Connect to database, or create it if does not exist
conn = sqlite3.connect('resultsdb.sqlite')
c = conn.cursor()

# Create a table
c.execute("CREATE TABLE Results (address text, burglaries integer)")

# Insert a row in that table 
c.execute("INSERT INTO Results VALUES ('Queen Vic',2)")

# commit and close database
conn.commit()
conn.close()
