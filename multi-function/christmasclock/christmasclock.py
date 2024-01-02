
from operatingmode import OperatingMode 
from common.util import current_time_ms
from common.util import debug
from common.util import draw_icon 
import small_font as sf
import christmasclock.christmasicons as ci 

WHITE_RGB       = (255,255,255)
BLACK_RGB       = (0,0,0)
DATE_RGB        = (255,0,0)
CLOCK_RGB       = (0,255,0)
COUNTDOWN_RGB   = (255,255,255)
MERRY_XMAS_RGB  = (255,0,200)

CLOCK_TICK_TIME = 250 # redisplay clock every 0.25 seconds 
TWINKLE_TICK_TIME = 750 # twinke xmas tree every n milliseconds 

class ChristmasClockMode(OperatingMode):

    def __init__(self): 
        super().__init__()
        
        self.next_twinkle_time = -1
        self.next_clock_time = -1 
        self.utc_hours = 0
        self.utc_offset = 0

    def set_active(self, is_active):
        super().set_active(is_active)
        # Force redisplay of time. 
        self.next_twinkle_time = -1
        self.next_clock_time = -1

    def set_unicorn(self, unicorn):
        super().set_unicorn(unicorn)

    def set_display(self, display):
        super().set_display(display)
        
        # Now we have the display, create the pens this mode will use.  
        self.WHITE_PEN = display.create_pen(*WHITE_RGB) 
        self.BLACK_PEN = display.create_pen(*BLACK_RGB) 
        self.DATE_PEN = display.create_pen(*DATE_RGB) 
        self.CLOCK_PEN = display.create_pen(*CLOCK_RGB)
        self.COUNTDOWN_PEN = display.create_pen(*COUNTDOWN_RGB)
        self.MERRY_XMAS_PEN = display.create_pen(*MERRY_XMAS_RGB)

    def run(self):
        if self.is_active:
            self.show_clock()
            self.show_tree()
            
        return OperatingMode.OK

    # Think about moving clock display into base class as it may be a very common feature for multiple modes. 
    def show_clock(self):
        
        if ( self.next_clock_time == -1 or current_time_ms() > self.next_clock_time ):
            
            year, month, day, wd, hour, minute, second, _ = self.rtc.datetime()
            
            self.utc_hours = hour
            hour += self.utc_offset 
            
            self.display.set_pen(self.BLACK_PEN)
            self.display.rectangle(9, 0, 44,11)
            #self.display.rectangle(11, 6, 42,5)
            
            # calculate the time in hours, minutes and seconds until 7am christmas day.
            year_seconds_till_christmas = self.get_year_seconds_until(year,25,12,7,0,0);
            year_seconds_till_now = self.get_year_seconds_until(year,day,month,hour,minute,second)
            
            seconds_till_christmas = year_seconds_till_christmas - year_seconds_till_now
            
            is_christmas_day = False
            
            if ( seconds_till_christmas < 0 and month == 12 and day == 25 ):
                is_christmas_day = True 

            if ( seconds_till_christmas < 0 ):
                seconds_till_christmas = 0
                
            if ( not is_christmas_day ):
                sf.display_time(self.display, hour, minute, 11, 0, pen=self.CLOCK_PEN, justified='left')
                sf.display_long_date(self.display, day, month, 52, 0, pen=self.DATE_PEN, justified='right')

                days_till_christmas = int(seconds_till_christmas / (24 * 60 * 60))
                seconds_till_christmas %= (24*60*60)
                
                hours_till_christmas = int(seconds_till_christmas / (60 * 60))
                seconds_till_christmas %= (60 * 60)
                
                minutes_till_christmas = int(seconds_till_christmas / 60)
                seconds_till_christmas %= 60

                sf.display_long_time(self.display,
                                     [days_till_christmas, hours_till_christmas, minutes_till_christmas, seconds_till_christmas],
                                     52,6, pen=self.COUNTDOWN_PEN, justified='right') 


            else:
                # display merry xmas 
                sf.display_word(self.display, "merry", 10, 0, pen=self.MERRY_XMAS_PEN, justified='left')  
                sf.display_word(self.display, "christmas", 10, 6, pen=self.MERRY_XMAS_PEN, justified='left')  
                sf.display_time(self.display, hour, minute, 52, 0, pen=self.CLOCK_PEN, justified='right')
                #sf.display_long_date(self.display, day, month, 52, 6, pen=self.DATE_PEN, justified='right')
            
            self.next_clock_time = current_time_ms() + CLOCK_TICK_TIME
            
    def show_tree(self):
        
        if ( self.next_twinkle_time == -1 or current_time_ms() > self.next_twinkle_time ):
            
            tree_icon = ci.get_tree_icon()

            self.display.set_pen(self.BLACK_PEN)
            self.display.rectangle(0, 0, 9,11)
            
            draw_icon(self.display, tree_icon, 0,0,10,11)
            
            self.next_twinkle_time = current_time_ms() + TWINKLE_TICK_TIME 
    
    def get_year_seconds_until(self,year,day,month,hours,minutes,seconds):
        month_day_counts = [31,28,31,30,31,30,31,31,30,31,30,31]
        
        if ( self.is_leap_year(year) ):
            month_day_counts[1] = 29
            
        year_seconds_until = 0
        
        for index,month_day_count in enumerate(month_day_counts):
            if ( index < (month-1) ):
                year_seconds_until += (month_day_count * 24 * 60 * 60)
            else:
                break
        
        year_seconds_until += ((day-1) * 24 * 60 * 60)
        year_seconds_until += hours * 60 * 60
        year_seconds_until += minutes * 60
        year_seconds_until += seconds
 
        #debug(f'{day}: year_seconds_until = {year_seconds_until}')
        return year_seconds_until
    
    def is_leap_year(self, year):
        
        is_leap_year = False
        
        if ( (year % 4) == 0 ):
            if ( ((year % 100) != 0) or ((year % 400) == 0)):
                is_leap_year = True
            
        return is_leap_year
