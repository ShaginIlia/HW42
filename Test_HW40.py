import HW40
import unittest

"""
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. 
Далее 10 раз у объектов вызываются методы run и walk соответственно. 
Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов."""


def frozen_test(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print('Тесты в этом кейсе заморожены')
        else:
            func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen_test
    def test_walk(self):
        sportsmen = HW40.Runner('Коля')
        for i in range(10):
            sportsmen.walk()
        self.assertEqual(sportsmen.distance, 50)

    def test_run(self):
        sportsmen = HW40.Runner('Коля')
        for i in range(10):
            sportsmen.run()
        self.assertEqual(sportsmen.distance, 100)

    def test_challenge(self):
        sportsmen = HW40.Runner('Коля')
        sportsmen2 = HW40.Runner('Саша')
        for i in range(10):
            sportsmen.walk()
            sportsmen2.run()
        self.assertNotEqual(sportsmen.distance, sportsmen2.distance)


if __name__ == "__main__":
    unittest.main()
