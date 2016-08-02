

class Word:
  counter = 0

  def __init__(self, name, leds):
    self.name = name
    self.leds = leds
    self.id = Word.counter
    Word.counter += 1

  def __str__(self):
    return self.name

  def __lt__(self, other):
    return self.id - other.id

  def getLeds(self):
    return self.leds

  def isWeather(self):
    return False


class Weather(Word):
  def isWeather(self):
    return True


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


HOT = RED
COLD = BLUE

OFF = (0, 0, 0)
DEFAULT_COLOR = WHITE

# So far only holidays with fixed dates. 
HOLIDAYS = {
  (2, 14): [RED], # Valentine's Day
  (3, 17): [GREEN], # St. Patrick's Day
  (7, 4): [RED, WHITE, BLUE], # Independence Day
  (12, 25): [RED, GREEN], # Christmas
}

BIRTHDAY_COLORS = [YELLOW, CYAN, MAGENTA]

# You need to have a file called 'birthdays'
# that contains lines of "<MONTH> <DAY>\n"
with open('birthdays', 'r') as birthday_file:
  raw_birthdays = birthday_file.read()
  for entry in raw_birthdays.splitlines():
    HOLIDAYS[(entry.split()[0], entry.split()[1])] = BIRTHDAY_COLORS


# Weather
SUN = Weather('SUN', [])
CLOUD = Weather('CLOUD', [])
RAIN = Weather('RAIN', [])
STORM = Weather('STORM', [])
SNOW = Weather('SNOW', [])
WIND = Weather('WIND', [])

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


# Minutes
M_HALF = Word('HALF', [])
M_TWENTY = Word('TWENTY', [])
M_FIVE = Word('FIVE', [])
M_QUARTER = Word('QUARTER', [])
M_TEN = Word('TEN', [])

# Transitions
IT = Word('IT', [])
PAST = Word('PAST', [])
IS = Word('IS', [])
TO = Word('TO', [])

# Hours
H_ONE = Word('ONE', [])
H_SIX = Word('SIX', [])
H_NINE = Word('NINE', [])
H_THREE = Word('THREE', [])
H_SEVEN = Word('SEVEN', [])
H_ELEVEN = Word('ELEVEN', [])
H_FIVE = Word('FIVE', [])
H_TEN = Word('TEN', [])
H_FOUR = Word('FOUR', [])
H_TWO = Word('TWO', [])
H_EIGHT = Word('EIGHT', [])
H_TWELVE = Word('TWELVE', [])

# Other stuff
OCLOCK = Word('OCLOCK', [])
AM = Word('AM', [])
PM = Word('PM', [])


def TimeToEnums(hour, minutes, seconds, meridiem):
  flip_meridiem = False
  add_oclock = False
  increment_hr = False

  # Round seconds
  if seconds > 30:
    minutes = minutes + 1

  # Add enums for minutes
  if minutes <= 2:
    out = [IT, IS]
    add_oclock = True
  elif minutes <= 7:
    out = [M_FIVE, PAST]
  elif minutes <= 12:
    out = [M_TEN, PAST]
  elif minutes <= 17:
    out = [M_QUARTER, PAST]
  elif minutes <= 22:
    out = [M_TWENTY, PAST]
  elif minutes <= 27:
    out = [M_TWENTY, M_FIVE, PAST]
  elif minutes < 32:
    out = [M_HALF, PAST]
  elif minutes < 37:
    out = [M_TWENTY, M_FIVE, TO]
    increment_hr = True
  elif minutes < 42:
    out = [M_TWENTY, TO]
    increment_hr = True
  elif minutes < 47:
    out = [M_QUARTER, TO]
    increment_hr = True
  elif minutes < 52:
    out = [M_TEN, TO]
    increment_hr = True
  elif minutes < 57:
    out = [M_FIVE, TO]
    increment_hr = True
  else:
    out = [IT, IS]
    add_oclock = True
    increment_hr = True

  # If we are doing X minutes to Y. We need to increment the hr.
  if increment_hr:
    hour = hour + 1

    # Still no 13
    if hour > 12:
      flip_meridiem = True
      hour = hour - 12

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

  # Handle Meridiem
  if meridiem == 'AM' and not flip_meridiem:
    out.append(AM)
  elif meridiem == 'PM' and not flip_meridiem:
    out.append(PM)
  elif meridiem == 'AM': # and flip_meridiem
    out.append(PM)
  else: # meridiem == 'PM' and flip_meridiem
    out.append(AM)

  return out
