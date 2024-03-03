import sys

import pygame
from pygame.locals import QUIT
import random
from time import sleep
import os

#Map Generation -----------------------------------------------|
def generate_map(width, height,  frequency):
  map = [[0 for _ in range(width)] for _ in range(height)]
  for y in range(0, height, 3):
    for x in range(0, width, 3):
      map[y][x] = 1
      rand = random.randint(1,4)
      try:
        if rand == 1:
          map[y][x + 1] = 1
          map[y][x + 2] = 1
        elif rand == 2:
          map[y][x - 1] = 1
          map[y][x - 2] = 1
        elif rand == 3:
          map[y - 1][x] = 1
          map[y - 2][x] = 1
        elif rand == 4:
          map[y + 1][x] = 1
          map[y + 2][x] = 1
      except:
        pass

  print("Map generated")
  return add_border(add_doors(map, frequency))
  
def update_avatar(avatar, zoom, playerX, playerY):
  display.blit(avatar,((playerX-1)*(zoom+1),(playerY-1)*(zoom+1)))
  pygame.display.update()  
  
def print_map(map, zoom, avatar):
    display.fill((0,0,0))
    tiles = {
        0: pygame.image.load("ProceduralRoomGeneration/floor.png").convert(), 
        1: pygame.image.load("ProceduralRoomGeneration/wall.png").convert(),   
        2: pygame.image.load("ProceduralRoomGeneration/door_horizontal_left.png").convert(),     
        3: pygame.image.load("ProceduralRoomGeneration/door_horizontal_right.png").convert(),   
        4: pygame.image.load("ProceduralRoomGeneration/door_vertical_top.png").convert(),     
        5: pygame.image.load("ProceduralRoomGeneration/door_vertical_bottom.png").convert(),    
    }
    for row in range(len(map)):
        for cell in range(len(map[row])):
            display.blit(pygame.transform.scale(tiles[map[row][cell]],(zoom,zoom)), (cell*(zoom+1),row*(zoom+1)))
  
    update_avatar(avatar, zoom, 4, 4)
    pygame.display.update()

def add_doors(map, frequency):
  for y in range(len(map)):
    for x in range(len(map[y])):
      radius = {
         'center':map[y][x],
         'left':map[y][x - 1] if x > 0 else 0,
         'left2':map[y][x - 2] if x > 0 else 0,
         'right':map[y][x + 1] if x < len(map[0])-1 else 0,
         'right2':map[y][x + 2] if x < len(map[0])-2 else 0,
         'top':map[y - 1][x] if y > 0 else 0,
         'top2':map[y - 2][x] if y > 0 else 0,
         'bottom':map[y + 1][x] if y < len(map)-1 else 0,
         'bottom2':map[y + 2][x] if y < len(map)-2 else 0,
      }
      if random.randint(1,frequency) == 1:
        if radius['center'] == 0:
          if (radius['left'] == 1 and
              radius['right'] == 0 and
              radius['right2'] == 1 and

              radius['top'] == 0 and 
              radius['bottom'] == 0 and
              radius['top2'] == 0 and 
              radius['bottom2'] == 0):

            map[y][x] = 2
            map[y][x+1] = 3
          elif (radius['top'] == 1 and 
                radius['bottom'] == 0 and 
                radius['bottom2'] == 1 and 

                radius['right'] == 0 and 
                radius['left'] == 0 and
                radius['right2'] == 0 and 
                radius['left2'] == 0):

            map[y][x] = 4
            map[y+1][x] = 5

  return map

def add_border(map):
  for y in range(len(map)):
    map[y][0] = 1
    map[y][len(map[y]) - 1] = 1
  for x in range(len(map[0])):
    map[0][x] = 1
    map[len(map) - 1][x] = 1
  return map

#Map Generation -----------------------------------------------|

def player_view (x, y, map, distance):
  newmap = []
  for i in map[y-(distance+1):y+distance]:
    newmap.append(i[x-(distance+1):x+distance])
  return newmap


def game_init(width,length,name):
  pygame.init()
  global display 
  pygame.display.set_caption(name)
  display = pygame.display.set_mode((width,length))
  return display

def rotate(direction, angle, avatar):
  avatar = pygame.transform.rotate(avatar, -direction)
  angle -= direction
  if angle > 180:
    angle -= 360
  elif angle <= -180:
    angle += 360
  print(angle)
  return avatar, angle


  

def try_move(map, x, y, amount, angle, distance):
  direction_map = {
    180 : [0,-1],
    90 : [1,0],
    0 : [0,1],
    -90 : [-1,0],
  }
  
  for i in range(abs(amount)):
    if x <= distance:
      info = 'left'
    elif x > len(map[0]) - distance:
      info = 'right'
    elif y <= distance:
      info = 'top'
    elif y > len(map) - distance:
      info = 'bottom'
    elif map[y-1][x-1] == 1:
      info = 'wall'
    else:
      if amount > 0:
        x -= direction_map[angle][0]
        y -= direction_map[angle][1]
      elif amount < 0:
        x += direction_map[angle][0]
        y += direction_map[angle][1]
      info = 'worked'
    return x, y, player_view(x,y,map, distance), info
      