from app_logger import logger
from app_exception.exception import AppException
import pyowm
import sys

#Weather_data.py
class WeatherData:
    def __init__(self):
        self.owmapikey='fd9706b192f3a51cc627504afa900c05'
        self.owm = pyowm.OWM(self.owmapikey)
    
    '''
    processing the request from dialogflow
    
    '''
    def processRequest(self,req):
        
        try:
            print("⚙️ Starting weather request handling...")
            self.result = req.get("queryResult", {})
            self.parameters = self.result.get("parameters", {})

            # Try to get city from parameters first
            self.city = self.parameters.get("city_name")

            # If city is None, try from alternativeQueryResults
            if not self.city:
                alt_results = req.get("alternativeQueryResults", [])
                if alt_results:
                    self.city = alt_results[0].get("parameters", {}).get("city_name")
                    
            print(self.city)
            mgr = self.owm.weather_manager()

            observation = mgr.weather_at_place(self.city)
            print(mgr)
            w = observation.weather

            location = observation.location
            self.lat = str(location.lat)
            self.lon = str(location.lon)

            self.wind_speed = str(w.wind().get('speed'))
            self.humidity = str(w.humidity)
            self.celsius_result = w.temperature('celsius')
            self.temp_min_celsius = str(self.celsius_result.get('temp_min'))
            self.temp_max_celsius = str(self.celsius_result.get('temp_max'))

            speech = "Today's the weather in " + str(self.city) + ":" + " , " +"Humidity : " + str(self.humidity) +" , " + "Wind Speed : " +str(self.wind_speed)+ " , " + "minimum temperature : " + str(self.temp_min_celsius) + " , " + "maximum temperature : " + str(self.temp_max_celsius)
        except Exception as e:
            raise AppException(e, sys)  from e  

        return {
            "fulfillmentText": speech,
            "displayText": speech
            }