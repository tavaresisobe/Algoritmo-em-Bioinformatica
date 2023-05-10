# Algoritmos em Bioinformatica
# Lista 1 de Exerecicios

def lista1_ex1():
    nome = input('Nome: ')
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))

    imc=peso/(altura*altura)

    print(str(nome)+" tem "+str(peso)+" kilos e altura de "+
          str(altura)+" e portanto o IMC e de "+str(imc))


def lista1_ex2():
    metros = input('Valor em metros: ')
    milimetros = metros * 1000
    print("Isso e igual a " + str(milimetros) + " milimetros")

def lista1_ex3():
    dias = input('Dias: ')
    horas = input('Horas: ')
    minutos = input('Minutos: ')
    segundos = input('Segundos: ')

    horas = dias * 24 + horas
    minutos = horas * 60 + minutos
    segundos = minutos * 60 + segundos

    print("O total em segundos e igual a " + str(segundos) + " segundos")

def lista1_ex4():
    salario = input("Salario: ")
    porcentagem = input("Porcentagem de aumento (sem o %): ")

    aumento = salario * porcentagem / 100
    salario = salario + aumento

    print("Valor do aumento: R$ " + str(aumento))
    print("Salario novo: R$ " + str(salario))


def lista1_ex5():
    km = input("Quilometragem percorrida: ")
    dias = input("Dias que o carro foi alugado: ")

    total = 0.15 * km + 60 * dias

    print("Tota a pagar: R$ " + str(total))


def lista1_ex6():
    r1 = input("Resistencia R1: ")
    r2 = input("Resistencia R2: ")
    r3 = input("Resistencia R3: ")

    r = 1.0 / ((1.0 / r1) + (1.0 / r2) + (1.0 / r3))

    print("Resistencia resultante: " + str(r) + " Ohms")
