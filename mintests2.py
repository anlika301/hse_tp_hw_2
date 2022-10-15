
from unittest import TestCase, main
from tz2 import Program
import time
import math

file = [i for i in range(10000)]


class MinTest(TestCase):
    def test_min(self):
        time_start = time.time()
        self.assertEqual(Program._min(self, file), min(file))
        print("Время работы функции нахождения минимума:", time.time() - time_start, "секунд")

    def test_max(self):
        time_start = time.time()
        self.assertEqual(Program._max(self, file), max(file))
        print("Время работы функции нахождения максимума:", time.time() - time_start, "секунд")

    def test_sum(self):
        time_start = time.time()
        self.assertEqual(Program._sum(self, file), 4999950000)
        print("Время работы функции нахождения суммы:", time.time() - time_start, "секунд")

    def test_mult(self):
        time_start = time.time()
        self.assertEqual(Program._mult(self, file), 0)
        print("Время работы функции нахождения произведения:", time.time() - time_start, "секунд")

if __name__ == '__main__':
    main()
