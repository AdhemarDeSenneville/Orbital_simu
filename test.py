import math
from utils import proj_cart
import matplotlib.pyplot as plt

pres_step = 1/360*2*math.pi

class Orbite():
    def __init__(self,a,e,i,o,w,grafics_dico):
        self.a = a
        self.e = e
        self.i = i
        self.o = o
        self.w = w

        #Grafics Properties
        self.grafics = grafics_dico

    def get_points(self):
        point_list = []
        for v in range(0,2*math.pi,pres_step):
            point_list.append(proj_cart(self,v))
        return point_list

class Objet():
    def __init__(self,orbite,v):
        self.orbite = orbite
        self.v = v
        self.r = orbite.a*(1-orbite.e^2)/(1+orbite.e*math.cos(v))
    
    def get_point(self):
        return pres_step(self.orbite,self.v)

class Astre():
    def __init__():
        pass

class Systeme():
    def __init__():
        pass