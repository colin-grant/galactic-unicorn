
import urequests
from common.util import debug
from setup import TIME_API_URL 

class RealTimeClock:
    """ Real Time Clock that can query timeapi.io to update to a local timezone. """
    
    def __init__(self, machine_rtc, timezone):
        self.machine_rtc = machine_rtc
        self.timezone = timezone 
        self.last_timezone_query_day = 0 
        
    def datetime(self):
        
        year, month, day, weekday, hours, minutes, seconds, subseconds = self.machine_rtc.datetime() 
        
        # update timezone each day at 3 in the morning when hopefully we'll catch daylight savings time changes.
        if ((hours == 3) and (self.last_timezone_query_day != day)):
            self.sync_time()
            self.last_timezone_query_day = day # only do the timezone query once per day. 
                
        return year, month, day, weekday, hours, minutes, seconds, subseconds  
        
    
    def sync_time(self):
        """ Send a query to timeapi.io to get the current time given the setup time location. """
        try:
            # get current weather from weatherapi.com
            fullurl = f'{TIME_API_URL}?timeZone={self.timezone}' 
            debug(f"Requesting call to {fullurl}")
                
            json_response = None
            
            response = urequests.get(fullurl)
            
            if ( response.status_code == 200 ):
                json_response = response.json()

                debug(f"OK: {json_response}") 
                
                new_date_time = (json_response['year'],
                                 json_response['month'],
                                 json_response['day'],
                                 0, 
                                 json_response['hour'],
                                 json_response['minute'],
                                 json_response['seconds'],
                                 0  )
                debug(f"new date/time: {new_date_time}") 
                self.machine_rtc.datetime(new_date_time)

            response.close()
                
        except Exception as e:
            debug(f"Error occurred requesting time data: {e}") 
    
    
