import random
import math
import pygame



SCREEN_WIDTH = 800
SCREEN_HEIGHT =500
PLAYERSTART_X =370
PLAYERATART_Y =  380
ENEMYSTART_Y_MIN =50
ENEMYSTART_Y_MAX = 150
ENEMYSPEED_X_ =50
ENEMYSPEED_Y = 150
BULLET_SPEED_Y=10
COLLOSION_DISTANCE= 27


pygame.init()




screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


backround = pygame.image.load('background.png')



pygame.display.set_caption("Space invasion")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('player.png')
player_x = PLAYERSTART_X
player_y = PLAYERATART_Y
player_x_change = 0



enemyImg = []
enemy_x = []
enemy_x_change = []
enemy_y= []
enemy_y_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0,SCREEN_WIDTH - 64)) 
    enemy_y.append(random.randint(ENEMYSTART_Y_MIN,ENEMYSTART_Y_MAX))
    enemy_x_change.append(ENEMYSPEED_X_)
    enemy_y_change.append(ENEMYSPEED_Y)

bulletimg =pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = PLAYERATART_Y
bullet_X_change= 0
bullet_y_change= BULLET_SPEED_Y
bullet_state ="ready" 


score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
text_x = 10
text_y = 10


game_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


def game_over_text():
    over_text= game_font.render("game over",True,(255,255,255))
    screen.blit(over_text,(200,500))


def player(x,y):
    screen.blit(playerImg, (x,y))


def firebullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x,y))

def enemy (x,y,i):
    screen.blit(enemyImg[i],x,y)


def iscollision(enemyx,enemyy,bulletx, bullety):
    distance = maths.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return distance < COLLOSION_DISTANCE


running= True
while running:
    screen.fill((0,0,0))
    screen.blit(backround,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - 5
           
            if event.key == pygame.K_RIGHT:
                playerX_change =  5
    
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x= player_x
                firebullet(bullet_x,bullet_y)

        if  event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            player_x_change = 0
   
    
    player_x += player_x_change
    player_x = max(0, min(player_x,SCREEN_WIDTH - 64))


    for i in range(num_of_enemy):
        if enemy_y[i] > 340:
            for j in range(num_of_enemy ):
                enemy_y[j] = 2000

            game_over_text()
            break


        # need correction from here

            enemy_x[i] += enemyX_change[i]
            if enemy_x[i] <= 0 or enemy_x[i] >= SCREEN_WIDTH - 64:
                enemyX_change[i] *= -1
                enemy_y[i] += enemyY_change[i]

        # Collision Check
            if isCollision(enemy_x[i], enemy_y[i], bullet_x, bulletY):
                bulletY = PLAYERATART_Y
                bullet_state = "ready"
                score_value += 1
                enemy_x[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemy_y[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

            enemy(enemy_x[i], enemy_y[i], i)

    # Bullet Movement
    if bullet_y <= 0:
        bullet_y = PLAYERATART_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        firebullet(bullet_x, bulletY)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()

     