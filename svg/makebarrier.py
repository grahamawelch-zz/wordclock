from xml.etree.ElementTree import QName, ElementTree, Element, SubElement, register_namespace
from sys import stdout, stderr

# (Amt, Size)
RECTS = [
  (9, 10.5),
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
      width='11.5in',
      height='11.5in',
      version='1.1',
      viewBox = '0 0 11.5 11.5',
  )

  x_off = 0.1
  y_off = 0.1

  y_inc = 1

  x = 0
  y = 0

  for rect in RECTS:
    amt, size = rect

    while(amt > 0):

      if (x + x_off + size) > 11.2:
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
