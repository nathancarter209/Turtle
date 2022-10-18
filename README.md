## Turtle

Hello, 
	
This is a normal Turtle Program with a heart and a "Hello" inside the heart.
 
 Yor are free to clone this code 
> git clone git@github.com:NathanCarter209/Turtle.git



```
import turtle
my_turtle_cursor = turtle.Turtle()
def pause():
    my_turtle_cursor.speed(20)
    for i in range(100):
        my_turtle_cursor.left(90)
```
In this part we initialise the Turtle (Download the Turtle from python packages or from Terminal (```pip install Turtle```).


```
def write_Hello_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(-50, 15)
    my_turtle_cursor.pencolor("Red")
    my_turtle_cursor.write("Hello", font=("Amatic SC", 74, "bold"))
```
In this part we insert the things we want to write inside the heart.
```
my_turtle_cursor.goto(-50, 15)
```
We need to setup the position of the text by X-axis and Y-axis.
Setup the pen color and setup what you want to write and the which fonts, size, font type you want to use for the perticular word.
```
def draw_complete_heart():
    my_turtle_cursor.left(140)
    my_turtle_cursor.forward(294)
    draw_left_curve_of_heart()
    my_turtle_cursor.right(190)
    draw_right_curve_of_heart()
    my_turtle_cursor.forward(294)
    my_turtle_cursor.end_fill()
```
This is the part where we complete the heart, basically this is the bottom part of the heart.

```
def draw_left_curve_of_heart():
    my_turtle_cursor.speed(50)
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)
```
As in this part we initialise a loop here for the left side of the heart, as we set up speed, angle of the turtle.
Same thing goes for the left side of the heart and then we are done
