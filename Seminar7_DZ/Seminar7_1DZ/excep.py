from user_interface import *
from model_div import *
from model_mult import *
from model_sub import *
from model_sum import *


def program():
    x = 1
    while x !=0:
        x = Worling_with()

        if x == 1:
            n = Operations()

            if n == 1:
                print(sum(*numbers()))

            if n == 2:
                print(sub(*numbers()))

            if 2 < n < 5:
                n = Operations_calculations(n)
                if n == 10:
                    print(mult(*numbers()))
                if n == 20:
                    print(mult2(*numbers()))
                if n == 11:
                    print(div(*numbers()))
                if n == 21:
                    print(div2(*numbers()))
                if n == 31:
                    print(div3(*numbers()))

            if n == 5:
                print(pow(float(input("Введите число: "))))

            if n == 6:
                print(sqrt(*numbers()))

        if x == 2:
            n = Operations()

            if n == 1:
                sum_complex(*numbers_complex())

            if n == 2:

                sub_complex(*numbers_complex())

            if 2 < n < 5:
                n = Operations_calculations(n)
                if n == 10:

                    mult_complex(*numbers_complex())
                if n == 20:

                    mult2_complex(*numbers_complex())
                if n == 11:

                    div_complex(*numbers_complex())
                if n == 21:
                    div2_complex(*numbers_complex())
                if n == 31:

                    div3_complex(*numbers_complex())
            if n == 5:
                pow_complex(*numbers())

            if n == 6:
                sqrt_complex(*numbers_complex())



