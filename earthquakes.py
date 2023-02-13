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

earthquake_info = json.load(infile)

print(len(earthquake_info["features"]))
# part 1 end

# (not needed) Location = {"place"} 
# (not needed) Magnitude = {"mag"}
# (not needed) Longitude = {"coordinates"[0]}
# (not needed) Latitude = {"coordinates"[1]}
eq_dict = {}

# part 2/3 start
for eq in earthquake_info["features"]:

    if eq["properties"]["mag"] > 6:
        Location = eq["properties"]["place"]
        Magnitude = eq["properties"]["mag"]
        Longitude = eq["geometry"]["coordinates"][0]
        Latitude = eq["geometry"]["coordinates"][1]
        eq_dict[eq["properties"]["title"]] = {
            "Location": Location,
            "Magnitude": Magnitude,
            "Longitude": Longitude,
            "Latitude": Latitude,
        }

earthquakes = 0

for eq in earthquake_info["features"]:
    earthquakes = earthquakes + 1

    # print("Location: ", eq["properties"]["place"])
    # print("Magnitude: ", eq["properties"]["mag"])
    # print("Longitude: ", eq["geometry"]["coordinates"][0])
    # print("Latitude: ", eq["geometry"]["coordinates"][1])
    # print()
    # print()

for eq in eq_dict:
    print("Location: ", str(eq_dict[eq]["Location"]))
    print("Magnitude: ", str(eq_dict[eq]["Magnitude"]))
    print("Longitude: ", str(eq_dict[eq]["Longitude"]))
    print("Latitude: ", str(eq_dict[eq]["Latitude"]))
    print("_____________________________")
    print("                             ")
# part 2/3 end
