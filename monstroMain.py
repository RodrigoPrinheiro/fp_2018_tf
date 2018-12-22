import pygame, sys, random, math
from pygame.locals import *
from grid import *
from lib import Heroi, badThings, item

fps = 120
#funcoes
#Sprites eventos do jogador

def clock():
    currentTime = pygame.time.get_ticks()
    return currentTime

def drawText(text, font, surface, x, y, Color = WHITE):
    textobj = font.render(text, 1, Color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def die():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                die()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    die()
                if event.key == K_h:
                    return 1
                return 0
#setup
mainClock = pygame.time.Clock()
Player = Heroi.player()
playerSprite = Heroi.spritesheet('./textures/player/players.png', 32,1, 46, 32)
goblinSprite = Heroi.spritesheet('./textures/monstro.png',16,1, 27*2,16*2)
Player.Image = pygame.transform.scale(Player.Image, [32,46])
Player.Rect = Player.Image.get_rect()

pygame.time.set_timer(USEREVENT, 20) #TIMER PARA FAZER O MONSTRO MOVER
pygame.time.set_timer(USEREVENT + 1, 20) #TIMER PARA MOVIMENTO DO PROJETIL
Projetil = item.rock()
died = False
Won = False
done = False
nextFrame = clock()
frame = 0
Goblin = badThings.Monster() #instanciar a class monstro
Goblin.Imagem = pygame.transform.scale(Goblin.Imagem,[32*2,27*2]) #2* tamanho original

#INICIO, ECRA DE ENTRADA
screen.fill(BLACK)
drawText('GOLD DIG', fontScore, screen, 9 *tileSize, 2 *tileSize, ORANGE)
drawText('Press any key to start!', fontScore, screen, 8 *tileSize, 3 *tileSize)
drawText('Escava o terreno com o <ESPAÇO> e encontra os tesouros escondidos!', fontScore, screen, 15, (5)*tileSize)
drawText('Precisas de 5 tesouros para escapar.', fontScore, screen, 15, (5.55)*tileSize)
drawText('Tem cuidado para nao escavares por de cima dos poços ou o jogo termina.', fontScore, screen, 15, (6.10)*tileSize)
drawText('Se andares por cima de um poço tens um aviso por cima do Heroi.', fontScore, screen, 15, (6.65)*tileSize)
drawText('E ainda ha um monstro ganancioso...Ele só te quer roubar os tesouros.', fontScore, screen, 15, (7.20)*tileSize)
drawText('Apanha os tesouros do chão com a tecla <E> depois de os teres encontrado a todos.', fontScore, screen, 15, (7.75)*tileSize)
pygame.display.update()
waitForPlayerToPressKey()
goldCount = 0 #PARA EXPRIMENTAR GANHAR E SO MUDAR PARA 5
while True:
    died = Won = False
    Player.Rect.topleft = (1*tileSize, 1*tileSize)
    Goblin.Rect.bottomleft =(18*tileSize, 14*tileSize)
    moveL = moveR = moveU = moveD = dig = False
    fullInventory = warningMoreGold = False
    shoot = False
    #----------Main Loop-------------------
    while True:
        # --- Animacao ---
        Player.warningVisible = False
        if clock() >nextFrame:
                frame =(frame+1) % 8
                nextFrame += 80 #mudar o 80 se queremos a animacao mais rapida/lenta
        # --- Events ---
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                #ANDAR PARA CIMA
                if event.key == K_UP:
                    
                    moveU = True
                    moveD = moveL = moveR = False
                #ANDAR PARA BAIXO
                elif event.key == K_DOWN:
                    
                    moveD = True
                    moveU = moveR = moveL = False
                #ANDAR PARA A ESQUERDA
                elif event.key == K_LEFT:
                    
                    moveL = True
                    moveU = moveR =moveD = False
                #ANDAR PARA A DIREITA
                elif event.key == K_RIGHT:
                    
                    moveR = True
                    moveD = moveU = moveL = False
                #Espaco, escavar a terra
                elif event.key == K_SPACE:
                    moveD = moveU = moveL = moveR = False
                   
                elif event.key == K_e: #apanhar um Tesouro
                    moveD = moveU = moveL = moveR = False

                    for ouro in item.gold:
                        if int((Player.Rect.centery/tileSize)) == ouro.Pos[1] and int(Player.Rect.centerx/tileSize) == ouro.Pos[0] and ouro.Visible == True:
                            if goldCount < 5:
                                goldCount += 1
                                pickupSound.play()
                                item.gold.remove(ouro)
                            else:
                                fullInventory = True
                elif event.key == K_w:
                    shoot = True
                    Projetil.Rect.move_ip(Player.Rect.centerx,Player.Rect.centery)
                else:
                    moveD = moveU = moveL = moveR = False
                    Player.Image = 1*8 +5
            
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_DOWN:
                    moveD = False
                elif event.key == K_LEFT:
                    moveL = False
                elif event.key == K_UP:
                    moveU = False
                elif event.key == K_RIGHT:
                    moveR = False
                elif event.key == K_SPACE:
                    if grid[int((Player.Rect.centery/tileSize)+0.5)][int(Player.Rect.centerx/tileSize)] != 'SAND':
                        grid[int((Player.Rect.centery/tileSize)+0.5)][int(Player.Rect.centerx/tileSize)] = 'SAND'
                        digSound.play()
                    for ouro in item.gold:
                        if int((Player.Rect.centery/tileSize)+0.5) == ouro.Pos[1] and int(Player.Rect.centerx/tileSize) == ouro.Pos[0]:
                            ouro.Visible = True
                    for poço in badThings.Wells:
                        if int((Player.Rect.centery/tileSize) + 0.5) == poço.Pos[1] and int(Player.Rect.centerx/tileSize) == poço.Pos[0]:
                            poço.Visible = True
            

            if event.type == USEREVENT: #AI DO MONSTRO
                if Player.Rect.colliderect(Goblin.Rect) == True: #ROUBAR UM OURO
                    if goldCount > 0:
                        goldCount -= 1
                        Goblin.Rect.bottomleft =(18*tileSize, 14*tileSize)
                #MOVIMENTO
                if Player.Rect.centery > Goblin.Rect.centery:
                    Goblin.Rect.move_ip(0, 1*Goblin.Speed)
                if Player.Rect.centery < Goblin.Rect.centery:
                    Goblin.Rect.move_ip(0, -1*Goblin.Speed) 
                if Player.Rect.centerx > Goblin.Rect.centerx:
                    Goblin.imageIndex = 0*8 + frame
                    Goblin.Rect.move_ip(1*Goblin.Speed,0)
                if Player.Rect.centerx < Goblin.Rect.centerx:
                    Goblin.imageIndex = 1*8 + frame
                    Goblin.Rect.move_ip(-1*Goblin.Speed,0)
            elif event.type == (USEREVENT + 1): #FAZER MOVER O PROJETIL
               if shoot == True:
                    if Projetil.direction == 'U':
                        Projetil.Rect.move_ip(0, -1 * Projetil.Speed)
                    if Projetil.direction == 'D':
                        Projetil.Rect.move_ip(0, 1*Projetil.Speed)
                    if Projetil.direction == 'L':
                        Projetil.Rect.move_ip(-1*Projetil.Speed, 0)
                    if Projetil.direction == 'R':
                        Projetil.Rect.move_ip(Projetil.Speed, 0)
                    

        #MOVIMENTO PLAYER
        if moveU and Player.Rect.top > 15:
            Player.imageIndex = 3*8+frame
            Player.Rect.move_ip(0, -1 * Player.Speed)
            Projetil.direction = 'U'
        elif moveD and Player.Rect.bottom < (Height*tileSize) - 35:
            Player.imageIndex = 1*8+frame
            Player.Rect.move_ip(0, Player.Speed)
            Projetil.direction = 'D'
        elif moveL and Player.Rect.left > 5:
            Player.imageIndex =  2*8+frame
            Player.Rect.move_ip(-1*Player.Speed, 0)
            Projetil.direcition = 'L'
        elif moveR and Player.Rect.right < (Width*tileSize):
            Player.imageIndex = 0*8+frame
            Player.Rect.move_ip(Player.Speed, 0)
            Projetil.direction = 'R'
        else:
            Player.imageIndex = 1*8 +5
            Projetil.direction = Projetil.direction
       
        if goldCount <5:
            fullInventory = False
        else:
            fullInventory = True
        
        for poço in badThings.Wells:
            if int((Player.Rect.centery/tileSize) + 0.5) == poço.Pos[1] and int(Player.Rect.centerx/tileSize) == poço.Pos[0]:
                Player.warningVisible = True
 
        for poço in badThings.Wells:
            if int((Player.Rect.centery/tileSize) + 0.5) == poço.Pos[1] and int(Player.Rect.centerx/tileSize) == poço.Pos[0] and poço.Visible == True:
                died = True
                break
        if died == True: #acabar com o main loop
            break
        if fullInventory == True and int((Player.Rect.centery/tileSize) + 0.5) == Extraction.Pos[1] and int(Player.Rect.centerx/tileSize) == Extraction.Pos[0]: #condicao de ganhar
            Won = True
            break
        elif fullInventory == False and int((Player.Rect.centery/tileSize) + 0.5) == Extraction.Pos[1] and int(Player.Rect.centerx/tileSize) == Extraction.Pos[0]:
            warningMoreGold = True
  #    desenhar o mapa        
        for i in range(Height):
            for j in range(Width):
                screen.blit(Textures[grid[i][j]], (j*tileSize, i*tileSize))
                
        for flower in sorted(flowers, key = lambda t: t.Pos[1]):
            screen.blit(flower.Image, (flower.Pos[0], flower.Pos[1]))
        
        for ouro in sorted(item.gold, key =lambda o: o.Pos[1]):
            if ouro.Visible == True:
                screen.blit(ouro.Imagem,(ouro.Pos[0]*tileSize, ouro.Pos[1]*tileSize))
        
        for poço in sorted(badThings.Wells, key =lambda p: p.Pos[1]):
            if poço.Visible == True:
                screen.blit(poço.Imagem,(poço.Pos[0]*tileSize, poço.Pos[1]*tileSize))

        screen.blit(Extraction.Image, (Extraction.Pos[0],Extraction.Pos[1]))
  #inimigos/player/objetos depois daqui
        playerSprite.draw(screen, Player.imageIndex, Player.Rect.x, Player.Rect.y, 0)
        if Player.warningVisible == True: #blit do ponto de exclamacao de aviso
            screen.blit(Player.warningImage,(Player.Rect.left, Player.Rect.top - 25))
        goblinSprite.draw(screen, Goblin.imageIndex, Goblin.Rect.x, Goblin.Rect.y, 0)
        #screen.blit(Projetil.Imagem,Projetil.Rect)
  #UI
        score_board()
        drawText('Gold Bags: '+ str(goldCount) +' ', fontScore, screen, 15, (Height-0.75)*tileSize)
        if fullInventory == True:
            drawText('You cannot carry more Gold!', fontScore, screen, 3.5*tileSize, (Height-0.75)*tileSize)
        elif warningMoreGold == True:
            drawText('You need 5 Gold Bags to Leave!', fontScore, screen, 3.5*tileSize, (Height-0.75)*tileSize)
        drawText('Press E to pick up Gold and SPACE to dig', fontScore, screen, 15, (Height-1.75)*tileSize, BLACK)
        pygame.display.update()
        mainClock.tick(fps)
  
  #gameover screen
    screen.fill(BLACK)
    if died == True:
        drawText('You died', fontScore, screen, 9 *tileSize, 7 *tileSize)
        drawText('Press any key to try again!', fontScore, screen, 7 *tileSize, 8*tileSize)
        dieSound.play()
    if Won == True:
        winSong.play()
        drawText('You Won!!', fontScore, screen, 9 *tileSize, 7 *tileSize)
        drawText('You retrieved the 5 hidden Sacks of Gold!!', fontScore, screen, 6 *tileSize, 8*tileSize)
        pygame.display.update()
        waitForPlayerToPressKey()
        die()
    pygame.display.update()
    waitForPlayerToPressKey()
  
