"""
Script that draws a Koch snowflake with recursion.

"""


__author__ = 'sean'

import turtle

def drawFlake(t, degree, size):
    """
    Draws a Koch snowflake with turtle t, of degree degree, with side lengths of size.
    """
    drawSide(t, degree, size)
    t.right(120)
    drawSide(t, degree, size)
    t.right(120)
    drawSide(t, degree, size)
    t.right(120)


def drawSide(t, degree, size):
    """
    Draws one side of a Koch snowflake. Requires 3 sides to complete.
    """
    if degree == 0:
        t.forward(size)
        return

    drawSide(t, degree - 1, size)
    t.left(60)
    drawSide(t, degree - 1, size)
    t.right(120)
    drawSide(t, degree - 1, size)
    t.left(60)
    drawSide(t, degree - 1, size)


def main():

    wn = turtle.Screen()

    bob = turtle.Turtle()
    bob.speed(0)

    drawFlake(bob, 3, 10)

    wn.exitonclick()

main()




