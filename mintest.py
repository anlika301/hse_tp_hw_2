from unittest import TestCase, main
from tz2 import Program
#import time


file = [i for i in range(10000)]


class MinTest(TestCase):
    def test_min(self):
        time_start = time.time()
        self.assertEqual(Program._min(self, file), min(file))
        print("Время работы функции нахождения минимума:", time.time() - time_start, "секунд")


if __name__ == '__main__':
    main()
