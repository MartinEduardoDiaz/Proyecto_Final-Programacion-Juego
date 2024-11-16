import pygame 
import random
from buttons import Button


"""
ARCHIVO DE CONFIGURACIONES GENERALES 
-window size
"""



#funcion para escalar imagenes a un porcentaje
def img_scale(image , scale):
    height = image.get_height()
    Width = image.get_width()
    img = pygame.transform.scale(image , (height * scale, Width * scale))
    return img

#configuracion de ventana
WIN_HEIGHT = 1280
WIN_WIDTH = 720 
ICON = pygame.image.load("assets/UI/Icon_1.png")



#Menu background_
menubackgroundOptions = []
for i in  range(2):
       backgrounds_menu = pygame.image.load(f"assets/UI/Background_Menu_{i}.png") 
       menubackgroundOptions.append(backgrounds_menu)
Menu_background = random.choice(menubackgroundOptions)
image_scale = Menu_background.get_height() / Menu_background.get_width()
new_height = WIN_HEIGHT * image_scale
Menu_background = pygame.transform.scale(Menu_background, (WIN_HEIGHT, new_height)) 


#Buttons menu
button_pos = 150
button_text = ["Jugar", "Logros","Opciones", "Salir"]
buttons = []
for txt in button_text: 
    button = Button(button_pos,400 , 50, 200 , txt, txt)
    button_pos += 250
    buttons.append(button)


#floor background
background = pygame.image.load("assets/images/backgrounds/Floor_01.jpeg")
image_scale = background.get_height() / background.get_width()
new_height = WIN_HEIGHT * image_scale
background = pygame.transform.scale(background, (WIN_HEIGHT, new_height)) 



#personaje 
pj_scale = 1.3
animations = []
for x in range(8): 
            img = pygame.image.load(f"assets/images/characters/player/frame {x}.png")
            img = img_scale(img , pj_scale)
            animations.append(img)
        




















