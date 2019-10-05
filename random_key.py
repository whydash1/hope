from random import shuffle, randint
from string import ascii_letters, digits
import pygame #cmd 창에서 pip install pygame 명령 실행

abc = list(ascii_letters) + list(digits)
floor = 1
go_up = None
go_down = None
reset_it = None

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
pygame.init()
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
SKYBLUE = (80, 188, 233)
GRAY = (128, 128, 128)

size = [640, 360]
screen = pygame.display.set_mode(size)
done = False
pygame.display.set_caption("Hope")
fontObj = pygame.font.Font(None, 32)

while not done:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
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
            else:
                continue
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, [270, 50, 100, 150]) # 문 기본
    pygame.draw.rect(screen, BLACK, [270, 50, 100, 150], 4) #문 윤곽
    pygame.draw.rect(screen, GRAY, [270, 25, 100, 25]) #상단부
    pygame.draw.rect(screen, BLACK, [270, 25, 100, 25], 4) #상단부 윤곽
    pygame.draw.rect(screen, BLACK, [280, 29, 80, 18]) #전광판
    pygame.draw.line(screen, BLACK, [320, 50], [320, 200], 2) #문 가운데 선
    pygame.draw.rect(screen, SKYBLUE, [0, 200, 640, 160]) #바닥
    pygame.display.flip()

quit()
