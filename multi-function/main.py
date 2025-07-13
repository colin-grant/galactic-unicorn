# The main.py script that runs at startup on the pico.

import os
import time
import math
import machine
import network

from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
from common.galacticunicornbutton import GalacticUnicornButton 

from realtimeclock import RealTimeClock 

from operatingmode import OperatingMode 
from setup import OPERATING_MODES
from setup import TIMEZONE 

# Make sure we can get the wifi credentials. 
try:
    from secrets import WIFI_CREDENTIALS
    wifi_available = True
except ImportError:
    print("Create secrets.py with your security credentials.")
    wifi_available = False
   
# create galactic object and graphics surface for drawing
gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

# create the real time clock object
rtc = RealTimeClock(machine.RTC(), TIMEZONE)

# day we last ran end of day (so we only do it once a day). 
last_eod_run_day = 0 

# Control the brightness using the light sensor
BRIGHTNESS_CHECK_TIME = 5000 # check brightness every 5 seconds
next_brightness_check_time = -1

MIN_BRIGHTNESS = 0.05
MAX_BRIGHTNESS = 0.6

MIN_LIGHT_LEVEL_DAY = 10
MAX_LIGHT_LEVEL_DAY = 100

MIN_LIGHT_LEVEL_NIGHT = 16
MAX_LIGHT_LEVEL_NIGHT = 100

# night start and stop times (UTC only I think). 
NIGHT_TIME_START_HOUR = 23
NIGHT_TIME_END_HOUR = 6 


# the wireless lan device:
wlan = None

show_debug = True

def current_time_ms():
    ct_ms = time.ticks_ms()
    return (ct_ms) 

def debug(output_string):
    if ( show_debug ):
        print(output_string)

def clear_screen():
    graphics.set_pen(graphics.create_pen(0,0,0))
    graphics.clear()
    gu.update(graphics) 
    
def show_connecting():
    clear_screen()
    graphics.set_pen(graphics.create_pen(255,255,255))
    graphics.set_font("bitmap8")
    graphics.text("Connecting",0,1, scale=0.5)
    gu.update(graphics)
    
def hello():
    clear_screen() 
    graphics.set_pen(graphics.create_pen(255,255,255))
    graphics.set_font("bitmap8")
    graphics.text("Hello",0,1, scale=0.5)
    gu.update(graphics)
    time.sleep(1)

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

        print("Connecting"); 
        while not wlan.isconnected():

            for wifi_ssid, wifi_password in WIFI_CREDENTIALS:
            
                debug(f"Connecting to {wifi_ssid}") 
                wlan.connect(wifi_ssid, wifi_password)
                
                # Wait for connection
                for _ in range(0,10):
                    if not wlan.isconnected():
                        # TODO - maybe have graphical representation of connecting.
                        debug("Waiting for Connection") 
                        clear_screen()
                        time.sleep(0.5)
                        show_connecting()
                        time.sleep(0.5) 
                    else:
                        break;
                    
                if ( wlan.isconnected() ):
                    ip, subnet, gateway, dns_server = wlan.ifconfig() 
                    debug(f"Connected to {wifi_ssid}, ip address = {ip}")
                    break ;
                else:
                    debug(f"Failed to connect to sid {wifi_ssid}")
            
        clear_screen()

# Connect to wifi and synchronize the RTC time from NTP
def sync_time():
    if not wifi_available:
        return

    rtc.sync_time()
    
def is_end_of_day():
    
    global last_eod_run_day
    
    is_end_of_day = False

    _, _, day, _, hours, minutes, _, _ = rtc.datetime() 
        
    # EOD is at 3:30 every night. 
    if ((hours == 3) and (minutes == 30) and (last_eod_run_day != day)):
        print("End of day detected") 
        is_end_of_day = True
        last_eod_run_day = day

    return is_end_of_day, day    
    
def run_end_of_day(status):
    
    # The status tuple contains the current active mode and the eod day. 
    current_mode, eod_day = status 
    
    # At 4am every night we'll do a full reset to prevent lockup issues that can occur
    # if we run too long (memory leak or something?).
    # Before we do the reset we need to write the current mode to memory so we don't change
    # modes overnight.
    file = open("./status.txt","wt")
    file.write(f"mode:{active_mode_index};eod_day:{eod_day}")
    file.close()
    
    # Now reboot.
    machine.reset()

def load_saved_status():

    global active_mode_index
    global last_eod_run_day

    print("loading saved status"); 
    try:
        f = open("./status.txt" )
        start_status = f.read()
        print(f"start_status = {start_status}")
        
        status_list = start_status.split(";")
        
        for status in status_list:
            tag,value = status.split(":");
            print(f"tag = {tag}")
            print(f"value = {value}")
            if ( tag == "mode" ):
                active_mode_index = int(value);
            elif ( tag == "eod_day" ):
                last_eod_run_day = int(value);
                
        f.close();
        
        # Delete the status file - we only want this to exist if the unicorn
        # has reset itself. We don't maintain the status on a manual restart. 
        os.remove("./status.txt");
    except OSError:
        print("No status.txt file exists") 

def is_night():
    # Work out if it is night 
    _, _, _, _, hour, _, _, _ = rtc.datetime()
    #debug(f'is_night() hour = {hour}')
    return (hour >= NIGHT_TIME_START_HOUR) or (hour < NIGHT_TIME_END_HOUR)

def get_min_max_light_levels():
    is_night_time = is_night()
    
    min_light_level = MIN_LIGHT_LEVEL_NIGHT if is_night_time else MIN_LIGHT_LEVEL_DAY
    max_light_level = MAX_LIGHT_LEVEL_NIGHT if is_night_time else MAX_LIGHT_LEVEL_DAY
    
    return min_light_level, max_light_level 
    
def check_brightness():
    
    global next_brightness_check_time

    if ( next_brightness_check_time == -1 or current_time_ms() > next_brightness_check_time ):

        brightness = 0
        
        light_level = gu.light()
        
        min_light_level, max_light_level = get_min_max_light_levels() 

        #graphics.set_pen(BLACK)
        #graphics.line(0,5,53,5)
        #graphics.set_pen(WHITE)
        #graphics.line(0,5,min(53,int(light_level)),5)
        #print(f'light level = {light_level}')
        #print(f'min = {min_light_level}, max = {max_light_level}, is_night = {is_night()}')
            
        if light_level < min_light_level:
            brightness = 0
        else:
            brightness = (light_level - min_light_level) / (max_light_level - min_light_level)
            brightness = (brightness * (MAX_BRIGHTNESS - MIN_BRIGHTNESS)) + MIN_BRIGHTNESS 

        #print(f"brightness = {brightness}")

        gu.set_brightness(brightness)
        
        #if brightness == 0:
        #    print("Going into a deep sleep now")
        #    time.sleep(0.5)
        #    clear_screen()
            #machine.lightsleep(5000)
        #    time.sleep(5)
        #    print("Out of deep sleep")

        next_brightness_check_time = current_time_ms() + BRIGHTNESS_CHECK_TIME 
    

# ------------------------------------------------------------------------
# -                       INITIALISATION                                  -
# ------------------------------------------------------------------------

gu.set_brightness(0.15)
hello()

# check_brightness will go into a deep sleep causing a reset if the light level is too low.
# so we should do this before trying to connect to the network. 
check_brightness()

check_wifi()
sync_time()

for mode in OPERATING_MODES:
    mode.set_rtc(rtc)
    mode.set_unicorn(gu)
    mode.set_display(graphics)
    
# Set the first mode active.
active_mode_index = 0
prev_active_index = None

# Load the saved status if we're coming back up from a self inflicted
# reset. This means that we won't change modes overnight.
load_saved_status()

if len(OPERATING_MODES) > 0:
    OPERATING_MODES[active_mode_index].set_active(True)

switch_a = GalacticUnicornButton(gu, GalacticUnicorn.SWITCH_A)

# ------------------------------------------------------------------------
# -                       THE MAIN LOOP                                  -
# ------------------------------------------------------------------------
while True:
    
    check_wifi() 
    
    if switch_a.is_clicked():
        # change operating mode
        OPERATING_MODES[active_mode_index].set_active(False)
        active_mode_index += 1
        if active_mode_index >= len(OPERATING_MODES):
            active_mode_index = 0
        clear_screen() 
        OPERATING_MODES[active_mode_index].set_active(True)
        prev_mode_index = None 

    # Go through the modes - sending them a run request.
    # They will maintain whether they are active or not, so only the active mode should do any
    # updates to the display.
    for mode_index, mode in enumerate(OPERATING_MODES):

        status = mode.run()
        
        if status == OperatingMode.CHANGE_ACTIVE:
            # This mode wants to become active, so we change it, and save the previous active
            # mode so we can roll back if the mode is temporary and then wants to become inactive.
            # (eg. Football score just changed and wants to display new score for 1 minute?). 
            OPERATING_MODES[active_mode_index].set_active(False) 
            prev_active_index = active_mode_index
            mode.set_active(True) 
            active_mode_index = mode_index
            
        elif status == OperatingMode.CHANGE_INACTIVE:
            # If there's a previous mode, then roll back since the temporary mode has become inactive.
            # (Note - this can become confusing if multiple modes do this - so use carefully. We could consider using a stack
            # for the previous modes so we can roll back to previous temporary modes?). 
            if prev_active_index != None:
                mode.set_active(False) 
                active_mode_index = prev_active_index   
                prev_active_index = None 
                OPERATING_MODES[active_mode_index].set_active(True)

    # update the display
    check_brightness()
    
    gu.update(graphics)

    is_eod, eod_day = is_end_of_day()
    
    if is_eod:
        run_end_of_day((active_mode_index,eod_day))

    time.sleep(0.01)