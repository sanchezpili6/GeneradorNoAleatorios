import math
import matplotlib.pyplot as plt
from numpy import random


def generaAleatorios(generador, lista_generador, funcion, lista_funcion, n, bars):
    x0 = lista_generador[0]
    a = lista_generador[1]
    no_aleatorios = []

    if generador == "mixto":
        no_aleatorios = mixed_generator(x0, lista_generador[3], lista_generador[1], lista_generador[2], n)
        c = lista_generador[2]
        m = lista_generador[3]
    elif generador == 'multiplicativo':
        c = 0
        m = lista_generador[2]
        no_aleatorios = multiplicative_generator(x0, m, a, n)
    else:
        return "Por favor elige entre mixto o multiplicativo"

    print("C: " + str(c) + " M: " + str(m))

    if funcion == 'exponencial':
        exponential_distribution(lista_funcion)
    elif funcion == 'normal':
        normal_distribution(lista_funcion)
    elif funcion == 'poisson':
        poisson_distribution(lista_funcion)
    elif funcion == 'binomial':
        binomial_distribution(lista_funcion)

    plt.hist(x=no_aleatorios, bins='auto', color='#0504aa',
             alpha=0.7, rwidth=0.85)
    plt.show()
    return no_aleatorios


def mixed_generator(x0, m, a, c, n):
    no_aleatorios = [x0]
    xn = x0
    m_generador = m
    for i in range(n):
        xn = (a * xn + c) % m
        no_aleatorio = xn / m_generador
        no_aleatorios.append(no_aleatorio)
        print("Xn : " + str(xn) + "             No. aleatorio: " + str(no_aleatorio))
    return no_aleatorios


def multiplicative_generator(x0, m, a, n):
    no_aleatorios = [x0]
    xn = x0
    m_generador = m - 1
    for i in range(n):
        xn = (a * xn) % m
        no_aleatorio = xn / m_generador
        no_aleatorios.append(no_aleatorio)
        print("Xn : " + str(xn) + "             No. aleatorio: " + str(no_aleatorio))
    return no_aleatorios


# plt.hist(x=random.exponential(5, 10000), bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
# plt.hist(x=multiplicative_generator(5, 7, 3, 1000), bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
# plt.show()


# print(mixed_generator(7, 7, 3, 3, 10000, 0.45))


def exponential_distribution(function_list):
    x = function_list[0]
    mean = function_list[1]
    new_random_numbers = []
    r = multiplicative_generator(47, 2, 3, 10)
    for number in r:
        distribution = -1/mean * math.log(number)
        new_random_numbers.append(distribution)
    return new_random_numbers


def normal_distribution(function_list):
    media = function_list[0]
    variation = function_list[1]
    x = function_list[2]
    exponential = -((x - media) ^ 2) / 2 * variation
    distribution = (1 / math.sqrt(2 * math.pi * variation)) * math.exp(exponential)
    return distribution


def poisson_distribution(function_list):
    x = function_list[0]
    mean = function_list[1]
    distribution = ((math.pow(mean, x)) / math.factorial(x)) * math.exp(-mean)
    return distribution


def binomial_distribution(function_list):
    x = function_list[0]
    p = function_list[1]
    n = function_list[2]
    distribution = combination(n, x) * math.pow(p, x) * math.pow((1 - p),(n - x))
    return distribution


def combination(n, r):
    c = math.factorial(n) / math.factorial(r) * math.factorial(n - r)
    return c


generador = "mixto"
lista_generador = [[15, 8, 16, 10], [13, 50, 17, 64], [7, 5, 24, 32], [3, 5, 21, 100], [0, 3, 3, 7]]
funcion = "poisson"
lista_funcion = [4, 18]
n = 10
bars = 5

#print(generaAleatorios(generador, lista_generador[4], funcion, lista_funcion, n, bars))

generador_m = "multiplicativo"
lista_generador_m = [[17, 203, 100000], [3, 211, 1000], [7, 5, 64], [1, 6, 13], [2777, 19, 32]]
funcion_m = "exponencial"
lista_funcion_m = [3, 18]
n_m = 10
bars_m = 50

#print(generaAleatorios(generador_m, lista_generador_m[4], funcion_m, lista_funcion_m, n_m, bars_m))

print(multiplicative_generator(47, 2, 3, 100))
print(exponential_distribution([5,2]))
plt.hist(x=exponential_distribution([5, 2]), bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
plt.show()