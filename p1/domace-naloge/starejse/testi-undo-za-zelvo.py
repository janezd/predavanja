from math import *
import unittest

import risar


class Turtle:
    def __init__(self):
        self.x = risar.maxX / 2
        self.y = risar.maxY / 2
        self.angle = 0
        self.pen_active = True
        self.pause = 0
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.update()

    def update(self):
        phi = radians(90 - self.angle)
        self.body.setPos(self.x, self.y)
        self.head.setPos(self.x + 5 * cos(phi), self.y + 5 * sin(phi))
        risar.obnovi()
        if self.pause:
            self.wait(self.pause)

    def forward(self, a):
        phi = radians(90 - self.angle)
        nx = self.x + a * cos(phi)
        ny = self.y + a * sin(phi)
        if self.pen_active:
            crta = risar.crta(self.x, self.y, nx, ny)
        self.x = nx
        self.y = ny
        self.update()

    def turn(self, phi):
        self.angle += phi
        self.update()

    def backward(self, a):
        self.forward(-a)

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)

    def fly(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.update()

    def pen_up(self):
        self.pen_active = False

    def pen_down(self):
        self.pen_active = True

    def wait(self, s):
        risar.cakaj(s)

    def hide(self):
        self.body.hide()
        self.head.hide()

    def show(self):
        self.body.show()
        self.head.show()

    def set_pause(self, s):
        self.pause = s

    def no_pause(self):
        self.set_pause(0)


def z_crta(x1, y1, x2, y2, *args):
    x0, y0 = risar.maxX / 2, risar.maxY / 2
    crta = stara_crta(x1, y1, x2, y2, *args)
    tups = (x1 - x0, y1 - y0), (x2 - x0, y2 - y0)
    crta.setData(42, min(tups) + max(tups))
    return crta

stara_crta = risar.crta
risar.crta = z_crta


class TestZelva(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.square = [(0, 0, 0, 20), (-20, 20, 0, 20),
                       (-20, 0, -20, 20), (-20, 0, 0, 0)
        ]

    def new_turtle(self):
        self.turtle = Turtle()
        for line in list(self.scene_lines()):
            risar.widget.scene.removeItem(line)
        return self.turtle

    @staticmethod
    def scene_lines():
        from PyQt4.QtGui import QGraphicsLineItem
        return (item for item in risar.widget.scene.items()
                if isinstance(item, QGraphicsLineItem)
        )

    @classmethod
    def get_lines(cls):
        return {item.data(42) for item in cls.scene_lines()}

    def check_turtle_pos(self, x, y, angle):
        body = self.turtle.body
        head = self.turtle.head
        tx, ty = self.turtle.x, self.turtle.y
        tangle = self.turtle.angle
        self.assertEqual((x + risar.maxX / 2, y + risar.maxY / 2), (tx, ty),
                         "Zelva ni, kjer bi morala biti")
        self.assertEqual(angle, tangle,
                         "Zelva ni obrnjena, kamor bi morala biti")
        phi = radians(90 - tangle)
        self.assertEqual((tx, ty), (body.x(), body.y()),
                         "Telo ni narisano, kjer bi moralo biti")
        self.assertEqual((tx + 5 * cos(phi), ty + 5 * sin(phi)),
                         (head.x(), head.y()),
                         "Glava ni narisana, kjer bi morala biti")

    def test_square(self):
        turtle = self.new_turtle()
        turtle.square(20)
        self.assertSetEqual(set(self.square), self.get_lines())

        turtle = self.new_turtle()
        turtle.right()
        turtle.square(30)
        self.assertSetEqual(
            {(0, 0, 30, 0), (30, 0, 30, 30), (0, 30, 30, 30), (0, 0, 0, 30)},
            self.get_lines()
        )

    def test_undo_obvezni(self):
        turtle = self.new_turtle()
        turtle.square(20)
        self.assertSetEqual(set(self.square), self.get_lines())

        turtle.undo()
        self.assertSetEqual(set(self.square[:3]), self.get_lines())
        self.check_turtle_pos(-20, 0, -270)

        turtle.fly(-100, 100, 0)
        turtle.undo()
        self.assertNotEqual((turtle.x, turtle.y),
                            (risar.maxX / 2 - 20, risar.maxY / 2))

        turtle = self.new_turtle()
        turtle.square(20)
        turtle.left()
        self.assertSetEqual(set(self.square), self.get_lines())

        turtle = self.new_turtle()
        turtle.undo()
        self.check_turtle_pos(0, 0, 0)
        self.assertSetEqual(set(), self.get_lines())

        turtle.forward(20)
        turtle.left()
        turtle.fly(100, 100, 50)
        turtle.undo()
        self.check_turtle_pos(0, 0, 0)
        self.assertSetEqual(set(), self.get_lines())

    def test_undo_dodatni(self):
        turtle = self.new_turtle()
        turtle.square(20)
        self.assertSetEqual(set(self.square), self.get_lines())

        turtle.undo()
        self.assertSetEqual(set(self.square[:3]), self.get_lines())
        self.check_turtle_pos(-20, 0, -270)

        turtle.undo()
        self.assertSetEqual(set(self.square[:2]), self.get_lines())
        self.check_turtle_pos(-20, 20, -180)

        turtle.undo()
        self.assertSetEqual(set(self.square[:1]), self.get_lines())
        self.check_turtle_pos(0, 20, -90)

        turtle.undo()
        self.assertSetEqual(set(), self.get_lines())
        self.check_turtle_pos(0, 0, 0)

        turtle.undo()
        self.assertSetEqual(set(), self.get_lines())
        self.check_turtle_pos(0, 0, 0)

        turtle.undo()
        self.assertSetEqual(set(), self.get_lines())
        self.check_turtle_pos(0, 0, 0)

        turtle = self.new_turtle()
        turtle.undo()
        self.check_turtle_pos(0, 0, 0)
        self.assertSetEqual(set(), self.get_lines())

        turtle.fly(risar.maxX / 2 + 100, risar.maxY / 2 + 100, 90)
        turtle.forward(20)
        turtle.undo()
        self.check_turtle_pos(100, 100, 90)
        self.assertSetEqual(set(), self.get_lines())

        turtle.forward(20)
        turtle.pen_up()
        turtle.forward(20)
        turtle.pen_down()
        turtle.forward(20)
        turtle.fly(risar.maxX / 2 + 100, risar.maxY / 2 + 100, 0)
        turtle.forward(20)
        turtle.fly(risar.maxX / 2 + 100, risar.maxY / 2 + 200, 0)
        turtle.undo()
        self.check_turtle_pos(100, 100, 0)
        self.assertSetEqual({(100, 100, 120, 100), (140, 100, 160, 100)},
                            self.get_lines())
        turtle.undo()
        self.check_turtle_pos(140, 100, 90)
        self.assertSetEqual({(100, 100, 120, 100)}, self.get_lines())

        turtle.undo()
        self.check_turtle_pos(100, 100, 90)
        self.assertSetEqual(set(), self.get_lines())

        turtle.undo()
        self.check_turtle_pos(100, 100, 90)
        self.assertSetEqual(set(), self.get_lines())

if __name__ == "__main__":
    unittest.main()