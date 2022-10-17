import turtle
my_turtle_cursor = turtle.Turtle()
def pause():
    my_turtle_cursor.speed(20)
    for i in range(100):
        my_turtle_cursor.left(90)

def write_Nobo_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(-90, 15)
    my_turtle_cursor.pencolor("Red")
    my_turtle_cursor.write("Naba", font=("Amatic SC", 74, "bold"))

def write_Item_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(-30, 15)
    my_turtle_cursor.pencolor("Red")
    my_turtle_cursor.write("Item", font=("Amatic SC", 74, "bold"))

def draw_complete_heart():
    my_turtle_cursor.left(140)
    my_turtle_cursor.forward(294)
    draw_left_curve_of_heart()
    my_turtle_cursor.right(190)
    draw_right_curve_of_heart()
    my_turtle_cursor.forward(294)
    my_turtle_cursor.end_fill()

def draw_left_curve_of_heart():
    my_turtle_cursor.speed(50)
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)

def draw_right_curve_of_heart():
    my_turtle_cursor.speed(80)
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)

my_turtle_cursor.penup()

my_turtle_cursor.goto(0, -200)

my_turtle_cursor.pendown()

my_turtle_cursor.speed(70)

draw_complete_heart()

write_Nobo_inside_heart()
write_Item_inside_heart()

turtle.done()