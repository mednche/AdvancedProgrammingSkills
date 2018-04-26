# Mapping places mentionned in a poem - an application of Natural Language Processing

<p align="center">
  <img src="MapOfPlaces.png">
</p>

This script:
1. Extracts the raw text from the poem ['The Waste Land'by T. S. Eliot](http://www.gutenberg.org/ebooks/1321?msg=welcome_stranger) from an html format
2. Performs Part of Speech tagging to extract proper nouns
3. Querries the names in google maps to get the corresponding lat/lon (providing the proper noun corresponds to a place name)
4. Displays the location of the places in the poem on an interractive world map using [Bokeh](https://bokeh.pydata.org/en/latest/)

Note: Bokeh maps do not display on Github.
