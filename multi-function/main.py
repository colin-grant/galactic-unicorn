# The main.py script that runs at startup on the pico.

import time
import math
import machine
import network
import urequests
import ntptime
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

from weather_api_map import WEATHER_API_MAP
import small_font as sf
import weathericons

# Make sure we can get the wifi credentials. 
try:
    from secrets import WIFI_CREDENTIALS, WEATHER_API_KEY
    wifi_available = True
except ImportError:
    print("Create secrets.py with your security credentials.")
    wifi_available = False
   

WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'
WEATHER_API_LOCATION = 'Berkhamsted'

# create galactic object and graphics surface for drawing
gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

# create the real time clock object
rtc = machine.RTC()

# task timers
WEATHER_POLL_TIME = 60 * 1000 # poll weather every minute.
next_weather_time = -1

CLOCK_TICK_TIME = 500 # redisplay clock every 0.5 seconds 
next_clock_time = -1

utc_hours = 0
utc_offset = 0

WHITE = graphics.create_pen(255,255,255)
BLACK = graphics.create_pen(0,0,0)
DATE_PEN = graphics.create_pen(255,50,100)
TEMP_C_PEN = graphics.create_pen(255,128,0) 
HUMIDITY_PEN = graphics.create_pen(0,255,255)
CLOCK_PEN = graphics.create_pen(0,255,0)
WEATHER_BG_PEN = graphics.create_pen(0,0,0)

WEATHER_WIDTH=29

# Control the brightness using the light sensor
BRIGHTNESS_CHECK_TIME = 5000 # check brightness every 5 seconds
next_brightness_check_time = -1

MIN_BRIGHTNESS = 0.05
MAX_BRIGHTNESS = 0.6

MIN_LIGHT_LEVEL = 15
MAX_LIGHT_LEVEL = 100 

# the wireless lan device:
wlan = None

show_debug = True

def current_time_ms():
    ct_ms = time.ticks_ms()
    return (ct_ms) 

def debug(output_string):
    if ( show_debug ):
        print(output_string) 

# Check status of wifi and connect if necessary
# (Might put this in a library) 
def check_wifi():
    global wifi_available
    global wlan 
    
    if not wifi_available:
        return
    
    if ( wlan == None ):
        debug("creating wlan object") 
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

    # TODO - may want to put a timer in here so that we only check the connected status
    #        every n seconds. (Not sure if wlan.is_connected() is expensive or not - need to test.
    if ( not wlan.isconnected() ):

        for wifi_ssid, wifi_password in WIFI_CREDENTIALS:
            
            debug(f"Connecting to {wifi_ssid}") 
            wlan.connect(wifi_ssid, wifi_password)
            
            # Wait for connection
            for _ in range(0,10):
                if not wlan.isconnected():
                    # TODO - maybe have graphical representation of connecting.
                    debug("Waiting for Connection") 
                    time.sleep(0.5)
                else:
                    break;
                
            if ( wlan.isconnected() ):
                ip, subnet, gateway, dns_server = wlan.ifconfig() 
                debug(f"Connected to {wifi_ssid}, ip address = {ip}")
                break ;
            else:
                debug(f"Failed to connect to sid {wifi_ssid}") 

# Connect to wifi and synchronize the RTC time from NTP
def sync_time():
    if not wifi_available:
        return

    try:
        ntptime.settime()
        debug("Time set")
    except OSError:
        pass


def show_weather():
    
    global next_weather_time
    global current_hours 
    
    if ( next_weather_time == -1 or current_time_ms() > next_weather_time ):
        
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

                h,m = localtime.split(":")
                debug(f"Time = {h}:{m}") 
                utc_offset = utc_hours - int(h)
                
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
                display_weather(weather)

            response.close()
            
        except Exception as e:
            debug(f"Error occurred requesting weather data: {e}") 

        next_weather_time = current_time_ms() + WEATHER_POLL_TIME
        

# This bit actually displays the weather on the galactic unicorn. 
def display_weather(weather):
    
    graphics.set_pen(WEATHER_BG_PEN)
    graphics.rectangle(0,0,WEATHER_WIDTH,11)
    temp_c = int(weather['temp_c'])
    sf.display_temp_c(graphics, temp_c, 6, 6, pen=TEMP_C_PEN, justified='right')
    humidity = int(weather['humidity'])
    sf.display_humidity(graphics, humidity, 6,0, pen=HUMIDITY_PEN, justified='right')
    weathericons.draw_weather_icon(graphics, weather['text'], 18,0)
    
    
    
def show_centred_text(text, offset, width):
    
    # set the font
    graphics.set_font("bitmap8")
    graphics.set_pen(WHITE)
    
    # calculate text position so that it is centred
    w = graphics.measure_text(text, 1)
    x = int(width / 2 - w / 2 + 1) + offset 
    y = 2
    
    graphics.text(text, x, y, -1, 1) 
    
    
def show_clock():
    
    global next_clock_time
    global rtc
    global utc_offset
    global utc_hours
    
    if ( next_clock_time == -1 or current_time_ms() > next_clock_time ):
        
        year, month, day, wd, hour, minute, second, _ = rtc.datetime()
        
        utc_hours = hour
        hour += utc_offset 
        
        graphics.set_pen(BLACK)
        graphics.rectangle(29, 0, 24,5)
        graphics.rectangle(29, 6, 24,5)
        
        sf.display_time(graphics, hour, minute, 52, 0, pen=CLOCK_PEN, justified='right')
        sf.display_long_date(graphics, day, month, 52, 6, pen=DATE_PEN, justified='right')
        
        next_clock_time = current_time_ms() + CLOCK_TICK_TIME 
    
def check_brightness():
    
    global next_brightness_check_time

    if ( next_brightness_check_time == -1 or current_time_ms() > next_brightness_check_time ):

        brightness = 0
        
        light_level = gu.light()

        #graphics.set_pen(BLACK)
        #graphics.line(0,5,53,5)
        #graphics.set_pen(WHITE)
        #graphics.line(0,5,min(53,int(light_level)),5)
        #print(f'light level = {light_level}')
            
        if light_level < MIN_LIGHT_LEVEL:
            brightness = 0
        else:
            brightness = (light_level - MIN_LIGHT_LEVEL) / (MAX_LIGHT_LEVEL - MIN_LIGHT_LEVEL)
            brightness = (brightness * (MAX_BRIGHTNESS - MIN_BRIGHTNESS)) + MIN_BRIGHTNESS 

        #print(f"brightness = {brightness}")

        gu.set_brightness(brightness)

        next_brightness_check_time = current_time_ms() + BRIGHTNESS_CHECK_TIME 
    


# ------------------------------------------------------------------------
# -                       INITIALISATION                                  -
# ------------------------------------------------------------------------

gu.set_brightness(0.15)

check_wifi()
sync_time() 


# ------------------------------------------------------------------------
# -                       THE MAIN LOOP                                  -
# ------------------------------------------------------------------------
while True:
    
    check_wifi() 
    
    # Monitor brightness buttons 
    #if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
    #    gu.adjust_brightness(+0.01)

    #if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
    #    gu.adjust_brightness(-0.01)

    if gu.is_pressed(GalacticUnicorn.SWITCH_A):
        sync_time()

    # update the display
    show_weather()
    show_clock()
    check_brightness()
    
    gu.update(graphics)

    time.sleep(0.01)