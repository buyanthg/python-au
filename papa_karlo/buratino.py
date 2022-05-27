import random as rand
from math import exp
from time import perf_counter
from scipy import integrate
from numba import njit


@njit
def f(x):
    return 4*x*exp(-2*x)


@njit
def ext(f):               # она типо ищет экстремумы, но это слишком сложно,
    return [1/2]          # поэтому используйте воображение, экстремумы ищите сами


@njit
def s_quad(x_1, x_2, y_1, y_2):
    return (x_2-x_1)*(y_2-y_1)


def karlo(a, b, n):
    count_dot = 0
    extremum = ext(f)
    max_f = max(f(a), f(b), 0)
    min_f = min(f(a), f(b), 0)
    for i in extremum:
        max_f = max(max_f, f(i))
        min_f = min(min_f, f(i))

    for i in range(n):
        x = rand.uniform(a, b)
        y = rand.uniform(min_f, max_f)
        # то же самое что f(x) >= 0 and f(x) >= y or f(x) < 0 and f(y) < y
        if bool(f(x) > 0) == bool(f(x) > y):
            count_dot += 1

    return s_quad(a, b, min_f, max_f) * count_dot / n


@njit
def karlo_numba(a,b,n):
    return karlo(a,b,n)


if __name__ == '__main__':
    x0, x1 = map(float, input().split())
    n = int(input())
    extremum = [1/2]

    start = perf_counter()
    integra = karlo(x0, x1, n)
    end = perf_counter()

    start_nb = perf_counter()
    integra = karlo(x0,x1,n)
    end_nb = perf_counter()

    t = end-start
    t_nb = end_nb - start_nb

    v, err = integrate.quad(f, x0, x1)

    print(f'Интеграл с scipy: {v}\nИнтеграл мой: {integra} :)')
    print('Скорость без нумбы: %.2f' % t)
    print('Скорость с ней: %.2f' % t_nb)
    print('Скорость увеличилась в %.2f раз' % (t/t_nb))
    print("Вы арестованы за превышение скорости")

# искать экстремумы придется самим
# это не входит в план
