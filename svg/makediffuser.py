from xml.etree.ElementTree import QName, ElementTree, Element, SubElement, register_namespace
from sys import stdout, stderr

# (Amt, Size)
RECTS = [
  (1, 2.6), # 1
  (6, 2.25), # 1
  (5, 4.6), # 2
  (5, 7), # 3
  (7, 9.25), # 4
  (3, 12), # 5
  (3, 14.5), # 6
  (1, 17.25), # 7
]


class SVG(object):
  def __getattr__(self, name):
    def f(*children, **kwargs):
      qname = QName('http://www.w3.org/2000/svg', name)
      e = Element(qname, **kwargs)
      e.extend(children)
      return e
    return f


svg = SVG()


def MakeRectangle(x, y, width, height):

  rect = svg.rect(
    x=str(x),
    y=str(y),
    width=str(width),
    height=str(height),
    style='stroke:black;fill:none;stroke-width:.01;'
  )

  return rect

def BuildDiffuser():
  register_namespace('svg', 'http://www.w3.org/2000/svg')

  root = svg.svg(
      width='30cm',
      height='30cm',
      viewBox = '0 0 30 30',
      version='1.1',
  )

  x_off = 0.5
  y_off = 0.5

  y_inc = 2.25

  x = 0
  y = 0

  for rect in RECTS:
    amt, size = rect

    while(amt > 0):

      if (x + x_off + size) > 27:
        # Go to the next line if we get too long
        x = 0
        y += 1

      px = x + x_off
      py = (y * y_inc) + y_off


      rect = MakeRectangle(px, py, size, y_inc)
      #print 'Rect %s of %s for size %s, (%s,%s)' % (i, amt, size, px, py)
      root.append(rect)

      amt -= 1

      x += size

  tree = ElementTree(root)
  tree.write(stdout)

#Run everything
BuildDiffuser()
