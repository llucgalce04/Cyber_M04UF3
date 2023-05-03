#!/usr/bin/python3

import requests

api_url = "https://randomuser.me/api"

response = requests.get(api_url)

user = response.json()

user_name = user["results"][0]["name"]
user_location = user["results"][0]["location"]
user_picture = user["results"][0]["picture"]

print("Name: "+user_name["first"]+" "+user_name["last"])
print("Location: "+user_location["street"]["name"]+" "+str(user_location["street"]["number"])+", "+user_location["city"]+", "+user_location["country"])
print("Foto: "+user_picture["large"])
