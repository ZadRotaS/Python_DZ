

def sum(num1: float, num2: float):
    sum1 = num1 + num2
    return f"{sum1:0.4}"


def sum_complex(num1: float, num2: float, num3: float, num4: float):
    sum1 = num1 + num2
    sum2 = num3 + num4
    print(f"({sum1:0.4} , {sum2:0.4}j)")

#print(sum_complex(2,4,2,4))