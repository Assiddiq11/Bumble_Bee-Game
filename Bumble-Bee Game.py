import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False


bee = Actor("bee")
bee.pos = 200,200


flower = Actor("flower")
flower.pos = 200,300


def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score"+str(score),color="black",topleft = (10,10))
    if game_over:
        screen.fill("Blue")
        screen.draw.text("score"+str(score)) 

def place_flower():
    flower.x = randint(70,(WIDTH-70))
    flower.y = randint(70,(WIDTH-70))

def times_up():
    global game_over
    game_over = True

def update():
    global score 
    if keyboard.left:
        bee.x = bee.x - 2
        
    if keyboard.right:
        bee.x = bee.x + 2

    if keyboard.down:
        bee.y = bee.y + 2
    
    if keyboard.up:
        bee.y = bee.y - 2

    flower_collected = bee.colliderect(flower)

    if flower_collected:
        score = score + 10
        place_flower()
        
clock.schedule(times_up,60.0)

pgzrun.go()
        
    