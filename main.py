from cmu_graphics import *
import random
app.width=125
app.height=200

# Dice 1
dice1 = Rect(0,0,125,125,border="black",fill=None)
dice1.number = 5
#dice1 = Image(f"https://raw.githubusercontent.com/kanokid/DiceRoller/master/dice{dice1.number}.jpg",12,12,width=100,height=100)
dice1roll1 = Circle(63,63,20)

dice1roll2 = Group (
Circle(40,40,13),
    Circle(85,85,13),
)

dice1roll3 = Group (
    Circle(40,85,10),
    Circle(85,85,10),
    Circle(62,40,10),
)

dice1roll4 = Group (
    Circle(40,40,10),
    Circle(40,90,10),
    Circle(85,40,10),
    Circle(85,90,10),
)

dice1roll5 = Group (
    Circle(30, 30, 10),
    Circle(30, 100, 10),
    Circle(63,63,10),
    Circle(95, 30, 10),
    Circle(95, 100, 10),
)

if dice1.number == 1:
    dice1roll1.visible = True
    dice1roll2.visible = False
    dice1roll3.visible = False
    dice1roll4.visible = False
    dice1roll5.visible = False
    #dice1roll6.visible = False
elif dice1.number == 2:
    dice1roll1.visible = False
    dice1roll2.visible = True
    dice1roll3.visible = False
    dice1roll4.visible = False
    dice1roll5.visible = False
    #dice1roll6.visible = False
elif dice1.number == 3:
    dice1roll1.visible = False
    dice1roll2.visible = False
    dice1roll3.visible = True
    dice1roll4.visible = False
    dice1roll5.visible = False
    #dice1roll6.visible = False

elif dice1.number == 4:
    dice1roll1.visible = False
    dice1roll2.visible = False
    dice1roll3.visible = False
    dice1roll4.visible = True
    dice1roll5.visible = False
    #dice1roll6.visible = False
elif dice1.number == 5:
    dice1roll1.visible = False
    dice1roll2.visible = False
    dice1roll3.visible = False
    dice1roll4.visible = False
    dice1roll5.visible = True
    #dice1roll6.visible = False
'''
elif dice1.number == 6:
dice1roll1.visible = False
dice1roll2.visible = False
dice1roll3.visible = False
dice1roll4.visible = False
dice1roll5.visible = False
dice1roll6.visible = True
'''


cmu_graphics.run()