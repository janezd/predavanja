import risar
from math import *

class Turtle:
    def __init__(self):
        self.x = risar.maxX / 2
        self.y = risar.maxY / 2
        self.angle = 0
        self.pen_active = True
        self.pause = 0
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 3, risar.zelena, 3)
        self.update()

    def set_pause(self, n):
        self.pause = n

    def no_pause(self):
        self.set_pause(0)

    def hide(self):
        self.body.hide()
        self.head.hide()

    def show(self):
        self.body.show()
        self.head.show()

    def update(self):
        self.body.setPos(self.x, self.y)
        phi = radians(90 - self.angle)
        self.head.setPos(self.x + 5 * cos(phi), self.y + 5 * sin(phi))
        risar.cakaj(self.pause)

    def pen_up(self):
        self.pen_active = False

    def pen_down(self):
        self.pen_active = True

    def fly(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.update()

    def forward(self, a):
        phi = radians(90 - self.angle)
        nx = self.x + a * cos(phi)
        ny = self.y + a * sin(phi)
        if self.pen_active:
            risar.crta(self.x, self.y, nx, ny)
        self.x = nx
        self.y = ny
        self.update()

    def backward(self, a):
        self.forward(-a)

    def turn(self, phi):
        self.angle += phi
        self.update()

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)


import unittest
class TestPot(unittest.TestCase):
    def test_length(self):
        t = Turtle()
        self.assertEqual(t.length, 0)
        t.forward(15)
        self.assertEqual(t.length, 15)
        t.turn(50)
        self.assertEqual(t.length, 15)
        t.backward(5)
        self.assertEqual(t.length, 20)

        u = Turtle()
        self.assertEqual(u.length, 0)
        self.assertEqual(t.length, 20)

        u.forward(42)
        self.assertEqual(u.length, 42)
        self.assertEqual(t.length, 20)

    def test_length_pen(self):
        t = Turtle()
        self.assertEqual(t.length, 0)
        t.forward(15)
        self.assertEqual(t.length, 15)
        t.pen_up()
        self.assertEqual(t.length, 15)
        t.turn(50)
        self.assertEqual(t.length, 15)
        t.backward(5)
        self.assertEqual(t.length, 15)
        t.pen_down()
        self.assertEqual(t.length, 15)
        t.backward(10)
        self.assertEqual(t.length, 25)

    def test_fly(self):
        t = Turtle()
        self.assertEqual(t.length, 0)
        t.forward(15)
        self.assertEqual(t.length, 15)
        t.fly(0, 0, 0)
        self.assertEqual(t.length, 15)

if __name__ == "__main__":
    unittest.main()
