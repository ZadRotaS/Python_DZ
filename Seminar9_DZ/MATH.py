
def int_n(n):
    n = n.split(' ')
    for k in range(len(n)):
        n[k] = int(n[k])
    return n


def sum(n):
    n = int_n(n)
    for i in range(1, len(n)):
        n[0] += n[i]
    return n[0]

def sub(n):
    n = int_n(n)
    for i in range(1, len(n)):
        n[0] -= n[i]
    return n[0]

def mulf(n):
    n = int_n(n)
    for i in range(1, len(n)):
        n[0] *= n[i]
    return n[0]

def div(n):
    n = int_n(n)
    for i in range(1, len(n)):
        n[0] /= n[i]
    return n[0]



