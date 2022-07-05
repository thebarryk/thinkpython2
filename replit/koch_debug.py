import turtle


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


def xkoch(t, x=4, n=5):
  if x < 3:
    t.forward(x)
  else:
    draw(t, float(x)/3, n)
    t.lt(60)
    # draw(t, float(x)/3, n)
    # t.rt(120)
    # draw(t, float(x)/3, n)
    # t.lt(60)
    # draw(t, float(x)/3, n)

def koch(t, n):
    """Draws a koch curve with length n."""
    def fdf(n):
      print("forward {n}")
    def lt(n):
      print("left {n}")
    def rt(n):
      print("right {n}")
    if n < 10:
        fd(n)
        return
    m = n/3
    print(m)

    a=input("? ")
    if a=="x":
      exit(1)
    
    koch(t, m)
    lt(60)
    koch(t, m)
    rt(120)
    koch(t, m)
    lt(60)
    koch(t, m)

if __name__ == '__main__':

  bob = turtle.Turtle()
  koch(bob, 300)
  
  # wait for the user to close the window
  # turtle.mainloop()