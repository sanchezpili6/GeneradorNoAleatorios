import math
import matplotlib.pyplot as plt
from numpy import random


def generaAleatorios(generador, lista_generador, funcion, lista_funcion, n, bars):
    x0 = lista_generador[0]
    a = lista_generador[1]
    xn = x0
    no_aleatorios = []

    if generador == "mixto":
        c = lista_generador[2]
        m = lista_generador[3]
        m_generador = m
    elif generador == 'multiplicativo':
        c = 0
        m = lista_generador[2]
        m_generador = m - 1
    else:
        return "Por favor elige entre mixto o multiplicativo"

    # GENERA NUMEROS ALEATORIOS MIXTO O MULTIPLICATIVO
    for i in range(n):
        xn = (a * (xn) + c) % m
        no_aleatorio = xn / m_generador
        no_aleatorios.append(no_aleatorio)
        #print("Xn : "+ str(xn) + "             No. aleatorio: "+ str(no_aleatorio))

    if funcion == 'exponencial':
        new_random_numbers = exponential_distribution(lista_funcion, no_aleatorios)
    elif funcion == 'normal':
        new_random_numbers = normal_distribution(lista_funcion, no_aleatorios, n)
    elif funcion == 'poisson':
        new_random_numbers = poisson_distribution(lista_funcion, no_aleatorios)
    elif funcion == 'binomial':
        new_random_numbers = binomial_distribution(lista_funcion, no_aleatorios)
    elif funcion == 'uniforme':
        new_random_numbers = uniform_distribution(lista_funcion, no_aleatorios)

    plt.hist(x=new_random_numbers, bins=bars, color='#0504aa', alpha=0.7, rwidth=0.85)
    #plt.xlim(0,1.8)
    plt.show()


def uniform_distribution(function_list, no_aleatorios):
    limite_inferior = function_list[0]
    limite_superior = function_list[1]
    temp = limite_inferior + (limite_superior - limite_inferior)
    new_random_numbers = [no_aleatorio * temp for no_aleatorio in no_aleatorios]
    return new_random_numbers


def exponential_distribution(function_list, no_aleatorios):
    mean = 1/function_list[0]
    new_random_numbers = []
    for number in no_aleatorios:
        distribution = (-1 / mean * math.log(number))
        new_random_numbers.append(distribution)
    return new_random_numbers


def normal_distribution(function_list, no_aleatorios, n):
    media = function_list[0]
    desv = function_list[1]
    random_numbers = []
    new_random_numbers = []

    for number in no_aleatorios:
        exponential = -((number - media) / 2 * desv) ** 2
        distribution = (1 / (math.sqrt(2 * math.pi) * desv)) * (math.exp(exponential))
        random_numbers.append(distribution)

    sumatoria = sum(random_numbers)
    for number in no_aleatorios:
        for i in range(n):
            x = media + desv * ((number*i - n / 2) / (math.sqrt(n / 12)))
            new_random_numbers.append(x)

    return new_random_numbers


def poisson_distribution(function_list, no_aleatorios):
    mean = function_list[0]
    new_random_numbers = []
    for number in no_aleatorios:
        distribution = (-1 / mean * math.log(number))**-1
        new_random_numbers.append(distribution)
    return new_random_numbers


def binomial_distribution(function_list, no_aleatorios):
    p = function_list[0]
    n = function_list[1]
    new_random_numbers = []
    for number in no_aleatorios:
        distribution = (combination(n, number) * math.pow(p, number) * math.pow((1 - p), (n - number)))
        new_random_numbers.append(distribution)
    return new_random_numbers


def combination(n, r):
    c = math.factorial(int(n)) / math.factorial(int(r)) * math.factorial(int(n - r))
    return c


# Multiplicativo x0, a, m
# Mixto x0, a, c, m
# TODOS ESTOS JALAN BIEN
# generaAleatorios("multiplicativo", [5, 211, 10000], "exponencial", [5], 1000, 5)
# generaAleatorios("mixto", [7,5,24,32], "uniforme", [3,10], 100, 5)
#generaAleatorios("multiplicativo", [5, 211, 10000], "poisson", [20], 10000, 5)
#generaAleatorios("mixto", [5, 211, 16, 1000], "binomial", [0.1, 25], 10000, 20)
generaAleatorios("mixto", [8,9,13,10000], "normal", [4, 3], 12, 20)