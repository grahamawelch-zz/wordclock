
from light_map import *


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255) # Looks like purple
ORANGE = (255, 127, 0)
GRANNY_SMITH_APPLE = (170,232,162)
DARK_BLUE_SKY = (128,184,206)
LILAC = (182,166,202)
RHYTHM = (122,102,150) # Purple

HOT = RED
COLD = BLUE

OFF = (0, 0, 0)
DEFAULT_COLOR = WHITE
#DEFAULT_COLORS = [YELLOW, CYAN, MAGENTA, GREEN, RED, BLUE, ORANGE]
DEFAULT_COLORS = [GRANNY_SMITH_APPLE, DARK_BLUE_SKY, LILAC, GRANNY_SMITH_APPLE, LILAC, RHYTHM, GRANNY_SMITH_APPLE, RHYTHM, DARK_BLUE_SKY]

HOLIDAYS = {
  (2, 14): [RED], # Valentine's Day
  (3, 17): [GREEN], # St. Patrick's Day
  (7, 4): [RED, WHITE, BLUE], # Independence Day
  (10, 31): [ORANGE, MAGENTA], # Halloween
  (12, 25): [RED, GREEN], # Christmas
}

BIRTHDAY_COLORS = [WHITE]

# Create a file called 'birthdays' that contains birthdays on each line
# in the format "<month> <day>\n" as numbers.
with open('birthdays', 'r') as birthday_file:
  birthday_list = birthday_file.read().splitlines()
  for birthday in birthday_list:
    HOLIDAYS[(int(birthday.split()[0]), int(birthday.split()[1]))] = BIRTHDAY_COLORS


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
  'partlycloudy': [SUN, CLOUD],
  'partlysunny': [SUN, CLOUD],
  'rain': [RAIN],
  'sleet': [RAIN, SNOW],
  'snow': [SNOW],
  'sunny': [SUN],
  'tstorms': [STORM],
  'unknown': [],
}

# In MPH
WIND_CUTOFF = 15

# In F
HOT_CUTOFF = 90
COLD_CUTOFF = 40


def WeatherToEnums(icon, wind):
  if icon in FORECAST:
    # Use list() here, so when we append WIND, we don't accidentially update
    # the FORECAST map.
    out = list(FORECAST[icon])
  else:
    out = []

  if wind > WIND_CUTOFF:
    out.append(WIND)

  return out


def TimeToEnums(hour, minutes, seconds):
  add_oclock = False
  increment_hr = False

  # Round seconds
  if seconds > 30:
    minutes = minutes + 1

  # Add enums for minutes
  if minutes <= 3:
    out = [IT, IS]
    add_oclock = True
  elif minutes <= 8:
    out = [M_FIVE, PAST]
  elif minutes <= 13:
    out = [M_TEN, PAST]
  elif minutes <= 18:
    out = [M_QUARTER, PAST]
  elif minutes <= 23:
    out = [M_TWENTY, PAST]
  elif minutes <= 28:
    out = [M_TWENTY, M_FIVE, PAST]
  elif minutes < 33:
    out = [M_HALF, PAST]
  elif minutes < 38:
    out = [M_TWENTY, M_FIVE, TO]
    increment_hr = True
  elif minutes < 43:
    out = [M_TWENTY, TO]
    increment_hr = True
  elif minutes < 48:
    out = [M_QUARTER, TO]
    increment_hr = True
  elif minutes < 53:
    out = [M_TEN, TO]
    increment_hr = True
  elif minutes < 58:
    out = [M_FIVE, TO]
    increment_hr = True
  else:
    out = [IT, IS]
    add_oclock = True
    increment_hr = True

  # If we are doing X minutes to Y. We need to increment the hr.
  if increment_hr:
    hour = hour + 1

  # Handle Meridiem
  if hour >= 12 and hour <= 23:
    out.append(PM)
  else:
    # Make sure this handles the case where it's 23:32:30+ and we round up to 24
    out.append(AM)

  # Adjust back to 12 hours
  if hour >= 12:
    hour = hour - 12
  elif hour == 0:
    hour = 12

  # Add enums for hours
  if hour == 1:
    out.append(H_ONE)
  elif hour == 2:
    out.append(H_TWO)
  elif hour == 3:
    out.append(H_THREE)
  elif hour == 4:
    out.append(H_FOUR)
  elif hour == 5:
    out.append(H_FIVE)
  elif hour == 6:
    out.append(H_SIX)
  elif hour == 7:
    out.append(H_SEVEN)
  elif hour == 8:
    out.append(H_EIGHT)
  elif hour == 9:
    out.append(H_NINE)
  elif hour == 10:
    out.append(H_TEN)
  elif hour == 11:
    out.append(H_ELEVEN)
  else:
    out.append(H_TWELVE)

  if add_oclock:
    out.append(OCLOCK)

  return out
