# Mapping places mentionned in a poem - an application of Natural Language Processing

<p align="center">
  <img src="MapOfPlaces.png">
</p>

This script:
- Extracts the raw text from the poem 'The Waste Land'by T. S. Eliot from an html format
- Performs Part of Speech tagging to extract proper nouns
- Querries the names in google maps to get the corresponding lat/lon (providing the proper noun corresponds to a place name)
- Displays the location of the places in the poem on an interractive world map using Bokeh
