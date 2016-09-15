from neopixel import Adafruit_NeoPixel
from neopixel import Color
import random
import words


LED_COUNT      = 102
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 100 # Max 255
LED_INVERT     = False


# Initalize the strip
STRIP = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
STRIP.begin()

def ClearAll():
  for i in range(LED_COUNT):
    STRIP.setPixelColorRGB(i, 0, 0, 0)
  STRIP.show()

# Start fresh
ClearAll()



def Update(words, weather_color, colors):
  # Mix up the colors a little.
  # randint(a, b) returns a <= N <= b
  i = random.randint(0, len(colors) - 1)
  for word in words:
    if word.isWeather():
      cur_color = weather_color
    else:
      # Rotate through the colors for each word
      cur_color = colors[i]
      i += 1
      if i >= len(colors):
        i = 0
    for led in word.getLeds():
      print 'Updating pixel %s with %s' % (led, cur_color)
      STRIP.setPixelColorRGB(led, cur_color[0], cur_color[1], cur_color[2])


def Off(enums):
  Update(enums, words.OFF, [words.OFF])


def UpdateLights(new, old, date, temp):
  # new: List of Words
  # date: (month, day)
  # temp: number

  if temp > words.HOT_CUTOFF:
    weather_color = words.HOT
  elif temp < words.COLD_CUTOFF:
    weather_color = words.COLD
  else:
    weather_color = words.DEFAULT_COLOR

  if date in words.HOLIDAYS:
    colors = words.HOLIDAYS[date]
  else:
    colors = words.DEFAULT_COLORS

  # Call off first, then we might re turn on those same leds in a
  # different color
  print 'Old- ' + ' '.join(str(word) for word in old)
  print 'Old- ' + ' '.join(str(word.getLeds()) for word in old)
  print 'New- ' + ' '.join(str(word) for word in new)
  print 'New- ' + ' '.join(str(word.getLeds()) for word in new)

  Off(old)
  Update(new, weather_color, colors)
  STRIP.show()









