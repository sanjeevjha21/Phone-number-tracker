import phonenumbers
import folium
print("Type your number with your country code :")

number = input()
print('User who use this number')
ktr=input()

# How to get country name of the phone number
from phonenumbers import geocoder

#to get the key that we will use for longtitude and latitude go to opencage website and make a account there and the go to API key and then copy the digit and paste below
key = "6c88f3edf15448a582a99183d722b39c"
ch_number = phonenumbers.parse(number, "CH")
yourLocation = geocoder.description_for_number(ch_number, "en")
print(yourLocation)
#service provider of the phone number

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

#actuall longtitude and latitude of phone number location

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

##save map in html file
myMap.save(ktr+" number location.html")
#three pip package to install ( phonenumbers,opencage,folium)