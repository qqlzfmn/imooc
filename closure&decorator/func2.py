def dec(func):
    def in_dec(*args):
        if len(args) == 0:
            return 0
        for arg in args:
            if not isinstance(arg, int):
                return 0
        return func(*args)

    return in_dec


def my_sum(*args):
    return sum(args)


def my_average(*args):
    return sum(args) / len(args)


my_sum = dec(my_sum)
my_average = dec(my_average)

print(my_sum(1, 2, 3, 4, 5))
print(my_average(1, 2, 3, 4, 5))
print(my_sum(1, '2', 3, 4, 5))
print(my_average(1, '2', 3, 4, 5))
