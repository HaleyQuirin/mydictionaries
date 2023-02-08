"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""
# part 1 start
import json

infile = open("eq_data.json", "r")

earthquakes = json.load(infile)

print(len(earthquakes["features"]))

# part 1 end
# part 2 start
eq_dict = dict()
eq_dict[Location] = earthquakes["place"]
eq_dict[Magnitude] = earthquakes["mag"]
eq_dict[Longitude] = earthquakes["coordinates"]
eq_dict[Latitude] = earthquakes["coordinates"]


# print(eq_dict)

for earthquakes in earthquakes:

    if (earthquakes["feature"]["mag"]) > 6:
        print("Location: ", earthquakes["place"])
        print("Magnitude: ", earthquakes["mag"])
        print("Longitude: ", earthquakes["coordinates"])
        print("Latitude: ", earthquakes["coordinates"])
        print(eq_dict)

# info_to_extract = ["place", "mag", "coordinates"]
# info = dict(filter(lambda item: item[0] in info_to_extract, earthquakes.items()))
# print("Extracted Info: " + str(info))

# part 2/3 end
