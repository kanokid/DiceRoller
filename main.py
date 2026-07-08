from cmu_graphics import *
from time import sleep
import random
var = Rect(0,0,1,1,fill=None)
app.width=400
app.height=430

# Dice 1
dice1 = Rect(0,0,125,125,border="black",fill=None)
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
dice1roll6 = Group (
    Circle(35, 30, 10),
    Circle(35, 100, 10),
    Circle(35, 65, 10),
    Circle(90,65,10),
    Circle(90, 30, 10),
    Circle(90, 100, 10),
)
def rollDice1():
    dice1roll1.visible = False
    dice1roll2.visible = False
    dice1roll3.visible = False
    dice1roll4.visible = False
    dice1roll5.visible = False
    dice1roll6.visible = False
    dice1.number = randrange(1, 7)
    if dice1.number == 1:
        dice1roll1.visible = True
        dice1roll2.visible = False
        dice1roll3.visible = False
        dice1roll4.visible = False
        dice1roll5.visible = False
        dice1roll6.visible = False
    elif dice1.number == 2:
        dice1roll1.visible = False
        dice1roll2.visible = True
        dice1roll3.visible = False
        dice1roll4.visible = False
        dice1roll5.visible = False
        dice1roll6.visible = False
    elif dice1.number == 3:
        dice1roll1.visible = False
        dice1roll2.visible = False
        dice1roll3.visible = True
        dice1roll4.visible = False
        dice1roll5.visible = False
        dice1roll6.visible = False
    elif dice1.number == 4:
        dice1roll1.visible = False
        dice1roll2.visible = False
        dice1roll3.visible = False
        dice1roll4.visible = True
        dice1roll5.visible = False
        dice1roll6.visible = False
    elif dice1.number == 5:
        dice1roll1.visible = False
        dice1roll2.visible = False
        dice1roll3.visible = False
        dice1roll4.visible = False
        dice1roll5.visible = True
        dice1roll6.visible = False

    elif dice1.number == 6:
        dice1roll1.visible = False
        dice1roll2.visible = False
        dice1roll3.visible = False
        dice1roll4.visible = False
        dice1roll5.visible = False
        dice1roll6.visible = True

# Dice 2
dice2 = Rect(130,0,125,125,border="black",fill=None)
dice2roll1 = Circle(193,63,20)

dice2roll2 = Group (
Circle(170,40,13),
    Circle(215,85,13),
)

dice2roll3 = Group (
    Circle(170,85,10),
    Circle(215,85,10),
    Circle(192,40,10),
)

dice2roll4 = Group (
    Circle(170,40,10),
    Circle(170,90,10),
    Circle(215,40,10),
    Circle(215,90,10),
)

dice2roll5 = Group (
    Circle(160, 30, 10),
    Circle(160, 100, 10),
    Circle(193,63,10),
    Circle(225, 30, 10),
    Circle(225, 100, 10),
)
dice2roll6 = Group (
    Circle(165, 30, 10),
    Circle(165, 100, 10),
    Circle(165, 65, 10),
    Circle(220,65,10),
    Circle(220, 30, 10),
    Circle(220, 100, 10),
)

def rollDice2():
    dice2roll1.visible = False
    dice2roll2.visible = False
    dice2roll3.visible = False
    dice2roll4.visible = False
    dice2roll5.visible = False
    dice2roll6.visible = False
    dice2.number = randrange(1, 7)
    if dice2.number == 1:
        dice2roll1.visible = True
        dice2roll2.visible = False
        dice2roll3.visible = False
        dice2roll4.visible = False
        dice2roll5.visible = False
        dice2roll6.visible = False
    elif dice2.number == 2:
        dice2roll1.visible = False
        dice2roll2.visible = True
        dice2roll3.visible = False
        dice2roll4.visible = False
        dice2roll5.visible = False
        dice2roll6.visible = False
    elif dice2.number == 3:
        dice2roll1.visible = False
        dice2roll2.visible = False
        dice2roll3.visible = True
        dice2roll4.visible = False
        dice2roll5.visible = False
        dice2roll6.visible = False
    elif dice2.number == 4:
        dice2roll1.visible = False
        dice2roll2.visible = False
        dice2roll3.visible = False
        dice2roll4.visible = True
        dice2roll5.visible = False
        dice2roll6.visible = False
    elif dice2.number == 5:
        dice2roll1.visible = False
        dice2roll2.visible = False
        dice2roll3.visible = False
        dice2roll4.visible = False
        dice2roll5.visible = True
        dice2roll6.visible = False

    elif dice2.number == 6:
        dice2roll1.visible = False
        dice2roll2.visible = False
        dice2roll3.visible = False
        dice2roll4.visible = False
        dice2roll5.visible = False
        dice2roll6.visible = True

# Dice 3
dice3 = Rect(260,0,125,125,border="black",fill=None)
dice3roll1 = Circle(323,63,20)

dice3roll2 = Group (
Circle(300,40,13),
    Circle(345,85,13),
)

dice3roll3 = Group (
    Circle(300,85,10),
    Circle(345,85,10),
    Circle(322,40,10),
)

dice3roll4 = Group (
    Circle(300,40,10),
    Circle(300,90,10),
    Circle(345,40,10),
    Circle(345,90,10),
)

dice3roll5 = Group (
    Circle(290, 30, 10),
    Circle(290, 100, 10),
    Circle(323,63,10),
    Circle(355, 30, 10),
    Circle(355, 100, 10),
)
dice3roll6 = Group (
    Circle(295, 30, 10),
    Circle(295, 100, 10),
    Circle(295, 65, 10),
    Circle(350,65,10),
    Circle(350, 30, 10),
    Circle(350, 100, 10),
)
def rollDice3():
    dice3roll1.visible = False
    dice3roll2.visible = False
    dice3roll3.visible = False
    dice3roll4.visible = False
    dice3roll5.visible = False
    dice3roll6.visible = False
    dice3.number = randrange(1, 7)
    if dice3.number == 1:
        dice3roll1.visible = True
        dice3roll2.visible = False
        dice3roll3.visible = False
        dice3roll4.visible = False
        dice3roll5.visible = False
        dice3roll6.visible = False
    elif dice3.number == 2:
        dice3roll1.visible = False
        dice3roll2.visible = True
        dice3roll3.visible = False
        dice3roll4.visible = False
        dice3roll5.visible = False
        dice3roll6.visible = False
    elif dice3.number == 3:
        dice3roll1.visible = False
        dice3roll2.visible = False
        dice3roll3.visible = True
        dice3roll4.visible = False
        dice3roll5.visible = False
        dice3roll6.visible = False
    elif dice3.number == 4:
        dice3roll1.visible = False
        dice3roll2.visible = False
        dice3roll3.visible = False
        dice3roll4.visible = True
        dice3roll5.visible = False
        dice3roll6.visible = False
    elif dice3.number == 5:
        dice3roll1.visible = False
        dice3roll2.visible = False
        dice3roll3.visible = False
        dice3roll4.visible = False
        dice3roll5.visible = True
        dice3roll6.visible = False

    elif dice3.number == 6:
        dice3roll1.visible = False
        dice3roll2.visible = False
        dice3roll3.visible = False
        dice3roll4.visible = False
        dice3roll5.visible = False
        dice3roll6.visible = True

# Dice 4
dice4 = Rect(0,130,125,125,border="black",fill=None)
dice4roll1 = Circle(63,193,20)

dice4roll2 = Group (
Circle(40,170,13),
    Circle(85,215,13),
)

dice4roll3 = Group (
    Circle(40,215,10),
    Circle(85,215,10),
    Circle(62,170,10),
)

dice4roll4 = Group (
    Circle(40,170,10),
    Circle(40,220,10),
    Circle(85,170,10),
    Circle(85,220,10),
)

dice4roll5 = Group (
    Circle(30, 160, 10),
    Circle(30, 230, 10),
    Circle(63,193,10),
    Circle(95, 160, 10),
    Circle(95, 230, 10),
)
dice4roll6 = Group (
    Circle(35, 160, 10),
    Circle(35, 230, 10),
    Circle(35, 195, 10),
    Circle(90,195,10),
    Circle(90, 160, 10),
    Circle(90, 230, 10),
)

def rollDice4():
    dice4roll1.visible = False
    dice4roll2.visible = False
    dice4roll3.visible = False
    dice4roll4.visible = False
    dice4roll5.visible = False
    dice4roll6.visible = False
    dice4.number = randrange(1, 7)
    if dice4.number == 1:
        dice4roll1.visible = True
        dice4roll2.visible = False
        dice4roll3.visible = False
        dice4roll4.visible = False
        dice4roll5.visible = False
        dice4roll6.visible = False
    elif dice4.number == 2:
        dice4roll1.visible = False
        dice4roll2.visible = True
        dice4roll3.visible = False
        dice4roll4.visible = False
        dice4roll5.visible = False
        dice4roll6.visible = False
    elif dice4.number == 3:
        dice4roll1.visible = False
        dice4roll2.visible = False
        dice4roll3.visible = True
        dice4roll4.visible = False
        dice4roll5.visible = False
        dice4roll6.visible = False
    elif dice4.number == 4:
        dice4roll1.visible = False
        dice4roll2.visible = False
        dice4roll3.visible = False
        dice4roll4.visible = True
        dice4roll5.visible = False
        dice4roll6.visible = False
    elif dice4.number == 5:
        dice4roll1.visible = False
        dice4roll2.visible = False
        dice4roll3.visible = False
        dice4roll4.visible = False
        dice4roll5.visible = True
        dice4roll6.visible = False

    elif dice4.number == 6:
        dice4roll1.visible = False
        dice4roll2.visible = False
        dice4roll3.visible = False
        dice4roll4.visible = False
        dice4roll5.visible = False
        dice4roll6.visible = True

# Dice 5
dice5 = Rect(130,130,125,125,border="black",fill=None)
dice5roll1 = Circle(193,193,20)

dice5roll2 = Group (
Circle(170,170,13),
    Circle(215,215,13),
)

dice5roll3 = Group (
    Circle(170,215,10),
    Circle(215,215,10),
    Circle(192,170,10),
)

dice5roll4 = Group (
    Circle(170,170,10),
    Circle(170,220,10),
    Circle(215,170,10),
    Circle(215,220,10),
)

dice5roll5 = Group (
    Circle(160, 160, 10),
    Circle(160, 230, 10),
    Circle(193,193,10),
    Circle(225, 160, 10),
    Circle(225, 230, 10),
)
dice5roll6 = Group (
    Circle(165, 160, 10),
    Circle(165, 230, 10),
    Circle(165, 195, 10),
    Circle(220,195,10),
    Circle(220, 160, 10),
    Circle(220, 230, 10),
)
dice5roll1.visible = False
dice5roll2.visible = False
dice5roll3.visible = False
dice5roll4.visible = False
dice5roll5.visible = False
dice5roll6.visible = False
def rollDice5():
    dice5roll1.visible = False
    dice5roll2.visible = False
    dice5roll3.visible = False
    dice5roll4.visible = False
    dice5roll5.visible = False
    dice5roll6.visible = False
    dice5.number = randrange(1, 7)
    if dice5.number == 1:
        dice5roll1.visible = True
        dice5roll2.visible = False
        dice5roll3.visible = False
        dice5roll4.visible = False
        dice5roll5.visible = False
        dice5roll6.visible = False
    elif dice5.number == 2:
        dice5roll1.visible = False
        dice5roll2.visible = True
        dice5roll3.visible = False
        dice5roll4.visible = False
        dice5roll5.visible = False
        dice5roll6.visible = False
    elif dice5.number == 3:
        dice5roll1.visible = False
        dice5roll2.visible = False
        dice5roll3.visible = True
        dice5roll4.visible = False
        dice5roll5.visible = False
        dice5roll6.visible = False
    elif dice5.number == 4:
        dice5roll1.visible = False
        dice5roll2.visible = False
        dice5roll3.visible = False
        dice5roll4.visible = True
        dice5roll5.visible = False
        dice5roll6.visible = False
    elif dice5.number == 5:
        dice5roll1.visible = False
        dice5roll2.visible = False
        dice5roll3.visible = False
        dice5roll4.visible = False
        dice5roll5.visible = True
        dice5roll6.visible = False

    elif dice5.number == 6:
        dice5roll1.visible = False
        dice5roll2.visible = False
        dice5roll3.visible = False
        dice5roll4.visible = False
        dice5roll5.visible = False
        dice5roll6.visible = True

# Dice 6
dice6 = Rect(260,130,125,125,border="black",fill=None)
dice6roll1 = Circle(323,193,20)

dice6roll2 = Group (
Circle(300,170,13),
    Circle(345,215,13),
)

dice6roll3 = Group (
    Circle(300,215,10),
    Circle(345,215,10),
    Circle(322,170,10),
)

dice6roll4 = Group (
    Circle(300,170,10),
    Circle(300,220,10),
    Circle(345,170,10),
    Circle(345,220,10),
)

dice6roll5 = Group (
    Circle(290, 160, 10),
    Circle(290, 230, 10),
    Circle(323,193,10),
    Circle(355, 160, 10),
    Circle(355, 230, 10),
)
dice6roll6 = Group (
    Circle(295,160, 10),
    Circle(295, 230, 10),
    Circle(295, 195, 10),
    Circle(350,195,10),
    Circle(350, 160, 10),
    Circle(350, 230, 10),
)
def rollDice6():
    dice6roll1.visible = False
    dice6roll2.visible = False
    dice6roll3.visible = False
    dice6roll4.visible = False
    dice6roll5.visible = False
    dice6roll6.visible = False
    dice6.number = randrange(1, 7)
    if dice6.number == 1:
        dice6roll1.visible = True
        dice6roll2.visible = False
        dice6roll3.visible = False
        dice6roll4.visible = False
        dice6roll5.visible = False
        dice6roll6.visible = False
    elif dice6.number == 2:
        dice6roll1.visible = False
        dice6roll2.visible = True
        dice6roll3.visible = False
        dice6roll4.visible = False
        dice6roll5.visible = False
        dice6roll6.visible = False
    elif dice6.number == 3:
        dice6roll1.visible = False
        dice6roll2.visible = False
        dice6roll3.visible = True
        dice6roll4.visible = False
        dice6roll5.visible = False
        dice6roll6.visible = False
    elif dice6.number == 4:
        dice6roll1.visible = False
        dice6roll2.visible = False
        dice6roll3.visible = False
        dice6roll4.visible = True
        dice6roll5.visible = False
        dice6roll6.visible = False
    elif dice6.number == 5:
        dice6roll1.visible = False
        dice7roll3.visible = False
        dice6roll3.visible = False
        dice6roll4.visible = False
        dice6roll5.visible = True
        dice6roll6.visible = False

    elif dice6.number == 6:
        dice6roll1.visible = False
        dice6roll2.visible = False
        dice6roll3.visible = False
        dice6roll4.visible = False
        dice6roll5.visible = False
        dice6roll6.visible = True
# Dice 7
dice7 = Rect(130,260,125,125,border="black",fill=None)
dice7roll1 = Circle(323,193,20)

dice7roll2 = Group (
Circle(40,170,13),
    Circle(85,215,13),
)

dice7roll3 = Group (
    Circle(300,215,10),
    Circle(345,215,10),
    Circle(322,170,10),
)

dice7roll4 = Group (
    Circle(300,170,10),
    Circle(300,220,10),
    Circle(345,170,10),
    Circle(345,220,10),
)

dice7roll5 = Group (
    Circle(290, 160, 10),
    Circle(290, 230, 10),
    Circle(323,193,10),
    Circle(355, 160, 10),
    Circle(355, 230, 10),
)
dice7roll6 = Group (
    Circle(295,160, 10),
    Circle(295, 230, 10),
    Circle(295, 195, 10),
    Circle(350,195,10),
    Circle(350, 160, 10),
    Circle(350, 230, 10),
)
def rollDice7():
    dice7roll1.visible = False
    dice7roll2.visible = False
    dice7roll3.visible = False
    dice7roll4.visible = False
    dice7roll5.visible = False
    dice7roll6.visible = False
    dice7.number = randrange(1, 7)
    if dice7.number == 1:
        dice7roll1.visible = True
        dice7roll2.visible = False
        dice7roll3.visible = False
        dice7roll4.visible = False
        dice7roll5.visible = False
        dice7roll6.visible = False
    elif dice7.number == 2:
        dice7roll1.visible = False
        dice7roll2.visible = True
        dice7roll3.visible = False
        dice7roll4.visible = False
        dice7roll5.visible = False
        dice7roll6.visible = False
    elif dice7.number == 3:
        dice7roll1.visible = False
        dice7roll2.visible = False
        dice7roll3.visible = True
        dice7roll4.visible = False
        dice7roll5.visible = False
        dice7roll6.visible = False
    elif dice7.number == 4:
        dice7roll1.visible = False
        dice7roll2.visible = False
        dice7roll3.visible = False
        dice7roll4.visible = True
        dice7roll5.visible = False
        dice7roll6.visible = False
    elif dice7.number == 5:
        dice7roll1.visible = False
        dice7roll3.visible = False
        dice7roll3.visible = False
        dice7roll4.visible = False
        dice7roll5.visible = True
        dice7roll6.visible = False

    elif dice7.number == 6:
        dice7roll1.visible = False
        dice7roll2.visible = False
        dice7roll3.visible = False
        dice7roll4.visible = False
        dice7roll5.visible = False
        dice7roll6.visible = True
# Dice 8
dice8 = Rect(260,130,125,125,border="black",fill=None)
dice8roll1 = Circle(323,193,20)

dice8roll2 = Group (
Circle(300,170,13),
    Circle(345,215,13),
)

dice8roll3 = Group (
    Circle(300,215,10),
    Circle(345,215,10),
    Circle(322,170,10),
)

dice8roll4 = Group (
    Circle(300,170,10),
    Circle(300,220,10),
    Circle(345,170,10),
    Circle(345,220,10),
)

dice8roll5 = Group (
    Circle(290, 160, 10),
    Circle(290, 230, 10),
    Circle(323,193,10),
    Circle(355, 160, 10),
    Circle(355, 230, 10),
)
dice8roll6 = Group (
    Circle(295,160, 10),
    Circle(295, 230, 10),
    Circle(295, 195, 10),
    Circle(350,195,10),
    Circle(350, 160, 10),
    Circle(350, 230, 10),
)
def rollDice8():
    dice8roll1.visible = False
    dice8roll2.visible = False
    dice8roll3.visible = False
    dice8roll4.visible = False
    dice8roll5.visible = False
    dice8roll6.visible = False
    dice8.number = randrange(1, 7)
    if dice8.number == 1:
        dice8roll1.visible = True
        dice8roll2.visible = False
        dice8roll3.visible = False
        dice8roll4.visible = False
        dice8roll5.visible = False
        dice8roll6.visible = False
    elif dice8.number == 2:
        dice8roll1.visible = False
        dice8roll2.visible = True
        dice8roll3.visible = False
        dice8roll4.visible = False
        dice8roll5.visible = False
        dice8roll6.visible = False
    elif dice8.number == 3:
        dice8roll1.visible = False
        dice8roll2.visible = False
        dice8roll3.visible = True
        dice8roll4.visible = False
        dice8roll5.visible = False
        dice8roll6.visible = False
    elif dice8.number == 4:
        dice8roll1.visible = False
        dice8roll2.visible = False
        dice8roll3.visible = False
        dice8roll4.visible = True
        dice8roll5.visible = False
        dice8roll6.visible = False
    elif dice8.number == 5:
        dice8roll1.visible = False
        dice8roll3.visible = False
        dice8roll3.visible = False
        dice8roll4.visible = False
        dice8roll5.visible = True
        dice8roll6.visible = False

    elif dice8.number == 6:
        dice8roll1.visible = False
        dice8roll2.visible = False
        dice8roll3.visible = False
        dice8roll4.visible = False
        dice8roll5.visible = False
        dice8roll6.visible = True
# Dice 9
dice9 = Rect(260,130,125,125,border="black",fill=None)
dice9roll1 = Circle(323,193,20)

dice9roll2 = Group (
Circle(300,170,13),
    Circle(345,215,13),
)

dice9roll3 = Group (
    Circle(300,215,10),
    Circle(345,215,10),
    Circle(322,170,10),
)

dice9roll4 = Group (
    Circle(300,170,10),
    Circle(300,220,10),
    Circle(345,170,10),
    Circle(345,220,10),
)

dice9roll5 = Group (
    Circle(290, 160, 10),
    Circle(290, 230, 10),
    Circle(323,193,10),
    Circle(355, 160, 10),
    Circle(355, 230, 10),
)
dice9roll6 = Group (
    Circle(295,160, 10),
    Circle(295, 230, 10),
    Circle(295, 195, 10),
    Circle(350,195,10),
    Circle(350, 160, 10),
    Circle(350, 230, 10),
)
def rollDice9():
    dice9roll1.visible = False
    dice9roll2.visible = False
    dice9roll3.visible = False
    dice9roll4.visible = False
    dice9roll5.visible = False
    dice9roll6.visible = False
    dice9.number = randrange(1, 7)
    if dice9.number == 1:
        dice9roll1.visible = True
        dice9roll2.visible = False
        dice9roll3.visible = False
        dice9roll4.visible = False
        dice9roll5.visible = False
        dice9roll6.visible = False
    elif dice9.number == 2:
        dice9roll1.visible = False
        dice9roll2.visible = True
        dice9roll3.visible = False
        dice9roll4.visible = False
        dice9roll5.visible = False
        dice9roll6.visible = False
    elif dice9.number == 3:
        dice9roll1.visible = False
        dice9roll2.visible = False
        dice9roll3.visible = True
        dice9roll4.visible = False
        dice9roll5.visible = False
        dice9roll6.visible = False
    elif dice9.number == 4:
        dice9roll1.visible = False
        dice9roll2.visible = False
        dice9roll3.visible = False
        dice9roll4.visible = True
        dice9roll5.visible = False
        dice9roll6.visible = False
    elif dice9.number == 5:
        dice9roll1.visible = False
        dice9roll3.visible = False
        dice9roll3.visible = False
        dice9roll4.visible = False
        dice9roll5.visible = True
        dice9roll6.visible = False

    elif dice9.number == 6:
        dice9roll1.visible = False
        dice9roll2.visible = False
        dice9roll3.visible = False
        dice9roll4.visible = False
        dice9roll5.visible = False
        dice9roll6.visible = True

def rollDice():
    rollDice1()
    rollDice2()
    rollDice3()
    rollDice4()
    rollDice5()
    rollDice6()
    rollDice7()
    rollDice8()
    rollDice9()
def onMousePress(mouseX, mouseY, button):
    if button == 0:
        rollDice()

    elif button == 1:
        var.width = 250
rollDice()

cmu_graphics.run()