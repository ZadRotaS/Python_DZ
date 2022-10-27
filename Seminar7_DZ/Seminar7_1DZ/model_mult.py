


def mult(num1: float, num2: float):
    mult = num1 * num2
    return mult


def mult_complex(num1: float, num2: float, num3: float, num4: float):
    mult1 = num1 * num2
    mult2 = num3 * num4
    print(f"({mult1:0.4} , {mult2:0.4}j)")


def mult2(num1: float, num2: float):
    mult = num1 ** num2
    return mult


def mult2_complex(num1: float, num2: float, num3: float, num4: float):
    mult1 = num1 ** num2
    mult2 = num3 ** num4
    print(f"({mult1:0.4} , {mult2:0.4}j)")


def pow(num1: float):
    pow = num1 * num1
    return pow


def pow_complex(num1: float, num3: float):
    pow1 = num1 * num1
    pow2 = num3 * num3
    print(f"({pow1:0.4} , {pow2:0.4}j)")

