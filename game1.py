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
        
        
        if event.type == pygame.KEYDOWN:            
            l = abs(850 - x)
            if 30< l < 45 :
                if event.key == pygame.K_UP:
                        dc = False
                        print("good")
            if l < 30 :
                if event.key == pygame.K_UP:
                        dc = False
                        print("great")


            if l > 45 :
                if event.key == pygame.K_UP:
                    print("fail")
            
                

    if dc == True:
        one = pygame.draw.circle(background, (255,0,255), (x,160), 35)
        x += 3
                      
                                                                                       
                 
    pygame.draw.circle(background, (0,0,255), (850,160), 40)
    pygame.display.update()

pygame.quit()
