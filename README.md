For this project I become in the owner of a game company, and I need to find the right spot to place my
office, for this task I am given a list of needs from my employees, such as follows: a starbucks close to the office, train station / airport not too far, elementary school / kindergarten in the area, and the CEO is vegetarian, so...

I choosed to place my office in the city of San Jose, CA, because it is one of the best cities to place a tech company due to be located in Sillicon Valey. My company will be in the same buildings as one of the best startups in San Jose by the time this project is being done. These are : 'Savioke', 'Whatfix', 'CNEX Labs, Inc.', 'Petzila', 'uSens, Inc.', 'Trustlook Inc.', 'Signifyd', 'IntelliVision', 'Stratio, Inc.'

I will be using mongoDB to storage all the data I gather from google places API, and a .csv with information about startups got from angel.co.

I choose to use the pipelane structure for this project, with a main.py in wich a display a menu to make the work of getting data and manipulate them much more easier, and with a few changes the code can be reused in the future not only for San Jose, but for any other place.

In order to choose where to place my company I created a geocoordinates in mongoDB and a 2D sphere, then I make a list with a ranking by order of importance in wich places my employees want to be close to.

To conclude I ranked all the buildings, based on the startups coordinates, taking in consideration the rankig made by my employees and I choose a winner, shown in the final_ranking.csv, this is is shown in the visual_results.ipynb, and using folium i printed a map with the location of all the places, with the startups being represented with the cloud icon.

