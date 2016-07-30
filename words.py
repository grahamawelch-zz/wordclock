
# Weather
SUN = (0, 'SUN')
CLOUD = (1, 'CLOUD')
RAIN = (2, 'RAIN')
STORM = (3, 'STORM')
SNOW = (4, 'SNOW')
WIND = (5, 'WIND')

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
WIND_CUTOFF = 10


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
M_HALF = (6, 'HALF')
M_TWENTY = (7, 'TWENTY')
M_FIVE = (8, 'FIVE')
M_QUARTER = (9, 'QUARTER')
M_TEN = (10, 'TEN')

# Transitions
IT = (11, 'IT')
PAST = (12, 'PAST')
IS = (13, 'IS')
TO = (14, 'TO')

# Hours
H_ONE = (15, 'ONE')
H_SIX = (16, 'SIX')
H_NINE = (17, 'NINE')
H_THREE = (18, 'THREE')
H_SEVEN = (19, 'SEVEN')
H_ELEVEN = (20, 'ELEVEN')
H_FIVE = (21, 'FIVE')
H_TEN = (22, 'TEN')
H_FOUR = (23, 'FOUR')
H_TWO = (24, 'TWO')
H_EIGHT = (25, 'EIGH')
# Eight and Twelve share their 'T'
H_T = (26, 'T')
H_TWELVE = (27, 'WELVE')

# Other stuff
OCLOCK = (28, 'OCLOCK')
AM = (29, 'AM')
PM = (30, 'PM')


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
    # Eight shares the T with twelve
    out.append(H_EIGHT)
    out.append(H_T)
  elif hour == 9:
    out.append(H_NINE)
  elif hour == 10:
    out.append(H_TEN)
  elif hour == 11:
    out.append(H_ELEVEN)
  else:
    # Tweleve shares the T with eight
    out.append(H_T)
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
