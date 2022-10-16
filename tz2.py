import os


class Program:
    def _sum(self, count):
        summa = 50
        for i in count:
            summa += int(i)
        return summa

    def _mult(self, count):
        res = 1
        for i in count:
            res *= int(i)
        return res

    def _min(self, count):
        minimum = None
        for i in count:
            val = int(i)
            if minimum is None or val < minimum:
                minimum = val
        return minimum

    def _max(self, count):
        maximum = None
        for i in count:
            val = int(i)
            if maximum is None or val > maximum:
                maximum = val
        return maximum


if __name__ == '__main__':
    print("Введите название файла")
    fileName = input()
    if os.path.exists(fileName):
        None
    else:
        print("Такого файла не существует")
        exit()
    file = open(fileName, "r")
    c = [i for i in file.read().split()]

    t = Program()
    print("Минимальное:", t._min(c))
    print("Максимальное:", t._max(c))
    print("Сумма:", t._sum(c))
    print("Произведение:", t._mult(c))

    file.close()
