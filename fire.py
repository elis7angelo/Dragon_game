import pgzrun
import random
from pgzero.builtins import Actor, mouse, keyboard  #, animate

WIDTH = 1200
HEIGHT = 750

TITLE = "Dragon fight"
FPS = 30

#objects and variables
bg = Actor("bg.png")
dragon = Actor("red.png", (530, 370))
type1 = Actor("red.png", (400, 500))
type2 = Actor("blue.png", (900, 500))

enemies_l = []
enemies_r = []

fireballs = []
fireballs_r = []

balls = 0
new_balls = "0"

mode = "menu"

score = 0
new_score = "0"

type = 0
current_image = "l"

w = 0                   #for not shooting more than one fireball at a time

h_score = 0
new_h_score = "0"
en_count = 0
new_en_count = "0"

sucess = 0
n_sucess = "0"


#making the enemy list
def create_enemy():
    global en_count, new_en_count
    for i in range(3):
        x = random.randint(-450, -200)
        y = random.randint(100, 700)
        ran = random.randint(1, 2)
        if ran == 1:
            enemy = Actor("villain_1", (x,y))
        else:
            enemy = Actor("villain_2", (x,y))
        enemy.speed = random.randint(2,4)
        enemies_l.append(enemy)
        x = random.randint(1400, 1650)
        y = random.randint(100, 700)
        ran = random.randint(1, 2)
        if ran == 1:
            enemy = Actor("villain_1l", (x,y))
        else:
            enemy = Actor("villain_2l", (x,y))
        enemy.speed = random.randint(2,4)
        enemies_r.append(enemy)

create_enemy()

def draw():
    global score, screen
    if mode == "menu":
        bg.draw()
        type1.draw()
        type2.draw()
        screen.draw.text("Select your dragon", center = (650, 300), color = "greenyellow", gcolor = "green", fontsize = 40)
    elif mode == "game":
        bg.draw()
        dragon.draw()
        for i in range(len(enemies_l)):
            enemies_l[i].draw()
        for i in range(len(enemies_r)):
            enemies_r[i].draw()
        for i in range(len(fireballs)):
            fireballs[i].draw()
        for i in range(len(fireballs_r)):
            fireballs_r[i].draw()
        screen.draw.text(new_score, center = (25, 25), color = "green", gcolor = "forestgreen", fontsize = 42)
    elif mode == "end":
        bg.draw()
        screen.draw.text("GAME OVER", center = (600, 150), color = "greenyellow", gcolor = "green", fontsize = 70)
        screen.draw.text("to RESTART click R", center = (600, 630), color = "greenyellow", gcolor = "green", fontsize = 70)
        screen.draw.text(new_score, center = (25, 25), color = "green", gcolor = "forestgreen", fontsize = 42)
        screen.draw.text(f"current score: {new_score}", center = (600, 480), color = "greenyellow", gcolor = "green", fontsize = 60)
        screen.draw.text(f"highest score: {new_h_score}", center = (600, 350), color = "greenyellow", gcolor = "green", fontsize = 60)
        screen.draw.text(f"sucess rate: {n_sucess}%", center = (300, 250), color = "greenyellow", gcolor = "green", fontsize = 60)
        screen.draw.text(f"dodged {new_en_count} enemies", center = (900, 250), color = "greenyellow", gcolor = "green", fontsize = 60)

"""
# Controls
def on_mouse_move(pos):
    dragon.pos = pos
"""
    
#New enemy
def new_enemy_l():
    x = -80
    y = random.randint(100, 700)
    ran = random.randint(1, 2)
    if ran == 1:
        enemy = Actor("villain_1", (x,y))
    else:
        enemy = Actor("villain_2", (x,y))
    enemy.speed = random.randint(2,4)
    enemies_l.append(enemy)

def new_enemy_r():
    x = 1280
    y = random.randint(100, 700)
    ran = random.randint(1, 2)
    if ran == 1:
        enemy = Actor("villain_1l", (x,y))
    else:
        enemy = Actor("villain_2l", (x,y))
    enemy.speed = random.randint(2,4)
    enemies_r.append(enemy)

def create_fireball():
    global w, current_image, balls, new_balls
    if w ==0:
#        fireball = Actor("fire_1.png")
#       fireball.pos = dragon.pos
        if type == 0:
            if current_image == "l":
                fireball = Actor("fire_1.png")
                fireball.x = dragon.x - 90
                fireball.y = dragon.y + 15
                fireballs.append(fireball)
            else:
                fireball = Actor("fire_1r.png")
                fireball.x = dragon.x + 90
                fireball.y = dragon.y + 15
                fireballs_r.append(fireball)
        elif type == 1:
            if current_image == "l":
                fireball = Actor("fire_1.png")
                fireball.x = dragon.x - 100
                fireball.y = dragon.y + 30
                fireballs.append(fireball)
            else:
                fireball = Actor("fire_1r.png")
                fireball.x = dragon.x + 100
                fireball.y = dragon.y + 30
                fireballs_r.append(fireball)
        w = 1
        balls += 1
        new_balls = str(balls)

#Enemy movement
def enemy_move():
    global en_count, new_en_count
    for i in range(len(enemies_l)):
        if enemies_l[i].x < 1300:
            enemies_l[i].x += enemies_l[i].speed
        else:
            enemies_l.pop(i)
            en_count += 1
            new_en_count = str(en_count)
            new_enemy_l()
    
    for i in range(len(enemies_r)):
        if enemies_r[i].x > - 100:
            enemies_r[i].x -= enemies_r[i].speed
        else:
            enemies_r.pop(i)
            en_count += 1
            new_en_count = str(en_count)
            new_enemy_r()

#Controls
def collisions():
    global mode, score, new_score
    for i in range(len(enemies_l)):
        if dragon.colliderect(enemies_l[i]):
            mode = "end"
        #fireball collision
        for j in range(len(fireballs)):
            if fireballs[j].colliderect(enemies_l[i]):
                score += 1
                new_score = str(score)
                enemies_l.pop(i)
                fireballs.pop(j)
                new_enemy_l()
                break
        for h in range(len(fireballs_r)):
            if fireballs_r[h].colliderect(enemies_l[i]):
                score += 1
                new_score = str(score)
                enemies_l.pop(i)
                fireballs_r.pop(h)
                new_enemy_l()
                break

    for u in range(len(enemies_r)):
        if dragon.colliderect(enemies_r[u]):
            mode = "end"
        #fireball collision
        for j in range(len(fireballs)):
            if fireballs[j].colliderect(enemies_r[u]):
                score += 1
                new_score = str(score)
                enemies_r.pop(u)
                fireballs.pop(j)
                new_enemy_r()
                break

        for h in range(len(fireballs_r)):
            if fireballs_r[h].colliderect(enemies_r[u]):
                score += 1
                new_score = str(score)
                enemies_r.pop(u)
                fireballs_r.pop(h)
                new_enemy_r()
                break

#fireball movement
def fireball_move():
    for b in range(len(fireballs)):
        if fireballs[b].x < -20:
            fireballs.pop(b)
            break
        else:
            fireballs[b].x -= 10

    for q in range(len(fireballs_r)):
        if fireballs_r[q].x > 1220:
            fireballs_r.pop(q)
            break
        else:
            fireballs_r[q].x += 10

def update(dt):
    global current_image, w, dragon, type, mode, fireballs_r, fireballs, enemies_l, enemies_r, score, new_score, new_h_score, h_score
    global sucess, en_count, new_en_count, n_sucess, balls, new_balls
    if mode == "menu":
        if keyboard.left:
            dragon.image = "red.png"
            mode = "game"
            type = 0
        elif keyboard.right:
            dragon.image = "blue.png"
            mode = "game"
            type = 1
    if mode == "game":
        enemy_move()
        collisions()
        fireball_move()
        if keyboard.right or keyboard.d:
            if dragon.x < 1125:
                dragon.x += 7
                if current_image != "r":
                    if dragon.image == "red.png":
                        dragon.image = "red_r.png"
                        current_image = "r"
                    elif dragon.image == "blue.png":
                        dragon.image = "blue_r.png"
                        current_image = "r"

        if keyboard.left or keyboard.a:
            if dragon.x > 75:
                dragon.x -= 7
                if current_image != "l":
                    if dragon.image == "red_r.png":
                        dragon.image = "red.png"
                        current_image = "l"
                    elif dragon.image == "blue_r.png":
                        dragon.image = "blue.png"
                        current_image = "l"
        if keyboard.up or keyboard.w:
            if dragon.y > 75:
                dragon.y -= 7
        if keyboard.down or keyboard.s:
            if dragon.y < 675:
                dragon.y += 7
        
        if keyboard.space:
            create_fireball()
        else:
            w = 0
    if mode == "end":
        if score > h_score:
            new_h_score = str(score)
            h_score = score
        if balls == 0:
            sucess = 0
        else:
            sucess = round(score / balls * 100, 2)
        n_sucess = str(sucess)
        if keyboard.r:
            enemies_l = []
            enemies_r = []
            fireballs = []
            fireballs_r = []
            mode = "menu"
            score = 0
            new_score = "0"
            type = 0
            current_image = "l"
            w = 0
            en_count = 0
            new_en_count = "0"
            sucess = 0
            n_sucess = "0"
            balls = 0
            new_balls = "0"
            create_enemy()
            mode = "menu"
         

def on_mouse_down(button, pos):
    global mode, dragon, type

    if mode == "menu":
        if type1.collidepoint(pos):
            dragon.image = "red.png"
            mode = "game"
            type = 0
        elif type2.collidepoint(pos):
            dragon.image = "blue.png"
            mode = "game"
            type = 1

    if mode == "game" and button == mouse.LEFT:
        """fireball = Actor("fire_1.png")
#        fireball.pos = dragon.pos
        if type == 0:
            fireball.x = dragon.x - 90
            fireball.y = dragon.y + 15
        elif type == 1:
            fireball.x = dragon.x - 100
            fireball.y = dragon.y + 30
        fireballs.append(fireball)"""
        create_fireball()

pgzrun.go()