import pygame

pygame.init()

background = pygame.display.set_mode((551, 372))

image_ai = pygame.image.load("C:/Users/kimsoo/Pictures/제목 없음.png")
image_bg = pygame.image.load("C:/Users/kimsoo/Pictures/010.jpg")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

background = pygame.display.set_mode(size_bg_height, size_bg_width)

size_ai_width = image_ai.get_rect().size[0]
size_ai_height = image_ai.get_rect().size[1]


x_ai = size_bg_width/2 - size_ai_width/2
y_ai = size_bg_height - size_ai_height

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    background.blit(image_bg, (0,0))
    background.blit(image_ai, (x_ai, y_ai))
    pygame.display.update()
    
pygame.quit()