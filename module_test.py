import classes
from classes import Dog

print '*' * 20
dog1 = Dog('sydney', 'yip', 'crate', 35)
dog1.print_habitat()


def my_print(*splat_args):
    for i in splat_args:
        print i,

my_print(1,'2',3)
