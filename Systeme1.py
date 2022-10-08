from Classes import *

#Unité de longueur : 1000Km ~ 10^6m

Terre = Astre(r=6.371)

Lunar_Orbit = Orbite(a = 300,
                     e = 0.054,
                     i = 5.14/180*3.14,
                     o = 6.68/180*3.14,
                     w = 1.54/180*3.14)
Lune = Astre(r = 1.737)

Lunar_Gateway_Orbit = Orbite(a = 100,
                             e = 0.7,
                             i = 90/180*3.14,
                             o = 6.68/180*3.14,
                             w = 90/180*3.14)
Lunar_Gateway = Astre(r = 0.3)

Terre.add_orbit(Lunar_Orbit)
Lunar_Orbit.add_astres(Lune,0.3)
Lune.add_orbit(Lunar_Gateway_Orbit)
Lunar_Gateway_Orbit.add_astres(Lunar_Gateway,0.3)

print(Lunar_Gateway_Orbit.position[0],
       Lunar_Gateway_Orbit.position[1],
       Lunar_Gateway_Orbit.position[2] )

sys1 = Systeme(300,[Terre])
sys1.Affichage()