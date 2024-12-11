import pygame 
import random
from ui import Button

pygame.init()

def img_scale(image , scale):
    height = image.get_height()
    Width = image.get_width()
    img = pygame.transform.scale(image , (height * scale, Width * scale))
    return img



#configuracion de ventana
WIN_HEIGHT = 720
WIN_WIDTH = 1280

ICON = pygame.image.load("assets/UI/Icon_1.png")


#Menu background_
menubackgroundOptions = []
for i in  range(2):
       backgrounds_menu = pygame.image.load(f"assets/UI/Background_Menu_{i}.png") 
       menubackgroundOptions.append(backgrounds_menu)


Menu_background = random.choice(menubackgroundOptions)
image_scale = Menu_background.get_height() / Menu_background.get_width()
new_height = WIN_WIDTH * image_scale
Menu_background = pygame.transform.scale(Menu_background, (WIN_WIDTH, new_height)) 



#Buttons menu
button_pos = 150
button_text = ["Jugar", "Logros","Opciones", "Salir"]
buttons = []
for txt in button_text: 
    button = Button(button_pos,400 , 50, 200 , txt, txt, (26, 26, 26) , (45, 58, 69 ))
    button_pos += 250
    buttons.append(button)


#floor background
background = pygame.image.load("assets/images/backgrounds/Floor_01.jpeg")
image_scale = background.get_height() / background.get_width()
new_height = WIN_WIDTH * image_scale
background = pygame.transform.scale(background, (WIN_WIDTH, new_height)) 



#personaje 
pj_scale = 1.3
animations_movement = []
ruta = f"assets/images/characters/player/frame {i}.png"

for i in range(8): 
            img = pygame.image.load(f"assets/images/characters/player/frame {i}.png")
            img = img_scale(img , pj_scale)
            animations_movement.append(img)
animations_attack_sw = []

for i in range(5): 
            img = pygame.image.load(f"assets/images/characters/player/attackAnimations/attack_Sw/frame_{i}.png")
            img = img_scale(img , pj_scale)
            animations_attack_sw.append(img)



#Enemigos 
#slime  

slime_Scale = 0.05
SlimeAnimation = []
for i in range(4):
        im = pygame.image.load(f"assets/images/characters/enemies/slime/slime {i}.png")
        im = img_scale(im, slime_Scale)
        SlimeAnimation.append(im)

#goblin
orco  = []
for i in range(1,4):
        im = pygame.image.load(f"assets/images/characters/enemies/orco/Goblin ({i}).png")
        im = img_scale(im, 0.07)
        orco.append(im)        

#life
animationsLife = []
for i in range(6):
        img = pygame.image.load(f"assets/UI/frame {i}.png")
        img = img_scale(img, 0.04)
        animationsLife.append(img)






#arrow 
dagascale = 0.02
dagaAni =  []
for i in range(1,7):
        img = pygame.image.load(f"assets/images/items/Daga/daga ({i}).png")
        img = img_scale(img , dagascale)
        dagaAni.append(img)



"""

        """


button_pos_op = 250
options_text = ["Maximizar", "Silenciar" , "FPS"]
buttons_op = []
for txt in options_text: 
    button = Button(button_pos_op,400 , 50, 200 , txt, txt, (26, 26, 26) , (45, 58, 69 ))
    button_pos_op += 250
    buttons_op.append(button)



resetpos = 200
texts_reset = ["Reiniciar", "Salir", "ir al titulo"]
buttonsD  = []
for txt in texts_reset:
        button = Button(500,resetpos , 50, 200 , txt, txt, (26, 26, 26) , (45, 58, 69 ))
        resetpos += 100
        buttonsD.append(button)