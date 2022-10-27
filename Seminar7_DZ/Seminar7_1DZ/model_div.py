

def div(num1: float, num2: float):
    mult = num1 / num2
    return mult


def div_complex(num1: float, num2: float, num3: float, num4: float):
    mult1 = num1 / num2
    mult2 = num3 / num4
    print(f"({mult1:0.4} , {mult2:0.4}j)")


def div2(num1: float, num2: float):
    mult = num1 // num2
    return mult


def div2_complex(num1: float, num2: float, num3: float, num4: float):
    mult1 = num1 // num2
    mult2 = num3 // num4
    print(f"({mult1:0.4} , {mult2:0.4}j)")


def div3(num1: float, num2: float):
    mult = num1 % num2
    return mult


def div3_complex(num1: float, num2: float, num3: float, num4: float):
    mult1 = num1 % num2
    mult2 = num3 % num4
    print(f"({mult1:0.4} , {mult2:0.4}j)")


def sqrt(num1: float, num2: float):
    sqrt = (num1 + num2) ** 0.5
    return sqrt


def sqrt_complex(num1: float, num2: float, num3: float, num4: float):
    sqrt1 = (num1 + num2) ** 0.5
    sqrt2 = (num3 + num4) ** 0.5
    print(f"({sqrt1:0.4} , {sqrt2:0.4}j)")
