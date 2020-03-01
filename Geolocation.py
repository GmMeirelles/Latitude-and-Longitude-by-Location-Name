from geopy.geocoders import Nominatim  # Importing an function of Geopy library
from time import sleep

geolocator = Nominatim(user_agent="geopy/1.21.0")  # Standard user_agent

country = ["Bronx",
           "Brooklyn",
           "Manhattan",
           "Queens",
           "Staten Island"]  # Locations

file = open("Location.csv", "a")  # Creating an csv archive
file.write("Local,latitude,longitude\n")
for i in range(0, len(country)):
    location = geolocator.geocode(country[i])
    file.write(f"{country[i]},{location.latitude},{location.longitude}\n") # Generating a file with csv formatting
    sleep(10)

file.close()
