import pygame

pygame.init()

background = pygame.display.set_mode((551, 372))

fps = pygame.time.Clock()

image_ai = pygame.image.load("C:/Users/kimsoo/Pictures/제목 없음.png")
image_bg = pygame.image.load("C:/Users/kimsoo/Pictures/010.jpg")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_ai_width = background.get_rect().size[0]
size_ai_height = background.get_rect().size[1]


x_ai = size_bg_width/2 - size_ai_width/2
y_ai = size_bg_height - size_ai_height

to_x = 0
to_y = 0

a = 3
b = 0

play = True
while play:
    deltaTime = fps.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -a
            elif event.key == pygame.K_DOWN:
                to_y = a
            elif event.key == pygame.K_RIGHT:
                to_x = a
            elif event.key == pygame.K_LEFT:
                to_x = -a
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y = b
            elif event.key == pygame.K_DOWN:
                to_y = b
            elif event.key == pygame.K_RIGHT:
                to_x = b
            elif event.key == pygame.K_LEFT:
                to_x = b

    x_ai += to_x
    y_ai += to_y

    background.blit(image_bg, (0,0))
    background.blit(image_ai, (x_ai, y_ai)) #수정 사항
    pygame.display.update()
    
pygame.quit()