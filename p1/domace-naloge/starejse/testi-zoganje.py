

import unittest
from PyQt4 import QtGui
import math

class BallTest(unittest.TestCase):
    def test_ocena5(self):
        k = Ball(1, 2, 3, 4, 5, risar.modra)
        self.assertAlmostEqual(k.get_x(), 1, msg="napacna koordinata x")
        self.assertAlmostEqual(k.get_y(), 2, msg="napacna koordinata y")
        self.assertAlmostEqual(k.get_r(), 3, msg="napacen polmer")
        self.assertAlmostEqual(k.get_vx(), 4, msg="napacna hitrost v smeri x")
        self.assertAlmostEqual(k.get_vy(), 5, msg="napacna hitrost v smeri y")

        krog = k.get_shape()
        self.assertIsInstance(k.get_shape(), QtGui.QGraphicsEllipseItem,
            msg="napacen lik")
        self.assertEqual(krog.pen().color(), risar.modra, msg="napacna barva")
        self.assertAlmostEqual(krog.x(), 1, msg="krog ni, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), 2, msg="krog ni, kjer bi moral biti (y)")

        xs, ys, rs, dxs, dys, vs = set(), set(), set(), set(), set(), set()
        for i in range(1000):
            k = Ball()
            x, y, r, = k.get_x(), k.get_y(), k.get_r()
            dx, dy = k.get_vx(), k.get_vy()
            v = math.sqrt(dx**2 + dy**2)
            self.assertGreaterEqual(x - r, -0.001, msg="zoga je levo od levega roba")
            self.assertGreaterEqual(y - r, -0.001, msg="zoga je nad gornjim robom")
            self.assertLessEqual(x + r, risar.maxX + 0.001, msg="zoga je desno od desnega roba")
            self.assertLessEqual(y + r, risar.maxY + 0.001, msg="zoga je pod spodnjim robom")
            self.assertGreaterEqual(v, 4.999, msg="zoga je prepocasna")
            self.assertLessEqual(v, 10.001, msg="zoga je prehitra")
            self.assertGreaterEqual(r, 14.999, msg="zoga je premajhna")
            self.assertLessEqual(r, 30.001, msg="zoga je prevelika")
            xs.add(x)
            ys.add(y)
            rs.add(r)
            dxs.add(dx)
            dys.add(dy)
            vs.add(v)

        self.assertGreaterEqual(len(xs), 10,
            msg="zoge imajo cudno malo razlicnih zacetnih koordinat x")
        self.assertGreaterEqual(len(ys), 10,
            msg="zoge imajo cudno malo razlicnih zacetnih koordinat y")
        self.assertGreaterEqual(len(rs), 10,
            msg="zoge imajo cudno malo razlicnih polmerov")
        self.assertGreaterEqual(len(vs), 6,
            msg="zoge imajo cudno malo razlicnih zacetnih hitrosti")
        self.assertGreaterEqual(len(dxs), 10,
            msg="zoge imajo cudno malo razlicnih zacetnih hitrosti v smeri x")
        self.assertGreaterEqual(len(dys), 10,
            msg="zoge imajo cudno malo razlicnih zacetnih hitrosti v smeri y")

    def test_ocena6_move(self):
        k = Ball(1, 2, 3, 4, 5, risar.modra)
        krog = k.get_shape()
        self.assertAlmostEqual(k.get_x(), 1)
        self.assertAlmostEqual(k.get_y(), 2)
        self.assertAlmostEqual(k.get_vx(), 4)
        self.assertAlmostEqual(k.get_vy(), 5)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")

        k.move()
        self.assertAlmostEqual(k.get_x(), 5)
        self.assertAlmostEqual(k.get_y(), 7)
        self.assertAlmostEqual(k.get_vx(), 4)
        self.assertAlmostEqual(k.get_vy(), 5)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")

        k.move()
        self.assertAlmostEqual(k.get_x(), 9)
        self.assertAlmostEqual(k.get_y(), 12)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")


        k = Ball(1, 2, 3, 0, 1, risar.modra)
        krog = k.get_shape()
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")
        k.move()
        self.assertAlmostEqual(k.get_x(), 1)
        self.assertAlmostEqual(k.get_y(), 3)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")
        k.move()
        self.assertAlmostEqual(k.get_x(), 1)
        self.assertAlmostEqual(k.get_y(), 4)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")

        k = Ball(1, 2, 3, 1, 0, risar.modra)
        krog = k.get_shape()
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")
        k.move()
        self.assertAlmostEqual(k.get_x(), 2)
        self.assertAlmostEqual(k.get_y(), 2)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")
        k.move()
        self.assertAlmostEqual(k.get_x(), 3)
        self.assertAlmostEqual(k.get_y(), 2)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")

        k = Ball(1, 2, 3, -2, -5, risar.modra)
        krog = k.get_shape()
        k.move()
        self.assertAlmostEqual(k.get_x(), -1)
        self.assertAlmostEqual(k.get_y(), -3)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")
        k.move()
        self.assertAlmostEqual(k.get_x(), -3)
        self.assertAlmostEqual(k.get_y(), -8)
        self.assertAlmostEqual(krog.x(), k.get_x(), msg="krog ni narisan, kjer bi moral biti (x)")
        self.assertAlmostEqual(krog.y(), k.get_y(), msg="krog ni narisan, kjer bi moral biti (y)")


    def test_ocena7_walls(self):
        k = Ball(5, 100, 6, -1, 2)
        k.walls()
        self.assertAlmostEqual(k.get_x(), 5, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_y(), 100, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_vx(), 1, msg="zoga se ne obrne pravilno ob levi steni")
        self.assertAlmostEqual(k.get_vy(), 2, msg="leva stena ne sme spreminjati hitrosti v navpični smeri")

        k = Ball(5, 100, 6, 1, 2)
        k.walls()
        self.assertAlmostEqual(k.get_x(), 5, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_y(), 100, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_vx(), 1, msg="zoga se mora odbiti stran od leve stene")
        self.assertAlmostEqual(k.get_vy(), 2, msg="leva stena ne sme spreminjati hitrosti v navpični smeri")

        k = Ball(risar.maxX-5, 100, 6, 1, 2)
        k.walls()
        self.assertAlmostEqual(k.get_x(), risar.maxX-5, "walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_y(), 100, "walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_vx(), -1, "zoga se ne obrne pravilno ob desni steni")
        self.assertAlmostEqual(k.get_vy(), 2, "desna stena ne sme spreminjati hitrosti v navpični smeri")

        k = Ball(risar.maxX-5, 100, 6, -1, 2)
        k.walls()
        self.assertAlmostEqual(k.get_x(), risar.maxX-5, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_y(), 100, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_vx(), -1, msg="zoga se mora odbiti stran od desne stene")
        self.assertAlmostEqual(k.get_vy(), 2, msg="desna stena ne sme spreminjati hitrosti v navpični smeri")


        k = Ball(100, 5, 6, 2, -1)
        k.walls()
        self.assertAlmostEqual(k.get_x(), 100, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_y(), 5, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_vx(), 2, msg="zgornja stena ne sme spreminjati hitrosti v vodoravni smeri")
        self.assertAlmostEqual(k.get_vy(), 1, msg="zoga se ne obrne pravilno ob gornji steni")

        k = Ball(100, 5, 6, 2, 1)
        k.walls()
        self.assertAlmostEqual(k.get_x(), 100, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_y(), 5, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_vx(), 2, msg="zgornja stena ne sme spreminjati hitrosti v vodoravni smeri")
        self.assertAlmostEqual(k.get_vy(), 1, msg="zoga se ne obrne pravilno ob gornji steni")

        k = Ball(100, risar.maxY-5, 6, 2, 1)
        k.walls()
        self.assertAlmostEqual(k.get_x(), 100, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_y(), risar.maxY-5, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_vx(), 2, msg="spodnja stena ne sme spreminjati hitrosti v vodoravni smeri")
        self.assertAlmostEqual(k.get_vy(), -1, msg="zoga se ne obrne pravilno ob spodnji steni")

        k = Ball(100, risar.maxY-5, 6, 2, 1)
        k.walls()
        self.assertAlmostEqual(k.get_x(), 100, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_y(), risar.maxY-5, msg="walls() naj ne spreminja koordinat")
        self.assertAlmostEqual(k.get_vx(), 2, msg="spodnja stena ne sme spreminjati hitrosti v vodoravni smeri")
        self.assertAlmostEqual(k.get_vy(), -1, msg="zoga se ne obrne pravilno ob spodnji steni")


    def test_ocena8_touches(self):
        k = Ball(100, 100, 5)

        self.assertFalse(k.touches(Ball(116, 100, 10)))
        self.assertFalse(k.touches(Ball(84, 100, 10)))
        self.assertFalse(k.touches(Ball(100, 116, 10)))
        self.assertFalse(k.touches(Ball(100, 84, 10)))

        self.assertTrue(k.touches(Ball(115, 100, 10)))
        self.assertTrue(k.touches(Ball(85, 100, 10)))
        self.assertTrue(k.touches(Ball(100, 115, 10)))
        self.assertTrue(k.touches(Ball(100, 85, 10)))

        self.assertTrue(k.touches(Ball(113, 100, 10)))
        self.assertTrue(k.touches(Ball(87, 100, 10)))
        self.assertTrue(k.touches(Ball(100, 113, 10)))
        self.assertTrue(k.touches(Ball(100, 87, 10)))

        self.assertTrue(k.touches(Ball(100, 100, 2)))
        self.assertTrue(k.touches(Ball(101, 101, 2)))

        k = Ball(100, 100, 4)
        self.assertTrue(k.touches(Ball(102, 103, 1)))
        self.assertTrue(k.touches(Ball(98, 103, 1)))
        self.assertTrue(k.touches(Ball(102, 97, 1)))
        self.assertTrue(k.touches(Ball(98, 97, 1)))

        k = Ball(100, 100, 4)
        self.assertTrue(k.touches(Ball(102, 103, 2)))
        self.assertTrue(k.touches(Ball(98, 103, 2)))
        self.assertTrue(k.touches(Ball(102, 97, 2)))
        self.assertTrue(k.touches(Ball(98, 97, 2)))

        k = Ball(100, 100, 3)
        self.assertTrue(k.touches(Ball(102, 103, 1)))
        self.assertTrue(k.touches(Ball(98, 103, 1)))
        self.assertTrue(k.touches(Ball(102, 97, 1)))
        self.assertTrue(k.touches(Ball(98, 97, 1)))

    def test_ocena8_intersects(self):
        k = Ball(100, 100, 5)
        balls = [Ball(10*j, 10*j, 5) for j in range(6)]
        self.assertFalse(k.intersects(balls))

        balls.append(Ball(102, 102, 5))
        self.assertTrue(k.intersects(balls))
        del balls[-1]

        balls.insert(0, Ball(102, 102, 5))
        self.assertTrue(k.intersects(balls))
        del balls[0]

        balls.insert(2, Ball(102, 102, 5))
        self.assertTrue(k.intersects(balls))

    def test_ocena8_setup(self):
        for i in range(100):
            balls = setup(42)
            self.assertEqual(len(balls), 42)
            for i, ball in enumerate(balls):
                self.assertFalse(ball.intersects(balls[:i]))
            self.assertGreaterEqual(len({ball.get_x() for ball in balls}), 10,
                "zoge imajo nekam malo razlicnih koordinat x")
            self.assertGreaterEqual(len({ball.get_y() for ball in balls}), 10,
                "zoge imajo nekam malo razlicnih koordinat y")

    def test_ocena8__init__(self):
        balls = setup(42)
        for i in range(100):
            k = Ball(existing=balls)
            self.assertFalse(k.intersects(balls))
