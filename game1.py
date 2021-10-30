import pygame
# 파이게임 시작
pygame.init()

background = pygame.display.set_mode((900, 320))
#pygame.display.set_caption("ABC")
#화면 설정

fps = pygame.time.Clock()
# 프레임 설정

x_pos = background.get_size()[0]//2
y_pos = background.get_size()[1]//2
#화면 중심 설정

play = True
# 게임을 켰을때
dc = False
# 구체가 안나왔을때
while play:
    deltaTime = fps.tick(300)
    #시간 조정으로 화면 속도 설정
    background.fill((255,255,255))
    #배경색 하얀색 설정
    for event in pygame.event.get(): 
    #발생 이벤트의 종류 확인    
        if event.type == pygame.QUIT:
        #게임 종료 설정
            play = False
            # 게임 꺼짐
        if event.type == pygame.MOUSEBUTTONDOWN:
        #마우스를 클릭했을때
            if event.button == 1:
            #좌클릭
               dc = True
               #구체가 나옴
               x = 100
               #구체의 시작 지점
               #pygame.draw.circle(background, (255,0,255), (100,160), 35)
        
        
        if event.type == pygame.KEYDOWN:
        #키보드 누를때 설정
            l = abs(850 - x)
            #구체와 나의 버튼판정 원 사이 거리
            if 10 < l < 45 :
            #구제와 나의 버튼판정 사이 거리가 10에서 45사이일때 
                if event.key == pygame.K_UP:
                #키보드 위쪽 키를 누르면
                        dc = False
                        #구체 사라짐
                        print("good")
                        # good 출력(리듬을 맞춤)
            if l < 10 :
            #사이 거리가 10아래일때        
                if event.key == pygame.K_UP:
                #키보드 위쪽 키를 누르면
                        dc = False
                        # 구체 사라짐
                        print("great")
                        #great 출력(리듬을 잘 맞춤)


            if l > 45 :
            #사이 거리가 45보다 크면
                if event.key == pygame.K_UP:
                #키보드 위쪽키를 누르면
                    print("fail")
                    #fail 츨력(리듬을 못맞춤)
            
                

    if dc == True:
    #구체가 나옴으로 설정되면
        one = pygame.draw.circle(background, (255,0,255), (x,160), 35)
        #구체의 처음 위치 설정
        x += 3
        #구체가 점점 x+ 방향으로 이동함
                      
                                                                                                       
    pygame.draw.circle(background, (0,0,255), (850,160), 40)
    #나의 리듬판정 원 위치 설정
    pygame.display.update()
    #디스플레이 작동
    

pygame.quit()
# 게임종료