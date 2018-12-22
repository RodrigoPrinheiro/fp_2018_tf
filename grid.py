import pygame
from random import randint

#dimensoes
tileSize = 32
Width = 20
Height = 15

DIRT = 0
FLOWER = 1
WALL = 4
SAND = 3
#objetos de cenario
class Flower:
    def __init__(self):
        self.Image = pygame.image.load('./textures/plant.png')
        self.Pos = [randint(0, 640), randint(30, 448)] #tileSize * a posicao do tabuleiro x(1,20) y(2,14)

class extract:
    def __init__(self):
        self.Image = pygame.image.load('./textures/extract.png')
        self.Pos = [0, 1]


numFlowers = 250
flowers =[Flower() for x in range (numFlowers)]
Extraction = extract()

Textures = {
    'DIRT': pygame.image.load('./textures/dirt.png'), #0
    'WALL': pygame.image.load('./textures/wall.png'), #1
    'SAND': pygame.image.load('./textures/sand.png')  #2
    #adicionar o resto das texturas aqui
}
 

grid = [
    ['WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT', 'DIRT'],
    ['WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL', 'WALL']
]


#CONFIG

pygame.init()
fontScore = pygame.font.SysFont(None, 20)
pygame.display.set_caption('Monstro e Companhia DEV BUILD')
def score_board():
    pygame.draw.rect(screen, BLACK, [0,(Height-1)*tileSize, Width*tileSize, 50 ])
    
pygame.mouse.set_visible(False)

#SONS
pickupSound = pygame.mixer.Sound('./Sound/gold_pickup.wav')
digSound = pygame.mixer.Sound('./Sound/dig.wav')
dieSound = pygame.mixer.Sound('./Sound/die.wav')
winSong = pygame.mixer.Sound('./Sound/winSong.wav')
#ecra
screen = pygame.display.set_mode((Width*tileSize, Height*tileSize))
#cores
BLACK = (0, 0 ,0)
WHITE = (255, 255 ,255)
GREEN = (0, 102 , 0)
RED   = (204, 0 ,0)
ORANGE= (253, 106, 2)
GREY  = (128, 128, 128)
BLUE  = (0, 0, 204)
#outras cores....
