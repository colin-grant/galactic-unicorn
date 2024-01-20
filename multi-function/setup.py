
from galactic import GalacticUnicorn

TIMEZONE = "Europe/London"

WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'
WEATHER_API_LOCATION = 'Berkhamsted'

from weatherclock.weatherclock import WeatherClockMode
from kitchentimer.kitchentimer import KitchenTimerMode
from christmasclock.christmasclock import ChristmasClockMode
#from footballscores import FootballScoresMode 

OPERATING_MODES = [ WeatherClockMode(), KitchenTimerMode(), ChristmasClockMode() ]




