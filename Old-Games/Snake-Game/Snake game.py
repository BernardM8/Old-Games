import pygame
pygame.init()
from pygame.locals import *
import random
import time

#Screen/display settings
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake Game')
Largefont = pygame.font.SysFont("None",36)
Smallfont = pygame.font.SysFont("None",20)
GameOverText=Largefont.render("Game Over!", True, (255,255,0))

#Variables
Score=0
Delay_time=125
Direction="Start None"

#Snake Head to GUI
x=[400]
y=[300]
width = 10
height = 10
velocity=10


#Food random generator to GUI
def Food_Gen():
 Food_X=random.randrange(0, 800, 20)
 Food_Y=random.randrange(0, 600, 20)
 return Food_X, Food_Y


#Snake length extend
def snake_len(x, y):
 x.append(x)
 y.append(y)
 return x, y


def movement(x, y):
 global velocity
 for i in range(len(x)-1, 0, -1):
    x[i] = x[i - 1]
    y[i] = y[i - 1]
 if Direction=="Left":
    x[0] -= velocity
 if Direction=="Right":
    x[0] += velocity
 if Direction=="Down":
    y[0] += velocity
 if Direction=="Up":
    y[0] -= velocity


def collision(x,y):
 for i in range (2,len(x)):                       #check collision of snake body
   if x[0] == x[i] and y[0] == y[i]:
      gameDisplay.blit(GameOverText, (350, 300))
      pygame.display.update()
      time.sleep(5)
      return False
 if x[0]<0 or x[0]>800:                           #check collision of Xscreen boarder
  gameDisplay.blit(GameOverText,(350,300))
  pygame.display.update()
  time.sleep(5)
  return False
 if y[0]<0 or y[0]>600:                           #check collision of Yscreen boarder
  gameDisplay.blit(GameOverText,(350,300))
  pygame.display.update()
  time.sleep(5)
  return False
 else:
  return True


#Main Section
running = True
Food_X, Food_Y = Food_Gen()
while running:
 pygame.event.pump()
 keys = pygame.key.get_pressed()
 if (keys[K_LEFT]):
    Direction="Left"
 if (keys[K_RIGHT]):
    Direction="Right"
 if (keys[K_UP]):
    Direction="Up"
 if (keys[K_DOWN]):
    Direction="Down"
 if (keys[K_ESCAPE]):
    pygame.quit()
    running = False
 if x[0]==Food_X and y[0]==Food_Y:       #When the Food is intercepted
    x, y = snake_len(x, y)
    Score=Score+10
    Delay_time-=5
    Food_X, Food_Y = Food_Gen()

 pygame.display.update()
 movement(x,y)
 pygame.display.update()
 pygame.time.delay(Delay_time)
 running = collision(x,y)
 gameDisplay.fill((0,0,0))                                                   #Clear Screen
 for i in range (0,len(x)):
   pygame.draw.rect(gameDisplay,(255,0,0),(x[i], y[i], width, height))       #Display Snake
 pygame.draw.rect(gameDisplay,(52,55,235),(Food_X, Food_Y, width, height))   #Display Food

 ScoreText = Smallfont.render('Your score is ' + str(Score), True, (255, 255, 0))
 gameDisplay.blit(ScoreText, (650, 575))
 pygame.display.update()
 print(x,y)