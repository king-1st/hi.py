import pygame

pygame.init()

background = pygame.display.set_mode((900, 320))
#pygame.display.set_caption("ABC")

fps = pygame.time.Clock()

x_pos = background.get_size()[0]//2
y_pos = background.get_size()[1]//2


play = True
dc = False
while play:
    deltaTime = fps.tick(300)
    background.fill((255,255,255))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
               dc = True
               x = 100
               #pygame.draw.circle(background, (255,0,255), (100,160), 35)
        
    if dc == True:
        one = pygame.draw.circle(background, (255,0,255), (x,160), 35)
        x += 3
        l = abs(850 - x)
        if l < 20 :
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                one = pygame.draw.circle(background, (255,255,255), (x,160), 35)
        

         
        
                
                 
    pygame.draw.circle(background, (0,0,255), (850,160), 40)
    pygame.display.update()
