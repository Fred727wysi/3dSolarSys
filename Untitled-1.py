from ursina import *

app = Ursina()
player = Entity(model="saddam_hussein.glb", color=color.red, scale=10)
def update():
    player.x += held_keys["d"] * 0.1
    player.x -= held_keys["a"] * 0.1
    player.y += held_keys["w"] * 0.1
    player.y -= held_keys["s"] * 0.1
    player.rotation_x += held_keys["q"] * 5
    player.rotation_y += held_keys["r"] * 5

    
app.run()
