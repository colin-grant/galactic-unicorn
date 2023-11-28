
from operatingmode import OperatingMode
import common.util 
import small_font as sf
import time

BLACK_RGB       = (0,0,0)
TIMER1_RGB      = (255,255,255)
TIMER2_RGB      = (255,255,255)
TIMER3_RGB      = (255,255,255)
TIMER4_RGB      = (255,255,255)

UPDATE_TICK_TIME = 100 # redisplay timers every 0.1 seconds 


class TimerDisplay():
    
    def __init__(self, xpos, ypos, pen_colour=(255,255,255), justified='left'):

        self.xpos = xpos
        self.ypos = ypos
        self.pen_colour = pen_colour
        self.justified = justified
        self.duration = 0
        self.start_time = 0
        self.isRunning = False 
        
    def display_timer(self, display):

        display_pen = display.create_pen(*self.pen_colour)
        
        if self.isRunning:
            seconds_left = int(((self.start_time + (self.duration * 1000)) - util.current_time_ms()) / 1000)
            if ( seconds_left < 0 ):
                seconds_left = 0
            seconds = seconds_left % 60
            minutes = int(seconds_left / 60)
            sf.display_time(display, minutes, seconds, self.xpos, self.ypos, pen=display_pen, justified=self.justified)
        else:
            seconds = self.duration % 60
            minutes = int(self.duration / 60)
            sf.display_time(display, minutes, seconds, self.xpos, self.ypos, pen=display_pen, justified=self.justified)


class KitchenTimerMode(OperatingMode):

    def __init__(self):
        super().__init__()
        self.next_update_time = -1
        
        # We'll have 4 timers - one in each corner. 
        self.timers = ( TimerDisplay(0,0, penColour=TIMER1_RGB, justified='left'),
                        TimerDisplay(0,6, penColour=TIMER2_RGB, justified='left'),
                        TimerDisplay(52,0, penColour=TIMER3_RGB, justified='right'),
                        TimerDisplay(52,6, penColour=TIMER4_RGB, justified='right') )

    def set_unicorn(self, unicorn):
        super().set_unicorn(unicorn)

    def set_display(self, display):
        super().set_display(display)

        # Now we have the display, create the pens 
        self.BLACK_PEN = display.create_pen(*BLACK_RGB) 

    def run(self):
        if self.is_active:
            
            # TODO - use buttons to allow timers to be selected, set and reset. 
            
            if ( self.next_update_time == -1 or util.current_time_ms() > self.next_update_time ):

                self.set_pen(self.BLACK_PEN)
                self.display.clear()
                self.update_timers()

                self.next_update_time = current_time_ms() + UPDATE_TICK_TIME 
    
        # TODO - go through each of the timers to see if any has completed, in which case we'll
        #        need to force a change to this mode and then let the alarm sound. 
        return OperatingMode.OK 
        
    def update_timers(self):

        for timer in self.timers:
            timer.display_timer(self.display)
            
