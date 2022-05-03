import math
import matplotlib.pyplot as plt


def generaAleatorios(generador, lista_generador, funcion, lista_funcion, n, bars):
    x0 = lista_generador[0]
    a = lista_generador[1]

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

    if funcion == 'exponencial':
        m_generador = exponential_distribution(lista_funcion)
    elif funcion == 'normal':
        m_generador = normal_distribution(lista_generador)
    elif funcion == 'poisson':
        m_generador = poisson_distribution(lista_generador)
    elif funcion == 'binomial':
        m_generador = binomial_distribution(lista_generador)

    print("C: " + str(c) + " M: " + str(m))

    xn = x0
    no_aleatorios = []

    no_aleatorio = 0
    periodo = 0
    found = False
    for i in range(n):
        xn = (a * xn + c) % m
        no_aleatorio = xn / m_generador

        if no_aleatorio in no_aleatorios and found is not True:
            periodo = i - no_aleatorios.index(no_aleatorio)
            found = True
            '''#SIRVE PARA DETERMINAR EL PERIODO
            print("\nSe repitió: " + str(no_aleatorio) + "  En ciclo: "+str(i)+"    First occurrence at: "+ str(no_aleatorios.index(no_aleatorio))+"  Periodo: "+ str(periodo) +"\n")
            print(no_aleatorios)
            break
            '''

        no_aleatorios.append(no_aleatorio)
        print("Xn : " + str(xn) + "             No. aleatorio: " + str(no_aleatorio))

    plt.hist(no_aleatorios, bars)
    plt.xlabel('Data points')
    plt.ylabel('Probability Density')
    plt.show()
    return no_aleatorios


def exponential_distribution(function_list):
    x = function_list[0]
    mu = function_list[1]
    distribution = 1 - math.exp((-x) / mu)
    return distribution


def normal_distribution(function_list):
    media = function_list[0]
    variation = function_list[1]
    x = function_list[2]
    exponential = -((x - media) ^ 2) / 2 * variation
    distribution = (1 / math.sqrt(2 * math.pi * variation)) * math.exp(exponential)
    return distribution


def poisson_distribution(function_list):
    x = function_list[0]
    events_per_unit = function_list[1]
    distribution = (math.exp(-events_per_unit) * events_per_unit ^ x) / math.factorial(x)
    return distribution


def binomial_distribution(function_list):
    x = function_list[0]
    p = function_list[1]
    n = function_list[2]
    distribution = combination(n, x) * p ^ x * (1 - p) ^ (n - x)
    return distribution


def combination(n, r):
    c = math.factorial(n) / math.factorial(r) * math.factorial(n - r)
    return c


generador = "mixto"
lista_generador = [[15, 8, 16, 10], [13, 50, 17, 64], [7, 5, 24, 32], [3, 5, 21, 100]]
funcion = "uniforme"
lista_funcion = [0, 18]
n = 10
bars = 5

print(generaAleatorios(generador, lista_generador[3], funcion, lista_funcion, n, bars))
# generaAleatorios(generador, lista_generador[1], funcion, lista_funcion, n, m)
# generaAleatorios(generador, lista_generador[2], funcion, lista_funcion, n, m)
# generaAleatorios(generador, lista_generador[3], funcion, lista_funcion, n, m)

generador_m = "multiplicativo"
# x0, a, c, m
lista_generador_m = [[17, 203, 100000], [3, 211, 1000], [7, 5, 64], [1, 6, 13], [2777, 19, 32]]
funcion_m = "exponencial"
lista_funcion_m = [3, 18]
n_m = 10
bars_m = 5

print(generaAleatorios(generador_m, lista_generador_m[3], funcion_m, lista_funcion_m, n_m, bars_m))
