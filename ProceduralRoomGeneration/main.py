from game import *  
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

display = game_init(800,800,'RoomGen')
map = generate_map(51, 51, 4)
zoom = 30
avatar = pygame.transform.scale(pygame.image.load("ProceduralRoomGeneration/avatar.png").convert_alpha(),(zoom,zoom))

distance = 4
angle = 180
x = 26
y = 26

print_map(player_view(x, y, map, distance), zoom, avatar)
while True:

  for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
  
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_UP]:
      print('up')
      x,y,view,info = try_move(map, x, y, -1, angle, distance)
      print_map(player_view(x, y, map, distance), 30, avatar)
      print(info)
      sleep(0.15)

      
  if keys[pygame.K_LEFT]:
      print('left')
      avatar, angle = rotate(-90, angle, avatar)
      print_map(player_view(x, y, map, distance), 30, avatar)
      sleep(0.15)

  
  if keys[pygame.K_DOWN]:
      print('down')
      x,y,view,info = try_move(map, x, y, -1, angle, distance)
      print_map(player_view(x, y, map, distance), 30, avatar)
      print(info)
      sleep(0.15)

  
  if keys[pygame.K_RIGHT]:
      print('right')
      avatar, angle = rotate(90, angle, avatar)
      print_map(player_view(x, y, map, distance), 30, avatar)
      sleep(0.15)

     
  pygame.event.pump()