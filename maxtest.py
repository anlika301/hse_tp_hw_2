from unittest import TestCase, main
from tz2 import Program
import time


file = [i for i in range(10000)]


class MaxTest(TestCase):
    def test_max(self):
        time_start = time.time()
        self.assertEqual(Program._max(self, file), max(file))
        print("Время работы функции нахождения максимума:", time.time() - time_start, "секунд")


if __name__ == '__main__':
    main()
