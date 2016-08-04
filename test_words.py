from neopixel import *
import time
import words


LED_COUNT      = 102
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False



strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()


ALL_WORDS = [
  words.SUN,
  words.CLOUD,
  words.RAIN,
  words.STORM,
  words.WIND,
  words.M_HALF,
  words.M_TWENTY,
  words.M_FIVE,
  words.M_QUARTER,
  words.M_TEN,
  words.IT,
  words.PAST,
  words.IS,
  words.TO,
  words.H_ONE,
  words.H_SIX,
  words.H_NINE,
  words.H_THREE,
  words.H_SEVEN,
  words.H_ELEVEN,
  words.H_FIVE,
  words.H_TEN,
  words.H_FOUR,
  words.H_TWO,
  words.H_EIGHT,
  words.H_TWELVE,
  words.OCLOCK,
  words.AM,
  words.PM,
]

def Update(leds, cur_color):
  for led in leds:
    strip.setPixelColorRGB(led, cur_color[0], cur_color[1], cur_color[2])

prev = None

while(True):
  for word in ALL_WORDS:
    if prev:
      Update(prev.getLeds(), words.OFF)

    Update(word.getLeds(), words.WHITE)
    prev = word

    strip.show()

    time.sleep(.5)
