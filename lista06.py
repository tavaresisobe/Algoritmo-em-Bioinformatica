# Luan Olimpio Claro da Costa

# Algoritmos em Bioinformatica
# Lista 6 de Exerecicios


import math

def fatorial(numero):
    if numero < 2:
        return 1
    else:
        return numero * fatorial(numero-1)

def lista6_ex1():
    numero = int(input("Numero: "))

    print("Fatorial de " + str(numero) + ": "
          + str(fatorial(numero)))


def lista6_ex2():
    numeros = input("Lista de numeros: ")

    lista_numeros = numeros.split()

    maior = float(lista_numeros[0])

    for n in lista_numeros:
        if float(n) > maior:
            maior = float(n)

    print("Maior numero: " + str(maior))



def multiplos(numero1, numero2):
    return numero1 % numero2 == 0

def lista6_ex3():
    numero1 = int(input("Numero 1: "))
    numero2 = int(input("Numero 2: "))

    if multiplos(numero1, numero2):
        print("" + str(numero1) + " e multiplo de " +
              str(numero2))
    else:
        print("" + str(numero1) + " nao e multiplo de " +
              str(numero2))


def seno(radianos):
    resultado = 0.0
    for n in range(0, 60):
        resultado = resultado + math.pow(-1, n) * \
                    math.pow(radianos, 2*n+1) / fatorial(2*n+1)
    return round(resultado, 4)

def cosseno(radianos):
    return round(math.sqrt(1 - seno(radianos) * seno(radianos)), 4)

def lista6_ex4():
    angulo = float(input("Angulo (em multiplos de pi radianos): "))

    radianos = angulo * math.pi

    print("Seno de (" + str(angulo) + " pi) rad: " + str(seno(radianos)))
    print("Cosseno de (" + str(angulo) + " pi) rad: " + str(cosseno(radianos)))
