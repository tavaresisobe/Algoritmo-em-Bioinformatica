# Luan Olimpio Claro da Costa

# Algoritmos em Bioinformatica
# Lista 1 de Exerecicios

def lista2_ex1():
    string1 = input("1a string: ")
    string2 = input("2a string: ")

    if string1.find(string2) == 1:
        print("'" + string2 + "' esta dentro de '" + string1 + "'")
    else:
        print("'" + string2 + "' nao esta dentro de '" + string1 + "'")


def lista2_ex2():
    string1 = input("1a string: ")
    string2 = input("2a string: ")
    string3 = ""

    for letra in string1:
        if (string2.find(letra) != -1 and string3.find(letra) == -1):
            string3 = string3 + letra

    print(string3)


def lista2_ex3():
    string = input("String: ")

    letras = []

    for letra1 in string:
        if letra1 not in letras:
            contador = 0
            for letra2 in string:
                if(letra1 == letra2):
                    contador = contador + 1
            print(str(contador) + "x " + letra1)
            letras.append(letra1)


def lista2_ex4():
    string1 = input("1a string: ")
    string2 = input("2a string: ")
    string3 = input("3a string: ")

    i=0
    for letra in string2:
        string1 = string1.replace(letra, string3[i])
        i = i + 1

    print(string1)


def lista2_ex5():
    string = input("String: ")
    palindromo = True
    i = 0

    while i < len(string)/2:
        if string[i] != string[len(string)-i-1]:
            palindromo = False
            break
        i = i + 1

    if palindromo:
        print("'" + string + "' e um palindromo")
    else:
        print("'" + string + "' nao e um palindromo")


def lista2_ex6():
    string = input("String: ")
    array = string.split()
    i = 0

    while i < len(array):
        print(array[-i-1], end=" ")
        i = i + 1


def lista2_ex7():
    string = input("String: ")
    array = string.split()

    for palavra in array:
        if len(palavra) > 3:
            print(palavra, end=" ")
