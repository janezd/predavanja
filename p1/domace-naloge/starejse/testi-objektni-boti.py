

import unittest
from unittest.mock import patch, MagicMock, call
class TestUnit(unittest.TestCase):
    def test_unit(self):
        a = Unit()
        b = Unit()
        self.assertListEqual(
            a.chips, [],
            "Instances of 'Unit' must have a list attribute `chips` "
            "that is initially empty")
        a.receive(42)
        self.assertListEqual(a.chips, [42])
        self.assertListEqual(b.chips, [])


class TestOutput(unittest.TestCase):
    def test_hierarchy(self):
        self.assertTrue(
            issubclass(Output, Unit), "`Output` must be derived from `Unit`")

    def test_constructor(self):
        mock_list = []
        def my_init(obj):
            obj.chips = mock_list
        with patch.object(Unit, "__init__", my_init):
            a = Output(42)
            self.assertIs(
                a.chips, mock_list,
                "Attribute 'chips' must be assigned by Unit's constructor")
            self.assertEqual(mock_list, [])

    def test_receive_calls_inherited_receive(self):
        receive_mock = MagicMock(name="Unit.receive")
        with patch.object(Unit, "receive", receive_mock):
            a = Output(42)
            a.receive(13)
            receive_mock.assert_called_with(13)

    def test_receive_prints(self):
        print_mock = MagicMock(wraps=print, name="print")
        with patch("builtins.print", print_mock):
            a = Output(42)
            a.receive(13)
            print_mock.assert_called_with("Output 42: 13")
            a.receive(25)
            print_mock.assert_called_with("Output 42: 25")


class TestBot(unittest.TestCase):
    def test_hierarchy(self):
        self.assertTrue(
            issubclass(Bot, Unit), "`Output` must be derived from `Unit`")

    def test_constructor(self):
        mock_list = []
        def my_init(obj):
            obj.chips = mock_list
        with patch.object(Unit, "__init__", my_init):
            a = Bot()
            self.assertIs(
                a.chips, mock_list,
                "Attribute 'chips' must be assigned by Unit's constructor")
            self.assertListEqual(
                a.outputs, [],
                "Instances of `Bot` must have a list attribute `outputs` "
                "that is initially empty")

    def test_bot_receive(self):
        self.assertIs(
            Bot.receive, Unit.receive, "Bot must not overload Unit.receive")

        a = Bot()
        a.receive(42)
        self.assertEqual(a.chips, [42])
        a.receive(13)
        self.assertEqual(set(a.chips), {13, 42})
        a.receive(25)
        self.assertEqual(set(a.chips), {13, 25, 42})

    def test_attach(self):
        a = Bot()
        b = Bot()
        c = Bot()
        d = Bot()
        self.assertEqual(a.outputs, [])
        a.attach(b)
        self.assertEqual(a.outputs, [b])
        a.attach(c)
        self.assertEqual(a.outputs, [b, c])
        a.attach(d)
        self.assertEqual(a.outputs, [b, c, d])

    def test_process(self):
        a = Bot()
        b = Bot()
        c = Output(25)
        b.receive = MagicMock()
        c.receive = MagicMock()

        a.attach(b)
        a.attach(c)
        a.receive(42)
        self.assertFalse(a.process())
        b.receive.assert_not_called()
        c.receive.assert_not_called()
        a.receive(13)
        self.assertTrue(a.process())
        b.receive.assert_called_with(13)
        c.receive.assert_called_with(42)
        self.assertEqual(a.chips, [])

    def test_process_more_than_2(self):
        a = Bot()
        bots = []
        for i in range(5):
            b = Bot()
            bots.append(b)
            a.attach(b)
        a.receive(25)
        a.receive(42)
        a.receive(5)
        a.receive(25)
        a.receive(13)
        a.process()
        for bot, number in zip(bots, [5, 13, 25, 25, 42]):
            self.assertEqual(bot.chips, [number])

class TestAutoBot(unittest.TestCase):
    def test_hierarchy(self):
        self.assertTrue(
            issubclass(AutoBot, Bot), "`AutoBot` must be derived from `Bot`")

    def test_auto_process(self):
        a = AutoBot()
        b = AutoBot()
        c = AutoBot()
        b.receive = MagicMock()
        c.receive = MagicMock()
        a.attach(b)
        a.attach(c)
        a.receive(42)
        a.receive(13)
        b.receive.assert_called_with(13)
        c.receive.assert_called_with(42)

    def test_process_hierarchy(self):
        a = AutoBot()
        ab1 = AutoBot()
        a2 = Output(25)
        a.attach(ab1)
        a.attach(a2)

        b = AutoBot()
        b2 = Output(26)
        b.attach(ab1)
        b.attach(b2)

        a11 = AutoBot()
        a12 = AutoBot()
        ab1.attach(a11)
        ab1.attach(a12)

        a11.receive = MagicMock()
        a12.receive = MagicMock()

        a.receive(1)
        a.receive(2)
        b.receive(3)
        b.receive(4)

        a11.receive.assert_called_with(1)
        a12.receive.assert_called_with(3)


class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        print_mock = MagicMock(wraps=print, name="print")
        with patch("builtins.print", print_mock):

            for bot, value in read_file("input.txt"):
                bot.receive(value)

            print_mock.assert_has_calls(
                any_order=True,
                calls=[call(x) for x in """Output 16: 2
Output 6: 3
Output 11: 5
Output 0: 7
Output 18: 11
Output 4: 13
Output 15: 17
Output 13: 19
Output 8: 23
Output 3: 29
Output 19: 31
Output 2: 37
Output 10: 41
Output 14: 43
Output 7: 47
Output 1: 53
Output 5: 59
Output 12: 61
Output 17: 67
Output 20: 71
Output 9: 73""".splitlines()])
