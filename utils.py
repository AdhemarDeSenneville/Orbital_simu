from math import cos, sin

def proj_cart(orbite,v):
    a = orbite.a
    e = orbite.e
    i = orbite.i
    o = orbite.o
    w = orbite.w

    r = a*(1-e*e)/(1+e*cos(v))

    x = r*(cos(v+w)*cos(o)-sin(v+w)*sin(o)*cos(i)) + orbite.position[0]
    y = r*(cos(v+w)*sin(o)+sin(v+w)*cos(o)*cos(i)) + orbite.position[1]
    z = r*(sin(v+w)*sin(i))                        + orbite.position[2]


    return [x,y,z]

import matplotlib.pyplot as plt
import numpy as np
