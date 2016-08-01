from neopixel import Adafruit_NeoPixel
from neopixel import Color
import words


LED_COUNT      = 10
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 100 # Max 255
LED_INVERT     = False


# Initalize the strip
STRIP = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
STRIP.begin()


def Update(words, weather_color, colors):
  i = 0
  for word in words:
    if word.isWeather():
      cur_color = weather_color
    else:
      # Rotate through the colors for each word
      cur_color = colors[i]
      i += 1
      if i > len(colors):
        i = 0
    for led in word.getLeds():
      strip.setPixelColor(led, cur_color)


def Off(enums):
  update(enums, words.OFF, [words.OFF])


def UpdateLights(new, date, temp):
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
    colors = [words.DEFAULT_COLOR]

  # Call off first, then we might re turn on those same leds in a
  # different color
  Off(old)
  Update(new, weather_color, colors)
  strip.show()









