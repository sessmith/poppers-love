import turtle
import time

# --- Setup ---
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightblue")
screen.title("Bunny Kiss & Popper! ❤️")
turtle.hideturtle()  # Hide the default turtle icon

# --- Bunny Creation Function ---
def create_bunny(color, start_x, start_y):
    """Creates a turtle object representing a bunny."""
    bunny = turtle.Turtle()
    bunny.shape("circle")
    bunny.color(color)
    bunny.shapesize(stretch_wid=2, stretch_len=2)
    bunny.penup()
    bunny.goto(start_x, start_y)
    bunny.speed(0) # Max speed for instant movement
    return bunny

# --- Create the two bunnies ---
bunny_left = create_bunny("pink", -150, 0)
bunny_right = create_bunny("lightgray", 150, 0)

# --- The Kiss Animation ---
def perform_kiss():
    # 1. Bunny 2 moves (pops up) and kisses Bunny 1
    bunny_right.speed(1) # Slow down for animation
    bunny_right.goto(-50, 0)

    # 2. The "Kiss" effect (quick color change)
    bunny_left.color("red")
    bunny_right.color("red")
    screen.update()
    time.sleep(0.5)
    bunny_left.color("pink")
    bunny_right.color("lightgray")
    screen.update()

# --- Popper and Text Display ---
def shoot_popper():
    popper = turtle.Turtle()
    popper.hideturtle()
    popper.penup()
    popper.goto(0, -100) # Start below center

    # 1. Draw the "popper" shooting up
    popper.color("gold")
    popper.pensize(5)
    popper.pendown()
    popper.setheading(90) # Point up
    popper.speed(3)
    popper.forward(200) # Shoot up

    # 2. Display the message
    popper.penup()
    popper.goto(0, 150) # Position for text
    popper.color("purple")
    popper.write("I LOVE YOU!", align="center", font=("Comic Sans MS", 30, "bold"))

# --- Main sequence ---
time.sleep(1) # Pause before starting
perform_kiss()
shoot_popper()

# Keep the window open until manually closed
screen.mainloop()
