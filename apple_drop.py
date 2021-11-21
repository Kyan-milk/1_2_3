#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()

all_apples = [apple,apple2,apple3,apple4,apple5]
letters=["a","b","c","d","e"]

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(apple):
  apple.shape(apple_image)
  apple2.shape(apple_image)
  apple3.shape(apple_image)
  apple4.shape(apple_image)
  apple5.shape(apple_image)
  wn.update()

def drop_apples():
  apple.penup()
  rand_apple=rand.randint(-200,200)
  apple.setposition(rand_apple,0)
  apple.setposition(rand.randint(-200,200),-200)

def drop_apple2():
  apple2.penup()
  rand_apple=rand.randint(-200,200)
  apple2.setposition(rand_apple,0)
  apple2.setposition(rand.randint(-200,200),-200)

def drop_apple3():
  apple3.penup()
  rand_apple=rand.randint(-200,200)
  apple3.setposition(rand_apple,0)
  apple3.setposition(rand.randint(-200,200),-200)

def drop_apple4():
  apple4.penup()
  rand_apple=rand.randint(-200,200)
  apple4.setposition(rand_apple,0)
  apple4.setposition(rand.randint(-200,200),-200)
  
def drop_apple5():
  apple5.penup()
  rand_apple=rand.randint(-200,200)
  apple5.setposition(rand_apple,0)
  apple5.setposition(rand.randint(-200,200),-200)



#-----function calls-----
wn.tracer(False)
draw_apple(apple)
wn.tracer(True)

wn.onkeypress(drop_apples, "a")
wn.onkeypress(drop_apple2, "b")
wn.onkeypress(drop_apple3, "c")
wn.onkeypress(drop_apple4, "d")
wn.onkeypress(drop_apple5, "e")

wn.listen()
wn.mainloop()
