# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:00:15 2018

@author: Natacha Chenevoy

This script:
- Extracts the raw text from The Waste Land by T. S. Eliot from an html format
- Performs Part of Speech tagging to extract proper nouns
- Querries the names in google maps to get the corresponding lat/lon 
(providing the proper noun corresponds to a place name)

"""

import requests
import nltk
from bs4 import BeautifulSoup
nltk.download("punkt")

################################################################################
# Extracts the raw text from The Waste Land by T. S. Eliot from an html format #
################################################################################

# Read HTML page
url = "http://www.gutenberg.org/files/1321/1321-h/1321-h.htm"
html = requests.get(url).text
raw = BeautifulSoup(html, "lxml").get_text()	# Without tags

# Cut down text
start = "il miglior fabbro"
start_pos = raw.find(start) + len(start) 
end_pos = raw.rfind("Line 415 aetherial] aethereal")
raw = raw[start_pos:end_pos]

# Tokenising
tokens = nltk.word_tokenize(raw)


text = nltk.Text(tokens)
len(text) #Number of words

# 20 most common words
fdist = nltk.FreqDist(text)
print(fdist.most_common(20))
fdist.plot(50, cumulative=True)


# 20 most common word length
fdist =  nltk.FreqDist(len(w) for w in text)
print(fdist.most_common(20))


# All unique words over 10 letters long 
sorted_words = sorted(set(text))   #Duplicates collapsed by set.
long_words = [w for w in sorted_words if len(w) > 10]
print(long_words)

#############################################################################
##         Perform Part of Speech tagging to extract proper nouns          ##
#############################################################################

# Part of Speech tagging
nltk.download('averaged_perceptron_tagger')                
tagged = nltk.pos_tag(text)                    

# Extract Proper Noun and remove false positive tags (numbers and uppercase words)
proper_nouns = []
for tag in tagged:
    if tag[1] == "NNP" and tag[0].isalpha() and not tag[0].isupper():
        proper_nouns.append(tag[0])


#############################################################################
##            Querry google maps for lat/lon of places in poem             ##
#############################################################################

import time

# Replace the value below with your personal API key:
mykey = ""

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

import pandas as pd
df = pd.DataFrame()

for noun in proper_nouns:
    
    params = {
        'address': noun,
        'key' : mykey
    }
    
    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()
    
    if res['results']:
        
        # Use the first result
        result = res['results'][0]
    
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        geodata['name'] = noun
    
        print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
        # 221B Baker Street, London, Greater London NW1 6XE, UK. (lat, lng) = (51.5237038, -0.1585531)
        df = df.append(geodata, ignore_index = True)
        # Wait for 5 seconds
        time.sleep(5)

import os
os.chdir("//ds.leeds.ac.uk/staff/staff19/mednche/GitHub/AdvancedProgrammingSkills/NLP")
df.to_csv("places.csv")
    