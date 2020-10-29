import numpy as np


def polyeval(polyonim, x):
    result = polyonim[0]
    for i in range(1, len(polyonim)):
        result = result * x + polyonim[i]
    return result


def prod_differences(value, roots):
    prod = 1
    for i in roots:
        if i != value:
            prod *= (value-i)
    return prod


def DK(args, iterations=100):
    roots = []
    print(np.poly1d(args))
    args[:] = [x / args[0] for x in args]
    func = polyeval

    rng = np.random.default_rng()
    for _ in range(len(args)-1):
        a = 100*rng.random()
        b = 100*rng.random()
        roots.append(complex(a, b))

    for _ in range(iterations):
        for i in range(len(roots)):
            roots[i] = roots[i]-func(args, roots[i]) / \
                prod_differences(roots[i], roots)

    roots = sorted(roots, key=lambda x: (x.real))

    for root in roots:
        if (round(root.imag, 4) > 0):
            print(str(round(root.real, 4))+'+'+str(round(root.imag, 4)), 'j')
        elif (round(root.imag, 4) < 0):
            print(str(round(root.real, 4))+str(round(root.imag, 4)), 'j')
        else:
            print(round(root.real, 4))
    return roots
