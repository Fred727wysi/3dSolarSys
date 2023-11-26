from ursina import *
import numpy as np

app = Ursina()

sun = Entity(model="sphere", color=color.yellow, scale=1.5)

mercury = Entity(model="sphere", color=color.hex("#b8b8b8"), scale=0.1)
venus = Entity(model="sphere", color=color.hex("#f3a55f"), scale=0.2)
earth = Entity(model="sphere", color=color.hex("#2c75ff"), scale=0.3)
mars = Entity(model="sphere", color=color.hex("#ff5f45"), scale=0.25)
jupiter = Entity(model="sphere", color=color.hex("#d3b26b"), scale=0.5)
saturn = Entity(model="sphere", color=color.hex("#e0cfa0"), scale=0.45)
uranus = Entity(model="sphere", color=color.hex("#76c7f0"), scale=0.4)
neptune = Entity(model="sphere", color=color.hex("#3456db"), scale=0.38)
pluto = Entity(model="sphere", color=color.hex("#9b9b9b"), scale=0.08)

planet_entities = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

planet_names = {
    'mercury': 'Mercury',
    'venus': 'Venus',
    'earth': 'Earth',
    'mars': 'Mars',
    'jupiter': 'Jupiter',
    'saturn': 'Saturn',
    'uranus': 'Uranus',
    'neptune': 'Neptune',
    'pluto': 'Pluto',
}

for planet_entity in planet_entities:
    planet_name = next(key for key, value in locals().items() if value == planet_entity)
    if planet_name in planet_names:
        text = Text(parent=scene, text=planet_names[planet_name], position=planet_entity.position + Vec3(0, 0.5, 0), origin=(0, 0), scale=0.2, color=color.white)

t = -np.pi

def update():
    global t

    t += time.dt  # Use time.dt for frame-rate independence

    for planet_entity, scale_factor in zip(planet_entities, [0.1, 0.2, 0.3, 0.25, 0.5, 0.45, 0.4, 0.38, 0.08]):
        angle = np.pi * 40 / 180
        planet_entity.x = np.cos(t + angle) * scale_factor * 3  # Multiplied by 3 for better spacing
        planet_entity.z = np.sin(t + angle) * scale_factor * 3

app.run()
