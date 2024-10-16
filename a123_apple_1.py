#a123_apple_1.py
import turtle as trtl

#setup
apple_image = "pear.gif"
background_image = "background.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.bgpic(background_image)
apple = trtl.Turtle()

#functions
#given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
#given a turtle, set that turtle to fall to the ground
def apple_fall(active_apple):
  xcor = active_apple.xcor()
  ycor = active_apple.ycor()
  active_apple.goto(xcor, ycor - 50)
#function calls
draw_apple(apple_image)

wn.mainloop()
