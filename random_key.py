from random import shuffle, randint
from string import ascii_lowercase, digits
import pygame #cmd 창에서 pip install pygame 명령 실행
pygame.init()

abc = list(ascii_lowercase) + list(digits)
floor = 1
font = pygame.font.Font('나눔명조',30)

shuffle(abc)
# 아래층, 1층, 위층
key1 = [str(abc[0]), str(abc[1]), None]
key2 = abc[2:4]
key3 = abc[5:7]
key4 = abc[8:10]
key5 = abc[11:13]
key6 = abc[14:16]
key7 = abc[17:19]
key8 = abc[20:22]
key9 = abc[23:25]
key10 = [None, None, None]

def floorup():
    global floor
    floor = floor + 1

def floordown():
    global floor
    floor = floor - 1

def reset():
    global floor
    floor = 1

#PyGame 함수 선언
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)

size = [640, 360]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock

pygame.display.set_caption("Hope")

while not done:
    clock.tick(30)  #FPS 설정
    if floor == 10:
        done = True
    #층수 확인 후 키 할당 명령어 필요
    for event in pygame.event.get(): #GUI 종료 시
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons= [pygame.key.name(k) for k,v in enumerate(pressed) if v]
            if buttons[0] == go_up:
                floorup()
            elif buttons[0] ==  go_down:
                floordown()
            elif buttons[0] == reset_it:
                reset()
    screen.fill(WHITE)
    #게임 코드 입력
    #그리기 입력
    pygame.display.flip()
