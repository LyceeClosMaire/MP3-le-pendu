import pygame
from pygame import *

mixer.init()
pygame.init()

mixer.music.load("menujeu.mp3")
mixer.music.play()

blanc = (255,255,255)
font = pygame.font.Font('BradBunR.ttf',180)
font1 = pygame.font.Font('BradBunR.ttf',55)
font2 = pygame.font.Font('BradBunR.ttf',180)
font3 = pygame.font.Font('BradBunR.ttf',100)
font4 = pygame.font.Font('BradBunR.ttf',100)
font5 = pygame.font.Font('BradBunR.ttf',100)

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("pendu")

bg = pygame.image.load('imagefond.jpg')
bg2 = pygame.image.load('menufond2.jpg')
screen.blit(bg,[0,0])

def accueil():
    Gt = font.render("PENDU",1,blanc)
    Pt = font1.render("Appuyer sur espace pour continuer",1,blanc)
    screen.blit(Gt,(200,-50))
    screen.blit(Pt,(40,500))

def main():
    Gt1 = font2.render("Main",1,blanc)
    Pt1 = font3.render("Easy",1,blanc)
    Pt2 = font4.render("Medium",1,blanc)
    Pt3 = font5.render("Hard",1,blanc)
    screen.blit(bg2,[0,0])
    screen.blit(Gt1,(250,-50))
    screen.blit(Pt1,(50,250))
    screen.blit(Pt2,(50, 350))
    screen.blit(Pt3,(50, 450))

continuer = 1
partie = 'intro'

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
        if partie == 'intro' and event.type == pygame.KEYDOWN and event.key == K_SPACE:
            partie = 'menu'

    if partie == 'intro':
        accueil()
    elif partie == 'menu':
        main()

    pygame.display.flip()



pygame.quit()
quit()