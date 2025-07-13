
import urequests
import time
from common.util import current_time_ms

"""
    Class that represents the next football match. This may either be a future match,
    an active in-play match, or a match that has finished on the current day.
    (Completed matches will show the final score until the match is refreshed to the next match overnight).
"""
class FootballMatch:
    
    STS_UNKNOWN = -1 
    STS_FUTURE = 0
    STS_IN_PLAY = 1
    STS_PAST = 2
    
    EVT_KICK_OFF = 0
    EVT_GOAL = 1 
    
    UPDATE_HOUR = 6 # time in hours at which to update the match details. 

    MAX_RETRY_COUNT = 3 # number of times to retry getting current match details
                        # before giving up.
                        
    KICK_OFF_POLL_INTERVAL_SECS = 30 
                        
    API_HEADERS = { "x-api-sports-key" : FOOTBALL_API_KEY }

    def __init__(self):
        
        self.status = STS_UNKNOWN 
        self.update_day = -1
        
        self.kick_off_date = 0 
        
        self.home_team = None 
        self.away_team = None
        
        self.home_goals = 0
        self.away_goals = 0
        
        self.elapsed = 0
        self.is_half_time = False 
        
    def update(self):
        
        event_list = [] 
        
        # do we need to get the next match details?
        year, month, day, wd, hour, minute, second, _ = self.rtc.datetime()
        
        if (day != self.update_day) or (self.update_retry_count > 0):
            if ( day != self.update_day ):
                # first time we've seen the day switch so reset the retry count.
                self.update_retry_count = 0

            self.update_day = day
            
            # If we haven't exhausted our max number of retries, check that we've passed the hour at which we
            # should attempt the update.
            if ( (self.update_retry_count < self.MAX_UPDATE_RETRIES
                 and (hour >= (self.UPDATE_HOUR + self.update_retry_count)) ):
                # Try to update the match details.
                try:
                     self.get_match_details()
                     self.update_retry_count = -1 # don't retry next time round. 
                except:
                     self.update_retry_count += 1
        
        # If the match details are in the future then we need to check for kick_off. 
        if ( self.status == STS_FUTURE ):
            # Should the match have started? 
            if ( time.time() >= self.kick_off_time) ):
                # Move it to a live game.
                self.status = STS_IN_PLAY
                self.next_in_play_update_time = 0 # force update
                event_list.insert(FootballMatch.EVT_KICK_OFF) 
                        
        if ( self.status == STS_IN_PLAY ): 
            if ( current_time_ms() > self.next_in_play_update_time ):
                try:
                    old_away_goals = self.away_goals
                    old_home_goals = self.home_goals 
                    
                    self.fetch_in_play_details()
                    
                    if ( old_away_goals != self.away_goals
                         or old_home_goals != self.home_goals ):
                        event_list.insert(FootballMatch.EVT_GOAL)
                except:
                finally: 
                    self.next_in_play_update_time = time.current_time_ms() + IN_PLAY_POLL_INTERVAL_SECS
        
        return event_list 
        
    def get_match_info(self):
            
        json_response = call_api(f'{FOOTBALL_API_URL}fixtures?team={FOOTBALL_TEAM_ID}&next=1')            
            
        if ( json_response ):
            
            fixture = json_response['fixture']
            timestamp = fixture['timestamp']
            
            teams = fixture['teams']
            
            home_team_id = teams['home']['id']
            self.home_team = get_team_info(home_team_id) 
            
            away_team_id = teams['away']['id']
            self.away_team = get_team_info(away_team_id)
            
            self.home_goals = 0
            self.away_goals = 0 
            
            self.status = STS_FUTURE
            
            self.kick_off_time = fixture['timestamp']
            
        else:
            debug(f"Error occurred requesting fixture data")
            raise Exception("Error occurred requesting fixture data") 

    def get_team_info(self, teamid):
        
        team_info = None
        
        json_response = self.call_api(f'{FOOTBALL_API}teams?id={teamid}')
        
        if ( json_response ):
            
            team = json_response['team']
            
            team_info['shortname'] = team['code']
            team_info['longname'] = team['name'] 
        else:        
            debug(f"Error occurred requesting team data")
        
        return team_info
    
    def fetch_in_play_details(self):
        
        # Call the api for the live details.
        response = call_api(f"{FOOTBALL_API}fixtures?team={FOOTBALL_TEAM_ID}&live=all") 
        
        # If there are results, update the current status.
        if len(response) > 0:
            # Should only be a single game. 
            live_game = response[0]
            
            goals = live_game['goals']
            fixture = live_game['fixture']
            live_status = fixture['status']['short'] 
            
            self.home_goals = goals['home']
            self.away_goals = goals['away']
            
            self.elapsed = live_status['elapsed']

            if ( live_status in [ '1H','HT','2H','ET','BT','P','INT','LIVE' ] ):
                # Game is currently ongoing.
                if ( live_status == 'HT' ):
                    self.is_half_time = True
                else:
                    self.is_half_time = False
            else:
                # Set game in past so we stop polling. 
                self.status = STATUS_PAST 
            
    def call_api(self, url):

        json_response = None 

        try:
            response = urequests.get(fullurl, headers=API_HEADERS)
            
            if ( response.status_code == 200 ):
                json_response = response.json['response']
                
            response.close() 
            
        except Exception as e:
            debug(f"Error calling API: {e}")
            
        return json_response 