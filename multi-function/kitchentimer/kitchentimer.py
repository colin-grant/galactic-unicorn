
from operatingmode import OperatingMode
import common.util as util
import small_font as sf
import time
from galactic import GalacticUnicorn
from common.galacticunicornbutton import GalacticUnicornButton 

BLACK_RGB       = (0,0,0)
TIMER_ACTIVE_RGB = (0,255,0)
TIMER_RUNNING_RGB = (0,255,255)
TIMER_INACTIVE_RGB = (255,255,255)
TIMER_WARNING_RGB = (255,0,255)
TIMER_COMPLETED_RGB = (255,0,0) 

TIMER_COMPLETED_DURATION_SEC = 5 # How long in seconds to show the timer in a completed state.

ACTIVE_DISPLAY_PERIOD_SECS = 5

WARNING_SECONDS = 10 # when to start warning that the timer is nearly expired. 

UPDATE_TICK_TIME = 100 # redisplay timers every 0.1 seconds 


class TimerDisplay():
    
    def __init__(self, xpos, ypos, justified='left'):

        self.xpos = xpos
        self.ypos = ypos
        self.justified = justified
        self.minutes = 0
        self.seconds = 0 
        self.end_time = 0
        self.is_running = False
        self.is_active = False
        
    def set_active(self):
        self.is_active = True
        
    def set_inactive(self):
        self.is_active = False 
        
    def display_timer(self, display):

        if self.is_running:
            # adjust time based on start time and current time.
            
            seconds_left = int((self.end_time - util.current_time_ms()) / 1000)
            if ( seconds_left < 0 ):
                seconds_left = 0
            self.seconds = seconds_left % 60
            self.minutes = int(seconds_left / 60)

        # display the current time remaining. 
        if self.is_active:
            display_pen = display.create_pen(*TIMER_ACTIVE_RGB)
        elif self.is_running:
            if ( seconds_left > 0 and seconds_left <= WARNING_SECONDS):
                display_pen = display.create_pen(*TIMER_WARNING_RGB)
            else:
                display_pen = display.create_pen(*TIMER_RUNNING_RGB)
        else:
            display_pen = display.create_pen(*TIMER_INACTIVE_RGB) 
        
        sf.display_time(display, self.minutes, self.seconds, self.xpos, self.ypos, pen=display_pen, justified=self.justified)
        
        if ( self.is_running and seconds_left == 0 ):
            # TODO - put in completed logic here
            self.is_running = False 
            
    def change_minutes(self, to_add):
        self.is_running = False 
        self.minutes = (self.minutes + to_add) % 99
        
    def change_seconds(self, to_add):
        self.is_running = False
        self.seconds = (self.seconds + to_add) % 60
        
    def toggle_start_stop(self):
        print('start/stop timer')
        if self.is_running:
            # Just stop the timer at the current time. 
            self.is_running = False
            print('timer stopped') 
        else:
            # Start the clock.
            if (self.minutes > 0) or (self.seconds > 0):
                self.end_time = util.current_time_ms() + (((self.minutes * 60) + self.seconds) * 1000)
                self.is_running = True
                print('timer started')
        

class KitchenTimerMode(OperatingMode):

    def __init__(self):
        super().__init__()
        self.next_update_time = -1
        
        # We'll have 4 timers - one in each corner. 
        self.timers = ( TimerDisplay(0,0, justified='left'),
                        TimerDisplay(0,6, justified='left'),
                        TimerDisplay(52,0, justified='right'),
                        TimerDisplay(52,6, justified='right') )
        
        self.active_timer = -1
        self.active_display_end_time = 0
        
    def set_unicorn(self, unicorn):
        super().set_unicorn(unicorn)
        
        # create the buttons we'll need to monitor. 

        # button b is used to move between the timers to select the active timer. 
        self.btn_change_active = GalacticUnicornButton(self.unicorn, GalacticUnicorn.SWITCH_B)
        # volume up and down are used to set the minutes for the active timer.
        self.btn_mins_inc = GalacticUnicornButton(self.unicorn, GalacticUnicorn.SWITCH_VOLUME_UP) 
        self.btn_mins_dec = GalacticUnicornButton(self.unicorn, GalacticUnicorn.SWITCH_VOLUME_DOWN) 
        # brightness(lux) up and down are used to set the seconds for the active timer.
        self.btn_secs_inc = GalacticUnicornButton(self.unicorn, GalacticUnicorn.SWITCH_BRIGHTNESS_UP) 
        self.btn_secs_dec = GalacticUnicornButton(self.unicorn, GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN) 
        # button d is used to start/stop the active timer.
        self.btn_start_stop = GalacticUnicornButton(self.unicorn, GalacticUnicorn.SWITCH_D) 

    def set_display(self, display):
        super().set_display(display)

        # Now we have the display, create the pens 
        self.BLACK_PEN = display.create_pen(*BLACK_RGB) 

    def run(self):
        if self.is_active:
            
            if ( self.next_update_time == -1 or util.current_time_ms() > self.next_update_time ):

                self.display.set_pen(self.BLACK_PEN)
                self.display.clear()
                self.update_timers()

                self.next_update_time = util.current_time_ms() + UPDATE_TICK_TIME

            # If we've currently got an active timer, see if the active display indicator should be timed out.
            if ((self.active_timer >= 0) and (util.current_time_ms() > self.active_display_end_time)):
                self.timers[self.active_timer].set_inactive()
                self.active_timer = -1 

            # Change active timer if B button clicked. 
            if ( self.btn_change_active.is_clicked() ):
                if ( self.active_timer == -1 ):
                    self.active_timer = 0
                    self.timers[0].set_active()
                else: 
                    self.timers[self.active_timer].set_inactive() 
                    self.active_timer = (self.active_timer + 1) % len(self.timers)
                    self.timers[self.active_timer].set_active() 

                self.reset_active_display_timeout()
          
            # Check the time change buttons.
            if ( self.active_timer >= 0 ):
                if (self.btn_mins_inc.is_clicked() ):
                    self.timers[self.active_timer].change_minutes(1)
                    self.reset_active_display_timeout()
                if ( self.btn_mins_dec.is_clicked() ):
                    self.timers[self.active_timer].change_minutes(-1)
                    self.reset_active_display_timeout()
                if ( self.btn_secs_inc.is_clicked() ):
                    self.timers[self.active_timer].change_seconds(1)
                    self.reset_active_display_timeout()
                if ( self.btn_secs_dec.is_clicked() ):
                    self.timers[self.active_timer].change_seconds(-1)
                    self.reset_active_display_timeout()
                
                # Check the start stop button.
                if ( self.btn_start_stop.is_clicked() ):
                    self.timers[self.active_timer].toggle_start_stop() 
    
        return OperatingMode.OK 
        
    def reset_active_display_timeout(self):
        self.active_display_end_time = util.current_time_ms() + (ACTIVE_DISPLAY_PERIOD_SECS * 1000)
    
    def update_timers(self):

        for timer in self.timers:
            timer.display_timer(self.display)
            
