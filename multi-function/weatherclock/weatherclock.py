
from operatingmode import OperatingMode 
from weatherclock.weather_api_map import WEATHER_API_MAP
from common.util import current_time_ms
from common.util import debug
from common.util import draw_icon 
import weatherclock.weathericons as weathericons
import small_font as sf
import urequests
import time

# Make sure we can get the weather API key
try:
    from secrets import WEATHER_API_KEY
except ImportError:
    print("Create secrets.py with your security credentials.")

WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'
WEATHER_API_LOCATION = 'Berkhamsted'

WHITE_RGB       = (255,255,255)
BLACK_RGB       = (0,0,0)
DATE_RGB        = (255,50,100)
TEMP_C_RGB      = (255,128,0) 
HUMIDITY_RGB    = (0,255,255)
CLOCK_RGB       = (0,255,0)
WEATHER_BG_RGB  = (0,0,0)

WEATHER_WIDTH   = 29

WEATHER_POLL_TIME = 60 * 1000 # poll weather every minute.
CLOCK_TICK_TIME = 500 # redisplay clock every 0.5 seconds 

class WeatherClockMode(OperatingMode):


    def __init__(self): 
        super().__init__()
        
        self.next_weather_time = -1
        self.next_clock_time = -1 
        self.utc_hours = 0
        self.utc_offset = 0

    def set_active(self, is_active):
        super().set_active(is_active)
        # Force redisplay of time. 
        self.next_weather_time = -1
        self.next_clock_time = -1
        
    def set_unicorn(self, unicorn):
        super().set_unicorn(unicorn)

    def set_display(self, display):
        super().set_display(display)
        
        # Now we have the display, create the pens 
        self.WHITE_PEN = display.create_pen(*WHITE_RGB) 
        self.BLACK_PEN = display.create_pen(*BLACK_RGB) 
        self.DATE_PEN = display.create_pen(*DATE_RGB) 
        self.TEMP_C_PEN = display.create_pen(*TEMP_C_RGB) 
        self.HUMIDITY_PEN = display.create_pen(*HUMIDITY_RGB) 
        self.CLOCK_PEN = display.create_pen(*CLOCK_RGB) 
        self.WEATHER_BG_PEN = display.create_pen(*WEATHER_BG_RGB)

    def run(self):
        if self.is_active:
            self.show_clock()
            self.show_weather()
            
        return OperatingMode.OK 
        
    def show_weather(self):

        if ( self.next_weather_time == -1 or current_time_ms() > self.next_weather_time ):
            
            try:
                # get current weather from weatherapi.com
                fullurl = f'{WEATHER_API_URL}?key={WEATHER_API_KEY}&q={WEATHER_API_LOCATION}&aqi=yes'
                debug(f"Requesting call to {fullurl}")
                
                json_response = None
                
                response = urequests.get(fullurl)
                
                if ( response.status_code == 200 ): 
                    json_response = response.json()

                    # extract time and compare with displayed time to see if we need to change the UTC offset.
                    location = json_response['location']
                    local_timedate_string = location['localtime']
                    parts = local_timedate_string.split(" ")
                    localtime = parts[1] 

                    # use the weather time to work out the local timezone. 
                    h,m = localtime.split(":")
                    debug(f"Time = {h}:{m}") 
                    self.utc_offset = self.utc_hours - int(h)
                    
                    # extract weather fields we're interested in 
                    response_weather = json_response['current'] 
                    response_weather_condition = response_weather['condition'] 

                    weather = dict()
                    
                    weather_text = WEATHER_API_MAP.get(response_weather_condition['text']) 
                    
                    weather['text'] = weather_text
                    weather['temp_c'] = response_weather['temp_c']
                    weather['wind_mph'] = response_weather['wind_mph']
                    weather['humidity'] = response_weather['humidity']
                    
                    debug(f"weather condition = {response_weather_condition}")
                    debug(f"weather = {weather}")
                    
                    # convert to display
                    self.display_weather(weather)

                response.close()
                
            except Exception as e:
                debug(f"Error occurred requesting weather data: {e}") 

            self.next_weather_time = current_time_ms() + WEATHER_POLL_TIME
            

    # This bit actually displays the weather on the galactic unicorn. 
    def display_weather(self,weather):
        
        self.display.set_pen(self.WEATHER_BG_PEN)
        self.display.rectangle(0,0,WEATHER_WIDTH,11)
        temp_c = int(weather['temp_c'])
        sf.display_temp_c(self.display, temp_c, 6, 6, pen=self.TEMP_C_PEN, justified='right')
        humidity = int(weather['humidity'])
        sf.display_humidity(self.display, humidity, 6,0, pen=self.HUMIDITY_PEN, justified='right')
        weathericons.draw_weather_icon(self.display, weather['text'], 18,0)
    
    def show_clock(self):
        
        if ( self.next_clock_time == -1 or current_time_ms() > self.next_clock_time ):
            
            year, month, day, wd, hour, minute, second, _ = self.rtc.datetime()
            
            self.utc_hours = hour
            hour += self.utc_offset 
            
            self.display.set_pen(self.BLACK_PEN)
            self.display.rectangle(29, 0, 24,5)
            self.display.rectangle(29, 6, 24,5)
            
            sf.display_time(self.display, hour, minute, 52, 0, pen=self.CLOCK_PEN, justified='right')
            sf.display_long_date(self.display, day, month, 52, 6, pen=self.DATE_PEN, justified='right')
            
            self.next_clock_time = current_time_ms() + CLOCK_TICK_TIME  
    