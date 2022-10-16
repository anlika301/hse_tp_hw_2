from unittest import TestCase, main
from tz2 import Program
import time


file = [i for i in range(10000)]


class MultTest(TestCase):
    def test_mult(self):
        time_start = time.time()
        self.assertEqual(Program._mult(self, file), 0)
        print("Время работы функции нахождения произведения:", time.time() - time_start, "секунд")

if __name__ == '__main__':
    main()

