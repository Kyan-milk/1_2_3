#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
apple_image2 = "apple.gif"
apple_image3 = "apple.gif"
apple_image4 = "apple.gif"
apple_image5 = "apple.gif"

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(apple_image2)
wn.addshape(apple_image3)
wn.addshape(apple_image4)
wn.addshape(apple_image5)

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_apple2(active_apple):
  active_apple.shape(apple_image2)
  wn.update()

def draw_apple3(active_apple):
  active_apple.shape(apple_image3)
  wn.update()

def draw_apple4(active_apple):
  active_apple.shape(apple_image4)
  wn.update()

def draw_apple5(active_apple):
  active_apple.shape(apple_image5)
  wn.update()

def drop_apple():
  apple.penup()
  apple.goto(rand.randint(-200, 200),-200)

#-----function calls-----
wn.tracer(True)
draw_apple(apple)
draw_apple2(apple)
draw_apple3(apple)
draw_apple4(apple)
draw_apple5(apple)
wn.tracer(False)

wn.onkeypress(drop_apple, "space")

wn.listen()
wn.mainloop()