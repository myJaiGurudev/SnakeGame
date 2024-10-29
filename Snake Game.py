import pygame
import random
import os
from sys import exit
pygame.mixer.init()
pygame.init()
bgimg=pygame.image.load("sna.jpg")
bgimg=pygame.transform.scale(bgimg, (1100, 700))
rd=(255,120,0)
white=(255, 255, 255)
gr=(255, 100, 150)
red=(255,0,0)
black=(0, 0, 0)
yellow=(255,200,0)

gameWindow=pygame.display.set_mode((900, 600))
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock=pygame.time.Clock()
fnt=pygame.font.SysFont("Algerian", 70)
font=pygame.font.SysFont("Algerian", 50)
fot=pygame.font.SysFont("Times New Roman", 70)
def textcreen(text, color, a, b):
    screen_text=fnt.render(text, True, color)
    gameWindow.blit(screen_text, [a,b])
def text_screen(text, color, a, b):
    screen_text=font.render(text, True, color)
    gameWindow.blit(screen_text, [a,b])
def textscreen(text, color, a, b):
    screen_text=fot.render(text, True, color)
    gameWindow.blit(screen_text, [a,b])
def plot_snake(gameWindow, color, s_list, size):
    for x,y in s_list:
        pygame.draw.circle(gameWindow, color, [x, y], size, 0)
def welcome():
    pygame.mixer.music.load('gamestart.mp3')
    pygame.mixer.music.play()
    exit_game=False
    while not exit_game:
        bgim=pygame.image.load("py.jpg")
        bgim=pygame.transform.scale(bgim, (1000, 600))
        gameWindow.blit(bgim, (-70, 0))
        text_screen("Made  By:  Anurag  Singh", yellow, 120, 530)
        text_screen("Jai Guru Dev", white, 280, 150)
        textcreen("Snake  Game !", rd, 200, 50)
        text_screen("Press  Space  Bar  To  Play.", red, 110, 450)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
            pygame.display.update()
            clock.tick(60)
def gameloop():
    pygame.mixer.music.load('back.mp3')
    pygame.mixer.music.play()
    exit_game=False
    game_over=False
    x=55
    y=90
    vel_x=0
    vel_y=0
    size=20
    fps=60
    init_vel=5
    food_x=random.randint(20, 400)
    food_y=random.randint(20, 250)
    score=0
    s_list=[]
    s_length=1
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
            hiscore=f.read()
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            bgim=pygame.image.load("pyi.jpg")
            bgim=pygame.transform.scale(bgim, (900, 600))
            gameWindow.blit(bgim, (0, 0))
            if score==int(hiscore):
                text_screen("Nice !  You  made  a  Hiscore :"+str(hiscore)+"", rd, 75, 100)
            textscreen("Score:"+str(score)+"   Hiscore:"+str(hiscore)+"", gr, 10, 10)
            textcreen("Game  Over !", red, 250, 240)
            textscreen("Press  enter  to  continue.", white, 100, 450)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        vel_x=init_vel
                        vel_y=0
                    if event.key==pygame.K_LEFT:
                        vel_x=-init_vel
                        vel_y=0
                    if event.key==pygame.K_UP:
                        vel_y=-init_vel
                        vel_x=0
                    if event.key==pygame.K_DOWN:
                        vel_y=init_vel
                        vel_x=0
                    if event.key==pygame.K_q:
                        score+=10
            x=x+vel_x
            y=y+vel_y
            if abs(x-food_x)<12 and abs(y-food_y)<12:
                score+=10
                food_x=random.randint(20, 400)
                food_y=random.randint(20, 250)
                s_length+=5
                if score>int(hiscore):
                    hiscore=score
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (-70, 0))
            text_screen("Score:"+str(score)+"   Hiscore:"+str(hiscore)+"", red, 5, 5)
            pygame.draw.circle(gameWindow, yellow, [food_x, food_y], size, size-7)
            
            head=[]
            head.append(x)
            head.append(y)
            s_list.append(head)
            if len(s_list)>s_length:
                del s_list[0]
            if head in s_list[: -1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if x<0 or x>900 or y<0 or y>600:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, white, s_list, size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    exit()
welcome()
