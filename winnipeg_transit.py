# Copyright 2018 Ryan M. Spies
# This code is licensed under the MIT license (see LICENSE for details)
#
# winnipeg_transit.py 
#
# This file contains the main winnipeg_transit class which is used to
# initialize an API handler with the user's API key. Upon initialization
# of a winnipeg_transit object, the user can then make an API call to
# obtain the JSON response from Winnipeg Transit for specific requests.

import requests
import json

class winnipeg_transit:
  
  # Initialize the object with API key and the Winnipeg Transit API URL  
  def __init__(self, key:str):
    self.key = key
    self.url_base = "https://api.winnipegtransit.com/v2/"
  
  # Obtain a JSON response which contains stops within a walking distance
  # of dist from coordinates defined by a latitude of lat and a longtitude
  # of lon respectively.
  def get_stops(self,lat,lon,dist):
    stops_api = "stops.json?distance={}&lat={}&lon={}&walking=true&api-key={}".format(dist,lat,lon,self.key)
    stops_url = self.url_base + stops_api
    stops_request = requests.get(stops_url)
    stops = json.loads(stops_request.text)
    return stops
  
  # Obtain a JSON response which contains a list of estimated and scheduled
  # bus times for a given stop number.
  def get_times(self,stop):
    times_api = "stops/{}/schedule.json?api-key={}".format(stop,self.key)
    times_url = self.url_base + times_api
    times_request = requests.get(times_url)
    times = json.loads(times_request.text)
    return times
