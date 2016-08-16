
class Word:
  counter = 0

  def __init__(self, name, leds):
    self.name = name
    self.leds = leds
    self.id = Word.counter
    Word.counter += 1

  def __str__(self):
    return self.name

  def __lt__(self, other):
    return self.id - other.id

  def getLeds(self):
    return self.leds

  def isWeather(self):
    return False


class Weather(Word):
  def isWeather(self):
    return True


# Weather
SUN = Weather('SUN', [8])
CLOUD = Weather('CLOUD', [7])
RAIN = Weather('RAIN', [6])
STORM = Weather('STORM', [5])
SNOW = Weather('SNOW', [4])
WIND = Weather('WIND', [3])

# Minutes
M_HALF = Word('HALF', [0, 1, 2])
M_TWENTY = Word('TWENTY', [12, 13, 14, 15])
M_FIVE = Word('FIVE', [16, 17, 18, 19])
M_QUARTER = Word('QUARTER', [29, 28, 27, 26, 25])
M_TEN = Word('TEN', [24, 22]) # Also 23

# Transitions
IT = Word('IT', [33, 34])
PAST = Word('PAST', [35, 36, 37])
IS = Word('IS', [38])
TO = Word('TO', [39, 40])

# Hours
H_ONE = Word('ONE', [49, 47]) # Also 48
H_SIX = Word('SIX', [46, 45])
H_NINE = Word('NINE', [44, 43, 42])
H_THREE = Word('THREE', [51, 52, 53, 54])
H_SEVEN = Word('SEVEN', [55, 56, 57, 58])
H_ELEVEN = Word('ELEVEN', [68, 67, 66, 65, 64])
H_FIVE = Word('FIVE', [63, 62, 61])
H_TEN = Word('TEN', [70, 72])
H_FOUR = Word('FOUR', [73, 74, 75])
H_TWO = Word('TWO', [76, 77])
H_EIGHT = Word('EIGHT', [87, 86, 85, 84])
H_TWELVE = Word('TWELVE', [84, 83, 82, 81, 80])

# Other stuff
OCLOCK = Word('OCLOCK', [91, 92, 93, 94])
AM = Word('AM', [95, 96])
PM = Word('PM', [97, 98])
