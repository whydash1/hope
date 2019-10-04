from random import shuffle, randint
from string import ascii_letters, digits
import pygame #cmd 창에서 pip install pygame 명령 실행
pygame.init()

abc = list(ascii_letters) + list(digits)
floor = 1
go_up = None
go_down = None
reset_it = None
font = pygame.font.Font('나눔명조',30)

def amugona():
    global go_up, go_down, reset_it
    shuffle(abc)
    go_up = str(abc[0])
    go_down = str(abc[1])
    reset_it = str(abc[2])

def floorup():
    global floor
    floor = floor + 1
    amugona()

def floordown():
    global floor
    floor = floor - 1
    amugona()

def reset():
    global floor
    floor = 1
    amugona()

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