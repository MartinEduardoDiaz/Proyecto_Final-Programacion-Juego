import pygame
import math as mt 
import config

class Weapon():
    def __init__(self,AD):
        self.AD = AD

    def attack(self,other):
        other.life -= self.AD
        if other.life <= 0:
            other.death()


class Sword(Weapon):
    def __init__(self, AD, x , y):
        super().__init__(AD)
        self.x = x
        self.y = y
        self.range = 50 
    

    def attack(self, other):
        distance = mt.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        if distance <= self.range:
            super().attack(other)

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.range, 1 )



class Arrow():
    def __init__(self, AD, x , y , mouse):
        self.AD = AD
        self.x = x 
        self.y = y
        self.active = True
        angle = mt.atan2(mouse[1] - self.y, mouse[0] - self.x)
        self.vx = mt.cos(angle) * 2.5 
        self.vy = mt.sin(angle) * 2.5

    def move(self):
        if self.active:
            self.x += self.vx
            self.y += self.vy
    
    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)
    
    
    
    



    def collision(self, enemy):
            distance = mt.sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2)
            return distance < 20  
    


class Bow(Weapon):
    def __init__(self, AD):
        super().__init__(AD)
        self.carcaj = []

    def shoot(self, x , y , mouse):
        arrow = Arrow(self.AD, x , y , mouse)
        self.carcaj.append(arrow)

    def draw(self, screen):
        for arrow in self.carcaj:
            arrow.draw(screen)
            arrow.move()

    def update_arrows(self, enemy):
        for arrow in self.carcaj:
            if arrow.collision(enemy):
                super().attack(enemy)
                print("ataque de arco")
        self.carcaj = [arrow for arrow in self.carcaj if arrow.active]

    
    






































 

