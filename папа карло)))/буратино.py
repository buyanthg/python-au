import random as rand
from scipy import integrate
from math import exp
import time
import multiprocessing as mpc


def f(x):
    return 4*x*exp(-2*x)


def s_quad(x_1,x_2,y_1,y_2):
    return (x_2-x_1)*(y_2-y_1)


def karlo(a, b, n, ext):
    count_dot = 0
    max_f = max(f(a), f(b), 0)
    min_f = min(f(a), f(b), 0)
    for i in ext:
        max_f = max(max_f, f(i))
        min_f = min(min_f, f(i))

    for i in range(n):
        x = rand.uniform(a, b)
        y = rand.uniform(min_f, max_f)
        # то же самое что f(x) >= 0 and f(x) >= y or f(x) < 0 and f(y) < y
        if f(x)*(f(x)-y) >= 0:
            count_dot += 1

    return s_quad(a, b, min_f, max_f) * count_dot / n


if __name__ == '__main__':
    a, b = map(float, input().split())
    n = int(input())

    extremum = [1/2]
    integra = karlo(a, b, n, extremum)
    v, err = integrate.quad(f,a,b)

    print(v)
    print(integra)

# искать экстремумы придется самим
# это не входит в план
