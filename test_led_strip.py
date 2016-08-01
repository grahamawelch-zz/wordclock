from neopixel import *
import time


LED_COUNT      = 10
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False


RED = Color(255, 0, 0)
NO_COLOR = Color(0, 0, 0)


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()


def clear():
  for i in range(LED_COUNT):
    strip.setPixelColor(i, NO_COLOR)
  strip.show()

i = 0
while(True):
  clear()
  strip.setPixelColor(i, RED)
  strip.show()
  time.sleep(1)
  i += 1
  if i > LED_COUNT:
    i = 0
