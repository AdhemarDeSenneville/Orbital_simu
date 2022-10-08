from math import cos, sin
def proj_cart(orbite,v):
    a = orbite.a
    e = orbite.e
    i = orbite.i
    o = orbite.o
    w = orbite.w

    r = a*(1-e^2)/(1+e*cos(v))

    x = r*(cos(v+w)*cos(o)-sin(v+w)*sin(o)*cos(i))
    y = r*(cos(v+w)*sin(o)+sin(v+w)*cos(o)*cos(i))
    z = r*(sin(v+w)*sin(i))


    return [x,y,z]