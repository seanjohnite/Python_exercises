"""
Program that draws a Sierpinski triangle using recursion.
"""

__author__ = 'sean'

import turtle

def drawTriangle(points, color, t):
    """
    Draws a triangle using an array of 3 points given in points, with color color and turtle t
    """
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def getMid(p1, p2):
    """
    Returns the midpoint of two points p1 and p2
    """
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def sierpinski(points, degree, t):
    """
    Draws a Sierpinski triangle with several different colors.
    """
    colorMap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']

    drawTriangle(points, colorMap[degree], t)

    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], \
                   degree - 1, t)
        sierpinski([points[1], getMid(points[1], points[0]), getMid(points[1], points[2])], \
                   degree - 1, t)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[2], points[0])], \
                   degree - 1, t)

def main():
    wn = turtle.Screen()

    abby = turtle.Turtle()
    abby.speed(0)

    myPoints = [[-200, -100], [0, 200], [200, -100]]

    n = input("How many levels deep should I go? (3-5 suggested) ")

    sierpinski(myPoints, n, abby)

    wn.exitonclick()

main()