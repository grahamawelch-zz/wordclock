import json
import urllib2

DEBUG = True

WEATHER = ('http://api.wunderground.com/api/'
           '%(key)s/%(features)s/q/%(query)s.%(format)s')
QUERY = 'autoip'
FORMAT = 'json'

# You need to have a file called 'wunderground_key'
# that only contains your api key for wunderground.
with open('wunderground_key', 'r') as key_file:
    KEY = key_file.read()

TIME = 'http://www.timeapi.org/%(timezone)s/now'

HOURLY_FORECAST = 'hourly_forecast'

WIND = 'wspd'
TEMP = 'temp'
ICON = 'icon'
FCTTIME = 'FCTTIME'

FIELDS = [WIND, TEMP, ICON, FCTTIME]

TIMEZONE = None if not DEBUG else 'PDT'


def BuildWeatherRequestUrl():
  return WEATHER % {
    'key': KEY,
    'features': 'hourly',
    'query': QUERY,
    'format': FORMAT,
  }


def BuildTimezoneRequestUrl():
  return WEATHER % {
    'key': KEY,
    'features': 'conditions',
    'query': QUERY,
    'format': FORMAT,
  }


def BuildTimeRequestUrl(timezone):
  return TIME % {
    'timezone': timezone
  }


def MakeRequest(url, sample, is_json=True):
  if not DEBUG:
    resp = urllib2.urlopen(url).read()
  else:
    with open(sample, 'r') as sample_file:
      resp = sample_file.read()
  if is_json:
    return json.loads(resp)
  else:
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


def SetTimezone():
  global TIMEZONE
  # Poor style :'(
  TIMEZONE = MakeTimezoneRequest()['current_observation']['local_tz_short']


def MakeTimeRequest():
  if not TIMEZONE:
    SetTimezone()
  return MakeRequest(
    BuildTimeRequestUrl(TIMEZONE),
    'samples/sample_time.txt',
    is_json=False
  )
