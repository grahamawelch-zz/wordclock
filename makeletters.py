# coding=UTF-8


from xml.etree.ElementTree import QName, ElementTree, Element, SubElement, register_namespace
from sys import stdout, stderr


SAN_SERIF = 'sans-serif'
FONT = 'TC_Lasersans'
SIZE = '11'

SHOW_REC = False

REC_FILL = 'green' if SHOW_REC else 'white'
LET_FILL = 'white' if SHOW_REC else 'black'


# Numbers map to indices in special_tuple
rows = [
    "012345HALF",
    "TWENTYFIVE",
    "TENQUARTER",
    "ITPASTISTO",
    "ONESIXNINE",
    "THREESEVEN",
    "ELEVENFIVE",
    "TENFOURTWO",
    "EIGHTWELVE",
    "OCLOCK6789"]


# LETTER, SIZE, FONT
special_tuple = [
    ('☀', '8', FONT),        #'&#x2600',   # sun
    ('☁', '8', FONT),        #&#x2601',   # cloud
    ('☂', '8', FONT),        #&#x2602',   # umbrella
    ('❄', '8', FONT),        #&#x2744',   # snow flake
    ('🌪', '8', SAN_SERIF),        #&#x1F32A',   # Cloud with tornado
    ('⚡', '6', FONT),        #&#x26A1',   # lightning bolt
    ('XX', '6', FONT),       # XX
    ('GW', '6', FONT),       # GW
    ('AM', '6', FONT),       # AM
    ('PM', '6', FONT),       # PM
]

# More weather unicode at http://www.unicode.org/charts/PDF/U1F300.pdf
# Cyclone 🌀 &#x1F300
# Cloud with Tornado 🌪 &#x1F32A

# Cloud with Sun
# Cloud with Rain


class SVG(object):
    def __getattr__(self, name):
        def f(*children, **kwargs):
            qname = QName("http://www.w3.org/2000/svg", name)
            e = Element(qname, **kwargs)
            e.extend(children)
            return e
        return f


svg = SVG()


def NormalLetter(letter_x, letter_y, letter, font=FONT, size=SIZE):
    label = svg.text(
        x=letter_x,
        y=letter_y,
        fill=LET_FILL,
        attrib={
            "font-family": font,
            "font-size": size,
            "font-weight": "normal",
            "text-anchor": "middle",
            "alignment-baseline": "middle",
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
        size=tuple[1])


def BuildGrid():
    register_namespace('svg', "http://www.w3.org/2000/svg")

    root = svg.svg(
        # fill
        svg.rect(x="0", y="0", width="120", height="120", fill=REC_FILL),
        width="12in",
        height="12in",
        viewBox="0 0 120 120",
        version="1.1",
    );

    letters_elem = svg.g()

    x_off = 10
    y_off = 10

    x_inc = 10
    y_inc = 10

    x = 0
    y = 0

    for row in rows:
        for letter in row:
            px = (x * x_inc) + x_off
            py = (y * y_inc) + y_off

            sub = svg.g()

            letter_x = str(px + .5 * x_inc)
            letter_y = str(py + .5 * y_inc)

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
