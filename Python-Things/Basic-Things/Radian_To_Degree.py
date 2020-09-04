import math
from math import pi

def convert_to_degree():
    radians = float(input())
    print(math.floor(radians * 180 // math.pi))

convert_to_degree()