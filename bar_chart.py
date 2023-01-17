import turtle

# Set variables
window_width = 500
window_height = 500
axis_length = 400
origin_x = window_width/2.5
origin_y = window_width/2.5

data_points_input = turtle.numinput('Total count', 'How many data points?', minval=0, maxval=20)

# Set up the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("white")
t.speed(10)
t.width(3)

# Disable turtle animations
# turtle.tracer(5)

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

def create_axis(data_points=6):
    for i in range(int(data_points + 1 )):
        if i == int(data_points + 1):
            break
        else:
            t.forward(axis_length/(data_points + 1 ))
            t.right(90)
            t.forward(axis_length/40)
            t.back(axis_length/40)
            t.left(90)

# Set turtle starting position
t.back(origin_x)
t.right(90)
t.back(origin_y)
t.color("black")

create_triangle() # Creates y-axis triangle. Requires deviation_angle=30 (default)
create_axis()
t.left(90)
create_axis(data_points_input)
###
# t.forward(axis_length)
###
# Create x-axis triangle. Requires deviation_angle=210.
create_triangle(210)
t.back(200)
# for d in range(int(data_points_input + 1)):
#     distance_back = axis_length / (data_points_input + 1)
#     if d==(data_points_input + 1):
#         break
#     t.back(distance_back)
#     t.right(90)
#     t.forward(axis_length/40)
#     t.back(axis_length/40)
#     t.left(90)
    

# Show the drawing
turtle.done()