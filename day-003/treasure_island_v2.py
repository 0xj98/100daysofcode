import turtle

screen = turtle.Screen()
screen.title("Treasure Island")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

drawer = turtle.Turtle()
drawer.hideturtle()

def draw_path():
    drawer.penup()
    drawer.goto(0, 0)
    drawer.setheading(0)  # set direction to east/right
    drawer.pendown()

    # draw --- right path
    drawer.forward(100)
    drawer.write("Right", align="center", font=("Arial", 16, "normal"))

    # draw --- left path
    drawer.penup()
    drawer.goto(0, 0)
    drawer.setheading(180)  # set direction to west/left
    drawer.pendown()
    drawer.forward(100)
    drawer.write("Left", align="center", font=("Arial", 16, "normal"))

    drawer.hideturtle()


def go_left():
    drawer.clear()
    drawer.write("You chose left. Swim or wait?", align="center", font=("Arial", 16, "normal"))
    screen.onkey(swim, "s")
    screen.onkey(wait, "w")

def go_right():
    end_game("Fell into a hole. Game Over.")

def swim():
    end_game("Attacked by a trout. Game Over.")

def wait():
    drawer.clear()
    drawer.write("Choose a door: red (r), yellow (y), or blue (b)", align="center", font=("Arial", 16, "normal"))
    screen.onkey(red_door, "r")
    screen.onkey(yellow_door, "y")
    screen.onkey(blue_door, "b")

def red_door():
    end_game("Burned by fire. Game Over.")

def yellow_door():
    end_game("You Win!")

def blue_door():
    end_game("Eaten by beasts. Game Over.")

def end_game(message):
    drawer.clear()
    drawer.write(message, align="center", font=("Arial", 16, "normal"))
    # disable all keys and bindings used in the game as its now over
    screen.onkey(None, "l")
    screen.onkey(None, "r")
    screen.onkey(None, "s")
    screen.onkey(None, "w")
    screen.onkey(None, "r")
    screen.onkey(None, "y")
    screen.onkey(None, "b")

# draw intiial path
draw_path()

# kedyboard bindings
screen.listen()
screen.onkey(go_left, "l")
screen.onkey(go_right, "r")

# window loop
screen.mainloop()
