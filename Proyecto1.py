import math

def generadorMixto(listaGenerador, funcion, listaFuncion, n, m):
    x0=listaGenerador[0]
    a=listaGenerador[1]
    c=listaGenerador[2]
    m=listaGenerador[3]

    xn=x0
    noAleatorios = [xn]

    no_aleatorio = 0
    periodo=0
    found = False
    for i in range(n):
        xn=(a*(xn)+c) % m
        no_aleatorio = xn/m
        
        if no_aleatorio in noAleatorios and found!=True:
            periodo = i - noAleatorios.index(no_aleatorio) + 1
            print("\nSe repitió: " + str(no_aleatorio) + "  En ciclo: "+str(i)+"    First occurrence at: "+ str(noAleatorios.index(no_aleatorio))+"  Periodo: "+ str(periodo) +"\n")
            found = True
            break
        
        noAleatorios.append(no_aleatorio)
        print("Xn : "+ str(xn) + "             No. aleatorio: "+ str(no_aleatorio))




def generadorMultiplicativo(lista_generador, funcion, lista_funcion, n, m):
    x0 = lista_generador[0]
    a= lista_generador[1]
    m=lista_generador[2]
    d = math.log10(m)
    periodo = 0 

    numero=m
    numeros_primos = {}
    #SI ES BASE 10
    if(d.is_integer()):
        #print("Es base 10 "+str(d))
        if(d>=5):
            periodo = 5*10**(d-2)
        else: 
            #Calcular factores primos, comenzamos con 2
            #CREDITOS A https://ehack.info/python-imprimir-factores-primos/
            factor = 2
            # Continúe hasta que el factor sea mayor que el número
            while factor <= numero:
                # Verificar si el factor es un divisor de número
                if not (numero % factor != 0):
                # Si es así, imprímalo y divida el número original
                    #print(factor)

                    if(factor not in numeros_primos):
                        numeros_primos[factor]=1
                    else:
                        numeros_primos[factor] = numeros_primos[factor]+1
                    #numeros_primos.append(factor)
                    numero /= factor
                else:
                    # Si no es así, incremente el factor en uno
                    factor += 1
            print(numeros_primos)
    #SI ES BASE 2
    else:
        d = math.log2(m)
        #print("Es base 2 "+str(d))

        if(d>=3):
            periodo = 2**(d-2)

def generaAleatorios(generador, lista_generador, funcion, lista_funcion, n, m):
    if generador == "mixto":
        generadorMixto(lista_generador, funcion, lista_funcion, n, m)
    else: 
        generadorMultiplicativo(lista_generador, funcion, lista_funcion, n, m)



generador="mixto"
lista_generador= [[15,8,16,10],[13,50,17,64],[7,5,24,32],[3,5,21,100]]
funcion = "uniforme"
lista_funcion = [0,18]
n = 10
m = 5

#generaAleatorios(generador, lista_generador[0], funcion, lista_funcion, n, m)    
#generaAleatorios(generador, lista_generador[1], funcion, lista_funcion, n, m) 
#generaAleatorios(generador, lista_generador[2], funcion, lista_funcion, n, m)
#generaAleatorios(generador, lista_generador[3], funcion, lista_funcion, n, m)

'''
generador="multiplicativo"
#x0, a, c, m
lista_generador= [[17, 203, 100000],[3,211, 1000],[7,5,64], [1,6,13]]
funcion = "uniforme"
lista_funcion = [0,18]
n = 10
m = 5

generaAleatorios(generador, lista_generador[0], funcion, lista_funcion, n, m)
generaAleatorios(generador, lista_generador[2], funcion, lista_funcion, n, m)
generaAleatorios(generador, lista_generador[1], funcion, lista_funcion, n, m)
generaAleatorios("mixto", [1,6,0,13], funcion, lista_funcion, n, m)'''