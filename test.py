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

    def affichage(self):
        plt.3Dplot(self.get_points(),
                    self.grafics["color"])

class Objet():
    def __init__(self,orbite,v,grafics_dico):
        self.orbite = orbite
        self.v = v
        self.r = orbite.a*(1-orbite.e^2)/(1+orbite.e*math.cos(v))

        self.grafics = grafics_dico
    
    def get_point(self):
        return pres_step(self.orbite,self.v)
    
    def affichage(self):
        plt.3Dplot(self.get_point(),
                    self.grafics["color"])

class Astre():
    def __init__(self,x=0,y=0,z=0,grafics_dico=None):
        self.position = [x,y,z]
        self.grafics_dico
        pass

    def affichage(self.color):
        plt.3Dplot(self.position,self.grafics_dico[color])

class Systeme():
    def __init__():
        pass