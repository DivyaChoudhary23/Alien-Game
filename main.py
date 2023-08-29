from turtle import *
import time
import random
import math
import turtle


game = turtle.Screen()
game.title("Alien shooter")
game.bgcolor("black")
game.setup(width=600, height=800)
game.tracer(0)

player = turtle.Turtle()
player.speed(15)
player.shape("turtle")
player.color("White")
player.penup()
player.goto(0 , -250)

player.setheading(90)

bullets = []

aliens = []


for i in range(50):
    alien = turtle.Turtle()
    alien.speed(0)
    alien.shape("circle")
    alien.color("red")
    alien.penup()
    #alien.goto(random.randint(-290,290) , random.randint(290,1))
    alien.goto(random.randint(-290, 90), random.randint(100, 250))

    alien.speed_x = random.randint(1, 4)
    alien.speed_y = random.randint(1, 4)


    aliens.append(alien)


def fire_bullet():
    bullet = turtle.Turtle()

    bullet.shape("triangle")
    bullet.color("yellow")
    bullet.penup()
    bullet.goto(player.xcor(), player.ycor())
    bullet.setheading(90)
    bullet.speed = 10
    bullets.append(bullet)


def move_left():
    x = player.xcor()
    new_x = x - 20
    if new_x < -280:
        new_x = -280
    #player.setx(x)
    player.goto(new_x, player.ycor())


def move_right():
    x = player.xcor()
    new_x = x + 20
    if new_x > 280:
        new_x = 280
   # player.setx(x)

    player.goto(new_x, player.ycor())

game.listen()
game.onkeypress(move_left, "Left")
game.onkeypress(move_right, "Right")
game.onkeypress(fire_bullet, "space")

while True:
    time.sleep(0.1)
    game.update()
    if alien.ycor() == 0:
        alien.ycor() *= -1

    # Move aliens
    for alien in aliens:
        x = alien.xcor()
        y = alien.ycor()

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)

        alien.setx(x)
        alien.sety(y)

    distance = math.sqrt((player.xcor() - alien.xcor()) ** 2 + (player.ycor() - alien.ycor()) ** 2)
    if distance < 20:
        print("Game Over")
        time.sleep(0.01)
        player.hideturtle()
        alien.hideturtle()

        game.bye()

        # Check for collision with bullets
        for bullet in bullets:
            if bullet.ycor() > 275:
                bullet.hideturtle()
                bullets.remove(bullet)
            if bullet.distance(alien) < 20:
                bullet.hideturtle()
                bullets.remove(bullet)
                alien.goto(random.randint(-290, 290), random.randint(100, 250))

    for bullet in bullets:
        y = bullet.ycor()
        y += bullet.speed
        bullet.sety(y)


game.mainloop()
game.exitonclick()