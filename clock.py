import requests
import time
import words

# Seconds to sleep between polling time

SLEEP = 60


def ConvertWeatherToEnums(weather_resp):
  # Pass ICON and WIND
  return words.WeatherToEnums(weather_resp[0], weather_resp[1])


def ConvertTimeToEnums(time_resp):
  # Pass HOURS MINUTES SECONDS MERIDIEM
  return words.TimeToEnums(
    time_resp[0],
    time_resp[1],
    time_resp[2],
    time_resp[3],
  )


def BuildLightString(enums):
  '''Convert enums to space separated text.'''
  out = []
  for item in enums:
    out.append(item[1])

  return ' '.join(out)


# Initially just print list of enums when they change.
prev = None
while(True):
  weather_resp, time_resp = requests.Get()
  out = []
  out += ConvertWeatherToEnums(weather_resp)
  out += ConvertTimeToEnums(time_resp)

  string = BuildLightString(out)

  if string != prev:
    print string
    prev = string

  time.sleep(SLEEP)
