# 3.6.4
from xml.etree import ElementTree

root = ElementTree.fromstring(input())

counters = {
    "red": 0,
    "green": 0,
    "blue": 0
}


def recurse(root: ElementTree.Element, level: int):
    color = root.attrib["color"]
    counters[color] += level
    for child in root:
        recurse(child, level+1)


recurse(root, 1)

print(counters["red"], counters["green"], counters["blue"])
