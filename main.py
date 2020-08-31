from render import Render, V2, V3

from obj import Obj

from texture import Texture

from shaders import gourad, outline, toon_mod, unlit, transparent, zBufferFade, normalMap

from utils import color

import random

width = 1920
height = 1076

r = Render(width, height)

r.light = V3(0,0,1)
# For background image
r.bk_texture = Texture('./models/background.bmp')
r.setBackground()

r.glColor(255,255,255)
# r.lookAt(posModel, V3(0,0,0))


r.active_shader = gourad


# horse model
r.active_shader = toon_mod
posModel = V3(0,-20,-40)
r.active_texture = Texture('./models/horse.bmp')
r.loadModel('./models/horse.obj', posModel, V3(0.05,0.05,0.05), V3(0,160,0))

r.active_shader = toon_mod
posModel = V3(-10,-20,-40)
r.active_texture = Texture('./models/horse.bmp')
r.loadModel('./models/horse.obj', posModel, V3(0.06,0.06,0.06), V3(0,-45,0))


# UFO
r.active_texture = unlit
posModel = V3(-20,10,-30)
r.active_texture = Texture('./models/UFO.bmp')
r.loadModel('./models/UFO.obj', posModel, V3(0.1,0.1,0.1), V3(20,30,20))


# pig model
r.active_shader = zBufferFade
posModel = V3(-18,0,-30)
r.active_texture = Texture('./models/pig.bmp')
r.loadModel('./models/pig.obj', posModel, V3(0.05,0.05,0.05), V3(0,160,-30))


# duck model
r.active_shader = outline
posModel = V3(-40,-25,-50)
r.active_texture = Texture('./models/pato.bmp')
r.loadModel('./models/pato.obj', posModel, V3(0.15,0.15,0.15), V3(-90,0,90))

posModel = V3(-35,-20,-50)
r.active_texture = Texture('./models/pato.bmp')
r.loadModel('./models/pato.obj', posModel, V3(0.09,0.09,0.09), V3(-90,0,55))

posModel = V3(-32,-23,-50)
r.active_texture = Texture('./models/pato.bmp')
r.loadModel('./models/pato.obj', posModel, V3(0.09,0.09,0.09), V3(-90,0,180))

posModel = V3(-30,-15,-50)
r.active_texture = Texture('./models/pato.bmp')
r.loadModel('./models/pato.obj', posModel, V3(0.09,0.09,0.09), V3(-90,0,0))

posModel = V3(-25,-23,-50)
r.active_texture = Texture('./models/pato.bmp')
r.loadModel('./models/pato.obj', posModel, V3(0.09,0.09,0.09), V3(-90,0,80))

# house model
r.active_texture = Texture('./models/house.bmp')
r.active_normalMap = Texture('./models/house_normal.bmp')
r.active_shader = normalMap
posModel = V3(120,-20,-200)
r.loadModel('./models/house.obj', posModel, V3(2,2,2), V3(0,90,0))
r.active_normalMap = None

# cone model
#for yellow color
r.transparency = 0.2
r.glColor(0,255,0)
r.active_shader = transparent
r.active_texture = None
posModel = V3(-20,6,-30)
r.loadModel('./models/cone.obj', posModel, V3(10,10,10), V3(0,0,20))



r.glFinish('output.bmp')

#para los tres canales de color r,g,b
# colorFinal = (colorCono * transparencia) + (colorAtras * (1 - transparencia)) 
