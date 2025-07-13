
from operatingmode import OperatingMode 
from common.util import current_time_ms
from common.util import debug
from footballscres.footballmatch import FootballMatch

import small_font as sf
import urequests
import time

# Make sure we can get the weather API key
try:
    from secrets import FOOTBALL_API_KEY
except ImportError:
    print("Create secrets.py with your security credentials.")

from setup import FOOTBALL_API_TEAM_ID

WHITE_RGB       = (255,255,255)
BLACK_RGB       = (0,0,0)
SCORE_RGB = (255,255,255) # white
BACKGROUND_RGB  = (0,0,0)

SCORE_TICK_TIME = 500 # update score display every 500 ms 
TEMP_ACTIVE_TIME_MS = 20000 # display scores for 20 seconds after an event 

class FootballScoresMode(OperatingMode):

    def __init__(self): 
        super().__init__()

        # the football match object is responsible for updating the match details
        # at the appropriate times and tracking events such as kick off or goals scored. 
        self.nextMatch = FootballMatch()
        self.matchEvents = [] 
        self.temp_inactive_time = -1
        self.next_display_time = -1 
     
    def set_active(self, is_active):

        super().set_active(is_active)
        # Force redisplay  
        self.next_display_time = -1
        
    def set_unicorn(self, unicorn):
        super().set_unicorn(unicorn)

    def set_display(self, display):
        super().set_display(display)
        
        # Now we have the display, create the pens 
        self.WHITE_PEN = display.create_pen(*WHITE_RGB) 
        self.BLACK_PEN = display.create_pen(*BLACK_RGB) 
        self.SCORE_PEN = display.create_pen(*SCORE_RGB) 
        self.BACKGROUND_PEN = display.create_pen(*BACKGROUND_RGB)
        
    def run(self):

        return_mode = OperatingMode.OK 

        # handle any events that may have occured in the previous run.
        # (doing it here means we can handle a change in active status).
        if ( self.is_active and len(self.match_events) > 0 ):
            self.handle_events() 
            
        # Refresh the match details.
        self.match_events = self.next_match.update()

        if self.is_active:
            # If there's no new events to handle in the next run,
            # we can show the scores now. 
            if ( len(self.match_events) == 0 ):
                self.show_scores()
        else:
            if (len(self.match_events) > 0):
                # this mode is not active and there has been a new event,
                # so force a change to this mode.
                # TODO - change back after 20 seconds.
                return_mode = OperatingMode.CHANGE_ACTIVE
                self.switch_inactive_time = current_time_ms() + TEMP_ACTIVE_TIME_MS 
            
        return return_mode  
        
    def get_team_info(self, teamid):
        
        team_info = None
        
        try:
        
            fullurl = f'{FOOTBALL_API}teams?id={teamid}'
            
            response = urequests.get(fullurl)
            
            if ( response.status_code == 200 ):
                json_response = response.json['response']
                
                team = json_response['team']
                
                team_info['shortname'] = team['code']
                team_info['longname'] = team['name'] 
                
        except Exception as e:
                debug(f"Error occurred requesting team data: {e}")
        
        return team_info 
        

    def show_scores(self):
        
        if ( self.next_display_time == -1 or current_time_ms() > self.next_display_time ):
            
            if ( self.next_match.    
