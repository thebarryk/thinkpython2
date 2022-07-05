"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from math import *
import turtle


def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

def draw_centered_circle(t, radius):

  # draw a circle centered on the origin
  t.pu()
  t.fd(radius)
  t.lt(90)
  t.pd()
  circle(t, radius)

def divisor(n):
  if 0 <= n <=180:
    return n if 360%n==0 else divisor(n+1)
  else:
    return 360

def flower(t, n, radius):

  def petal():
    arc(t, radius, step)
    t.lt(180-step)
    arc(t, radius, step)
    t.lt(180)

  m = divisor(n)
  step = 360./float(m)
  
  for i in range(m):
    petal()

def pies(t, n, l):
  """
  Draw a polygon divided into triangular pies
  t ....... turtle object
  length .. side length of polygon
  n ....... number of sides
  """

  def triangle():
    t.fd(radius)
    t.left(180-base_angle)
    t.forward(length)
    t.left(180-base_angle)
    t.up()
    t.forward(radius)
    t.left(180)
    t.down()

  vertex_angle = float(360)/n
  base_angle = 90. - vertex_angle/2.
  radius = length / (2*sin(radians(vertex_angle/2.)))

  t.left(vertex_angle/2.)
  for i in range(n):
    triangle()
  t.left(-vertex_angle/2.)

def topolar(xy):
  x, y = xy
  r = sqrt(x**2 + y**2)
  if x == 0 and y ==0:
    th = 0
  else:
    th = atan2(x, y)
  return r, th

def tocartesion(rth):
  r, th = rth
  return r*cos(th), r*sin(th)

def archimedes(t, n=100, dtheta=.2, dr=1):
  r, th = topolar(t.position())
  print(f"r={r:f} theta={th:f}")
  for i in range(n):
    r += dr
    th += dtheta
    x, y = tocartesion((r,th))
    print(f"r={r:f} theta={th:f} x={x:f} y={y:f}")
    t.goto(x, y)

def osculating(t, n=100, dtheta=.2, dr=1, dosculate=.04, dn=5):
  pass

def draw(t, length, n):
  if n == 0:
    return
  angle = 50 
  t.fd(length*n)
  t.lt(angle)
  draw(t, length, n-1)
  t.rt(2*angle)
  draw(t, length, n-1)
  t.lt(angle)
  t.bk(length*n)

def koch(t, x=4, n=20):
  if x < 3:
    t.forward(x)
  else:
    draw(t, float(x)/3, n)
    t.left(60)
    draw(t, float(x)/3, n)
    t.left(120)
    draw(t, float(x)/3, n)
    t.left(60)
    draw(t, float(x)/3, n)


if __name__ == '__main__':

  bob = turtle.Turtle()

  length = radius = 100

  # draw_centered_circle(bob, radius)
  # flower(bob, 10, radius)
  # pies(bob, 7, length)
  # archimedes(bob, n=200, dr=1, dtheta=.3)
  koch(bob, x=10)
  
  # wait for the user to close the window
  turtle.mainloop()

  print("Done!")