# Turtle
## This is a normal Turtle Program with a heart and a "Hello" inside the heart.
 
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
- In this part we initialise the Turtle 
> (Download the Turtle from python packages or from Terminal (```pip install Turtle```).
- The code starts by creating a turtle object and naming it my_turtle_cursor.
- The code then creates a function called pause() that will be used to pause the program for 10 seconds. After this, the code starts looping through 100 numbers from 0 to 99.
- This is done using range().
- For each number in the range, the left() method of my_turtle_cursor is executed with 90 degrees as an argument.
- The code will cause the turtle to move left 90 degrees, then right 90 degrees.
```
def write_Hello_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(-50, 15)
    my_turtle_cursor.pencolor("Red")
    my_turtle_cursor.write("Hello", font=("Amatic SC", 74, "bold"))
```
> Note : all the positions are depeneded on X-axis and Y-axis
- The code starts by declaring a variable called my_turtle_cursor.
- Next, it sets the pen colour to red and then writes "Hello" inside of a heart shape using the font Amatic SC with 74 points bolded.
- The code will draw a red heart on the turtle's screen and write "Hello" inside it.
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
- The code draws a heart on the screen.
- The code starts by drawing a left curve of the heart and then draws a right curve of the heart.
- Finally, it ends up filling in the shape with color.
- The first line moves my_turtle_cursor to 140 pixels to the left.hen, it moves my_turtle_cursor forward by 294 pixels so that it is positioned at position (294,140).
- Next, draw_left_curve_of_heart() is called which draws out one side of the heart's left curve using turtle graphics commands such as "forward" and "left".
- Afterwards, my_turtle-cursor moves back to its original position (294,140) before moving forward again by another 294 pixels so that it can draw out one side of the other side's right curve using turtle graphics commands such as "right" and "end fill".
- The code will draw a heart with the left and right curves of the heart on either side of the centre.
```
def draw_left_curve_of_heart():
    my_turtle_cursor.speed(50)
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)
```
- The code starts by setting the turtle's speed to 50.
- Then, it iterates through 450 times and moves the turtle 0.5 units to the right each time.
- It then moves 1.2 units forward for every iteration of this loop until it reaches 450 iterations, at which point it stops moving because there are no more iterations in the loop.
- The code starts by creating a variable called my_turtle_cursor that will be used as a reference point for drawing on screen later on in the program.
- The next line sets my_turtle_cursor's speed to 50 so that it can move quickly across the screen while drawing curves with ease (50 is an arbitrary number).
- Then, we create a for loop that goes through 450 times and increments my_turtle_cursor's position by 0.5 each time before incrementing its position again by 1.2 after every iteration of this loop until reaching 450 iterations whereupon we stop moving because there are no more iterations left in our for loop (450 is an arbitrary number).
- The code draws a left-curve of the heart.
- For the right side of the heart we did eaxctly the same thing but we changed the value and names as per the left side of the heart.

