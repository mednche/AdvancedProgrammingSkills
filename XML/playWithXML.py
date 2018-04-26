# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:52:27 2018

@author: mednche

This script has two parts:
    - part 1: validate the schema of an XML file
    - part 2: Edit an XML file and tranform it into an HTML file
"""

import os
from lxml import etree

# change directory here
os.chdir("")

######################################################################
### validate the schema of an XML document
######################################################################

# open XML file 2
xml2 = open("map2.xml").read() 
xml2 = xml2.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
root = etree.XML(xml2)


# validate using XSD
xsd_file = open("map2.xsd")
xsd = etree.XMLSchema(etree.parse(xsd_file))

print(xsd.validate(root))


######################################################################
## Edit an XML file and tranform it into an HTML file
######################################################################

# open XML file 1
xml1 = open("map1.xml").read() 
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
root = etree.XML(xml1)


# validate using DTD
dtd_file = open("map1.dtd")
dtd = etree.DTD(dtd_file)
print(dtd.validate(root))

# parse XML
print (root.tag)			# "map"
print (root[0].tag)			# "polygon"
print (root[0].get("id"))		# "p1"
print (root[0][0].tag)		# "points"
print (root[0][0].text)		# "100,100 200,100" etc.

      
# edit xml file
p2 = etree.Element("polygon")				# Create polygon
p2.set("id", "p2");					# Set attribute
p2.append(etree.Element("points"))			# Append points
p2[0].text = "100,100 100,200 200,200 200,100"	# Set points text
root.append(p2)						# Append polygon
print (root[1].tag)
print (root[1].get("id"))		# "p2"
print (root[1][0].tag)		# "points"
print (root[1][0].text)		# "100,100 200,100" etc.

# write to an xlm file
out = etree.tostring(root, pretty_print=True)
print(out)
writer = open('xml3.xml', 'wb')		# Open for binary write
writer.write(out)
writer.close()

# open the new xml file created
xml2 = open("xml3.xml").read() 
xml2 = xml2.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
root2 = etree.XML(xml2)

# transform the new created xml into html
xsl3 = open("map3.xsl").read()		# Read stylesheet
xsl3 = xsl3.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
xslt_root = etree.XML(xsl3)			# Parse stylesheet
transform = etree.XSLT(xslt_root)		# Make transform
result_tree = transform(root2)			# Transform some XML root
transformed_text = str(result_tree)

print(transformed_text)
writer = open('xml3.html', 'w')		# Normal writer
writer.write(transformed_text)
