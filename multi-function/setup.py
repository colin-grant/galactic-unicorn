
from galactic import GalacticUnicorn

TIME_API_URL = 'https://timeapi.io/api/Time/current/zone'
TIMEZONE = "Europe/London"

WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'
WEATHER_API_LOCATION = 'Berkhamsted'

FOOTBALL_API_URL = 'https://v3.football.api-sports.io/'

# 10 is england - change to 38 for watford fixtures 
FOOTBALL_TEAM_ID = 1 

from weatherclock.weatherclock import WeatherClockMode
from kitchentimer.kitchentimer import KitchenTimerMode
from christmasclock.christmasclock import ChristmasClockMode
from footballscores import FootballScoresMode 

OPERATING_MODES = [ WeatherClockMode(), KitchenTimerMode(), ChristmasClockMode() ]




