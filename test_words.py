from neopixel import *
import time
import words
import light_map


LED_COUNT      = 102
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False



strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()


ALL_WORDS = [
  light_map.SUN,
  light_map.CLOUD,
  light_map.RAIN,
  light_map.STORM,
  light_map.SNOW,
  light_map.WIND,
  light_map.M_HALF,
  light_map.M_TWENTY,
  light_map.M_FIVE,
  light_map.M_QUARTER,
  light_map.M_TEN,
  light_map.IT,
  light_map.PAST,
  light_map.IS,
  light_map.TO,
  light_map.H_ONE,
  light_map.H_SIX,
  light_map.H_NINE,
  light_map.H_THREE,
  light_map.H_SEVEN,
  light_map.H_ELEVEN,
  light_map.H_FIVE,
  light_map.H_TEN,
  light_map.H_FOUR,
  light_map.H_TWO,
  light_map.H_EIGHT,
  light_map.H_TWELVE,
  light_map.OCLOCK,
  light_map.AM,
  light_map.PM,
]

def clear():
  for i in range(LED_COUNT):
    strip.setPixelColorRGB(i, 0, 0, 0)
  strip.show()

def Update(leds, cur_color):
  for led in leds:
    strip.setPixelColorRGB(led, cur_color[0], cur_color[1], cur_color[2])

clear()

prev = None

while(True):
  for word in ALL_WORDS:
    if prev:
      Update(prev.getLeds(), words.OFF)

    Update(word.getLeds(), words.WHITE)
    prev = word

    strip.show()

    time.sleep(.5)
