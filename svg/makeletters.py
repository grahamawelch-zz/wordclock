# coding=UTF-8


from xml.etree.ElementTree import QName, ElementTree, Element, SubElement, register_namespace
from sys import stdout, stderr

# https://erikflowers.github.io/weather-icons/
WEATHER = 'Weather Icons'

FONT = 'TC_Lasersans'
SIZE = '10'


def Move(x_i, y_i):
    def Custom(x, y):
        return (x + x_i, y + y_i)
    return Custom

def MoveZero():
    return Move(0, 0)


SHOW_REC = False

REC_FILL = 'green'
LET_FILL = 'black'


# Numbers map to indices in special_tuple
rows = [
    '012345HALF',
    'TWENTYFIVE',
    'QUARTERTEN',
    'ITPASTISTO',
    'ONESIXNINE',
    'THREESEVEN',
    'ELEVENFIVE',
    'TENFOURTWO',
    'EIGHTWELVE',
    'OCLOCKampm']


# LETTER, SIZE, FONT
special_tuple = [
    ('', '7', WEATHER, Move(0, -1)), # SUN f00d
    ('', '7', WEATHER, Move(0, -1)), # CLOUD f041
    ('', '7', WEATHER, Move(0, -2)), # RAIN f019 ALT: f01c (sprinkles), f04e (drops)
    ('', '7', WEATHER, Move(0, -2)), # STORM f01e ALT: f01d (storm shower)
    ('', '7', WEATHER, Move(0, -2)), # SNOW f01b
    ('', '7', WEATHER, Move(.65, -1)), # WIND f050 ALT: f011 (cloudy gusts)
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


def NormalLetter(letter_x, letter_y, letter, font=FONT, size=SIZE, Shift=MoveZero()):
    new_x, new_y = Shift(letter_x, letter_y)

    label = svg.text(
        x=str(new_x),
        y=str(new_y),
        fill=LET_FILL,
        attrib={
            'font-family': font,
            'font-size': size,
            'font-weight': 'normal',
            'text-anchor': 'middle',
            'alignment-baseline': 'middle',
        }
    )
    label.text = letter
    return label


def SpecialLetter(letter_x, letter_y, index):
    tuple = special_tuple[index]

    return NormalLetter(
        letter_x,
        letter_y,
        tuple[0].decode('utf-8'),
        font=tuple[2],
        size=tuple[1],
        Shift=tuple[3])


def BuildGrid():
    register_namespace('svg', 'http://www.w3.org/2000/svg')

    root = svg.svg(
        width='30cm',
        height='30cm',
        viewBox='0 0 120 120',
        version='1.1',
    );

    if (SHOW_REC):
        root.append(
            svg.rect(x='0', y='0', width='120', height='120', fill=REC_FILL))

    letters_elem = svg.g()

    x_off = 9.6
    y_off = 13.25

    x_inc = 10
    y_inc = 10

    x = 0
    y = 0

    for row in rows:
        for letter in row:
            px = (x * x_inc) + x_off
            py = (y * y_inc) + y_off

            sub = svg.g()

            letter_x = px + .5 * x_inc
            letter_y = py + .5 * y_inc

            rect = rect = svg.rect(
                x=str(px),
                y=str(py),
                width=str(x_inc),
                height=str(x_inc),
                fill='red',
                stroke='blue')

            label = None
            if letter.isdigit():
                label = SpecialLetter(letter_x, letter_y, int(letter))
            else:
                label = NormalLetter(letter_x, letter_y, letter)

            if SHOW_REC:
                sub.append(rect)

            sub.append(label)

            letters_elem.append(sub)

            x += 1
        x = 0
        y += 1

    root.append(letters_elem)

    tree = ElementTree(root)
    tree.write(stdout)


# Run everything
BuildGrid()
