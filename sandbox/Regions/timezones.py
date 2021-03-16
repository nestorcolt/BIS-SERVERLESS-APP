import requests
import time

##############################################################################################

api_key = "AIzaSyC6Y5n7-ta4T8GVtlwwzlUCnLsgKLa7YAs"
coordinates = (39.6034810, -119.6822510)
epoch_time = int(time.time())

url = "https://maps.googleapis.com/maps/api/timezone/json?location={},{}&timestamp={}&key={}"

##############################################################################################
query_string = url.format(*coordinates, epoch_time, api_key)
response = requests.get(query_string).json()
print(response)
