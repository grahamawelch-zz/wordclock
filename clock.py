import lights
import requests
import sys
import time
import words

# Seconds to sleep between polling time

SLEEP = 60

PREV = []

def ConvertWeatherToEnums(weather_resp):
  # Pass ICON and WIND
  return words.WeatherToEnums(weather_resp[0], weather_resp[1])


def ConvertTimeToEnums(time_resp):
  # Pass HOURS MINUTES SECONDS MERIDIEM MONTH DAY
  return words.TimeToEnums(
    time_resp[0],
    time_resp[1],
    time_resp[2],
    time_resp[3],
  )


# Initially just print list of enums when they change.

while(True):
  weather_resp, time_resp = requests.Get()
  out = []
  out += ConvertWeatherToEnums(weather_resp)
  out += ConvertTimeToEnums(time_resp)

  string = ' '.join(str(word) for word in out)

  month = time_resp[4]
  day = time_resp[5]

  temp = weather_resp[2]

  lights.UpdateLights(out, PREV, (month, day), temp)
  if out != PREV:
    print string
    #print >> sys.stderr, string
    PREV = out

  time.sleep(SLEEP)
