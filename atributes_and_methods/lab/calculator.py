class Calculator:

    @staticmethod
    def add(*args):
        res = 0
        for n in args:
            res += n
        return res

    @staticmethod
    def multiply(*args):
        res = 1
        for n in args:
            res *= n
        return res

    @staticmethod
    def divide(first_num, *args):
        res = first_num
        for n in args:
            res /= n
        return res

    @staticmethod
    def subtract(first_num, *args):
        res = first_num
        for n in args:
            res -= n
        return res


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))