import turtle
import random
import math

from tkinter import Tk, simpledialog, messagebox

root = Tk()
root.withdraw()

# Ask for number of options
n = simpledialog.askinteger(
    "Random Guesser",
    "How many options? (2-18)",
    minvalue=2,
    maxvalue=18
)

if n is None:
    quit()

# Create options list
options = []

for i in range(n):
    option = simpledialog.askstring(
        "Option",
        f"Enter option #{i+1}"
    )

    if not option:
        option = f"Option {i+1}"

    options.append(option)

# More colors
colors = [
    "#FF595E",
    "#FF924C",
    "#FFCA3A",
    "#8AC926",
    "#52A675",
    "#1982C4",
    "#4267AC",
    "#6A4C93",
    "#C77DFF",
    "#F15BB5",
    "#00BBF9",
    "#00F5D4",
    "#9B5DE5",
    "#F72585",
    "#4CC9F0",
    "#7209B7",
    "#43AA8B",
    "#F8961E"
]
if n <= 6:
    radius = 220
elif n <= 12:
    radius = 200
else:
    radius = 180
rotation = 0
spinning = False

# -----------------
# SCREEN
# -----------------

screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("white")
screen.title("Random Guesser Wheel")

wheel = turtle.Turtle()
wheel.hideturtle()
wheel.speed(0)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# -----------------
# DRAW POINTER
# -----------------

pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()
pointer.goto(0, radius + 20)

pointer.color("black")
pointer.begin_fill()
pointer.goto(-15, radius + 50)
pointer.goto(15, radius + 50)
pointer.goto(0, radius + 20)
pointer.end_fill()

# -----------------
# DRAW WHEEL
# -----------------

def draw_wheel(angle_offset=0):

    wheel.clear()

    n = len(options)
    angle_size = 360 / n

    for i in range(n):

        start = i * angle_size + angle_offset

        wheel.penup()
        wheel.goto(0, 0)

        wheel.setheading(start)

        wheel.color("black", colors[i % len(colors)])

        wheel.begin_fill()

        wheel.pendown()
        wheel.forward(radius)

        wheel.left(90)

        wheel.circle(radius, angle_size)

        wheel.goto(0, 0)

        wheel.end_fill()

        # text position
        middle = start + angle_size / 2

        x = math.cos(math.radians(middle)) * radius * 0.6
        y = math.sin(math.radians(middle)) * radius * 0.6

        wheel.penup()
        wheel.goto(x, y)

        wheel.write(
            options[i],
            align="center",
            font=("Arial", 12, "bold")
        )

# -----------------
# FIND WINNER
# -----------------

def get_winner():

    n = len(options)
    angle_size = 360 / n

    pointer_angle = (90 - rotation) % 360

    index = int(pointer_angle // angle_size)

    return options[index]

# -----------------
# SPIN
# -----------------

def spin():

    global rotation
    global spinning

    if spinning:
        return

    spinning = True

    speed = random.randint(20, 30)

    while speed > 0.2:

        rotation += speed

        draw_wheel(rotation)

        screen.update()

        speed *= 0.97

    winner = get_winner()

    writer.clear()
    writer.goto(0, -280)

    writer.write(
        f"Winner: {winner}",
        align="center",
        font=("Arial", 24, "bold")
    )

    spinning = False

# -----------------
# START
# -----------------

screen.tracer(0)

draw_wheel()

writer.goto(0, -280)
writer.write(
    "Press SPACE to spin",
    align="center",
    font=("Arial", 18, "bold")
)

screen.listen()
screen.onkey(spin, "space")

screen.mainloop()
