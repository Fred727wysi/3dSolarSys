from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
import numpy as np



def update(): 
    global t
    t=t+.02
    angle=np.pi*40/180
    radius_1=1

    mercury.x=np.cos(t)*radius_1
    mercury.z=np.sin(t)*radius_1

    radius_2=1.4
    venus.x=np.cos(t+angle)*radius_2
    venus.z=np.sin(t+angle)*radius_2

    radius_3=1.8
    earth.x=np.cos(t+angle*2)*radius_3
    earth.z=np.sin(t+angle*2)*radius_3

    radius_4=2.2 
    mars.x=np.cos(t+angle*3)*radius_4
    mars.z=np.sin(t+angle*3)*radius_4

    radius_5=2.6
    jupiter.x=np.cos(t+angle*4)*radius_5
    jupiter.z=np.sin(t+angle*4)*radius_5
   
    radius_6=3.0
    saturn.x=np.cos(t+angle*5)*radius_6
    saturn.z=np.sin(t+angle*5)*radius_6   

    radius_7=3.4
    uranus.x=np.cos(t+angle*6)*radius_7
    uranus.z=np.sin(t+angle*6)*radius_7

    radius_8= 3.7
    neptune.x=np.cos(t+angle*7)*radius_8
    neptune.z=np.sin(t+angle*7)*radius_8

    radius_9= 4
    pluto.x=np.cos(t+angle*8)*radius_9
    pluto.z=np.sin(t+angle*8)*radius_9


   

app = Ursina()
sun = Entity(model="sphere", color=color.yellow, scale=1.5)

mercury = Entity(model="sphere", color=color.hex("#b8b8b8"), scale=0.08)  
venus = Entity(model="sphere", color=color.hex("#f3a55f"), scale=0.15)
earth = Entity(model="sphere", color=color.hex("#2c75ff"), scale=0.2)
mars = Entity(model="sphere", color=color.hex("#ff5f45"), scale=0.14)
jupiter = Entity(model="sphere", color=color.hex("#d3b26b"), scale=0.3)
saturn = Entity(model="sphere", color=color.hex("#e0cfa0"), scale=0.27)
uranus = Entity(model="sphere", color=color.hex("#76c7f0"), scale=0.25)
neptune = Entity(model="sphere", color=color.hex("#3456db"), scale=0.24)
pluto = Entity(model="sphere", color=color.hex("#9b9b9b"), scale=0.05)




t=-np.pi
editor_camera = EditorCamera() #camera angle
editor_camera.ignore = False 
Entity(model=Grid(20,20), rotation_x=90, color=color.gray, y=-1, scale=20) #grid
app.run()