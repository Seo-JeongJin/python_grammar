
# 크게 세가지로 볼 수 있다
    # 1. pygame 초기화
    # 2. 이미지 생성 -> 무한 반복
    # while running:
        # 이미지 생성
        # 이벤트 처리: 어떤 키가 눌렸는지, 마우스 위치가 어디인지
        # while 문의 실행 간격 -> FPS
    # 3. 프로그램 종료

import pygame # 모듈을 가져옴
import random

# 1. pygame 초기화
pygame.init() # 파이게임 모듈을 쓰기 전 초기화 작업

screen = pygame.display.set_mode((640, 480)) # 작성하고자 하는 게임의 스크린 사이즈를 튜플 값으로 입력, 형식: (가로, 세로), 단위는 픽셀
clock = pygame.time.Clock()
running = True

x = 320
y = 240

# 2. 이미지 생성 -> 무한 반복
while running: # 러닝 한 번 반복 == 이미지 한 장 -> fps를 결정
        
    R = random.randrange(0, 255)
    G = random.randrange(0, 255)
    B = random.randrange(0, 255)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    
    # 이미지 생성    
    screen.fill((255, 255, 255)) # fill == 색상 주입(R, G, B)
    pygame.draw.circle(screen, (R, G, B), (x, y), 50)
    x += 1 # 한 번 반복할 때 마다 x값 1씩 증가, x축 양의 방향으로 이동
    pygame.display.flip() # flip == 화면에 이미지 출력, flip이 fill 보다 먼저 작성되면 의미가 없음
    clock.tick(60)
    
pygame.quit()