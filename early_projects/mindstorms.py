import turtle

star = turtle.Turtle()


def draw_square(some_turtle, x):
    for i in range(1, 5):
        some_turtle.forward(x)
        some_turtle.right(90)


def draw_circle(some_turtle, x):
    some_turtle.circle(x)


def draw_star(x, y):
    for i in range(5):
        x.forward(y)
        x.right(144)


def idea(y, x):
    star.color(str(y))
    draw_star(star, x)
    star.right(10)


def idea2(y, x):
    star.color(str(y))
    draw_circle(star, x)
    star.right(10)


def idea3(y, x):
    star.color(str(y))
    draw_square(star, x)
    star.right(10)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    # Create brad
    # PRETTY
    # brad = turtle.Turtle()
    # brad.color("white")
    # brad.speed(0)
    # for i in range(1, 37):
    #     draw_circle(brad)
    #     brad.right(10)
    #
    star.speed(0)
    x = 1
    for i in range(1, 30):
        idea2("yellow", x)
        x = x + 1
        idea2("orange", x)
        x = x + 1
        idea2("red", x)
        x = x + 1
        idea2("purple", x)
        x = x + 1
        idea2("blue", x)
        x = x + 1
        idea2("green", x)
        x = x + 1

    spiral = turtle.Turtle()
    spiral.color("white")
    spiral.speed(0)
    for i in range(36):
        spiral.forward(i * 15)
        spiral.right(144)

    # spiral.color("")
    #
    # x = 1
    # for i in range(1, 50):
    #     idea("yellow", x)
    #     x = x + 1
    #     idea("orange", x)
    #     x = x + 1
    #     idea("red", x)
    #     x = x + 1
    #     idea("purple", x)
    #     x = x + 1
    #     idea("blue", x)
    #     x = x + 1
    #     idea("green", x)
    #     x = x + 1

    # for i in range(1, 7):
    #     idea("yellow")
    #     idea("orange")
    #     idea("red")
    #     idea("purple")
    #     idea("blue")
    #     idea("green")
    #
    # for i in range(1, 7):
    #     idea2("yellow")
    #     idea2("orange")
    #     idea2("red")
    #     idea2("purple")
    #     idea2("blue")
    #     idea2("green")
    #
    star.color("")

    # Exit when clicked
    window.exitonclick()


draw_art()
