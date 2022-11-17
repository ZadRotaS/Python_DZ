
def int_n(n):
    n = n.split(' ')

    for k in range(len(n)):
        n[k] = int(n[k])
    return n


def complex_n(n):
    n = n.split(' ')

    for k in range(len(n)):
        n[k] = complex(n[k])
    return n


def Checking(n, num):
    if num > 0:
        if n.replace('-', '').isdigit():
            return n.replace(' ', '')
        else:
            n = int_n(n)
    else:
        if n.replace('+', '').replace('j', "").replace('-', '').isdigit():
            return n.replace(' ', '')
        else:
            n = complex_n(n)
    return n


def sum(n, num):

    n = Checking(n, num)
    if type(n) == list:
        for i in range(1, len(n)):
            n[0] += n[i]
        return n[0]
    return n


def sub(n, num):
    n = Checking(n, num)
    if type(n) == list:
        for i in range(1, len(n)):
            n[0] -= n[i]
        return n[0]
    return n


def mult(n, num):
    n = Checking(n, num)
    if type(n) == list:
        for i in range(1, len(n)):
            n[0] *= n[i]
        return n[0]
    return n


def div(n, num):
    n = Checking(n, num)
    if type(n) == list:
        for i in range(1, len(n)):
            n[0] /= n[i]
        return n[0]
    return n


def pow(n):
    if n.isdigit():
        return int(n.replace(' ', '')) ** 2
    else:
        n = int_n(n)
        for i in range(0, len(n)):
            n[i] = n[i] ** 2
        return n


def sqrt(n):
    if n.isdigit():
        return int(n.replace(' ', '')) ** 0.5
    else:
        n = int_n(n)
        for i in range(0, len(n)):
            n[i] = n[i] ** 0.5
        return n


# x = complex('10-10j')
# # # # # # for i in range(len(x)):
# # # # # #     x[i] = complex(x[i])
# # #
# print(x)
# print(sum(x,1))
