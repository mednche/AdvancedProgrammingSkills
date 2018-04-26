# Mapping the risk of burglary - a Python addin for ArcGIS

Manchester police, based on work by a variety of people, have found that in general, if somewhere is burgled, there is an increased risk of burglary for the houses within 400m of the burgled house for up to 4 weeks. This is known as the *Trafford Model*.

Our addin buffers a burglary file and then list the houses in an area by chance of burglary. Those houses that fall inside the most buffers will have the largest burglary risk. As our area is a rather small corner of the East End of London, we've used 80m buffers. 

Our addin displays the houses with the highest risk as a choropleth map, coloured by risk, and an associated sorted table. 

Note: you'll need to install arcpy and ArcGIS on your machine to run this script.
