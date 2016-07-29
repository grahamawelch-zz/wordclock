
# Weather
SUN = 0
CLOUD = 1
RAIN = 2
STORM = 3
SNOW = 4
WIND = 5

# Minutes
M_HALF = 6
M_TWENTY = 7
M_FIVE = 8
M_QUARTER = 9
M_TEN = 10

# Transitions
IT = 11
PAST = 12
IS = 13
TO = 14

# Hours
H_ONE = 15
H_SIX = 16
H_NINE = 17
H_THREE = 18
H_SEVEN = 19
H_ELEVEN = 20
H_FIVE = 21
H_TEN = 22
H_FOUR = 23
H_TWO = 24
H_EIGHT = 25
H_T = 26 # Eight and Twelve share their 'T'
H_TWELVE = 27

# Other stuff
OCLOCK = 28
AM = 29
PM = 30

# List of possible Forecast Icons
# https://www.wunderground.com/weather/api/d/docs?d=resources/phrase-glossary#forecast_description_phrases
FORECAST = {
  'chanceflurries': [SNOW],
  'chancerain': [RAIN],
  'chancesleet': [RAIN, SNOW],
  'chancesnow': [SNOW],
  'chancetstorms': [STORM],
  'clear': [SUN],
  'cloudy': [CLOUD],
  'flurries': [SNOW],
  'fog': [CLOUD],
  'hazy': [CLOUD],
  'mostlycloudy': [CLOUD],
  'mostlysunny': [SUN],
  'partlycloudy': [CLOUD],
  'partlysunny': [SUN],
  'rain': [RAIN],
  'sleet': [RAIN, SNOW],
  'snow': [SNOW],
  'sunny': [SUN],
  'tstorms': [STORM],
  'unknown': [],
}

# In MPH
WIND_CUTOFF = 5
