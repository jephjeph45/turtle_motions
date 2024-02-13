from turtle import Turtle, Screen
# turtle is the module name
# Turtle is the class. The thing in the module
# * imports everything in the module
# Aliasing modules using as
# e.g. import turtle as t
#


tim = Turtle()

tim.shape('turtle')
tim.color('red')

# tim.fd(100)
# tim.rt(90)
# tim.fd(100)
# tim.rt(90)
# tim.fd(100)
# tim.rt(90)
# tim.fd(100)

# Drawing square
# for _ in range(4):
#     tim.fd(100)
#     tim.rt(90)


 # Drawing dash line
# tim.pos(1)

def draw_shape (num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    draw_shape (shape_side_n)




screen = Screen()
screen.exitonclick()
