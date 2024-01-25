import turtle
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

turtle.end_fill()
turtle.done()