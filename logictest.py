from unittest import TestCase, main
from tz2 import Program

file = [i for i in range(10000)]


class LogicTest(TestCase):
    def test_log(self):
        self.assertTrue(Program._max(self, file) >= Program._min(self, file))


if __name__ == '__main__':
    main()
