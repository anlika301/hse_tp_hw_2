
from unittest import TestCase, main
from tz2 import Program
import time
import math

file = [i for i in range(10000)]
file1 = [i for i in range(100000)]


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
        self.assertEqual(Program._sum(self, file), 49995000)
        print("Время работы функции нахождения суммы:", time.time() - time_start, "секунд")

    def test_mult(self):
        time_start = time.time()
        self.assertEqual(Program._mult(self, file), 0)
        print("Время работы функции нахождения произведения:", time.time() - time_start, "секунд")

    def test_log(self):
        self.assertTrue(Program._max(self, file) >= Program._min(self, file))

    def test_time(self):
        time_start = time.time()
        Program._max(self, file)
        time_file = time.time()
        Program._max(self, file1)
        time_file1 = time.time()
        print("Время работы функции нахождения минимума:", time_file - time_start, "секунд")
        print("Время работы функции нахождения минимума для количества чисел в 10 раз больше:", time_file1 - time_file, "секунд")
        self.assertTrue(time_file - time_start <= time_file1 - time_file)


if __name__ == '__main__':
    main()
