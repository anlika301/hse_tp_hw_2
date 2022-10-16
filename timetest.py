from unittest import TestCase, main
from tz2 import Program
import time

file = [i for i in range(10000)]
file1 = [i for i in range(100000)]


class TimeTest(TestCase):
    def test_time(self):
        time_start = time.time()
        Program._max(self, file)
        time_file = time.time()
        Program._max(self, file1)
        time_file1 = time.time()
        print("Время работы функции нахождения минимума:", time_file - time_start, "секунд")
        print("Время работы функции нахождения минимума для количества чисел в 10 раз больше:", time_file1 - time_file,
              "секунд")
        self.assertTrue(time_file - time_start <= time_file1 - time_file)


if __name__ == '__main__':
    main()
