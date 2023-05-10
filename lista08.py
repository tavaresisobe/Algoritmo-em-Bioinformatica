# Luan Olimpio Claro da Costa

# Algoritmos em Bioinformatica
# Desafio Criptografia

def lista08():
    texto = input("Entre com o texto: ")
    chave = int(input("Entre com o chave: "))

    saida = ""
    for letra in texto:
        char = ord(letra) + chave
        if (char >= 65 and char <= 90) or (char >= 97 and char <= 122):
            saida = saida + chr(char)
        elif ord(letra) > 90 or ord(letra) > 122:
            saida = saida + chr(ord(letra) - 26 + chave)
        else:
            saida = saida + letra

    print("Saida: " + saida)
