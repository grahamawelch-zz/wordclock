
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
M_FIVE = Word('FIVE', [16, 17, 18])
M_QUARTER = Word('QUARTER', [28, 27, 26, 25, 24])
M_TEN = Word('TEN', [23, 22])

# Transitions
IT = Word('IT', [32, 33])
PAST = Word('PAST', [34, 35, 36])
IS = Word('IS', [37])
TO = Word('TO', [38, 39])

# Hours
H_ONE = Word('ONE', [49, 48])
H_SIX = Word('SIX', [47, 45])
H_NINE = Word('NINE', [44, 43, 42])
H_THREE = Word('THREE', [52, 53, 54, 55])
H_SEVEN = Word('SEVEN', [56, 57, 58, 59])
H_ELEVEN = Word('ELEVEN', [69, 68, 67, 66, 65])
H_FIVE = Word('FIVE', [64, 63, 62])
H_TEN = Word('TEN', [72, 73])
H_FOUR = Word('FOUR', [74, 75, 76])
H_TWO = Word('TWO', [77, 78, 79])
H_EIGHT = Word('EIGHT', [89, 88, 87, 86])
H_TWELVE = Word('TWELVE', [86, 85, 84, 83, 82])

# Other stuff
OCLOCK = Word('OCLOCK', [91, 92, 93, 94, 95])
AM = Word('AM', [96, 97])
PM = Word('PM', [98, 99])
