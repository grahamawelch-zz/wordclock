import json
import urllib2
import subprocess


DEBUG = False
LOG = False

WEATHER = ('http://api.wunderground.com/api/'
           '%(key)s/%(features)s/q/%(query)s.%(format)s')
WEATHER_QUERY = 'autoip'
FORMAT = 'json'

# You need to have a file called 'wunderground_key'
# that only contains your api key for wunderground.
with open('wunderground_key', 'r') as key_file:
    KEY = key_file.read().strip()

# Hour Minute Second Month Day
TIME = 'http://www.timeapi.org/%(timezone)s/now?%(query)s'
TIME_QUERY = '\H:\M:\S:\m:\d'

HOURLY_FORECAST = 'hourly_forecast'

WIND = 'wspd'
TEMP = 'temp'
ICON = 'icon'
UNIT = 'english'

# Save the current timezone, update once per day
TIMEZONE = None if not DEBUG else 'PDT'
CHECKED_TIMEZONE = ''
TODAY = ''

# Save the current weather, update on the 30mins
WEATHER_TUPLE = None
CHECKED_WEATHER = ''
NOW = ''


def BuildWeatherRequestUrl():
  return WEATHER % {
    'key': KEY,
    'features': 'hourly',
    'query': WEATHER_QUERY,
    'format': FORMAT,
  }


def BuildTimezoneRequestUrl():
  return WEATHER % {
    'key': KEY,
    'features': 'conditions',
    'query': WEATHER_QUERY,
    'format': FORMAT,
  }


def BuildTimeRequestUrl(timezone):
  return TIME % {
    'timezone': timezone,
    'query': TIME_QUERY,
  }


def MakeRequest(url, sample, is_json=True):
  print url
  if not DEBUG:
    resp = urllib2.urlopen(url).read()
  else:
    with open(sample, 'r') as sample_file:
      resp = sample_file.read()
  if is_json:
    if LOG:
      print url
    return json.loads(resp)
  else:
    if LOG:
      print ' '.join([url, resp])
    return resp


def MakeWeatherRequest():
  return MakeRequest(
    BuildWeatherRequestUrl(),
    'samples/sample_hourly.json'
  )


def MakeTimezoneRequest():
  return MakeRequest(
    BuildTimezoneRequestUrl(),
    'samples/sample_conditions.json'
  )


def GitPull():
  try:
    subprocess.check_output(["git", "pull"])
  except Exception as e:
    print >> sys.stderr, e


def SetTimezone():
  global TIMEZONE
  TIMEZONE = MakeTimezoneRequest()['current_observation']['local_tz_short']

  global CHECKED_TIMEZONE
  CHECKED_TIMEZONE = TODAY


def MakeTimeRequest():
  if not TIMEZONE or CHECKED_TIMEZONE != TODAY:
    SetTimezone()
    # Update once a day.
    GitPull()

  return MakeRequest(
    BuildTimeRequestUrl(TIMEZONE),
    'samples/sample_time.txt',
    is_json=False
  )


def ParseWeatherResp(weather_resp, specific_h):
  '''We care about ICON, WIND[UNIT], and TEMP[UNIT].'''
  hour = weather_resp[HOURLY_FORECAST][specific_h]
  icon = hour[ICON]
  wind = hour[WIND][UNIT]
  temp = hour[TEMP][UNIT]

  return (icon, int(wind), int(temp))


def ParseTimeResp(time_resp):
  split = time_resp.split(':')
  hour = int(split[0])
  minute = int(split[1])
  second = int(split[2])
  month = int(split[3])
  day = int(split[4])

  # Set TODAY so we know to update TIMEZONE tomorrow
  global TODAY
  TODAY = day

  # Check for AM or PM
  if hour >= 12:
    meridiem = 'PM'
  else:
    meridiem = 'AM'

  return (hour, minute, second, meridiem, month, day)


def GetWeather(specific_h=0):
  return ParseWeatherResp(MakeWeatherRequest(), specific_h)


def GetTime():
  return ParseTimeResp(MakeTimeRequest())


def TimeToUpdateWeather(time_resp):
  ''' Decide if we should update our forcast.'''
  return (not WEATHER_TUPLE
          or (time_resp[0] != CHECKED_WEATHER and time_resp[1] > 30))


def Get():
  time_resp = GetTime()

  # If the hour is not the hour we checked, and its after 30mins
  if TimeToUpdateWeather(time_resp):
    # Recheck the weather
    global WEATHER_TUPLE
    WEATHER_TUPLE = GetWeather()

    # Update when we last checked
    global CHECKED_WEATHER
    CHECKED_WEATHER = time_resp[0]

  return (WEATHER_TUPLE, time_resp)

