import unittest
from front_module import Environment, First, Second, MainClass


class TestFrontModule(unittest.TestCase):
    def setUp(self):
        self.parent = Parent()
        self.environment = Environment()

    def test_first(self):
        first = First(self.parent)
        first.click_link()
        first.scroll_down()
        first.loans()
        first.statementstoconfirm()
        first.currency()
        first.currency2()
        first.profile()

    def test_second(self):
        second = Second(self.parent)
        second.click_link()
        second.scroll_down()
        second.loans()
        second.statementstoconfirm()
        second.currency()
        second.currency2()
        second.profile()

    def test_mainclass(self):
        mainclass = MainClass(self.environment)
        mainclass.wait_time
        mainclass.tasks


if __name__ == '__main__':
    unittest.main()
