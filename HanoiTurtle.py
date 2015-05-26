"""
Script that uses the turtle module to animate the solution to the
Hanoi tower problem with any number of discs.

Exercises 6 and 12 from How to Think Like a Computer Scientist: 
http://interactivepython.org/runestone/static/Python-F2/Recursion/ProgrammingExercises.html
"""

__author__ = 'sean'

import turtle

def stackPole(poles, n, poleNumber):
    """Stacks a the first pole in a list of three lists representing Hanoi tower poles"""
    for i in range(n, 0, -1):
        poles[poleNumber - 1].append(i)


def makeTurtles(num):
    """
    Makes num number of stretched square turtles (to represent discs) and puts them into a list for later access.
    :param num:
    :return:
    """
    turtles = []
    for i in range(num):
        t = turtle.Turtle()
        #t.speed(0) # can set this for superfast disc movement
        t.up()
        t.shape('square')
        t.shapesize(stretch_len=(2 + i)) #bottom turtle is longest
        t.goto(0, num - i)
        turtles.append(t)
    return turtles

def drawPoles(wn):
    """
    Sets coordinates of window wn and draws poles for disc movement
    :param wn: Screen object of turtle module
    :return: no return
    """
    wn.setworldcoordinates(-1, -5, 3, 20)
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)
    t.up()
    t.goto(-.5, 0)
    t.down()
    t.goto(2.5, 0)
    t.up()
    for i in range(3):
        t.goto(i, 0)
        t.down()
        t.goto(i, 10)
        t.up()
    t.hideturtle()

def moveTurt(t, pole, count):
    """Moves selected turtle to selected pole number (0 to 2), no return"""
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y + 10)
    t.goto(pole, y + 10)
    t.goto(pole, y)
    count += 1

def legalMove(turtles, poles, m, n, count):
    """
    Makes legal move for a disc between poles m and n
    :param turtles: list of turtles
    :param poles: list of lists representing poles
    :param m: first pole
    :param n: second pole
    :return: no return
    """
    if len(poles[m]) != 0 and (len(poles[n]) == 0 or poles[m][-1] < poles[n][-1]):      #one possible legal move btwn m and n
        moveTurt(turtles[poles[m][-1] - 1], n, count)
        poles[n].append(poles[m].pop())
        if len(poles[0]) == 0 and len(poles[1]) == 0:
            return
    elif len(poles[n]) != 0 and (len(poles[m]) == 0 or poles[n][-1] < poles[m][-1]):    #other possible legal move btwn m and n
        moveTurt(turtles[poles[n][-1] - 1], m, count)
        poles[m].append(poles[n].pop())

def done(poles):
    """Checks if game is complete"""
    if len(poles[0]) == 0 and len(poles[1]) == 0:
        return True
    else:
        return False

def movePoles(poles, n, turtles):
    """
    Moves a set of n discs from the first pole to the last pole
    :param poles: list of poles containing discs
    :param n: number of discs or turtles
    :param turtles: list of turtles representing discs
    :return: no return
    """
    count = 0
    if n % 2 == 0:
        moveEvenPoles(poles, n, turtles, count)
    else:
        moveOddPoles(poles, n, turtles, count)
    return count

def moveEvenPoles(poles, n, turtles, count):
    """movePoles for an even number of discs"""
    if done(poles):
        return

    legalMove(turtles, poles, 0, 1, count)

    if done(poles):
        return

    legalMove(turtles, poles, 0, 2, count)

    if done(poles):
        return

    legalMove(turtles, poles, 1, 2, count)

    moveEvenPoles(poles, n, turtles, count)


def moveOddPoles(poles, n, turtles, count):
    """movePoles for an odd number of discs"""
    if done(poles):
        return

    legalMove(turtles, poles, 0, 2, count)

    if done(poles):
        return

    legalMove(turtles, poles, 0, 1, count)

    if done(poles):
        return

    legalMove(turtles, poles, 1, 2, count)

    moveOddPoles(poles, n, turtles, count)




def main():

    #make list of lists to represent poles
    poles = [[], [], []]

    #make screen and draw poles
    wn = turtle.Screen()
    drawPoles(wn)

    #pick number of turtles/discs here
    n = input("How many discs? ")

    #make the discs
    turtles = makeTurtles(n)

    #stack the number of poles in the original list
    stackPole(poles, n, 1)

    #move numbers in list and discs in animation
    count = movePoles(poles, n, turtles)

    print(count)

    wn.exitonclick()

if __name__ == "__main__":
    main()



