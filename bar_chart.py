import turtle

# Set variables
window_width = 500
window_height = 500
axis_length = 400
origin_x = window_width/2.5
origin_y = window_width/2.5

# data_points = turtle.numinput('Total count', 'How many data points?', minval=0, maxval=20)

# Set up the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("white")
t.speed(10)
t.width(3)

# Disable turtle animations
turtle.tracer(5)

# Set the window size
turtle.setup(window_width, window_height)

def create_triangle(deviation_angle=30, triangle_angle=120, distance=window_height/50):
    t.right(deviation_angle)
    t.begin_fill()
    for i in range(3):
        t.forward(distance)
        t.left(triangle_angle)
    t.end_fill()
    t.left(deviation_angle)

# Set turtle starting position
t.back(origin_x)
t.right(90)
t.back(origin_y)
t.color("black")
# Create y-axis triangle. Requires deviation_angle=30 (default)
create_triangle()
#Create L
t.forward(350)
t.left(90)
t.forward(350)
# Create x-axis triangle. Requires deviation_angle=210.
create_triangle(210)

# Show the drawing
turtle.done()