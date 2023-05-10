# Luan Olimpio Claro da Costa

# Algoritmos em Bioinformatica
# Lista 4 de Exerecicios

import datetime

def lista4_ex1():
    nome = input("Nome: ")
    ra = input("RA: ")
    media = int(input("Media: "))

    dicionario = {}

    dicionario["Nome"] = nome
    dicionario["RA"] = ra
    dicionario["Media"] = media

    for elemento in dicionario:
        print("" + elemento + ": " + str(dicionario[elemento]))

    if dicionario["Media"] < 6:
        print("Reprovado!")
    else:
        print("Aprovado!")


def lista4_ex2():
    dicionario = {}
    dicionario["Nome"] = []
    dicionario["Peso"] = []
    dicionario["Sexo"] = []
    dicionario["Altura"] = []
    dicionario["IMC"] = []

    while True:
        print("Digite o nome ou 'fim' para encerrar")
        nome = input("Nome: ")

        if nome == 'fim':
            break

        sexo = input("Sexo: ")
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))

        dicionario["Nome"].append(nome)
        dicionario["Sexo"].append(sexo)
        dicionario["Peso"].append(peso)
        dicionario["Altura"].append(altura)
        dicionario["IMC"].append(peso/(altura*altura))

    print("Foram cadastradas " + str(len(dicionario["Nome"])) + " pessoas")

    media = 0.0

    for elemento in dicionario["Altura"]:
        media = media + elemento / len(dicionario["Altura"])
    print("A media da altura e " + str(media))

    for elemento in dicionario["Peso"]:
        media = media + elemento / len(dicionario["Peso"])
    print("A media do peso e " + str(media))

    for elemento in dicionario["IMC"]:
        media = media + elemento / len(dicionario["IMC"])
    print("A media de IMC e " + str(media))


def lista4_ex3():
    dicionario = {}
    ano = int(datetime.date.today().year)

    dicionario["Nome"] = input("Nome: ")
    dicionario["Nascimento"] = int(input("Ano de Nascimento: "))
    dicionario["Carteira"] = int(input("Carteira de trabalho: "))
    dicionario["Idade"] = ano - dicionario["Nascimento"]

    if dicionario["Carteira"] != 0:
        dicionario["Contratacao"] = int(input("Ano de Contratacao: "))
        dicionario["Salario"] = float(input("Salario: "))

        if ano - dicionario["Contratacao"] >= 35:
            dicionario["Aposentadoria"] = ano
            print("Ano da Aposentadoria: ja pode aposentar")
        else:
            dicionario["Aposentadoria"] = 35 + dicionario["Contratacao"]
            print("Ano da Aposentadoria: " + str(dicionario["Aposentadoria"]))

    print("Idade atual: " + str(dicionario["Idade"]))


def lista4_ex4():
    dicionario = {}

    dicionario["Nome"] = input("Nome: ")
    dicionario["Partidas"] = int(input("Partidas jogadas: "))
    dicionario["Gols"] = []
    dicionario["Total"] = 0

    for i in range(0, dicionario["Partidas"]):
        gols = int(input("Gols no jogo n°" + str(i+1) + ": "))
        dicionario["Gols"].append(gols)
        dicionario["Total"] = dicionario["Total"] + gols

    print("Total de gols: " + str(dicionario["Total"]))
