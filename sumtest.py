from unittest import TestCase, main
from tz2 import Program
import time


file = [i for i in range(10000)]


class SumTest(TestCase):
    def test_sum(self):
        time_start = time.time()
        self.assertEqual(Program._sum(self, file), 49995000)
        print("Время работы функции нахождения суммы:", time.time() - time_start, "секунд")


if __name__ == '__main__':
    main()
