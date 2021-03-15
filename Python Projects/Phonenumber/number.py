import phonenumbers

from test import number

from phonenumbers import geocoder

#this give us country Name

ch_number = phonenumbers.parse(number, "ch")

print("Coutry: ", geocoder.description_for_number(ch_number, "en"))

#This give us carrier name

from phonenumbers import carrier

service_number = phonenumbers.parse(number, "Ro")

print("Carrier: ", carrier.name_for_number(service_number, "en"))