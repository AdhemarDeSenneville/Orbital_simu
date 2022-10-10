import math
from utils import proj_cart
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
pres_num = 50

pas = 10

class Orbite():
    def __init__(self,a,e,i,o,w,grafics_dico=None):
        self.position = [0,0,0]
        self.a = a
        self.e = e
        self.i = i
        self.o = o
        self.w = w

        #Grafics Properties
        self.grafics = grafics_dico

        self.ax = None
        self.astres = []

    def get_points(self):
        point_list = []
        for v in np.linspace(0, 2*math.pi, num=pres_num):
            point_list.append(proj_cart(self,v))
        return np.array(point_list)

    def affichage(self):
        data = self.get_points()
        self.ax.plot3D(data[:,0],data[:,1],data[:,2],'b')

        for i in self.astres:
            i.affichage()
    
    def add_ax(self,ax):
        self.ax = ax
        for i in self.astres:
            i.add_ax(ax)
    
    def add_astres(self,astre,v):
        astre.v = v
        astre.position = proj_cart(self,v)
        self.astres.append(astre)

    def maj(self):
        for i in self.astres:
            new_v = self.anomalie_update(i.v)
            i.position = proj_cart(self,new_v)
            i.maj()
    
    @classmethod
    def anomalie_update(self,v):
        return v+0.3

class Objet():
    def __init__(self,orbite,v,grafics_dico):
        self.orbite = orbite
        self.v = v
        self.r = orbite.a*(1-orbite.e^2)/(1+orbite.e*math.cos(v))

        self.grafics = grafics_dico
        self.ax = None
    
    def get_point(self):
        return proj_cart(self.orbite,self.v)
    
    def affichage(self):
        data = self.get_points()
        self.ax.scatter3D(data[0],data[1],data[2],'r*') # ,self.grafics["color"]
                
    def add_ax(self,ax):
        self.ax = ax

class Astre():
    def __init__(self,r=1,x=0,y=0,z=0,grafics_dico=None):
        self.position = [x,y,z]
        self.r = r
        self.grafics_dico = grafics_dico
        self.v = None

        self.ax = None
        self.orbits = []

    def affichage(self):
        u, v = np.mgrid[0:2 * np.pi:15j, 0:np.pi:10j]
        x = self.r*np.cos(u) * np.sin(v) + self.position[0]
        y = self.r*np.sin(u) * np.sin(v) + self.position[1]
        z = self.r*np.cos(v)             + self.position[2]
        #self.ax.plot_surface(x, y, z)
        self.ax.plot_surface(x, y, z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')

        for i in self.orbits:
            i.affichage()

    def add_ax(self,ax):
        self.ax = ax
        for i in self.orbits:
            i.add_ax(ax)
    
    def add_orbit(self,orbit):
        orbit.position = self.position
        self.orbits.append(orbit)

    def maj(self):
        for i in self.orbits:
            i.position = self.position
            i.maj()
    
class Systeme():
    def __init__(self,size,list_systeme):
        plt.style.use('dark_background')
        plt.rcParams["figure.figsize"] = [15, 8]
        plt.rcParams["figure.autolayout"] = True
        self.list_systems = list_systeme
        self.fig = None
        self.ax = None
        self.size = size
        self.init_axes(True)
        
        

    def init_axes(self,first = False):
        if first:
            self.fig = plt.figure()
            self.ax = plt.axes(projection='3d')
            self.fig.set_facecolor('black')
            self.ax.set_box_aspect([1,1,1])
            self.ax.set_xlim3d(-self.size, self.size)
            self.ax.set_ylim3d(-self.size, self.size)
            self.ax.set_zlim3d(-self.size, self.size)
            self.ax.grid(False)
            #self.ax.set_xticks([])
            #self.ax.set_yticks([])
            #self.ax.set_zticks([])
            self.ax.w_xaxis.pane.fill = False
            self.ax.w_yaxis.pane.fill = False
            self.ax.w_zaxis.pane.fill = False
            self.ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
            self.ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
            self.ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        else:
            self.ax.clear()

        for i in self.list_systems:
            i.add_ax(self.ax)

    def affichage(self,first = False):
        
        for i in self.list_systems:
            i.affichage()
        
        if first:
            plt.show()
    
    def maj(self):

        for i in self.list_systems:
            i.maj()
    
    def simulate(self):

        
        a = anim.FuncAnimation(self.fig, self.update, frames=7, repeat=False)
        plt.show()

    def update(self,i):

        self.init_axes()
        self.maj()
        self.affichage()

